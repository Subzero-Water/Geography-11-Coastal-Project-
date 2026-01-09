from manim import *

class introduction(Scene):
    def construct(self):

        title = Tex("Vetiver Grass", font_size = 60)
        source = Tex("Source: greenmeadowgrowers.com", font_size = 25).to_corner(DR, buff = 0.5)
        template = VGroup(title, source)

        slide_1 = [
            Tex(r"$\bullet$ Plant with deep and strong root system (2-3m)", font_size = 35),
            Tex(r"$\Rightarrow$ Increased strength, reduced coastal erosion", font_size = 35),
            Tex(r"$\bullet$ Slows surface runoff, traps sediment,\\ reduces erosive power of water", font_size = 35)
        ]
        VGroup(slide_1).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT).shift(UP * 1.5)

        slide_2 = [
            Tex(r"$\bullet$ Exceptional root strength", font_size = 35),
            Tex(r"$\bullet$ Flooding", font_size = 35),
            Tex(r"$\bullet$ Drought", font_size = 35),
            Tex(r"$\bullet$ Salinity", font_size = 35),
            Tex(r"$\bullet$ Extreme temperatures", font_size = 35),
            Tex(r"$\bullet$ Poor soil conditions", font_size = 35),
            Tex(r"$\Rightarrow$ Good for tropical coastal environments", font_size = 35)
        ]
        VGroup(slide_2).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT)

        slide_3 = [
            Tex(r"$\bullet$ Not widely implemented", font_size = 35),
            Tex(r"$\bullet$ Beneficial if combined with other vegetation", font_size = 35),
            Tex(r"$\bullet$ Exempli gratia: Coconut trees", font_size = 35),
            Tex(r"$\bullet$ More sustainable", font_size = 35), 
        ]
        VGroup(slide_3).arrange(DOWN, aligned_edge = LEFT, buff = 0.4).to_edge(LEFT).shift(UP * 1.5)

        set_of_slides = [slide_1, slide_2, slide_3]

        self.wait()
        self.play(Write(title))
        self.wait()
        self.play(title.animate.scale(2/3).to_corner(UL, buff = 0.5), Write(source))
        self.wait()
        
        for slide in set_of_slides:
            for information in slide:
                self.play(Write(information))
                self.wait()
            self.play(FadeOut(*slide))
            self.wait()
        self.play(FadeOut(template))
        self.wait()