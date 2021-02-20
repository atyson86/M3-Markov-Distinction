import numpy as np 
from graphics import *


COLOR_MATRIX = {
    "red": {"red": 0.10, "yellow": 0.30, "blue": 0.20, "green": 0.05, "cyan": 0.35},
    "yellow": {"red": 0.20, "yellow": 0.10, "blue": 0.50, "green": 0.10, "cyan": 0.10},
    "blue": {"red": 0.30, "yellow": 0.30, "blue": 0.10, "green": 0.20, "cyan": 0.10},
    "green": {"red": 0.05, "yellow": 0.25, "blue": 0.40, "green": 0.05, "cyan": 0.25},
    "cyan": {"red": 0.20, "yellow": 0.20, "blue": 0.20, "green": 0.20, "cyan": 0.20}

}

SHAPE_MATRIX = {
    "Rectange": {"Rectangle": 0.25, "Circle": 0.25, "Oval": 0.30, "Triangle": 0.20},
    "Circle": {"Rectangle": 0.15, "Circle": 0.30, "Oval": 0.40, "Triangle": 0.15},
    "Oval": {"Rectangle": 0.25, "Circle": 0.25, "Oval": 0.25, "Triangle": 0.25},
    "Triangle": {"Rectangle": 0.10, "Circle": 0.10, "Oval": 0.70, "Triangle": 0.10}

}

class MarkovArtist:
    def __init__(self, transition_color_matrix, transition_shape_matrix):
        """Simulates an artist that utilizes a Markov Chain

        Args:
            transition_matrix (dict): transition probabilities
        """

        self.transition_color_matrix = transition_color_matrix
        self.transition_shape_matrix = transition_shape_matrix
        self.colors = list(transition_color_matrix.keys())
        self.shapes = list(transition_shape_matrix.keys())

    def get_next_color(self, current_color):
        """Decides which color to paint with next based on the current color.

        Args:
            current_color (str): The current color being used
        """
        return np.random.choice(
            self.colors,
            p=[self.transition_color_matrix[current_color][next_color] \
                for next_color in self.colors]

        )

    def get_next_shape(self, current_shape):
        """Decides which shape to draw next based on the current shape.

        Args:
            current_shape (str): The current shape being drawn
        """

        return np.random.choice(
            self.shapes,
            p=[self.transition_shape_matrix[current_shape][next_shape] \
                for next_shape in self.shapes]
        )



def main():
    win = GraphWin('Masterpiece', 500, 500)

    pt = Point(100, 50)
    cir = Circle(pt, 50)
    cir.draw(win)

    cir.setOutline("blue")
    cir.setFill("cyan")
    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()


    


    

