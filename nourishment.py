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
        return


class dune(Scene):
    def construct(self):
        return

class example(Scene):
    def construct(self):
        return

class conclusion(Scene):
    def construct(self):
        return