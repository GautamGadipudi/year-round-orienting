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
