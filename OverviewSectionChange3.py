from manim import *
class Change(Scene):
    def construct(self):
        
        title = Tex("Lesson Overview", font_size=36*1.5, color=WHITE)
        title.to_corner(UL, buff=0.5)
        section_title = Tex(r"$\S$3. Look into the future", font_size = 60).move_to(ORIGIN)
        items = [
          Tex("1. Preliminary discussion on importance", font_size=54, color=WHITE),
          Tex("2. Soft engineering", font_size=54, color=WHITE),
          Tex("3. Look into the future", font_size=54, color=YELLOW)
        ]
        agenda = VGroup(*items).arrange(DOWN, aligned_edge=LEFT, buff=0.4).to_edge(LEFT).shift(UP * 1)

        self.wait(1)
        self.play(FadeIn(agenda, title))
        self.wait(2)
        self.play(ReplacementTransform(VGroup(agenda, title), section_title))
        self.wait(2)
        self.play(FadeOut(section_title))
        self.wait(2)