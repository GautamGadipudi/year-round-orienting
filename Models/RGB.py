color_dict = {(248, 148, 18): 'open_land',
              (255, 192, 0): 'rough_meadow',
              (255, 255, 255): 'easy_movement_forest',
              (2, 208, 60): 'slow_run_forest',
              (2, 136, 40): 'walk_forest',
              (5, 73, 24): 'impassible_vegetation',
              (0, 0, 255): 'water',
              (71, 51, 3): 'paved_road',
              (0, 0, 0): 'footpath',
              (205, 0, 101): 'out_of_bounds'}

class RGB:
    __slots__ = ['R', 'G', 'B']

    def __init__(self, R, G, B):
        self.R = R
        self.G = G
        self.B = B

    def get(self):
        return (self.R, self.G, self.B)

    def __str__(self):
        return f'(R={self.R}, G={self.G}, B={self.B}) => {color_dict[self.get()]}'