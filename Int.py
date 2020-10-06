#import necessary libraries
from manimlib.imports import *
import numpy as np

# Develop the graph and integration area under the curve
class Integral(GraphScene):
    CONFIG={
        'y_max':8,
        'y_axis_height':5
    }

    #define construction
    def construct(self):
        self.show_function_graph()

    #define functions
    def show_function_graph(self):
        self.setup_axes(animate = True)
        # Math function
        def func(x):
            return 0.1 * (x + 3-5) * (x- 3 - 5) * (x-5) + 5 # type function of choice

        #graph
        graph = self.get_graph(func, x_min=0.2, x_max=9)
        graph.set_color(YELLOW)

        #play graph
        self.play(ShowCreation(graph), run_time=3)
        self.wait(1)

        #Define rectangle function
        def rect(x):
            return x
        recta=self.get_graph(rect, x_min=-1, x_max=5)

        #adding reimann rectangle
        kwargs ={
            'x_min': 2,
            'x_max': 8,
            'fill_opacity': 0.75,
            'stroke_width': 0.25,
        }

        self.graph = graph
        interaciones = 6

        self.rect_list = self.get_riemann_rectangles_list(
            graph, interaciones, start_color=PURPLE_C, end_color = ORANGE, **kwargs
        )
        flat_rects = self.get_riemann_rectangles(
            self.get_graph(lambda x: 0), dx = 0.5, start_color=invert_color(PURPLE_C), end_color = invert_color(ORANGE), **kwargs
        )
        rects = self.rect_list[0]
        self.transform_between_riemann_rects(
            flat_rects, rects,
            replace_mobject_with_target_in_scene = True,
            run_time=5
        )

        #Loop
        for j in range(1,6):
            self.transform_between_riemann_rects(
                self.rect_list[j-1], self.rect_list[j], dx = 1,
                replace_mobject_with_target_in_scene = True,
                run_time=1.5
            )

        #Adding Text

        Sub=TextMobject("Riemann Rectangle").scale(1.3)
        Sub.next_to(graph, UP*1.8)
        # self.play(Sub.set_color_by_gradient, RED_D, YELLOW_A)
        self.play(FadeIn(Sub), Sub.set_color_by_gradient, RED_C, YELLOW_D, run_time = 3)
        self.wait(3)