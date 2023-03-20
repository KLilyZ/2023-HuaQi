import os
import openpyxl
import pandas as pd

path = r"D:\桌面\词频统计1\2、下载pdf年报\aim_data.xlsx"

wb = openpyxl.load_workbook(path)
sheet = wb.active
S=input("请输入公司名称：")
sheet['B2']=str(S)
sheet['B3']=str(S)
sheet['B4']=str(S)
sheet['B5']=str(S)
sheet['B6']=str(S)
sheet['B7']=str(S)
sheet['B8']=str(S)

wb.save(r"D:\桌面\词频统计1\2、下载pdf年报\aim_data.xlsx")