from PIL import Image
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
                input[(i, j)] = ((i, j, float(elev_matrix[i][j]), RGB_matrix[i][j]))
                # input.append((RGB_matrix[i][j], (i, j, float(elev_matrix[i][j]))))
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