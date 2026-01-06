from manim import *

class definition(Scene):
    def construct(self):
        
        definition = Tex(r"\textbf{Definition} (Soft Engineering). Protection of coastlines by working", font_size = 40).to_edge(UP, buff = 0.5)
        definition_part2 = Tex(r"with natural processes.", font_size = 40).next_to(definition, DOWN, buff = 0.2).to_edge(LEFT, buff = 1)
        source = Tex("Source: British Broadcasting Corporation (BBC)", font_size = 25).to_corner(DR, buff = 0.2)

        self.wait(2)
        self.play(Write(definition), Write(definition_part2), Write(source))
        self.wait(4)
        self.play(FadeOut(VGroup(definition, definition_part2, source)))
        self.wait(2)