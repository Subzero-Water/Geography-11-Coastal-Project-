from manim import *
class Tyftrs(Scene):
    def construct(self):
        
        card=Tex("Thanks for watching!").scale(2)
        
        self.play(Write(card))
        self.wait()
        self.play(Unwrite(card,reverse=False))
        self.wait()
