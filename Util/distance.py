import math

def get_distance(start_pixel, end_pixel):
    start = start_pixel.coordinate.get2D()
    end = end_pixel.coordinate.get2D()

    return math.sqrt((((start[0] - end[0]) * 10.29) ** 2) + (((start[1] - end[1]) * 7.55) ** 2))