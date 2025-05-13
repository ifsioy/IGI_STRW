from abc import ABC, abstractmethod
import math

from matplotlib import pyplot as plt
from matplotlib.patches import Polygon

from input_handler import input_positive_float, input_angle


class GeometricFigure(ABC):
    @abstractmethod
    def area(self):
        pass

class Color:
    def __init__(self, color):
        self._color = color

    @property
    def color(self):
        return self._color

class Triangle(GeometricFigure):
    name = "Triangle"

    def __init__(self, a, b, angle_degrees, color):
        self.a = a
        self.b = b
        self.angle_degrees = angle_degrees
        self.color_obj = Color(color)

    def area(self):
        angle_rad = math.radians(self.angle_degrees)
        return 0.5 * self.a * self.b * math.sin(angle_rad)

    def get_params_str(self):
        return f"{self.name}: sides {self.a}, {self.b}, angle {self.angle_degrees}°, color {self.color_obj.color}, square {self.area():.2f}"

    def __str__(self):
        return self.get_params_str()


def task4():
    a = input_positive_float("Enter len a: ")
    b = input_positive_float("Enter len b: ")
    angle = input_angle("Enter angle: ")
    color = input("Enter color (англ.): ")
    triangle = Triangle(a, b, angle, color)

    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    a = triangle.a
    b = triangle.b
    angle_rad = math.radians(triangle.angle_degrees)

    points = [
        (0, 0),
        (a, 0),
        (b * math.cos(angle_rad), b * math.sin(angle_rad))
    ]

    polygon = Polygon(points, closed=True, edgecolor='black', facecolor=triangle.color_obj.color)
    ax.add_patch(polygon)

    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    ax.set_xlim(-1, max_x + 1)
    ax.set_ylim(-1, max_y + 1)

    plt.title(triangle.get_params_str())
    plt.savefig('triangle.png')
    plt.show()