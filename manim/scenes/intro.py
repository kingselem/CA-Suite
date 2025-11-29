from manim import *

class HelloEngineer(Scene):
    def construct(self):
        # 1. Create a Title
        title = Text("The CA Suite", font_size=40, color=BLUE)
        subtitle = Text("Mechanical Engineering Portfolio", font_size=24, color=WHITE)
        subtitle.next_to(title, DOWN)

        # 2. Create Shapes (Engineering Metaphor)
        # A Square (Raw Stock) turning into a Circle (Finished Part)
        square = Square(side_length=2.0, color=RED)
        circle = Circle(radius=1.0, color=GREEN)

        # 3. Animation Sequence
        self.play(Write(title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        
        self.play(FadeOut(title), FadeOut(subtitle))
        
        self.play(Create(square))
        self.play(Rotate(square, angle=PI/2))
        
        # Morph the square into a circle
        self.play(Transform(square, circle))
        self.play(Indicate(square)) # Flash the final shape
        
        self.wait(2)