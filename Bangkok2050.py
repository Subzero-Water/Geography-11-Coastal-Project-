from manim import *

class Bangkok2050(Scene):
    def construct(self):
        BUFFER = 1  # seconds

        # Title
        title = Tex("What will Bangkok look like in 2050?").scale(1.5)
        self.play(Write(title), run_time=1.0)
        self.wait(BUFFER)

        self.play(FadeOut(title), run_time=0.6)
        self.wait(BUFFER)

        # Grid parameters
        box_size = 1.6
        gap = 0.2

        grid = VGroup(
            *[Square(side_length=box_size) for _ in range(9)]
        ).arrange_in_grid(
            rows=3,
            cols=3,
            buff=gap
        ).to_edge(UL, buff=1)

        boxes = VGroup()
        for i in range(9):
            square = Square(side_length=box_size)
            text = Tex(f"Sim. {i+1}").scale(0.6)
            text.move_to(square.get_center())
            box = VGroup(square, text)
            box.move_to(grid[i].get_center())
            boxes.add(box)

        # Boxes animation (3s)
        self.play(
            LaggedStart(
                *[FadeIn(box) for box in boxes],
                lag_ratio=0.08
            ),
            run_time=3.0
        )
        self.wait(BUFFER)

        # "Implies" arrow — moved further right
        implies_arrow = MathTex(r"\implies").scale(1.5)
        implies_arrow.next_to(boxes, RIGHT, buff=1.2)

        self.play(FadeIn(implies_arrow), run_time=0.6)
        self.wait(BUFFER)

        # Pan illusion
        scene_group = VGroup(boxes, implies_arrow)
        self.play(
            scene_group.animate.shift(LEFT * (config.frame_width + 1)),
            run_time=1.2,
            rate_func=smooth
        )
        self.wait(BUFFER)

        # --------------------
        # Left-aligned text scene
        # --------------------

        bullet1 = MathTex(r"\bullet \text{ Much more flooding}")
        bullet2 = MathTex(r"\bullet \text{ At times underwater}")

        bullet1.to_edge(LEFT, buff=1).shift(UP * 1.2)
        bullet2.align_to(bullet1, LEFT)
        bullet2.next_to(bullet1, DOWN, buff=0.4)

        self.play(Write(bullet1), run_time=0.8)
        self.wait(BUFFER)

        self.play(Write(bullet2), run_time=0.8)
        self.wait(BUFFER)

        # Merge into one statement
        unsafe_homes = MathTex(r"\bullet \text{ Unsafe homes}")
        unsafe_homes.move_to(bullet1.get_center())
        unsafe_homes.align_to(bullet1, LEFT)

        self.play(
            Transform(VGroup(bullet1, bullet2), unsafe_homes),
            run_time=1.0
        )
        self.wait(BUFFER)

        # Consequence lines
        rebuild_text = Tex(r"$\rightarrow$ Must be rebuilt")
        rebuild_text.align_to(unsafe_homes, LEFT)
        rebuild_text.next_to(unsafe_homes, DOWN, buff=0.5)

        self.play(Write(rebuild_text), run_time=0.8)
        self.wait(BUFFER)

        cost_text = Tex(r"$\implies$ Time and money expenditure")
        cost_text.to_edge(LEFT*1.2).shift(DOWN*0.575)


        self.play(Write(cost_text), run_time=0.8)
        self.wait(BUFFER)

        # Fade EVERYTHING out (including "Unsafe homes")
        
        self.play(
            *[FadeOut(mob) for mob in self.mobjects], # The * unpacks the list
            run_time=2 # Optional: control the duration
        )
        
        self.wait(BUFFER)

        notStonksImage = ImageMobject("notstonks.png").scale(0.375)
        self.play(FadeIn(notStonksImage))
        
        self.wait(BUFFER)
        
        self.play(FadeOut(notStonksImage))
        
        CapitalText=MathTex(r"\bullet \text{ Capital must be relocated}").to_edge(LEFT).shift(UP)
        TouristText=MathTex(r"\bullet \text{ Degraded touristic industry}").to_edge(LEFT)
        TouristSubText=Tex("30.3m visitors per year").to_edge(LEFT*2).shift(DOWN).scale(0.9)
        
        self.play(Write(CapitalText))
        self.play(Write(TouristText))
        self.play(Write(TouristSubText))
        
        Group1=VGroup(CapitalText, TouristText, TouristSubText)
        self.play(Unwrite(Group1, reverse=False))
        
        EndTitle=Tex(r"Soft Engineering Strategies\\[0.4em] in Thailand").scale(1.5)
        box=SurroundingRectangle(EndTitle, color=YELLOW, buff=MED_LARGE_BUFF)
        self.play(Write(EndTitle), Create(box))
        Group2=VGroup(EndTitle,box)
        self.play(Group2.animate.scale(0.00001))
        self.remove(Group2)
        self.wait(BUFFER)