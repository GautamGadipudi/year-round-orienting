default_speed_dict = {(248, 148, 18): 10,
                     (255, 192, 0): 2,
                     (255, 255, 255): 8,
                     (2, 208, 60): 5,
                     (2, 136, 40): 4,
                     (5, 73, 24): 0,
                     (0, 0, 255): 0,
                     (71, 51, 3): 10,
                     (0, 0, 0): 10,
                     (205, 0, 101): 0}

def get_speed(pixel, season):
    if season == 'summer':
        speed = default_speed_dict[pixel.RGB.get()]

    return speed

def get_relative_speed(start_point_pixel, end_point_pixel):
    start_point_elev = start_point_pixel.coordinate.z
    end_point_elev = end_point_pixel.coordinate.z

    slope = start_point_elev - end_point_elev
    multiplication_factor = 1
    if slope >= 0:
        multiplication_factor += (slope / start_point_elev)
    else:
        multiplication_factor -= -(slope / start_point_elev)

    default_speed = default_speed_dict[start_point_pixel.RGB.get()]
    actual_speed = default_speed * multiplication_factor
    return actual_speed