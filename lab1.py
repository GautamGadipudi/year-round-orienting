from input import get_points_to_visit, get_terrain_data, color_dict

terrain_data_dict = {}
points_to_visit = []
speed_dict = {}

def get_speed_dict(season):
    default_speed = {(248, 148, 18): 10,
                  (255, 192, 0): 2,
                  (255, 255, 255): 8,
                  (2, 208, 60): 5,
                  (2, 136, 40): 4,
                  (5, 73, 24): 0,
                  (0, 0, 255): 0,
                  (71, 51, 3): 10,
                  (0, 0, 0): 10,
                  (205, 0, 101): 0}
    speed_dict = {}

    if season == 'summer':
        for key in terrain_data_dict:
            speed_dict[key] = default_speed[terrain_data_dict[key][3]]

    return speed_dict

def get_speed(start_point, end_point):
    start_point_elev = terrain_data_dict[start_point][2]
    end_point_elev = terrain_data_dict[end_point][2]

    slope = start_point_elev - end_point_elev
    multiplication_factor = 1
    if slope >= 0:
        multiplication_factor += (slope / start_point_elev)
    else:
        multiplication_factor -= -(slope / start_point_elev)

    default_speed = speed_dict[start_point[3]]
    return default_speed * multiplication_factor

def main():
    img_file = './Input/terrain.png'
    elev_file = './Input/mpp.txt'
    point_file = './Input/points.txt'
    season = 'summer'

    terrain_data = get_terrain_data(img_file, elev_file)
    points_to_visit = get_points_to_visit(point_file)
    speed_dict = get_speed_dict(season)


    print(points_to_visit)
    for point in points_to_visit:
        data = terrain_data[point]
        print(f'x={data[0]}, y={data[1]}, z={data[2]}, RGB={data[3]}, Terrain={color_dict[data[3]]}')

main()