from manim import *

class hope(Scene):
    def construct(self):

        question = Tex("Is there hope?", font_size = 50)

        bullet_points = [
            Tex(r"$\bullet$ Absolutely possible", font_size = 35),
            Tex(r"$\bullet$ Multiple strategies", font_size = 35),
            Tex(r"$\bullet$ Consistency", font_size = 35, color = YELLOW),
            Tex(r"$\bullet$ Focused on urban areas, rejecting rural areas", font_size = 35),
            Tex(r"$\Rightarrow$ Small scale projects", font_size = 35)
        ]
        VGroup(bullet_points).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT).shift(UP * 1)

        self.wait()
        self.play(Write(question))
        self.wait()
        self.play(question.animate.scale(0.8).to_corner(UL, buff = 0.5))
        self.wait()

        for bullet in bullet_points:
            self.play(Write(bullet))
            self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.wait()

class conclusion(Scene):
    def construct(self):
 
        title = Tex("Conclusion", font_size = 50)
   
        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(Unwrite(title), reversed = False)
        self.wait()