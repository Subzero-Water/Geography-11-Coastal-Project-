from manim import *
import numpy as np

class OpeningQuote(Scene):
    def construct(self):

        title = Tex("Thailand Soft Engineering Strategies", font_size=60).move_to(ORIGIN).shift(UP*0.5)
        subtitle = Tex("A Manim production by: Elle, Manta, and Pie", font_size=35, color=BLUE).next_to(title, DOWN, buff=0.5)
        #banner = ManimBanner().scale(0.7).to_corner(UL, buff = 1.2)

        self.play(FadeIn(title, subtitle), run_time = 1)
        self.wait(2)
        #self.play(banner.create(run_time=1.5))

        self.play(FadeOut(VGroup(title, subtitle)))

        quote = Tex("\"You cannot escape the responsibility of tomorrow by evading it today.\"", font_size=36)
        quote.move_to(ORIGIN).shift(UP * 3)
        
        author = Tex(r"$-$ Abraham Lincoln", font_size=32, color=YELLOW)
        author.next_to(quote, DOWN, buff=0.5)
        author.shift(RIGHT * 3)
        
        self.add(quote)

        self.play(Write(quote), run_time=5)
        
        self.wait(1)
        self.play(
            Write(author, shift=RIGHT * 0.2), 
            run_time=3
        )
        self.wait(2)
        
        self.play(FadeOut(VGroup(quote, author)), run_time=1.5)
        self.wait(0.5)


class introduction(Scene):
    def construct(self):

        city = SVGMobject("City.svg").set_color(WHITE).move_to(ORIGIN).shift(LEFT * 1).scale(1.25)
        ground = Rectangle(width = 5.8, height = 2.25, stroke_width = 0).to_corner(DL).shift(RIGHT * 2.31).set_fill(DARK_BROWN, opacity = 1)
        water = Rectangle(width = 4, height = 1, stroke_width = 0).to_corner(DR).set_fill("#90D6FF", opacity = 1)

        vertices_ground = ground.get_vertices()
        vertices_water = water.get_vertices()
        trapezoid = Polygon(vertices_ground[0], vertices_ground[3], vertices_water[2], vertices_water[1], stroke_width = 0).set_fill(DARK_BROWN, opacity = 1)


        wave_amount = 6
        waves = [] 

        for i in range(wave_amount):
            waves.append(FunctionGraph(
                lambda x: (-0.075 + 0.015 * i ) * np.cos(4 * PI * x),
                x_range = [0,4],
                color = "#90D6FF"
            ).to_corner(DR).shift(UP * 1))

        height_arrow = DoubleArrow(
            start = vertices_ground[0], 
            end = vertices_ground[3],
            stroke_width = 2,
            max_tip_length_to_length_ratio=0.1)
        sinking_vect = Arrow(
            start = UP, 
            end = DOWN/2, 
            color = RED,
            stroke_width = 2,
            max_tip_length_to_length_ratio=0.1).next_to(height_arrow, LEFT * 15).shift(UP * 0.62)

        rising_vect = Arrow(
            start = DOWN,
            end = UP/2, 
            color = "#03AC13",
            stroke_width = 2,
            max_tip_length_to_length_ratio=0.1).next_to(height_arrow, RIGHT * 7).shift(UP * 0.52)

        challenged_text = Tex("Geographically challenged!", font_size = 55, color = RED).to_edge(UP, buff = 1)
        height_arrow_text = Tex(r"$\bar{h} = 1.5$m", font_size = 25).next_to(height_arrow, LEFT)
        sinking_vect_text = Tex(r"$1,2 \frac{\mathrm{cm}}{\mathrm{a}}$", font_size = 25).next_to(sinking_vect, RIGHT)
        rising_vect_text = Tex(r"$10 \frac{\mathrm{mm}}{\mathrm{a}}$", font_size = 25).next_to(rising_vect, RIGHT)
        disclaimer = Tex(r"$^*$Please note that the norms \\ of the vectors are not to scale.", font_size = 15).to_corner(UR, buff = 0.75)

        doomsday_year = Tex("2050", color = RED, font_size = 90).move_to(ORIGIN)
        doomsday_text = Tex("Predicted Doomsday:", color = RED, font_size = 60).next_to(doomsday_year, UP)


        self.play(FadeIn(city, ground, water, trapezoid),
                  *[FadeIn(wave) for wave in waves])  # Note: The atterix is the oeprator for unpacking lists using for loops so that each of them can be faded in by manim.
        self.wait(4)

        self.play(Write(challenged_text))
        self.wait(3)
        self.play(FadeOut(challenged_text))
        self.play(Create(height_arrow))
        self.wait(0.5)
        self.play(Write(disclaimer), Write(height_arrow_text))
        self.wait(3)
        self.play(Create(sinking_vect), Write(sinking_vect_text))
        self.wait(1.5)
        self.play(Create(rising_vect), Write(rising_vect_text))
        self.wait(7)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait(1.5)

        self.play(FadeIn(doomsday_year, doomsday_text), run_time = 6)
        self.wait(4)
        self.play(FadeOut(VGroup(doomsday_text, doomsday_year)))
        self.wait(2)

class lessonOverview(Scene):
    def construct(self):   
      self.wait(2)

      title = Tex("Lesson Overview", font_size=36*1.5, color=WHITE)
      title.to_corner(UL, buff=0.5)
      self.play(FadeIn(title))
      self.wait(1)
   
      items = [
          Tex("1. Preliminary discussion on importance", font_size=54, color=WHITE),
          Tex("2. Soft engineering", font_size=54, color=WHITE),
          Tex("3. Look into the future", font_size=54, color=WHITE)
      ]
      group = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
   
      group.to_edge(LEFT, buff=1.2).shift(UP * 0.8)
      self.play(FadeIn(group))
   
      for item in items:
          self.play(item.animate.scale(1.2).set_color(YELLOW), run_time=0.5)
          self.wait(3)
          self.play(item.animate.scale(1/1.2).set_color(WHITE), run_time=0.5)
          self.wait(0.5)
   
      self.play(FadeOut(group), FadeOut(title))
      self.wait(1)
   