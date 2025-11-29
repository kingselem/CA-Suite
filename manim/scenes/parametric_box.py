from manim import *
import json
import os

class ParametricBox(Scene):
    def construct(self):
        # 1. Load the Single Source of Truth
        # We look 2 folders up: manim/scenes -> manim -> CA-Suite -> config
        config_path = os.path.join("config", "design_specs.json")
        
        with open(config_path, "r") as f:
            specs = json.load(f)
        
        # 2. Read the variable
        side_len = specs["side_length"]
        
        # 3. Create Geometry (Scale down 1/20 for screen)
        # If side_len is 75, box is 3.75 units wide
        box = Square(side_length=side_len / 20.0, color=BLUE)
        
        # 4. Create Dynamic Label
        label = Text(f"Parametric Width: {side_len} mm", font_size=40)
        label.next_to(box, UP)
        
        # 5. Animate
        self.play(Create(box))
        self.play(Write(label))
        self.wait(2)
