from Util.distance import get_distance
from Util.speed import get_relative_speed

def get_heuristic_dict(goal_pixel, terrain_data_dict):
    heuristic_dict = {}
    for key in terrain_data_dict:
        if terrain_data_dict[key].RGB.get() == (0, 0, 255):
            heuristic_dict[key] = float('inf')
        else:
            heuristic_dict[key] = terrain_data_dict[key].get_straight_line_distance(goal_pixel)

    return heuristic_dict

def get_path(start_pixel, end_pixel, terrain_data_dict):
    heuristic_dict = get_heuristic_dict(end_pixel, terrain_data_dict)
    path_list = []
    curr_pixel = start_pixel
    time = 0

    path_list.append(start_pixel)
    while end_pixel not in path_list:
        (next_pixel, time) = get_next_pixel(curr_pixel, end_pixel, heuristic_dict, terrain_data_dict, time, path_list)
        path_list.append(next_pixel)
        curr_pixel = next_pixel
    return path_list

def get_next_pixel(start_pixel, goal_pixel, heuristic_dict, terrain_data_dict, time, path_list):
    adjecent_points = start_pixel.get_adjecent_points()
    next_pixel = None

    f = float("inf")
    for point in adjecent_points:
        pixel = terrain_data_dict[point]
        if pixel in path_list:
            continue
        if point == goal_pixel.coordinate.get2D():
            return (pixel, time)
        distance_to_point = get_distance(start_pixel, pixel)
        relative_speed = get_relative_speed(start_pixel, pixel)
        g = 0
        if relative_speed == 0:
            g = float('inf')
        else:
            g = time + distance_to_point / get_relative_speed(start_pixel, pixel)
        h = heuristic_dict[point]
        f1 = g + h
        if f1 < f:
            f = f1
            next_pixel = pixel

    return (next_pixel, g)