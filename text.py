from manimlib.imports import *
import numpy as np

class helloWorld(Scene):
    def construct(self):
        T = TextMobject('Hello World')
        self.play(Write(T), run_time = 4)
        self.wait()

        circle = Circle()
        square = Square()
        line = Line(np.array([4, 0, 0]), np.array([6, 0, 0]))
        triangle = Polygon(np.array([0, 0, 0]), np.array([1, 1, 0]), np.array([-1, -1, 0]))
        self.play(ShowCreation(circle), run_time = 4)
        self.play(ShowCreation(square), run_time=3)
        self.play(ShowCreation(line), run_time=2)
        self.play(ShowCreation(triangle), run_time=1)

class moveToscene(Scene):
    def construct(self):
        s = Circle()
        self.play(s.shift, DL)
        self.wait()


class moveTonxtObject(Scene):
    def construct(self):
        h = TextMobject('Hello')
        h.to_edge(UP)
        # i = TextMobject('Ed')
        # i.to_edge(DOWN)

        s = Square()
        s.next_to(h, DOWN)
        # s.next_to(i, DOWN)

        sandt = VGroup(h, s)

        self.play(sandt.rotate, PI / 2, run_time = 4)
        self.play(sandt.shift, 5*DR)

        self.add(h, s)
        self.wait()

class colorChange(Scene):
    def construct(self):
        t = TextMobject("Color changing Pandas")

        t.set_color(PURPLE_C)
        self.play(t.scale, 2)

        self.play(t.set_color_by_gradient, RED_D, YELLOW_A)

        self.wait()

class rainbow (Scene):
    def construct(self):
        r = TextMobject('J', 'O', "H", 'N', 'S', 'O', 'N')
        r[0].set_color(RED)
        r[1].set_color(ORANGE)
        r[2].set_color(YELLOW)
        r[3].set_color(GREEN)
        r[4].set_color(TEAL)
        r[5].set_color(BLUE)
        r[6].set_color(PURPLE)

        self.play(Write(r), run_time = 6)

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
