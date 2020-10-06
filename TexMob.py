from manimlib.imports import *
import numpy as np

class TestScene(Scene):
    def construct(self):
        eq = TextMobject(r"The integral is \( \int_a^b f(x) dx  \)")
        eq.scale(2)

        self.play(Write(eq))
        self.wait(3)


class work(Scene):
    def construct(self):
        w = TexMobject(r'W(',r's',r') = \int\vec{F}(', r's', r')\cdot d\vec{',r's',r'}')
        w[1].set_color(YELLOW)
        w[3].set_color(YELLOW)
        w[5].set_color(YELLOW)
        self.play(Write(w), run_time = 5)


class boxAndCross(Scene):
    def construct(self):
        SE = TexMobject(r"i\hbar\frac{\partial \Psi }{\partial x} (r,t) = ", r"\hat{H}\Psi (r, t)")
        box = SurroundingRectangle(SE[1])


        box.set_stroke(GREEN, 7)

        cross = Cross(SE[0])
        cross.set_stroke(RED)

        SGroup = VGroup(SE, box, cross)

        self.play(ShowCreation(SGroup), run_time =5)

