# Import libs
from manimlib.imports import *

class Logo(Scene):
    CONFIG = {
        "camera_config":{"background_color":BLACK}
    }

    def construct(self):
        #logo
        circle_logo=Circle(fill_opacity = 300).scale(2)
        circle_logo.set_fill()
        circle_logo.set_color(MAROON_D)
        # circle1 = Circle
        txt=TextMobject('Bloom','E', 'D').scale(0.8)
        txt[0].set_color(GOLD_A)
        txt[1].set_color(RED_D)
        txt[2].set_color(YELLOW_A)
        txt.next_to(circle_logo, 0, buff = 0).scale(2)
        self.play(DrawBorderThenFill(circle_logo, run_time=6), Write(txt, run_time=3))
        self.wait(1)

        #scaling logo and moving down
        txt.scale(0.15)
        circle_logo2=circle_logo.scale(0.15)
        circle_logo2.to_corner(DR)
        txt2=txt.next_to(circle_logo, 0, buff=0)

        self.play(Write(circle_logo2), Write(txt2))
        self.wait(1)

        # LATER TEXT
        abo=TextMobject('ABOUT US').to_edge(UP).scale(0.8)
        abo.to_edge(LEFT)
        txt3=TextMobject('1. BloomED, a startup by an MIT alumnus and the Founder of Bloom Nepal School.').next_to(abo, DOWN, buff=0.5).scale(0.8)
        txt3.to_edge(LEFT)
        txt4 = TextMobject('2. We provide free educational courses to Nepalese students in the style of edX/Udemy.').next_to(txt3, DOWN, buff=0.5).scale(0.8)
        txt4.to_edge(LEFT)
        txt5 = TextMobject('3. BloomED strives to fill the void in quality education through interactive and comprehendible notes.').next_to(txt4, DOWN, buff=0.5).scale(0.8)
        txt5.to_edge(LEFT)
        txt6 = TextMobject('4. BloomED is working to benefit everyone from top students to underprivileged ones through freely accessible notes. ').next_to(txt5, DOWN, buff = 0.5).scale(0.8)
        txt6.to_edge(LEFT)

        #play
        self.play(Write(abo), rate_func=rush_into)
        self.play(Write(txt3), run_time = 5)
        self.play(txt3.set_color_by_gradient, RED_D, YELLOW_A)
        self.play(Write(txt4), run_time = 6)
        self.play(txt4.set_color_by_gradient, RED_D, YELLOW_A)
        self.play(Write(txt5), run_time = 7)
        self.play(txt5.set_color_by_gradient, RED_D, YELLOW_A)
        self.play(Write(txt6), run_time = 8)
        self.play(txt6.set_color_by_gradient, RED_D, YELLOW_A)
        self.wait(4)