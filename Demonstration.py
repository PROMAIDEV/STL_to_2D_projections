from datetime import datetime
from os import walk, path
from utilities import model3D_to_Image2D_tools


now2D = datetime.now()  # Get time
time2D = now2D.strftime("%d%m%Y_%H%M%S")




# TODO add additional photo angles to dodecahedron_20V_sph also add random views of parts. The idea is to represent
#      3D model with dodecahedron 20 vertices views. Now I want if other views will be recognized.

dodecahedron_20V_sph = model3D_to_Image2D_tools.get_dodecahedron_20V_sph()  # generates 20 spherical coordinates of Regular Dodecahedron vertices
rho_d = dodecahedron_20V_sph[0][2]
std_views = [(0, 0, rho_d), (0, 180, rho_d), (0, 90, rho_d),  (0, 270, rho_d), (90, 0, rho_d), (-90, 0, rho_d)]

               # generates 20 spherical coordinates of Regular Dodecahedron vertices and
               # 6 standard views from the right and left sides, top, bottom, front and back.
               # https://en.wikipedia.org/wiki/Dodecahedron#:~:text=In%20geometry%2C%20a%20dodecahedron%20(Greek,which%20is%20a%20Platonic%20solid.

photo_angles = std_views + dodecahedron_20V_sph # If neededed and angles
print('Spherical angles of views to generate')
print(photo_angles)

image_path = r"C:\STL_to_2D_projections\Examples\ModelPack_1\Output"
models_path = r"C:\STL_to_2D_projections\Examples\ModelPack_1\Models\models.txt"


# Generate 2D images
Image2D_obj = model3D_to_Image2D_tools.Model3D_to_Image2D(image_path, models_path, photo_angles , 0)



# Save 2D data object

import pickle

path_images_2D_obj = path.normpath(path.abspath(path.join(image_path , '2Dimages__' + time2D + '.obj')))

with open(path_images_2D_obj, 'wb') as file:   # https://java2blog.com/save-object-to-file-python/
    pickle.dump(Image2D_obj, file)
    print(f'Object successfully saved to "{path_images_2D_obj}"')