# glpat-sba97_5Hppdmyz8kxz9y--token
import os

# Create a file
"""Creates a file with the given path and contents.

Args:
  path: The path of the file to create.
  contents: The contents of the file to create.

Returns:
  A file object for the created file.
"""
def create_file_with_path(path, contents =""):
  try:
    with open(path, "w") as f:
      f.write(contents)
  except FileNotFoundError:
        print(f"Error: The directory for '{path}' does not exist.")
        quit()
  except PermissionError:
        print(f"Error: Permission denied. Unable to create '{path}'.")
        quit()
  except Exception as e:
        print(f"An error occurred while creating the file: {e}")
        quit()

  return f

# -----------------------------------------------------------------
  # Move the file.
"""Moves a file from the source path to the destination path.

Args:
source_path: The path of the file to move.
destination_path: The path of the new location for the file.

Returns:
None.
"""
def move_file_with_path(source_path, destination_path):

    # Check if the source file exists.
    if not os.path.exists(source_path):
        raise FileNotFoundError("The source file does not exist.") 
        quit()

    # Check if the destination file exists.
    if os.path.exists(destination_path):
        raise FileExistsError("The destination file already exists.")
        quit()

    os.rename(source_path, destination_path)
    
# -------------------------------------------------------------------------------
# Rename a file

"""Renames a file from the source path to the destination path.

Args:
  source_path: The path of the file to rename.
  destination_path: The path of the new name for the file.

Returns:
  None.
"""
def rename_file_with_path(source_path, destination_path):

  # Check if the source file exists.
  if not os.path.exists(source_path):
    raise FileNotFoundError("The source file does not exist.")

  # Check if the destination file exists.
  if os.path.exists(destination_path):
    raise FileExistsError("The destination file already exists.")

  # Rename the file.
  os.rename(source_path, destination_path)

# ----------------------------------------------------------------------
# Delete a file

def delete_file(file_path):
    try:
        os.remove(file_path)
    except OSError as e:
        print(f"Error occurred while deleting file '{file_path}': {e}")
        quit()

# -------------------------------------------------------------------------

#    TEST CASES
if __name__ == "__main__":
    path = os.getcwd()
    path1= path+"\\1) File_and_Folder\\text.txt"
    path2= path+"\\Resource\\text.txt"
    path3= path+"\\Resource\\example.txt"
    
    #test case 1 start
    create_file_with_path(path1,"this is a test file")
    #test case 1 ends
    print("--test case 1 passed--")
    # ------------------------------------------------

    #test case 2 start
    move_file_with_path(path1,path2)
    #test case 2 ends
    print("--test case 2 passed--")  
    # ------------------------------------------------ 

    # test case 3 start
    rename_file_with_path(path2 ,path3)
    #test case 3 ends
    print("--test case 3 passed--")
    # ------------------------------------------------

    # test case 4 start
    delete_file(path3)
    #test case 4 ends
    print("--test case 4 passed--")   
