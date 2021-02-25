import numpy as np 
from graphics import *


COLOR_MATRIX = {
    "red": {"red": 0.10, "yellow": 0.10, "blue": 0.10, "green": 0.10, \
        "cyan": 0.10, "pink": 0.10, "orange": 0.10, "purple": 0.10, \
             "black": 0.10, "white": 0.10},
    "yellow": {"red": 0.15, "yellow": 0.10, "blue": 0.20, "green": 0.10, \
         "cyan": 0.10, "pink": 0.10, "orange": 0.10, "purple": 0.05, \
             "black": 0.05, "white": 0.05},
    "blue": {"red": 0.10, "yellow": 0.10, "blue": 0.10, "green": 0.10, \
        "cyan": 0.10, "pink": 0.15, "orange": 0.20, "purple": 0.05, \
            "black": 0.05, "white": 0.05},
    "green": {"red": 0.05, "yellow": 0.25, "blue": 0.10, "green": 0.05, \
        "cyan": 0.25, "pink": 0.05, "orange": 0.05, "purple": 0.05, \
            "black": 0.10, "white": 0.05},
    "cyan": {"red": 0.20, "yellow": 0.05, "blue": 0.20, "green": 0.20, \
        "cyan": 0.10, "pink": 0.05, "orange": 0.05, "purple": 0.05, \
            "black": 0.05, "white": 0.05},
    "pink": {"red": 0.05, "yellow": 0.05, "blue": 0.05, "green": 0.05, \
        "cyan": 0.05, "pink": 0.05, "orange": 0.20, "purple": 0.05, \
            "black": 0.15, "white": 0.30},
    "orange": {"red": 0.10, "yellow": 0.05, "blue": 0.05, "green": 0.00, \
        "cyan": 0.05, "pink": 0.25, "orange": 0.05, "purple": 0.10, \
            "black": 0.30, "white": 0.05},
    "purple": {"red": 0.10, "yellow": 0.10, "blue": 0.10, "green": 0.10, \
        "cyan": 0.10, "pink": 0.10, "orange": 0.10, "purple": 0.10, \
            "black": 0.10, "white": 0.10},
    "black": {"red": 0.20, "yellow": 0.05, "blue": 0.10, "green": 0.05, \
        "cyan": 0.00, "pink": 0.10, "orange": 0.20, "purple": 0.10, \
            "black": 0.10, "white": 0.10},
    "white": {"red": 0.05, "yellow": 0.05, "blue": 0.20, "green": 0.05, \
        "cyan": 0.10, "pink": 0.05, "orange": 0.05, "purple": 0.20, \
            "black": 0.20, "white": 0.05}

}

SHAPE_MATRIX = {
    "Rectangle": {"Rectangle": 0.25, "Circle": 0.25, "Oval": 0.30, \
        "Triangle": 0.20},
    "Circle": {"Rectangle": 0.15, "Circle": 0.30, "Oval": 0.40, \
         "Triangle": 0.15},
    "Oval": {"Rectangle": 0.25, "Circle": 0.25, "Oval": 0.25, \
         "Triangle": 0.25},
    "Triangle": {"Rectangle": 0.10, "Circle": 0.10, "Oval": 0.70, \
         "Triangle": 0.10}

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

    def make_shapes(self, current_shape='Rectangle', current_color='red', \
        total_shapes=15):
        """returns a dictionary that contains a series of different shapes
            with different outlines and fill colors

        Args:
             current_shape (str): The current shape that has been recorded
             current_color (str): The current color used for the outline and fill
             total_shapes (int): The total number of shapes that will be added to 
                the dictionary
        """

        shapes_dict = {"shape": [], "outline_color": [], "fill_color": []}
        count = 0

        while count < total_shapes:
            next_shape = self.get_next_shape(current_shape)
            next_color1 = self.get_next_color(current_color)
            current_color = next_color1
            next_color2 = self.get_next_color(current_color)
            current_shape = next_shape
            current_color = next_color2

            shapes_dict["shape"].append(next_shape)
            shapes_dict["outline_color"].append(next_color1)
            shapes_dict["fill_color"].append(next_color2)

            count+=1

        return shapes_dict

    def draw_masterpiece(self, shapes_dict, border1, border2, current_color='red'):
        win = GraphWin('Masterpiece', border1, border2)
        background_color = self.get_next_color(current_color)
        win.setBackground(background_color)

        list_of_shapes = shapes_dict.get("shape")
        list_of_outline_colors = shapes_dict.get("outline_color")
        list_of_fill_colors = shapes_dict.get("fill_color")

        total_shapes = len(list_of_shapes)

        for i in range(total_shapes):
            working_shape = list_of_shapes[i]
            if (working_shape == "Rectangle"):
                pt1 = Point(np.random.randint(border1), np.random.randint(border2))
                pt2 = Point(np.random.randint(border1), np.random.randint(border2))
                rect = Rectangle(pt1, pt2)

                rect.setOutline(list_of_outline_colors[i])
                rect.setFill(list_of_fill_colors[i])

                rect.draw(win)

            elif (working_shape == "Circle"):
                pt1 = Point(np.random.randint(border1), np.random.randint(border2))
                radius = np.random.randint((border1 - 1) / 2)
                circ = Circle(pt1, radius)

                circ.setOutline(list_of_outline_colors[i])
                circ.setFill(list_of_fill_colors[i])

                circ.draw(win)

            elif (working_shape == "Oval"):
                pt1 = Point(np.random.randint(border1), np.random.randint(border2))
                pt2 = Point(np.random.randint(border1), np.random.randint(border2))
                oval = Oval(pt1, pt2)

                oval.setOutline(list_of_outline_colors[i])
                oval.setFill(list_of_fill_colors[i])

                oval.draw(win)
            
            elif (working_shape == "Triangle"):
                pt1 = Point(np.random.randint(border1), np.random.randint(border2))
                pt2 = Point(np.random.randint(border1), np.random.randint(border2))
                pt3 = Point(np.random.randint(border1), np.random.randint(border2))
                vertices = [pt1, pt2, pt3]
                triangle = Polygon(vertices)

                triangle.setOutline(list_of_outline_colors[i])
                triangle.setFill(list_of_fill_colors[i])

                triangle.draw(win)

        win.getMouse()
        win.close()


def main():
    artist = MarkovArtist(COLOR_MATRIX, SHAPE_MATRIX)

    line_break = "*" * 50
    welcome = "Welcome to the Markov Artist Program"

    print(line_break)
    print(welcome)
    print(line_break)

    border1 = int(input("Choose a window width > "))
    border2 = int(input("Choose a window height > "))

    num_shapes = int(input("Choose number of shapes for masterpiece > "))
    print(line_break)

    dict_of_shapes = artist.make_shapes(total_shapes=num_shapes)


    artist.draw_masterpiece(dict_of_shapes, border1, border2)

if __name__ == "__main__":
    main()