# 14022023
# 3D model to 2D images conversion utility Functions
# Python 3
# uses object with internal dodecahedron_20V_sph


"""Tools for directory management..

List of tools:
        * get_trim_image(data): - Trim image:
        * cartesian2spherical(coordinates) - convert XYZ to spherical coordinates
        * et_dodecahedron_20V_sph():
        * class Model3D_to_Image2D: - creates object of model projection images taken from different directions.

        * create_dir(Path = '', DirName = 'NewDir') - Creates new directory.
        * create_output_dirs() - creates project output directories.
        * copy_models(original_model3D_path= '', destination_model3D_path= ''): - copies new database into general database:
        * add_labels2_3Dmodel_files() - adds labels to file names in accordance to directory name

Caution:

Example:

"""



####################################################################
# Imports

from stl import mesh
from mpl_toolkits import mplot3d
from matplotlib import pyplot as plt
from os import path, makedirs
import numpy as np
from PIL import Image, ImageChops
import dir_tools
import os



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def get_trim_image(data):

    """
    get_trim_image(data): - Trim image
    Input arguments:
        - data - image.

    Output
       - path_file_dir2copy
       - path_where2copy

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    image = Image.fromarray(data)
    image.thumbnail((500, 500), Image.ANTIALIAS)   # https://www.w3schools.com/howto/howto_css_thumbnail.asp
                                                   # https://www.geeksforgeeks.org/python-pil-image-thumbnail-method/
    # TODO instead try to use sampling or full size image
    back_ground_color = (255, 255, 255)
    background = Image.new(image.mode, image.size, back_ground_color) # https://www.geeksforgeeks.org/python-pil-image-new-method/
                # https://pillow.readthedocs.io/en/stable/handbook/concepts.html
                # Creating image background object which is of specific color (255, 255, 255)

    diffIm = ImageChops.difference(image, background) # Substract https://www.geeksforgeeks.org/python-pil-imagechops-add_modulo-and-imagechops-difference-method/
    bbox = diffIm.getbbox()   # https://www.geeksforgeeks.org/python-pil-imagepath-path-getbbox-method/

    # TODO check if crop really needed
    # Tal pay attention maybe you do not need it

    if bbox:
        print(bbox)
        return image.crop(bbox)   # https://www.geeksforgeeks.org/python-pil-image-crop-method/
    else:
        return Image   # No crop


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def cartesian2spherical(coordinates):

    """
    cartesian2spherical(coordinates) - convert XYZ to spherical coordinates
    Input arguments:
        - coordinates - Coordinates XYZ.

    Output
       - el, az, r - spherical coordinates
       -

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    (x, y, z) = coordinates
    hxy = np.hypot(x, y)
    r = np.hypot(hxy, z)
    el = np.arctan2(z, hxy)
    az = np.arctan2(y, x)
    az, el, r = float("{0:.2f}".format(np.rad2deg(az))), \
                float("{0:.2f}".format(np.rad2deg(el))), \
                float("{0:.2f}".format(r))   # https://numpy.org/doc/stable/reference/generated/numpy.rad2deg.html
    return (el, az, r)                                 #https://en.wikipedia.org/wiki/Spherical_coordinate_system


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################



#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################



def get_dodecahedron_20V_sph():


    """
    get_dodecahedron_20V_sph() - generates 20 spherical coordinates of Regular Dodecahedron vertices
    Input arguments:
        - No

    Output
       - el, az, r - spherical coordinates of Regular Dodecahedron vertices, 20 vertices.
       -

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    the = (1 + np.sqrt(5)) / 2  # Golden rule https://en.wikipedia.org/wiki/Regular_dodecahedron
    # The following Cartesian coordinates define the 20 vertices of a regular dodecahedron centered at the origin and suitably scaled and oriented
    in_the = 1/the

    # The idea
    # of LFD, as described by [34], uses 20 cameras placed
    # at the vertices of a regular dodecahedron to capture
    # images of the 3D model from various views.


    Cartesian_coordinates = [(1,1,1), (-1,1,1), (1,-1,1), (-1,-1,1), (1,1,-1), (-1,1,-1), (1,-1,-1), (-1,-1,-1),  # 20 dodecahedron vertices
                             (0, the, in_the), (0, -the, in_the), (0, the, -in_the), (0, -the, -in_the),
                             (in_the, 0, the), (-in_the, 0, the), (in_the, 0, -the), (-in_the, 0, -the),
                             (the, in_the, 0), (-the, in_the, 0), (the, -in_the, 0), (-the, -in_the, 0)]

    # Ding-Yun Chen, Xiao-Pei Tian, Yu-Te Shen, and Ming Ouhyoung. On visual similarity based 3D model retrieval. Computer Graphics Forum, 22(3):223–232, 2003.

    ang_sph_dodecahedron_20V = []
    for cc in Cartesian_coordinates:
        ang_sph_dodecahedron_20V.append(cartesian2spherical(cc)) # Calculate spherical coordinates of dodecahedron vertices

    return ang_sph_dodecahedron_20V


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################



def model3D_to_images2D(model3D_file_path, path_to_2DImages, axes, figure, angle, im_glob_ind, im_loc_ind):
    """
    model3D_to_images2D(model3D_file_path, path_to_2DImages, axes, figure, angle, im_glob_ind, im_loc_ind): -
    Generate Image from custom angle of view in spherical coordinates.
    Input arguments:
        - model3D_file_path - path to the 3D model file
        - path_to_2DImages - path to folder with 2D images
        - axes - to use
        - figure - to use
        - angle - of view in spherical coordinates
        - im_glob_ind - global index of 2D image files.
        - im_loc_ind - local index of 2D image files.


    Output
       - el, az, r - spherical coordinates of Regular Dodecahedron vertices, 20 vertices.
       -

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # Rotate 3D model for folowing point of view photography
    axes.view_init(angle[0], angle[1]) # https://matplotlib.org/stable/api/_as_gen/mpl_toolkits.mplot3d.axes3d.Axes3D.html
                                       # https://www.geeksforgeeks.org/how-to-change-angle-of-3d-plot-in-python/
                                       # Rotate 3D model
                                       # Syntax: view_init(elev, azim)
    category_folder = model3D_file_path.split('\\')[-2] # TODO check

    file_base_name, ext1 = path.splitext(path.basename(model3D_file_path))
    folder_path = path.join(path_to_2DImages, category_folder, file_base_name)
    folder_path = dir_tools.create_path(folder_path)
    # file_name = 'gi_' + str(im_glob_ind) + 'li_' + str(im_loc_ind) + '__elev' +str(angle[0]) + "_" + 'azim' + str(angle[1]) + '_' + file_base_name +".png"
    file_name = 'g' + str(im_glob_ind) + 'l' + str(im_loc_ind) + 'elev' +str(angle[0]) + "_" + 'azim' + str(angle[1]) + '_' + ".png"
    image_file_path = path.join(folder_path, file_name)

    # Image Creation
    figure.canvas.draw()
    # Now we can save it to a numpy array.
    # https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.draw.html
    data = np.fromstring(figure.canvas.tostring_rgb(), dtype=np.uint8, sep='')
                # https://numpy.org/doc/stable/reference/generated/numpy.fromstring.html
    data = data.reshape(figure.canvas.get_width_height()[::-1] + (3,))
    image = get_trim_image(data)
    image.save(image_file_path)

    return image, image_file_path




