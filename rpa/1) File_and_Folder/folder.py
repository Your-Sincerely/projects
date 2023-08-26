import os
import shutil

# Create a directory

def create_folder(path):
    try:
        os.mkdir(path)
    except OSError as error:
        print(f"Failed to create folder: {error}")
        quit()
    return path

# ------------------------------------------------------
# Move a directory

def move_folder(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
    except shutil.Error as error:
        print(f"Failed to move folder: {error}")
        quit()
    except OSError as error:
        print(f"Failed to move folder: {error}")
        quit()
    return destination_path

# --------------------------------------------------------
# Rename a directory

def rename_folder(folder_path, new_name):
    try:
        os.rename(folder_path, os.path.join(os.path.dirname(folder_path), new_name))
    except OSError as error:
        print(f"Failed to rename folder: {error}")
        quit()
    return new_name

# ------------------------------------------------------------
# Delete a directory
def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)
    except shutil.Error as error:
        print(f"Failed to delete folder: {error}")
        quit()
    except OSError as error:
        print(f"Failed to delete folder: {error}")
        quit()

# --------------------------------------------------------------

if __name__ == "__main__":
    path1=os.getcwd()+"\\1) File_and_Folder\\example_1"
    path2=os.getcwd()+"\\Resource\\example_1"
    path3=os.getcwd()+"\\Resource\\example_2"

    #test case 1 start
    #create_folder
    create_folder(path1)
    #test case 1 ends
    print("--test case 1 passed--")

    # -------------------------------------------------

    #test case 2 start
    #move folder
    move_folder(path1,path2)
    #test case 2 ends
    print("--test case 2 passed--")        
 
    # ------------------------------------------------ 

    # test case 3 start
    rename_folder(path2 ,path3)
    #test case 3 ends
    print("--test case 3 passed--")
    # ------------------------------------------------

    # test case 4 start
    delete_folder(path3)
    #test case 4 ends
    print("--test case 4 passed--")
