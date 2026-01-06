from manim import *

class Plans(Scene):
    def construct(self):
        
        def empty_screen():
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
        
        titleText=Tex(r"Look into Future\\(Planned Projects)").scale(2)
        ArtText=Tex(r"Artifical Mangrove Roots (AMRs)").scale(1.5).to_corner(UL)
        ul1=Underline(ArtText)
        amr_bullet_points=[
        MathTex(r"\bullet \text{ Positive results}").to_edge(LEFT*2).shift(UP*1.5),
        MathTex(r"\bullet \text{ Mimic mangrove roots}").to_edge(LEFT*2).shift(UP*0.5),
        MathTex(r"\bullet \text{ Stil reduce wave energy}").to_edge(LEFT*2).shift(DOWN*0.5),
        MathTex(r"\bullet \text{ Takes much less time}").to_edge(LEFT*2).shift(DOWN*1.5)
        ]
        Group1=VGroup(amr_bullet_points)
        PosText=Tex(r"Has potential!").scale(2.5)

        self.play(Write(titleText))
        self.wait()
        self.play(Transform(titleText,ArtText),Create(ul1))
        for item in amr_bullet_points:
            self.play(Write(item))
            self.wait()
        self.play(Unwrite(Group1,reverse=False),Unwrite(titleText,reverse=False),Uncreate(ul1))
        self.wait()
        self.play(Write(PosText),run_time=2)
        self.wait()
        empty_screen()
        self.wait()
        
        DMCR=Tex(r"Department of Marine\\and Coastal Resources").scale(2)
        DMCR2=Tex(r"DMCR").scale(1.5).to_corner(UL)
        ul2=Underline(DMCR2)
        Bullet1=Tex(r"$\bullet$ Restoration of 800 km$^2$ of mangroves").to_edge(LEFT*2).shift(UP*1.5)
        Par_Texts=[
        Tex(r"More progress").shift(UP*2),
        Tex(r"=").shift(UP*1),
        Tex(r"more participants"),
        Tex(r"=").shift(DOWN*1),
        Tex(r"more progress").shift(DOWN*2)
        ]
        Group2=VGroup(*Par_Texts)
        Par_Texts2=[
        Tex(r"More progress").shift(UP*2).to_edge(LEFT*2),
        Tex(r"=").shift(UP*1).to_edge(LEFT*2),
        Tex(r"more participants").to_edge(LEFT*2),
        Tex(r"=").shift(DOWN*1).to_edge(LEFT*2),
        Tex(r"more progress").shift(DOWN*2).to_edge(LEFT*2)
        ]
        Group3=VGroup(*Par_Texts2)
        
        self.play(Write(DMCR))
        self.wait()
        self.play(Transform(DMCR,DMCR2),Create(ul2))
        self.wait()
        self.play(Write(Bullet1))
        self.wait()
        empty_screen()
        self.wait()
        for item in Par_Texts:
            self.play(Write(item))
            self.wait()
        self.play(Transform(Group2,Group3))
        self.wait()
        
        vt=ValueTracker(0)
        ax=Axes(x_range=[-5,5,1],y_range=[-10,700,100])
        f=lambda x: x**4
        func=always_redraw(lambda: ax.plot(f,color=YELLOW,x_range=[0,vt.get_value()]))
        funcdot=always_redraw(lambda: Dot(ax.c2p(vt.get_value(),f(vt.get_value())),color=YELLOW))
        x_label = ax.get_x_axis_label(Tex("Amount of people")).shift(DOWN)
        y_label = ax.get_y_axis_label(Tex("Progress in mitigating coastal erosion"))
        
        self.play(Create(ax))
        self.wait()
        self.play(Write(x_label),Write(y_label))
        self.wait()
        self.add(func,funcdot)
        self.wait()
        self.play(vt.animate.set_value(5),run_time=6)
        self.wait()
        empty_screen()
        self.wait()