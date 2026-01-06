from manim import *
import numpy as np

class introduction(Scene):

    def construct(self):

        title = Tex("Bamboo Seawalls", font_size = 65).move_to(ORIGIN)
        transformed_title = Tex("Bamboo Seawalls", font_size = 50).to_corner(UL, buff = 0.4)

        information = [
            Tex(r"$\bullet$ Planting bamboo along coast", font_size = 35),
            Tex(r"$\bullet$ Reduce the impact of waves", font_size = 35)
        ]
        VGroup(*information).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT, buff = 0.5).shift(UP * 1.25)

        self.play(Write(title))
        self.wait()
        self.play(ReplacementTransform(title, transformed_title))
        self.wait()
        for bullet in information:
            self.play(Write(bullet))
            self.wait()
 
        self.play(*[FadeOut(mob) for mob in self.mobjects])
    
class seaWallAnimation(Scene):
    def construct(self):        

        def wave(x):
            return -(0.2 * np.sin(4 * x) + 0.3 * np.cos(x))
    
        coast_func = FunctionGraph(
            lambda x: wave(x),
            color = YELLOW
        )

        mudflat = Rectangle(height = 1.25, width = 14, stroke_width = 0).to_edge(DOWN).set_fill("#3C280D", opacity = 1)

        description = Tex("Mangroves", font_size = 40).to_edge(DOWN, buff = 1)
        carbon = Tex("Carbon Sink!", font_size = 65).to_edge(UP, buff = 1)

        bamboo = []
        gaps_lines = []
        water_vect = [] 
        for i in range(7):

            average = lambda x,y: (x + y)/2

            start = [6.5 - 2 * i, -2, 0]
            end = [5.5 - 2 * i, -2, 0]
            start_gap = [5.5 - 2 * i, -2, 0]
            end_gap = [4.5 - 2 * i, -2, 0]
            start_vect = [average(start_gap[0], end_gap[0]), -0.75, 0]
            end_vect = [average(start_gap[0], end_gap[0]), -1.75, 0]

            bamboo.append(Line(start, end, color = GREEN, stroke_width = 5))
            if i < 6:
                gaps_lines.append(Line(start_gap, end_gap, color = YELLOW, stroke_width = 5))  
                water_vect.append(Arrow(
                    start = start_vect,
                    end = end_vect,
                    buff = 0,
                    color = BLUE,
                    stroke_width = 6,
                    max_tip_length_to_length_ratio = 0.1,
                    max_stroke_width_to_length_ratio = 5 
                ))
        vectors = VGroup(*water_vect)

        self.wait()
        self.play(Create(coast_func), *[Create(item) for item in bamboo])
        self.wait()
        self.play(*[Create(gap) for gap in gaps_lines], run_time = 1.5)
        self.wait(1)
        self.play(*[gap.animate.shift(UP * 0.5) for gap in gaps_lines])
        self.wait()
        self.play(*[FadeOut(gap) for gap in gaps_lines])
        self.wait()
        self.play(*[GrowArrow(arrow) for arrow in water_vect])
        self.wait()
        self.play(ApplyMethod(vectors.shift, DOWN * 1.5))
        self.wait()
        self.play(FadeOut(vectors))
        self.wait()
        self.play(FadeIn(mudflat), run_time = 5)
        self.wait()
        self.play(Write(description))
        self.wait()
        self.play(Write(carbon))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()


    
class example(Scene):
    def construct(self):
        return

class conclusion(Scene):
    def construct(self):
        return