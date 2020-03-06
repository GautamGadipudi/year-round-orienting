import sys

from Util.heuristic import get_path
from Util.input import get_points_to_visit, get_terrain_data, get_commandline_params
from Util.output import draw_on_output_image

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

        result = []
        for i in range(len(points_to_visit) - 1):
            start = terrain_data_dict[points_to_visit[i]]
            goal = terrain_data_dict[points_to_visit[i + 1]]
            path = get_path(start, goal, terrain_data_dict)
            result.extend(path)

        draw_on_output_image(output_image_filename, result, img_file)
    else:
        print('Invalid arguments. Usage: python3 lab1.py terrain_image_filepath, elevation_filepath, path_filepath, season', 'output_image_filename')

if __name__ == '__main__':
    main()