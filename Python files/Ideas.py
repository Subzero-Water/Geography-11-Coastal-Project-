from manim import *

class Ideas(Scene):
    def construct(self):
        
        def empty_screen():
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
            
        title=MathTex(r"\text{Ideas for new strategies}").scale(2)
        SolText=MathTex(r"\text{Multiple other solutions!}").scale(2)
        
        self.play(Write(title))
        self.wait()
        self.play(Transform(title,SolText))
        self.wait()
        empty_screen()
        self.wait()
        
        HybText=Tex("Hybrid system").scale(1.5).to_corner(UL)
        ul1=Underline(HybText)
        hyb_system_bullet_points=[
        MathTex(r"\bullet \text{ Mangroves, oyster reefs, etc.").to_edge(LEFT*2).shift(UP*1.5),
        MathTex(r"\bullet \text{ Reduce wave energy}").to_edge(LEFT*2).shift(UP*0.5),
        MathTex(r"\bullet \text{ Economic upturn}").to_edge(LEFT*2).shift(DOWN*0.5)
        ]
        
        self.play(Write(HybText),Create(ul1))
        self.wait()
        for item in hyb_system_bullet_points:
            self.play(Write(item))
            self.wait()
        
        empty_screen()
        self.wait()
        
        DeiText=Tex(r"De-incentiving construction\\near coast").scale(2)
        DeiText2=Tex(r"De-incentivizing construction near coast").scale(1.25).to_corner(UL)
        ul2=Underline(DeiText2)
        dei_bullet_points=[
        MathTex(r"\bullet \text{ Silo exceptions}").to_edge(LEFT*2).shift(UP*1.5),
        MathTex(r'\bullet \text{ Introduce a "good and bad"}').to_edge(LEFT*2).shift(UP*0.5),
        MathTex(r"\bullet \text{ Higher taxes}").to_edge(LEFT*2).shift(DOWN*0.5),
        MathTex(r"\bullet \text{ Revocation of post-disaster rebuilding permits}").to_edge(LEFT*2).shift(DOWN*1.5)
        ]
        Par_Texts=[
        Tex(r"Construction in buffer zone").scale(1.25).shift(UP),
        MathTex(r"\models").scale(1.25),
        Tex(r"paradoxical reputation").scale(1.25).shift(DOWN)
        ]
        Group1=VGroup(*Par_Texts)
        
        self.play(Write(DeiText))
        self.wait()
        self.play(Transform(DeiText,DeiText2),Create(ul2))
        self.wait()
        for item in dei_bullet_points:
            self.play(Write(item))
            self.wait()
        empty_screen()
        self.wait()
        for item in Par_Texts:
            self.play(Write(item))
            self.wait()
        self.play(Unwrite(Group1,reverse=False))
        self.wait()
        