#import necessary libs
from manimlib.imports import *
import numpy as np

#Develop Graph
class graphx(GraphScene):
    CONFIG={
        'x_min': -4,
        'x_max':4 ,
        'y_min': -2,
        'y_max': 2,
        'x_axis_label': '$x$',
        'y_axis_label': '$y$',
        'graph_origin': 0.5 * DOWN + 0 * LEFT,
    }

    #Defining graph function
    def show_function_graph(self):
        self.setup_axes()
        def func(x):
            return np.sin(x)

        def func2(x):
            return np.cos(x)

        graph_sin = self.get_graph(func, x_min=-np.pi, x_max=np.pi)
        graph_sin.set_color(RED)

        graph_cos = self.get_graph(func2, x_min=-np.pi, x_max=np.pi)
        graph_cos.set_color(YELLOW)

        #playing Graphs
        self.play(ShowCreation(graph_sin), run_time = 4)
        self.wait(3)
        self.play(ShowCreation(graph_cos), run_time=4)
        self.wait(3)

        #Add text
        text1=TextMobject('y=Sine(x)  y=cos(x)')
        text1.set_color(BLUE_C)
        text1.next_to(graph_cos, UP*1.9)
        text1.shift(1.5*UP)
        self.play(Write(text1))
        self.wait(3)

        #create a picture
        picture = Group(*self.mobjects)
        picture.scale(0.6).to_edge(LEFT, buff=SMALL_BUFF)
        manim = TextMobject('M', 'a', 'n', 'i', 'm').set_height(1.3).next_to(picture, RIGHT)
        manim.shift(DOWN*0.7)
        manim[0].set_color(TEAL)
        manim[1].set_color(GREEN)
        manim[2].set_color(YELLOW)
        manim[3].set_color(ORANGE)
        manim[4].set_color(RED)
        self.play(Write(manim), rate_func = rush_into, run_time = 3)
        self.wait(3)


    #Define construction
    def construct(self):
        self.show_function_graph()

