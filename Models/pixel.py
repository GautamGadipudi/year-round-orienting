import math

from Util import speed

class pixel:
    __slots__ = ['coordinate', 'RGB']

    def __init__(self, coordinate, RGB):
        self.coordinate = coordinate
        self.RGB = RGB

    def __str__(self):
        return str(self.coordinate) + '; ' + str(self.RGB)

    def get_speed(self, season):
        return speed.get_speed(self, season)

    def get_straight_line_distance(self, pixel):
        return math.sqrt((self.coordinate.x - pixel.coordinate.x) ** 2
                         + (self.coordinate.y - pixel.coordinate.y) ** 2
                         + (self.coordinate.z - pixel.coordinate.z) ** 2)

    def __filter(var):
        if var[0] >= 0 and var[0] < 395 and var[1] >= 0 and var[1] < 500:
            return True
        return False

    def get_adjecent_points(self):
        x = self.coordinate.x
        y = self.coordinate.y
        all_possible_points = \
            [(x + 1, y),
             (x - 1, y),
             (x, y + 1),
             (x, y - 1),
             (x + 1, y + 1),
             (x - 1, y + 1),
             (x + 1, y - 1),
             (x - 1, y - 1)]

        result = filter(lambda var: var[0] >= 0 and var[0] < 395 and var[1] >= 0 and var[1] < 500, all_possible_points)
        return list(result)