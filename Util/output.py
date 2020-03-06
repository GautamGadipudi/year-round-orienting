from shutil import copyfile

from PIL import Image

def draw_on_output_image(filename, result, img_file):
    open(f'./Output/{filename}', 'w+')
    copyfile(img_file, f'./Output/{filename}')
    img = Image.open(img_file)
    img.convert('RGB')

    for node in result:
        img.putpixel(node.coordinate.get2D(), (255, 0, 0))

    img.save(f'./Output/{filename}', "PNG")