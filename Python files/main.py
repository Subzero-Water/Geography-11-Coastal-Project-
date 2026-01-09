from manim import *

class Test(Scene):
    def construct(self):

        text = Tex("Hello World!")
        self.play(Write(text))
        self.wait(5)