from manim import *
import numpy as np

class sectionTitle(Scene):
    def construct(self):

      title = Tex("Lesson Overview", font_size=36*1.5, color=WHITE)
      title.to_corner(UL, buff=0.5)
      section_title = Tex(r"$\S$2. Soft engineering", font_size = 60).move_to(ORIGIN)
   
      items = [
          Tex("1. Preliminary discussion on importance", font_size=54, color=WHITE),
          Tex("2. Soft engineering", font_size=54, color=YELLOW),
          Tex("3. Look into the future", font_size=54, color=WHITE)
      ]
      agenda = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT).shift(UP * 1)

      self.wait(1)
      self.play(FadeIn(agenda, title))
      self.wait(2)
      self.play(ReplacementTransform(VGroup(agenda, title), section_title))
      self.wait(2)
      self.play(FadeOut(section_title))
      self.wait(2)

 

class seperation(Scene):
    def construct(self):

        strategies = [
        Tex("Beach Nourishment", font_size = 50),
        Tex("Dune Nourishment", font_size = 50)
        ]
        group = VGroup(*strategies).arrange(RIGHT, buff = 1).move_to(ORIGIN).shift(UP * 0.5)

        self.wait(2)
        self.play(Write(group))
        self.wait(2)
        self.play(strategies[0].animate.scale(1.2).set_color(YELLOW))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)


    
class beach(Scene):
    def construct(self):

        defn = Tex(r"\textbf{Definition} (Beach nourishment). Soft engineering strategy involving", font_size = 40).to_corner(UL)
        defn1 = Tex("adding sand to the beach or in front of cliffs.", font_size = 40).next_to(defn, DOWN, buff = 0.2).to_edge(LEFT)
        source = Tex("GCSE Geography Textbook", font_size = 20).to_corner(DR, buff = 0.5)
        definition = VGroup(defn, defn1, source)

        bullet_points = [
            Tex(r"$\bullet$ Bigger beach", font_size = 40),
            Tex(r"$\bullet$ Nice for tourists", font_size = 40),
            Tex(r"$\bullet$ Absorb energy from incoming waves", font_size = 40),
            Tex(r"$\Rightarrow$ Less coastal erosion", font_size = 40, color = YELLOW)
        ]
        points = VGroup(*bullet_points).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT).shift(UP * 0.5)

        self.wait(2)
        self.play(Write(definition))
        self.wait(5)

        for item in bullet_points:
            self.play(Write(item))
            self.wait(2) 

        self.play(FadeOut(definition, points))
        self.wait(2)

