# 18012023
# Directory organization utility Functions
# Python 3
"""Tools for directory management..

List of tools:
        * overwrite_file_dir(path_file_dir2copy,path_where2copy): - Copies directory or file and overwrites if needed:
        * check_path_name_str(model3D_path) - validates path name
        * check_dir_name_str(model3D_dir): - validates directory name:
        * create_path(NewDirPath = ''): - creates new directory :
        * create_dir(Path = '', DirName = 'NewDir') - Creates new directory.
        * create_output_dirs() - creates project output directories.
        * copy_models(original_model3D_path= '', destination_model3D_path= ''): - copies new database into general database:
        * add_labels2_3Dmodel_files() - adds labels to file names in accordance to directory name
        * check_dir_exist(DirPath = ''): - checks existence of the directory
        * check_file_exist(DirPath = ''): - checks existence of the file

Caution:

Example:

"""


import os
#from datetime import datetime

#from docx import Document
#from docx.shared import Inches
#from docx.shared import Pt
#import numpy as np
#import pandas as pd   # https://pandas.pydata.org/


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def overwrite_file_dir(path_file_dir2copy = '' ,path_where2copy = '' ):
    """
    overwrite_file_dir(path_file_dir2copy,path_where2copy): - Copies directory or file and overwrites if needed:
    Input arguments:
        - path_file_dir2copy - path to directory to copy
        - path_where2copy - path where to copy directory

    Output
       - path_file_dir2copy
       - path_where2copy

       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # import
    import os
    import shutil


    # Check input
    path_file_dir2copy = check_path_name_str(path_file_dir2copy)
    path_where2copy = check_path_name_str(path_where2copy)

    path_file_dir2copy = os.path.normpath(os.path.abspath(path_file_dir2copy))
    path_where2copy = os.path.normpath(os.path.abspath(path_where2copy))


    # Check if original data directory exists
    if not os.path.exists(path_file_dir2copy):
        print("No data directory: " + path_file_dir2copy )
        raise NameError("No Directory: " + path_file_dir2copy )
    else:
        print("Data directory exists: " + path_file_dir2copy )

    # Create target Directory if don't exist

    path_where2copy = create_path(path_where2copy)
    path_above_path_file_dir2copy, path_file_dir2copy_original_dir = os.path.split(path_file_dir2copy)
    destination_path_F = os.path.normpath(os.path.abspath(os.path.join(path_where2copy, path_file_dir2copy_original_dir)))





    # # List files and directories
    # print("Before moving file:")
    # print(os.listdir(path_file_dir2copy))


    # Check if file already exists
    if os.path.isdir(destination_path_F):
        print(destination_path_F , '\nexists in the destination path!')
        shutil.rmtree(destination_path_F)
        print(destination_path_F , '\nWas removed!')


    elif os.path.isfile(destination_path_F):
        print(destination_path_F , '\nexists in the destination path!')
        os.remove(destination_path_F)
        print(destination_path_F , '\nWas removed!')


    ###################################
    # Copy

    shutil.copytree(path_file_dir2copy, destination_path_F)
    print('Copied: \n' + path_file_dir2copy + '\n' + 'To: ' + '\n' + path_where2copy)



    return path_file_dir2copy , destination_path_F

#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def check_dir_name_str(model3D_dir):

    """
    check_dir_name_str(model3D_dir): - validates directory name:
    Input arguments:
        - model3D_dir - Directory name string for validation

    Output
       - model3D_dir - Validated directory name
            * If model3D_dir not a string rise error
            * If model3D_dir empty string use project root directory instead
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    # Check input
    if type(model3D_dir) != str:
        raise TypeError("Only string is allowed as directory name!")

    if len(model3D_dir)==0:
        path_above_root, root_dir = os.path.split(os.getcwd())
        model3D_dir = root_dir

        # Path = os.path.normpath(os.getcwd())
        # model3D_dir = os.path.dirname(os.path.abspath("top_level_file.txt")) #Get project root https://www.adamsmith.haus/python/answers/how-to-get-the-path-of-the-root-project-structure-in-python
        # ROOT_DIR = os.path.normpath(os.getcwd())

    return model3D_dir


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def check_path_name_str(model3D_path):

    """
    check_path_name_str(model3D_path): - validates path name:
    Input arguments:
        - model3D_path - Path string for validation

    Output
       - model3D_path - Validated path to the directory
            * If model3D_path not a string rise error
            * If model3D_path empty string use project root path instead
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    # Check input
    if type(model3D_path) != str:
        raise TypeError("Only string is allowed as directory name!")

    if len(model3D_path)==0:
        # Path = os.path.normpath(os.getcwd())
        model3D_path = os.path.dirname(os.path.abspath("top_level_file.txt")) #Get project root https://www.adamsmith.haus/python/answers/how-to-get-the-path-of-the-root-project-structure-in-python
        # ROOT_DIR = os.path.normpath(os.getcwd())

    return model3D_path

#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def create_path(NewDirPath = ''):

    """
    create_path(NewDirPath = ''): - creates new path :
    Input arguments:
        - NewDirPath - Directory path string

    Output
       - NewDirPath - Created directory path
            * If NewDirPath not a string rise error
            * If NewDirPath empty string use project root directory instead
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    NewDirPath = check_path_name_str(NewDirPath)

    # Create target Directory if don't exist
    if not os.path.exists(NewDirPath):
        os.makedirs(NewDirPath)
        print("Directory ", NewDirPath, " Created ")
    else:
        print("Directory ", NewDirPath, " already exists")

    return NewDirPath


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def create_dir(Path = '', DirName = 'NewDir'):
    """create_dir() - creates directory:
    Input arguments:
        - Path - Path string where the directory will be created. Default empty string - project root
        - DirName - Directory name string. Default NewDir

    Output
       - DirPath - Path to the directory
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # Imports
    import os

    # QA

    DirName = check_dir_name_str(DirName)

    Path = check_path_name_str(Path)

    # define the name of the directory to be created
    DirPath = os.path.join(Path , DirName )

    DirPath = create_path(DirPath)


    return DirPath


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def create_output_dirs():

    """create_output_dirs() - creates main project output directories as follows:

    - Output

       - Organized_Data
            - All_databases
            - Models_list
            - CAD_3D_Models
            - Projections_2D
                *******************************************************************************
                * Created in separate function
                - Date + Time    -  in format dd_mm_yyyy__hhmm
                    - All
                    - Training
                    - Validation
                    - Testing
                *******************************************************************************

       - Results
            *******************************************************************************
            * Created in separate function
            - Date + Time    -  in format dd_mm_yyyy__hhmm
                - Automatic_reports
                - Plots
                - Tables
                - Net
                    - Checkpoints
                    - Net_Metrics
                - Notes
            *******************************************************************************
       - Notes
       ..

    Output:
           pathOutput, Organized_Data , Models_list, Projections_2D, \
           CAD_3D_Models, Results

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # Create main output directory and paths

    ################################################################
    pathNow = os.getcwd()  # Get working directory
    # pathNow = os.path.normpath(os.getcwd() + os.sep + os.pardir)  # Get directory above working directory
    # https://stackoverflow.com/questions/12280143/how-to-move-to-one-folder-back-in-python
    # https://www.geeksforgeeks.org/python-os-pardir-method-with-example/
    # https://docs.python.org/2/library/os.html

    # now = datetime.now()  # Get time
    # time = now.strftime("%d%m%Y_%H%M%S")
    ################################################################


    ################################################################
    # Create output directory
    # define the name of the directory to be created

    pathOutput = create_dir(pathNow, 'Output')

    # Create subdirectories

    Organized_Data = create_dir(pathOutput, "Organized_Data")

    All_databases = create_dir(Organized_Data, "All_databases")
    Models_list = create_dir(Organized_Data, "Models_list")
    Projections_2D = create_dir(Organized_Data, "Projections_2D")
    CAD_3D_Models = create_dir(Organized_Data, "CAD_3D_Models")

    Results = create_dir(pathOutput, "Results")


    return pathOutput, Organized_Data , All_databases, Models_list, Projections_2D, \
           CAD_3D_Models, Results
    ###########################################################


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def copy_models(original_model3D_path= '', destination_model3D_path= ''):

    """
    copy_models(original_model3D_path= '', destination_model3D_path= ''): - copies new database into general database:
    Input arguments:
        - original_model3D_path - Path string link to directory with the original 3D models. Default empty string - project root.
          This is the directory that will be copied
        - destination_model3D_path - Path string link to destination directory. Default empty string - project root.
          Path to directory that will include copied directory.

    Output
       - destination_model3D_path
       - destination_model3D_path_F - This the copied directory at the new path
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    # Imports
    import os
    import shutil

    ###################################
    # Code
    ###################################

    # Check input
    original_model3D_path = check_path_name_str(original_model3D_path)
    destination_model3D_path = check_path_name_str(destination_model3D_path)

    original_model3D_path = os.path.normpath(os.path.abspath(original_model3D_path))
    destination_model3D_path = os.path.normpath(os.path.abspath(destination_model3D_path))


    # Check if original data directory exists
    if not os.path.exists(original_model3D_path):
        print("No data directory: " + original_model3D_path )
        raise NameError("No Directory: " + original_model3D_path )
    else:
        print("Data directory exists: " + original_model3D_path )

    # Create target Directory if don't exist

    destination_model3D_path = create_path(destination_model3D_path)
    path_above_or_model_dir, original_models_dir = os.path.split(original_model3D_path)


    destination_model3D_path_F = os.path.normpath(os.path.abspath(os.path.join(destination_model3D_path, original_models_dir)))

    ###################################
    # Copy

    if not os.path.exists(destination_model3D_path_F):

        shutil.copytree(original_model3D_path, destination_model3D_path_F)
        print('Copied: \n' + destination_model3D_path_F)

    else:

        print('Was copied before: \n' + destination_model3D_path_F)


    return destination_model3D_path , destination_model3D_path_F




#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def check_dir_exist(DirPath = ''):

    """
    check_dir_exist(DirPath = ''): - checks existence of the directory
    Input arguments:
        - DirPath - Directory path string for validation

    Output
       - DirPath - Directory path string for validation
            * If DirPath doesn't exist use project root directory instead
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # Check if directory already exists
    if os.path.isdir(DirPath):
        print(DirPath, '\nexists in the destination path!')
    else:
        print(DirPath, '\ndoes not exists in the destination path!')
        # ROOT_DIR = os.path.normpath(os.getcwd())
        DirPath = os.path.dirname(os.path.abspath(
            "top_level_file.txt"))  # Get project root https://www.adamsmith.haus/python/answers/how-to-get-the-path-of-the-root-project-structure-in-python
        print('Instead using: ' + DirPath)


    return DirPath


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################


