import os
import openpyxl
import pandas as pd

path = r"D:\桌面\city cup\2、下载pdf年报\aim_data.xlsx"

wb = openpyxl.load_workbook(path)
sheet = wb.active
S=input("请输入公司名称：")
D = input("请输入股票代码：")
sheet['B2']=str(S)
sheet['B3']=str(S)
sheet['B4']=str(S)
sheet['B5']=str(S)
sheet['B6']=str(S)
sheet['B7']=str(S)
sheet['B8']=str(S)

sheet['A2']=str(D)
sheet['A3']=str(D)
sheet['A4']=str(D)
sheet['A5']=str(D)
sheet['A6']=str(D)
sheet['A7']=str(D)
sheet['A8']=str(D)

wb.save(r"D:\桌面\city cup\2、下载pdf年报\aim_data.xlsx")
wb.close()