class longshoreDrift(Scene):
    def construct(self):

        def wave(x):
            return -(0.2 * np.sin(4 * x) + 0.3 * np.cos(x)) - 1
    
        coast_func = FunctionGraph(
            lambda x: -(0.2 * np.sin(4 * x) + 0.3 * np.cos(x)) - 1,
            color = YELLOW
        )

        prev_vect = []

        for i in range(3):
            prev_vect.append(Arrow(
                start = [5.5 - i, 3.5, 0], #These vector objects need 3 coordinates
                end = [4.5 - i, 2.5, 0],
                buff = 0,
                color = BLUE,
                stroke_width = 6
            ))
        prevailing_wind = VGroup(*prev_vect)
        prevailing_label = Tex("Prevailing wind", font_size = 40).next_to(prevailing_wind, DOWN, buff = 0.5)

        long1_vect = []
        long2_vect = []

        for i in range(14):
            x_pos = 7 - i
            y_pos = wave(x_pos)
            y_pos_new = wave(x_pos - 1)

            long1_vect.append(Arrow(
                start = [x_pos, y_pos , 0], #These vector objects need 3 coordinates
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

        temporary_label = Tex("Temporary!", font_size = 50, color = YELLOW). to_corner(UL, buff = 0.5).shift(RIGHT * 2).shift(DOWN * 0.5)
        long_vs_short = Tex(r"May be more expensive in the long run$^*$", font_size = 30, color = YELLOW).next_to(temporary_label, DOWN, buff = 0.3)
        fine_details = Tex(r"$^*$This is clearly an argument that appeals to plausibility. More data is required to fully determine when it is indeed more expensive.", color = GRAY, font_size = 22).to_edge(DOWN).shift(RIGHT * 2.5)


        self.wait(2)
        self.play(Create(coast_func))
        self.wait()
        self.play(*[GrowArrow(arrow) for arrow in prev_vect], Write(prevailing_label))

        for arrow1, arrow2 in zip(long1_vect, long2_vect):
            self.play(GrowArrow(arrow1), run_time = 0.07)
            self.play(GrowArrow(arrow2), run_time = 0.07)

        self.wait(2)
        self.play(Write(temporary_label))
        self.wait(6)
        self.play(Write(long_vs_short), Write(fine_details))
        self.wait(6)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

class transitionDune(Scene):
    def construct(self):
        strategies = [
        Tex("Beach Nourishment", font_size = 50, color = YELLOW).scale(1.2),
        Tex("Dune Nourishment", font_size = 50)
    ]
        group = VGroup(*strategies).arrange(RIGHT, buff = 1).move_to(ORIGIN).shift(UP * 0.5)

        self.play(FadeIn(group))
        self.wait()
        self.play(strategies[0].animate.scale(1/1.2).set_color(WHITE), strategies[1].animate.scale(1.2).set_color(YELLOW))
        self.wait(2)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)



class dune(Scene):
    def construct(self):
        
        defn = Tex(r"\textbf{Definition} (Sand Dune Regeneration). Soft engineering strategy involving", font_size = 40).to_corner(UL)
        defn1 = Tex("the creation or stabilization of small hills of sand.", font_size = 40).next_to(defn, DOWN, buff = 0.2).to_edge(LEFT)
        source = Tex("GCSE Geography Textbook", font_size = 20).to_corner(DR, buff = 0.5)
        definition = VGroup(defn, defn1, source)

        bullet_points = [
            Tex(r"$\bullet$ Absorb wave energy", font_size = 35),
            Tex(r"$\bullet$ Exempli gratia: Building wooden fences", font_size = 35)
        ]
        points = VGroup(*bullet_points).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT)

        title = Tex("Sand Dune Regeneration", font_size = 50).to_corner(UL, buff = 0.5)

        self.wait(2)
        self.play(Write(definition))
        self.wait(2)

        for bullet in bullet_points:
            self.play(Write(bullet))
            self.wait()
        self.wait(2)

        self.play(FadeOut(points), ReplacementTransform(definition, title))

        horizontal_line = Line([-5, 2, 0], [5, 2, 0], color = BLUE)
        vertical_line = Line([0, 3, 0], [0, -4, 0], color = BLUE)
        
        pro_text = Tex("Pros", color = GREEN, font_size = 40).next_to(vertical_line, LEFT).next_to(horizontal_line, UP).shift(LEFT * 4)
        con_text = Tex("Cons", color = RED, font_size = 40).next_to(vertical_line, RIGHT).next_to(horizontal_line, UP).shift(RIGHT * 1)
        
        naturalis = [
            Tex(r"$\bullet$ Very natural solution", font_size = 40),
            Tex(r"$\bullet$ Can form new habitats", font_size = 40)
        ]
        left = VGroup(*naturalis).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).next_to(pro_text, DOWN, buff = 1).shift(RIGHT * 1.2)

        disadvantages = [
            Tex(r"$\bullet$ Tourism restrictions", font_size = 40),
            Tex(r"$\bullet$ Subjective eyesore", font_size = 40),
            Tex(r"$\bullet$ Ecotourism", font_size = 40, color = GREEN)
        ]
        right = VGroup(*disadvantages).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).next_to(con_text, DOWN, buff = 1).shift(RIGHT * 1.5)


        inequality = Tex(r"$\mathrm{Ecotourism} \ll \mathrm{ Traditional tourism}$", font_size = 60, color = YELLOW).move_to(ORIGIN)

        squiggly_line = FunctionGraph(
            lambda x: 0.05 * np.sin(4 * PI * x),
            x_range = [0, 3.3],
            color = YELLOW
        ).shift(RIGHT * 0.9, UP * 0.12)

        self.play(Create(horizontal_line), Create(vertical_line))
        self.wait()
        self.play(Write(pro_text), Write(con_text))
        self.wait(2)

        for item in naturalis:
            self.play(Write(item))
            self.wait()
        
        for item in disadvantages:
            self.play(Write(item))            
            if item == disadvantages[1]:
                self.wait()
                self.play(Create(squiggly_line))
                self.wait(5)
                self.play(FadeOut(squiggly_line))
            self.wait()
        self.wait(2)

        self.play(ReplacementTransform(VGroup(vertical_line, 
        horizontal_line,
        pro_text,
        con_text,
        left,
        right
        ), inequality))

        self.wait(4)
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(2)

class example(Scene):
    def construct(self):
        title = Tex("Case Study", font_size = 70).move_to(ORIGIN)
        smaller_title = Tex("Case Study: Pattaya", font_size = 40).to_corner(UL, buff = 0.5)

        bullet = [
            Tex(r"$\bullet$ 2.7km beach renourishment", font_size = 40),
            Tex(r"$\bullet$ 429 million THB project", font_size = 40),
            Tex(r"$\bullet$ Erosion rate $\approx 5 \frac{\mathrm{m}}{\mathrm{a}}$", font_size = 40),
            Tex(r"$\bullet$ Tourism", font_size = 40)
        ]
        VGroup(*bullet).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT, buff = 0.5).shift(UP * 0.8)

        self.wait(2)
        self.play(Write(title))
        self.wait(5)
        self.play(ReplacementTransform(title, smaller_title))
        self.wait(3)

        for item in bullet:
            self.play(Write(item))
            self.wait(2) 
        self.play(*[FadeOut(mob) for mob in self.mobjects])

        source = Tex("Source: Elle's iPhone camera", font_size = 20).to_corner(DR, buff = 0.5)

        self.play(FadeIn(source))
        self.wait(10)
        self.play(FadeOut(source))
        self.wait(2)

class quote(Scene):
    def construct(self):    
        quote = Tex("\"Without restoration and constant maintenance Pattaya beach was at risk of disappearing.\"", font_size=36)
        quote.move_to(ORIGIN).shift(UP)
        
        author = Tex(r"$-$ Mr Ekkarat Khanthano, the director of the 6th Marine Region office in Pattaya", font_size=32, color=YELLOW)
        author.next_to(quote, DOWN, buff=0.5)
        
        self.add(quote)

        self.play(Write(quote), run_time=3) 
        self.play(Write(author, shift=RIGHT * 0.2))
        self.wait(3) 
        self.play(FadeOut(VGroup(quote, author)))
        self.wait(0.5)

class conclusion(Scene):
    def construct(self):
        title = Tex("Conclusion", font_size = 70).move_to(ORIGIN)

        self.play(Write(title))
        self.wait(10)
        self.play(FadeOut(title))
        self.wait(2)