def check_file_exist(FilePath = ''):

    """
    check_file_exist(DirPath = ''): - checks existence of the file
    Input arguments:
        - FilePath - File path string for validation

    Output
       - FilePath - Directory path string for validation
            * If DirPath doesn't exist rise error
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """

    # Check if directory already exists
    if os.path.isfile(FilePath):
        print(FilePath, '\nexists in the destination path!')
    else:
        raise NameError(FilePath, '\ndoes not exists in the destination path!')


    return FilePath


#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

#########################################################################################################################################################################################
#########################################################################################################################################################################################
#########################################################################################################################################################################################

def add_labels2_3Dmodel_files(model3D_path= '', global_data_count = 0):

    """add_labels2_3Dmodel_files() - adds labels to file names in accordance to directory name:
    Input arguments:
        - model3D_path - Path string link to directory with the original 3D models. Default empty string - project root
        - global_data_count - global index of models in the whole database. default global_data_count = 0.

    Output
        - model3D_path - Path string link to directory with the original 3D models. Default empty string - project root
       ..

    Caution:

    Example:

    Notes:
        Update as needed.

    """


    # Imports
    import os
    from os import walk, path

    ###################################
    # Code
    ###################################

    # Check input
    model3D_path = check_path_name_str(model3D_path)
    path_above_or_model_dir, original_models_dir = os.path.split(model3D_path)

    ###################################

    ###################################
    # Save new 3D model files with labels in the name.


    countRenamed = 0
    countAll = 0

    for root1, dir1, files1 in walk(model3D_path):  # https://www.geeksforgeeks.org/os-walk-python/
        for file2 in files1:
            path_above_root, root_name = os.path.split(root1)
            FilePathName, extension = path.splitext(file2)
            FIND_LB = FilePathName.find('_label_')
            countAll += 1
            global_data_count +=1
            print(countAll)

            if FIND_LB == -1:
                New_FileName = 'gdInd_' + str(global_data_count) + '__' + FilePathName + '_label_' + root_name + extension
                src_path = os.path.normpath(os.path.abspath(os.path.join(root1, file2)))
                dst_path = os.path.normpath(os.path.abspath(os.path.join(root1, New_FileName)))
                os.rename(src_path, dst_path)
                countRenamed += 1
                print(countRenamed)

    print('Number of renamed files: ' + str(countRenamed))
    print('Number of files: ' + str(countAll))
    print('Number of models in all databases: ' + str(global_data_count))

    return model3D_path , global_data_count