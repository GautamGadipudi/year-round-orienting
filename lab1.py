import sys

from input import get_points_to_visit, get_terrain_data, get_commandline_params

terrain_data_dict = {}
points_to_visit = []
season = ''

def main():
    arguments = sys.argv;
    if len(arguments) == 6:
        global terrain_data_dict, points_to_visit, speed_dict, season
        (img_file, elev_file, path_file, season, output_image_filename) = get_commandline_params(arguments)
        terrain_data_dict = get_terrain_data(img_file, elev_file)
        points_to_visit = get_points_to_visit(path_file)

        for point in points_to_visit:
            data = terrain_data_dict[point]
            print(str(data) + '; Speed=' + str(data.get_speed(season)) + '\n')
    else:
        print('Invalid arguments. Usage: python3 lab1.py terrain_image_filepath, elevation_filepath, path_filepath, season', 'output_image_filename')





main()