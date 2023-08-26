import pytesseract as ppt
import cv2

def image_to_string(inp_path,out_path):
    try:
        img = cv2.imread(inp_path)
        ppt.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
        text = ppt.image_to_string(img)
        with open(out_path,"w") as f:
            f.write(text)
        return text
    except:
        return None


# img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# cv2.imshow('result',img)
# cv2.waitKey(0)
# my_config = r"--psm 6 --oem 3"
# text = pytesseract.image_to_string(PIL.image.open("CaptchaImage.jpeg")), my_config
# print(text)