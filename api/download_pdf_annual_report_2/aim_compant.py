import os
import openpyxl
import pandas as pd
import sys
# sys.path.insert(0,os.path.dirname(__file__))


def match_code(name):
    pathroot = (os.path.dirname(__file__))+'\\\\'
    # data = pd.read_excel(pathroot+'all_url_data.xlsx', dtype=str,engine='openpyxl')
    data = pd.read_csv(pathroot+'all_url_data.csv',dtype=str, encoding='GBK',engine='python')
    if name in data.secName.values:
        a = data[data.secName==name].code.values
        return a[0]
    else:
        return None
# print(match_code("云南白药"))
def aim_company(companyName):
    pathroot = (os.path.dirname(__file__)) + '\\\\'
    S = companyName
    D = match_code(S)
    print(D)
    if D is None:
        return -1
    else:
        path = pathroot+"aim_data.xlsx"

        wb = openpyxl.load_workbook(path)
        sheet = wb.active
        # S = input("请输入公司名称：")

        print(D)
        sheet['B2'] = str(S)
        sheet['B3'] = str(S)
        sheet['B4'] = str(S)
        sheet['B5'] = str(S)
        sheet['B6'] = str(S)
        sheet['B7'] = str(S)
        sheet['B8'] = str(S)

        sheet['A2'] = str(D)
        sheet['A3'] = str(D)
        sheet['A4'] = str(D)
        sheet['A5'] = str(D)
        sheet['A6'] = str(D)
        sheet['A7'] = str(D)
        sheet['A8'] = str(D)

        wb.save(pathroot+"aim_data.xlsx")
        wb.close()
        return D

