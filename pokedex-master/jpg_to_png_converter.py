import sys
import os
import glob
from PIL import Image

project_name = 'pokedex-master'
current_working_dir = os.getcwd()
project_dir = current_working_dir if str(current_working_dir).find(
    project_name) >= 1 else os.path.join(current_working_dir, project_name)


def remove_directory_prefix(dir):
    '''
        Removes the backslash / forwardslash from the directory name
    '''
    prefix = dir[0]

    return dir[1:] if ((prefix == '/') or (prefix == '\\')) else dir


def make_new_directory(new_dir):
    '''
        Creates the target directory
    '''
    try:
        os.mkdir(new_dir)
        return True
    except FileExistsError:
        # do nothing and just continue the program flow
        return False


def main():
    '''
        Converts images to PNG and saves it on the target directory provided on the 
        3rd argument sys.argv[2]

        Accepts two-argument
        sys.argv[1] Pokedex directory.
        sys.argv[2] target directory where the new images will be saved. 
    '''

    dir_pokedex = os.path.join(
        project_dir, remove_directory_prefix(sys.argv[1]))
    dir_new_pokedex = os.path.join(
        project_dir, remove_directory_prefix(sys.argv[2]))

    try:
        make_new_directory(dir_new_pokedex)

        # creates an image generators
        pkms = glob.iglob(
            os.path.join(dir_pokedex, '*.jpg'))

        while True:
            try:
                with Image.open(next(pkms)) as pkm_img:
                    png_filename = os.path.splitext(
                        os.path.basename(pkm_img.filename))[0] + '.png'

                    new_png_file = os.path.join(
                        dir_new_pokedex, png_filename)

                    if not os.path.exists(new_png_file):
                        pkm_img.save(new_png_file, 'PNG')
                    else:
                        continue
            except StopIteration:
                break

    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    main()
