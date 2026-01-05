from manim import *

class Mangroves(Scene):
    def construct(self):
        
        MangroveARText=Tex(r"Mangrove Afforestation\\[0.4em] and Reforestation").scale(1.75)
        MangroveARText2=Tex(r"Mangrove Aff. and Ref.").scale(1.5).to_edge(UP)
        ul1=Underline(MangroveARText2)
        
        self.play(Write(MangroveARText))
        self.wait()
        self.play(Transform(MangroveARText,MangroveARText2))
        self.wait()
        self.play(Write(ul1))
        self.wait()
        
        Bullet1=MathTex(r"\bullet \text{ Small to medium trees}").to_edge(LEFT*2).shift(UP*1.5)
        Bullet2=MathTex(r"\bullet \text{ Grow in brackish water}").to_edge(LEFT*2).shift(UP*0.5)
        
        self.play(Write(Bullet1))
        self.wait()
        self.play(Write(Bullet2))
        self.wait()
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        
        vt = ValueTracker(0.2)
        ax = Axes(
            x_range=[0.1, 5, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=4,
            tips=False,
            axis_config={"stroke_width": 2}
        )
        ax.scale(1.3)
        f = lambda x: 1 / x
        function1 = always_redraw(lambda: ax.plot(f,x_range=[0.2, vt.get_value(), 0.02],color=YELLOW,use_smoothing=False))
        function1dot = always_redraw(lambda: Dot(ax.c2p(vt.get_value(), f(vt.get_value())),color=YELLOW))

        x_label=ax.get_x_axis_label(Tex("Amount of Mangroves"))
        x_label.scale(0.6).shift(DOWN*0.75)
        y_label=ax.get_y_axis_label(Tex("Water Velocity and Wave Energy"))
        y_label.scale(0.6).shift(LEFT*2.5)

        self.play(Create(ax),Write(x_label),Write(y_label))
        self.add(function1, function1dot)
        self.play(vt.animate.set_value(5), run_time=5, rate_func=smooth)
        self.play(FadeOut(function1dot))
        self.wait()

        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)

        AdvText=Tex("Advantages").shift(UP*1.2).scale(2)
        DisText=Tex("Disadvantages?").shift(DOWN*1.2).scale(2)
        GreText=Text(">").scale(1.5)
        LesText=Text("<").scale(1.5)
        
        self.play(Write(AdvText), Write(DisText), Write(GreText))
        self.wait()
        self.play(Transform(GreText,LesText))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        
        DichoText = MathTex(r"\text{Aff.} \neq \neg \text{Ref.}").scale(2)
        
        self.play(Write(DichoText), run_time=2)
        self.wait()
        self.play(Unwrite(DichoText, reverse=False))
        self.wait()
        
        AffText=Tex("Mangrove Afforestation").scale(1.5).to_edge(UP)
        Bullet3=MathTex(r"\bullet \text{ Planting trees}").to_edge(LEFT*2).shift(UP*1.5)
        Bullet4=MathTex(r"\bullet \text{ Heavily dependent on miscellaneous factors}").to_edge(LEFT*2).shift(UP*0.5)
        Bullet5=MathTex(r"\bullet \text{ Sustainability} \neq 100\%").to_edge(LEFT*2).shift(DOWN*0.5)
        Bullet6=MathTex(r"\bullet \text{ Generally fails}").to_edge(LEFT*2).shift(DOWN*1.5)
        
        self.play(Write(AffText))
        self.wait()
        self.play(Write(Bullet3))
        self.wait()
        self.play(Write(Bullet4))
        self.wait()
        self.play(Write(Bullet5))
        self.wait()
        self.play(Write(Bullet6))
        self.wait()
        
        Group1=VGroup(AffText,Bullet3,Bullet4,Bullet5,Bullet6)
        ResText=Tex("Mangrove Restoration").scale(2)
        box=SurroundingRectangle(ResText,color=YELLOW,buff=MED_LARGE_BUFF)
        
        self.play(Transform(Group1,ResText))
        self.wait()
        self.play(Create(box))
        self.wait()
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        
        AffText2=Tex("Mangrove Afforestation").scale(2)
        self.play(Write(AffText2))
        cross=Cross(AffText2)
        self.wait()
        self.play(Create(cross))
        self.wait()
        self.play(Transform(AffText2,ResText), FadeOut(cross))
        self.wait()
        self.play(Unwrite(AffText2, reverse=False))
        self.wait()
        
        ResText2=Tex("Mangrove Restoration").scale(1.5)
        Bullet7=MathTex(r"\bullet \text{ Reinstating mangroves}").to_edge(LEFT*2).shift(UP*1.5)
        Bullet8=MathTex(r"\bullet \text{ Reinvesting into tidal flow and sediment supply}").to_edge(LEFT*2).shift(UP*0.5)
        Group2=VGroup(ResText2,Bullet7,Bullet8)
        
        self.play(Write(ResText2))
        self.wait()
        self.play(ResText2.animate.to_edge(UP))
        self.wait()
        self.play(Write(Bullet7))
        self.wait()
        self.play(Write(Bullet8))
        self.wait()
        
        self.play(Group2.animate.shift(DOWN*(config.frame_width+1)),run_time=1.5,rate_func=smooth)
        
        DisText2=Tex("Disadvantages").scale(1.5).to_edge(UP)
        Bullet9=MathTex(r"\bullet \text{ Non-adaptive}").to_edge(LEFT*2).shift(UP*1.5)
        Bullet10=MathTex(r"\implies \text{ You can't restore nothing}").to_edge(LEFT*2).shift(UP*0.5)
        Bullet11=MathTex(r"\bullet \text{ Cannot grow in non-tropical,subtropical coastal areas}").to_edge(LEFT*2).shift(DOWN*0.5)
        
        self.play(Write(DisText2))
        self.wait()
        self.play(Write(Bullet9))
        self.wait()
        self.play(Write(Bullet10))
        self.wait()
        self.play(Write(Bullet11))
        self.wait()
        
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        
        AffText3=Tex("Mangrove Afforestation").scale(1.5).to_edge(UP)
        Bullet12=MathTex(r"\bullet \text{ Self-sabotaging prospects}").to_edge(LEFT*2).shift(UP*1.5)
        EndTitle=MathTex(r"\text{Aff.} < \text{Res.}").scale(2)
        
        self.play(Write(AffText3))
        self.wait()
        self.play(Write(Bullet12))
        self.wait()
        self.play(Transform(AffText3,EndTitle), FadeOut(Bullet12))
        self.wait()
        self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        self.wait()