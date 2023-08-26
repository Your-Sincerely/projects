import smtplib
import os
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
SENDER_ADDR = os.getenv("GMAIL_ADDR")
SENDER_PASS = os.getenv("GMAIL_APP_PASS")
SUBJECT = "Attention , Your Application Status is Incomplete, pl. complete ASAP"

path = os.getcwd()
path1 = path+"\\Resource\\Excel_Email_input.xlsx"
path2 = path+"\\Resource\\body.txt"
RECEIVER_ADDRS = "secopi5247@anwarb.com"

# Load environment variables
def set_email_content(row):
    try:
        # Read template file
        with open(path2) as template:
            message = template.read()

            # updating excel
            message = message.replace("{trainee_name}", row[1])
            message = message.replace("{trainer_name}", row[2])
            message = message.replace("{Login_Id}", row[3])
            message = message.replace("{starting_date}", row[4])
            message = message.replace("{Ending_date}", row[5])
            # message = message.replace("{train_email}",row[6])
            BODY = message
            return BODY
    except:
        return None

def Create_email_message(RECEIVER_ADDRS,BODY):
    try:
        mail = MIMEMultipart()
        mail["Subject"] = SUBJECT
        mail["From"] = SENDER_ADDR
        mail["To"] = RECEIVER_ADDRS
        mail.attach(MIMEText(BODY,'plain'))

        # Check if sender address and password are provided
        if SENDER_ADDR is None:
            print("Sender address is not provided.")
        if SENDER_PASS is None:
            print("Sender password is not provided.")
        return mail
    except:
        return None
    


def  Attaching_attachment(mail,PATH = path2):
    try:
        # Attaching_attachment
        file = PATH
        with open(file,'rb') as f:
            attach = MIMEApplication(f.read(),_subtype = 'txt')
            attach.add_header('training_body','attachment',filename = file)
            mail.attach(attach)
        return mail
    except:
        return None

def Send_email_using_SMTP(RECEIVER_ADDRS,excel_data , PATH = path2):
    try:
        
        if excel_data:
            for row in excel_data:
                if row[1] == "name" :
                    continue
                # RECEIVER_ADDRS = row[6]
                body = set_email_content(row)
                mail = Create_email_message(RECEIVER_ADDRS,body)
                mail = Attaching_attachment(mail)
                context = ssl.create_default_context()
                with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
                    smtp.login(SENDER_ADDR, SENDER_PASS)
                    smtp.sendmail(SENDER_ADDR, RECEIVER_ADDRS, mail.as_string())
        return True
    except:
        return False