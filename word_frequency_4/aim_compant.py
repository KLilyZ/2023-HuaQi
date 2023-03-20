import os
import openpyxl
import pandas as pd
import sys
def aim_company(companyName):
    #path = r"..\download_pdf_annual_report_2\aim_data.xlsx"
    print(os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))
    wb = openpyxl.load_workbook(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))+r"\download_pdf_annual_report_2\aim_data.xlsx")
    sheet = wb.active
    S = companyName
    # print("aim_company收到公司名称:" + companyName)
    # S = input("请输入公司名称：")
    sheet['B2'] = str(S)
    sheet['B3'] = str(S)
    sheet['B4'] = str(S)
    sheet['B5'] = str(S)
    sheet['B6'] = str(S)
    sheet['B7'] = str(S)
    sheet['B8'] = str(S)
    print("aim_company收到公司名称:"+companyName)
    wb.save(os.path.dirname((os.path.dirname(os.path.abspath(__file__))))+r"\download_pdf_annual_report_2\aim_data.xlsx")
