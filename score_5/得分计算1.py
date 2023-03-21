import pandas as pd
import xlwt
import os
import pymongo
from pymongo import MongoClient
import openpyxl


# 从每个文件夹下读取excel并进行如上计算后，将值全部存入一个list1中

code=int(input("请输入股票代码"))

def getscore(ThePath, w_list, aim_path,p):
    dir_list = os.listdir(ThePath)

    print(dir_list)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    score = 0
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('得分列表', cell_overwrite_ok=True)
    sheet.write(0, 0, '小分')
    num = 0
    index =0
    ind=0
    for file in dir_list:
        dir_path = ThePath + '\\'
        with open(os.path.join(dir_path, file)):
            xls_path = os.path.join(dir_path, file)
            print(xls_path)
            cj = pd.read_excel(xls_path)

            # 将所有词汇按类别放到一个list里
            temp = cj.loc[:, :]

            # print(temp)

            row_all = temp.sum(axis=1, numeric_only=True)

            cj['出现次数'] = temp.sum(axis=1, numeric_only=True)

            cn = cj[['出现次数']]

            count = cn.sum(axis=0)

            count['出现次数'] = count['出现次数'] - 2020 - 2017 - 2018 - 2019 - 2021-code*5
            print(count['出现次数'])
            if count['出现次数'] > 0:
                if count['出现次数'] >= 4:
                    count['出现次数'] = 1
                else:
                    count['出现次数'] = 0.5
            num += 1
            print(w_list[num])
            ps=w_list[num] * count['出现次数']

            print(ps)
            re_path=os.path.join(aim_path,'result.xlsx')

            sheet.write(index + 1, ind, str(ps))
            index += 1

            score += ps


            print(score)
            # count['weight']

            with pd.ExcelWriter(aim_path) as writer:
                count.to_excel(writer, index=1, sheet_name='得分1')

                # 写入乘积

        print(file)
    book.save(p)
    return score


W = [[0, 4, 4, 4, 2, 3, 6, 3, 3, 1, 5], [0, 2, 3, 3, 4, 4, 3, 3, 6, -5.0, 6, 3], [0, 5, 2, 2, 2, 7, 3, 3, 2, 3, 2]]
ThePath1 = r'D:\first_01\词频统计\三级指标\E'
ThePath2 = r'D:\first_01\词频统计\三级指标\S'
ThePath3 = r'D:\first_01\词频统计\三级指标\G'
aimpath = r"D:\first_01\得分\分数汇总.xlsx"
p1=r'D:\first_01\E.xls'
p2=r'D:\first_01\S.xls'
p3=r'D:\first_01\G.xls'
sE = getscore(ThePath1, W[0], aimpath,p1)
sS = getscore(ThePath2, W[1], aimpath,p2)
sG = getscore(ThePath3, W[2], aimpath,p3)

host = 'localhost'  # 你的ip地址
client = MongoClient(host, 27017)  # 建立客户端对象
db = client.test_database
myset = db.test_database
n = myset.estimated_document_count()
print(sE, sS, sG)
print(sE + sS + sG)
print(n)
if n <= 20:
    sE += 2
if n >= 40:
    sE -= 2

S = sE + sS + sG
print(S)

