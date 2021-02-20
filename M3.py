import numpy as np 
from graphics import *

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
            p=[self.transition_matrix[current_color][next_color] \
                for next_color in self.colors]

        )

    


    

