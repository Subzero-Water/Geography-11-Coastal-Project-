from manim import *

class title(Scene):
    def construct(self):

        title = Tex("Sand Sausages", font_size = 65)

        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(Unwrite(title), reversed  = False)
        self.wait()

class longshoreDrift(Scene):
    def construct(self): 

        def wave(x):
            return -(0.2 * np.sin(4 * x) + 0.3 * np.cos(x)) - 1
    
        coast_func = FunctionGraph(
            lambda x: wave(x),
            color = YELLOW
        )

        prev_vect = []

        for i in range(3):
            prev_vect.append(Arrow(
                start = [5.5 - i, 3.5, 0], 
                end = [4.5 - i, 2.5, 0],
                buff = 0,
                color = BLUE,
                stroke_width = 6
            ))
        prevailing_wind = VGroup(*prev_vect)
        prevailing_label = Tex("Prevailing wind", font_size = 40).next_to(prevailing_wind, DOWN, buff = 0.5)

        long1_vect = []
        long2_vect = []
        groynes = []

        for i in range(6):
            x_pos = 7 - i
            y_pos = wave(x_pos)
            y_pos_new = wave(x_pos - 1)

            long1_vect.append(Arrow(
                start = [x_pos, y_pos , 0],
                end = [x_pos - 1, y_pos - 1, 0],
                buff = 0,
                color = RED,
                stroke_width = 6,
                max_tip_length_to_length_ratio = 0.1,
                max_stroke_width_to_length_ratio = 3
            ))

            long2_vect.append(Arrow(
                start = [x_pos - 1, y_pos - 1, 0],
                end = [x_pos - 1, y_pos_new, 0],
                buff = 0,
                color = RED,
                stroke_width = 6,
                max_tip_length_to_length_ratio= 0.1,
                max_stroke_width_to_length_ratio = 3
            ))

            x_pos_line = x_pos - 6
            y_pos_line = wave(x_pos_line)

            start_line = [x_pos_line, y_pos_line - 0.2, 0]
            end_line = [x_pos_line, y_pos_line + 1.5, 0]

            groynes.append(Line(start_line, end_line, color = WHITE, stroke_width = 5)) 

        self.wait(2)
        self.play(Create(coast_func))
        self.wait()
        self.play(*[GrowArrow(arrow) for arrow in prev_vect], Write(prevailing_label), *[Create(groyne) for groyne in groynes])

        self.wait()
        for arrow1, arrow2 in zip(long1_vect, long2_vect):
            self.play(GrowArrow(arrow1), run_time = 0.07)
            self.play(GrowArrow(arrow2), run_time = 0.07)
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class issues(Scene):
    def construct(self):
        
        short = Tex("Short-term solution", font_size = 50, color = GREEN)
        long = Tex("Long-term solution", font_size = 50, color = RED)
        title = Tex("Long-term issues", font_size = 40).to_corner(UL, buff = 0.5)

        issues = [
            Tex(r"$\bullet$ Sandbag damage", font_size = 35),
            Tex(r"$\bullet$ Land subsidence", font_size = 35),
            Tex(r"$\Rightarrow$ Environmental issues", font_size = 35),
            Tex(r"$\therefore$ Temporary and not standalone", font_size = 35)
        ]
        VGroup(issues).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT).shift(UP * 1.5)

        self.wait()
        self.play(Write(short))
        self.wait()
        self.play(ReplacementTransform(short, long))
        self.wait()
        self.play(ReplacementTransform(long, title), run_time = 3)
        self.wait()

        for issue in issues:
            self.play(Write(issue))
            self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


