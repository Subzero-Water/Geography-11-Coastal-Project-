from manim import *

class Setback(Scene):
    def construct(self):
        
        def empty_screen():
            self.play(*[FadeOut(mob) for mob in self.mobjects], run_time=2)
            
            
        # --------------------
        # Shoreline (outer circle)
        # --------------------
        shoreline = Circle(radius=2.4, color=WHITE)
        shoreline.to_edge(LEFT, buff=1)

        self.play(Create(shoreline))
        self.wait(1)

        # Shoreline label + arrow (tip on LEFT, text on RIGHT)
        shoreline_label = Tex("Shoreline").scale(0.7)
        shoreline_label.next_to(shoreline, RIGHT, buff=1)

        shoreline_arrow = Arrow(
            start=shoreline_label.get_left(),   # flat end (right side)
            end=shoreline.get_right(),           # tip touches circle (left side)
            buff=0,
            stroke_width=3
        )

        self.play(Create(shoreline_arrow), Write(shoreline_label))
        self.wait(1)

        self.play(FadeOut(shoreline_arrow), FadeOut(shoreline_label))
        self.wait(1)

        # --------------------
        # Buffer zone (yellow ring)
        # --------------------
        buffer_ring = Annulus(
            inner_radius=1.5,
            outer_radius=2.4,
            fill_color=YELLOW,
            fill_opacity=0.6,
            stroke_width=0
        ).move_to(shoreline.get_center())

        inner_boundary = Circle(radius=1.5, color=WHITE)
        inner_boundary.move_to(shoreline.get_center())

        self.play(FadeIn(buffer_ring), Create(inner_boundary))
        self.wait(1)

        # Buffer zone label + arrow
        buffer_label = Tex("Buffer zone").scale(0.7)
        buffer_label.next_to(shoreline, RIGHT, buff=1)

        # Arrow tip extends slightly INTO the buffer ring
        buffer_arrow = Arrow(
            start=buffer_label.get_left(),                      # flat end (right)
            end=shoreline.get_right() + LEFT * 0.25,            # tip inside ring
            buff=0,
            stroke_width=3
        )

        self.play(Create(buffer_arrow), Write(buffer_label))
        self.wait(1)

        self.play(FadeOut(buffer_arrow), FadeOut(buffer_label))
        self.wait(1)
        
        Bullet1=MathTex(r"\bullet \text{ Construction in buffer zone illegal}").shift(RIGHT*3).shift(UP*1.5)
        Bullet2=MathTex(r"\bullet \text{ No damage when coast shifts}").align_to(Bullet1,LEFT).shift(UP*0.5)
        
        self.play(Write(Bullet1))
        self.wait()
        self.play(Write(Bullet2))
        self.wait()
        empty_screen()
        self.wait()
        
        SetText=Tex("Setback").scale(1.75).to_edge(UP)
        ul1=Underline(SetText)
        Bullet3=MathTex(r"\bullet \text{ Multiple setback proposals, although lapsed}").to_edge(LEFT*2).shift(UP)
        Bullet4=MathTex(r"\bullet \text{ Not at all used}").to_edge(LEFT*2)
        Bullet5=MathTex(r"\bullet \text{ Managable problem turned chaotic}").to_edge(LEFT*2).shift(DOWN)
        AdvText=Tex("Advantages").scale(1.75).to_edge(UP)
        DisText=Tex("Disadvantages").scale(1.75).to_edge(UP)
        Bullet6=MathTex(r"\bullet \text{ Future-proof}").to_edge(LEFT*2).shift(UP*1.5)
        Bullet7=MathTex(r"\bullet \text{ Cheapest long-term solution}").to_edge(LEFT*2).shift(UP*0.5)
        Bullet8=MathTex(r"\bullet \text{ Strict enforcement necessary").to_edge(LEFT*2).shift(UP*1.5)
        Bullet9=MathTex(r"\implies \text{ Zoning laws} \land \text{corruption resistance}").to_edge(LEFT*2).shift(UP*0.5)
        
        self.play(Write(SetText),Create(ul1))
        self.wait()
        self.play(Write(Bullet3))
        self.wait()
        self.play(Write(Bullet4))
        self.wait()
        self.play(Write(Bullet5))
        self.wait()
        self.play(Transform(SetText,AdvText),Unwrite(Bullet4,reverse=False),Unwrite(Bullet5,reverse=False),Transform(Bullet3,Bullet6),Unwrite(ul1))
        self.wait()
        self.play(Write(Bullet7))
        self.wait()
        self.play(Transform(SetText,DisText),Unwrite(Bullet7,reverse=False),Transform(Bullet3,Bullet8))
        self.wait()
        self.play(Write(Bullet9))
        self.wait()
        empty_screen()
        self.wait()