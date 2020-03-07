'''
    Author: Gautam Gadipudi
    Id: gg7148@rit.edu
'''
from PIL import Image

from Models.RGB import RGB
from Models.coordinate import coordinate
from Models.pixel import pixel

def get_terrain_data(terrain_image_file, elevation_text_file):
    try:
        img = Image.open(terrain_image_file)
        RGB_pixel_list = list(img.convert('RGB').getdata())
        RGB_matrix = []
        for i in range(500):
            RGB_matrix.append(RGB_pixel_list[i * 395: (i + 1) * 395])

        elev_file = open(elevation_text_file)
        elev_matrix = []
        for line in elev_file:
            elev_matrix.append(list(line.strip(' ').replace('\n', '').split('   ')))
        input = {}
        for i in range(500):
            for j in range(395):
                input[(i, j)] = \
                    pixel(coordinate(i, j, float(elev_matrix[i][j])), RGB(RGB_matrix[i][j][0], RGB_matrix[i][j][1], RGB_matrix[i][j][2]))
    except FileNotFoundError as ferror:
        print('File not found:' + ferror)
    except Exception as error:
        print(error)
    return input

def get_points_to_visit(point_file):
    points_to_visit = []
    try:
        file = open(point_file)
        for line in file:
            line = line.strip(' ').replace('\n', '').split(' ')
            x = int(line[0])
            y = int(line[1])
            points_to_visit.append((x, y))
    except Exception as error:
        print(error)
    return points_to_visit

def get_commandline_params(parameters):
    return (parameters[1], parameters[2], parameters[3], parameters[4], parameters[5])