import os
import sys
sys.path.append("1) File_and_Folder")
sys.path.append("2) Excel_Automation")
sys.path.append("3) Email_Automation")
sys.path.append("4) image recognition")
sys.path.append("7) Rpa_Challenge_website")
sys.path.append("Resource")
import file
import folder
import excel_automation
import Email_Automation
import ocr_image_recognition
from openpyxl.utils import get_column_letter
# import Rpa_Challenge_website

# path
path = os.getcwd()
path1=path+"\\example_1"
path2=path+"\\Resource\\example_1"
path3=path+"\\Resource\\example_2"

path4="\\text.txt"
path5="\\example.txt"


path6 = path+"\\Resource\\Excel_Email_input.xlsx"
path7 = path+"\\Resource\\Excel_output.xlsx"
path8 = path+"\\Resource\\body.txt"

path9 = path + "\\Resource\\images.png"
path10 = path + "\\Resource\\text.txt"

def print_e(excel_data):
    if excel_data:
        for row in excel_data:
            print(row)


if __name__ == "__main__":

    print("file and folder")
    #test case 1 start
    # creating file and folder
    path = folder.create_folder(path1)
    file.create_file_with_path(path+path4,"")
    #test case 1 ends
    print("--test case 1 passed--creating file and folder")
     # ------------------------------------------------

    #test case 2 start
    # moving file and folder
    path = folder.move_folder(path,path2)
    # file.move_file_with_path(path+path4,path+path4)
    #test case 2 ends
    print("--test case 2 passed--moving file and folder")
     # ------------------------------------------------

    #test case 3 start
    # renaming file and folder
    path = folder.rename_folder(path,path3)
    file.move_file_with_path(path+path4,path+path5)
    #test case 3 ends
    print("--test case 3 passed--renaming file and folder")
     # ------------------------------------------------
 
    #test case 4 start
    # deleting file and folder
    file.delete_file(path+path5)
    path = folder.delete_folder(path)
    #test case 4 ends
    print("--test case 4 passed--deleting file and folder\n")
# ------------------------------------------------



# ----------test case--------------
    print("excel automation")

    # reading
    excel_data = excel_automation.read_excel(path6)
    if excel_data != None:
        print("___test_case1 passed____reading_excel")
    else:
        print("___test_case1 failed__")

    #  write
    excel_data[0][0] = "serial_no."
    if excel_automation.write_excel(path6,excel_data,path7):
        print("___test_case2 passed____write in excel")
    else:
        print("___test_case2 failed__")


    # format
    if excel_automation.format_excel(path6,path7):
        print("___test_case3 passed___format in excel")
    else:
        print("___test_case3 failed__")


    # calculating
    column_index = 0  # Specify the column index (e.g., 1 for column A, 2 for column B, etc.)
    average = excel_automation.calculate_column_average(path6, column_index)
    if average is not None:
        print("___test_case4 passed____calculating average of column in excel\n")
    else:
        print("___test_case4 failed__\n")

# _____________________________________________________________________________

# -------------test_ case--------------------

    print("email automation")
# Load environment variables
    RECEIVER_ADDRS = "secopi5247@anwarb.com"
    body = Email_Automation.set_email_content(excel_data[1])
    if body is not None:
        print("___test_case 1 passed____setting_email_content")
    else:
        print("___test_case 1 failed__")

    mail = Email_Automation.Create_email_message(RECEIVER_ADDRS,body)
    if mail is not None:
        print("___test_case 2 passed____Creating_email_message")
    else:
        print("___test_case 2 failed__")

    mail = Email_Automation.Attaching_attachment(mail)
    if mail is not None:
        print("___test_case 3 passed____Attaching_attachment")
    else:
        print("___test_case 3 failed__")

    send = Email_Automation.Send_email_using_SMTP(RECEIVER_ADDRS,excel_data,mail)
    if send:
        print("___test_case 4 passed____Send_email_using_SMTP\n")
    else:
        print("___test_case 4 failed__\n")

# _________________________________________________________________

    print("image to text")
    text = ocr_image_recognition.image_to_string(path9,path10)
    if text is not None:
        print("___test_case 1 passed____image to string")
    else:
        print("___test_case 1 failed__")

# # __________________________________________________________________

    # print("____RPA_Challenge____")
    # excel_data=0
    # Rpa_Challenge_website.RPA(excel_data)