#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################







class Model3D_to_Image2D:
    """
    get_dodecahedron_20V_sph() - generates 20 spherical coordinates of Regular Dodecahedron vertices
    Input arguments:
        - No

    Output
       - el, az, r - spherical coordinates of Regular Dodecahedron vertices, 20 vertices.
       -

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    # ROOT_DIR = os.path.normpath(os.getcwd())
    ROOT_DIR = os.path.dirname(os.path.abspath(
        "top_level_file.txt"))  # Get project root https://www.adamsmith.haus/python/answers/how-to-get-the-path-of-the-root-project-structure-in-python


    def __init__(self, path_to_2DImages = ROOT_DIR, path_to_models_list = ROOT_DIR, additional_photo_angles=None , global_image_count = 0):
        """
        :param path_to_2DImages: path to output folder with resulting 2D images
        :param path_to_models_list: path to .txt file which contain all mesh models names
        :param additional_photo_angles: tuple of set of angles from which the model is rotated and taken images
        """

        # QA
        dir_tools.check_path_name_str(path_to_2DImages)
        dir_tools.check_path_name_str(path_to_models_list)

        path_to_2DImages = dir_tools.create_path(path_to_2DImages)
        path_to_2DImages = dir_tools.check_dir_exist(path_to_2DImages)
        path_to_models_list = dir_tools.check_file_exist(path_to_models_list)


        self.dodecahedron_20V_sph = get_dodecahedron_20V_sph()  # generates 20 spherical coordinates of Regular Dodecahedron vertices

        if additional_photo_angles == None:

            # TODO add additional photo angles to dodecahedron_20V_sph also add random views of parts. The idea is to represent
            #      3D model with dodecahedron 20 vertices views. Now I want if other views will be recognized.

            additional_photo_angles = [(0, 0), (0, 180), (0, 90),  (0, 270), (90, 0), (-90, 0)]

        self.additional_photo_angles = additional_photo_angles
        self.path_to_models_list = path_to_models_list
        self.path_to_2DImages = path_to_2DImages
        self.global_image_count = global_image_count
        self.generate_Image()



    def generate_Image(self):
        file_no = 0
        files = open(self.path_to_models_list, 'r')
        for file in files:
            file_no += 1
            self.global_image_count +=1
            model3D_file_path = file[:-1]
            self.file_name, exe = path.splitext(model3D_file_path)
            print(str(file_no) + " " + self.file_name + exe)
            # Create a new plot
            figure = plt.figure(figsize=(10, 10))  # TODO try to change size if needed
            axes = mplot3d.Axes3D(figure)

            # Load the STL files and add the vectors to the plot
            Mesh = mesh.Mesh.from_file(model3D_file_path)
            axes.add_collection3d(mplot3d.art3d.Poly3DCollection(Mesh.vectors, edgecolor='k'))
            # https://matplotlib.org/3.1.1/api/_as_gen/mpl_toolkits.mplot3d.art3d.Poly3DCollection.html

            # Auto scale to the mesh size
            # scale = Mesh.points.flatten(1)

            scale = Mesh.points.flatten() #BY https://numpy.org/doc/stable/reference/generated/numpy.ndarray.flatten.html
            axes.auto_scale_xyz(scale, scale, scale)
            axes.set_axis_off()

            # Generate Image from Different angle
            angle_no = 0
            for angle in self.dodecahedron_20V_sph:
                angle_no += 1

                image, image_file_path = model3D_to_images2D(model3D_file_path, self.path_to_2DImages, axes, figure, angle, self.global_image_count, file_no)

                print(str(file_no) + "," + str(angle_no) + " >> " + image_file_path + "  Done!")
                # figure.clf()
                # plt.close(figure)


#BY 22122022
#Look for file_list files


if __name__ == "__main__":

    Model3D_to_Image2D(image_folder='Data_lfd', files_list= 'file_list_1.txt')

