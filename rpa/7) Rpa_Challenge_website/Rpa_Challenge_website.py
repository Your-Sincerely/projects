

import modules
import pandas as pd
import rpa as r
def RPA(excel_data=0):
    try:
        df= pd.read_excel('C:\\Users\\LENOVO\\Desktop\\gitlab\\rpa\\7) Rpa_Challenge_website\\challenge.xlsx')
        r.init()
        r.url('https://www.rpachallenge.com/')
        r.wait(10)
        r.click('//button[text()="Start"]')
        for index,row in df.iterrows():
            r.type('//input[@ng-reflect-name="labelFirstName"]',row['First Name'])
            r.type('//input[@ng-reflect-name="labelLastName"]',row['Last Name '])
            r.type('//input[@ng-reflect-name="labelCompanyName"]',row['Company Name'])
            r.type('//input[@ng-reflect-name="labelRole"]',row['Role in Company'])
            r.type('//input[@ng-reflect-name="labelAddress"]',row['Address'])
            r.type('//input[@ng-reflect-name="labelEmail"]',row['Email'])
            r.type('//input[@ng-reflect-name="labelPhone"]',str(row['Phone Number']))
            r.click('//input[@value="Submit"]')
        r.snap('/html/body/app-root/div[2]','results.png')
        r.close()
        return True
    except:
        return False