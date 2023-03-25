import pandas as pd
import xlwt
import os
import requests
import json
from faker import Factory
class gsxt():

    def search(self,companyName):
        # S=input("请输入公司：")
        S = companyName
        ua = Factory.create().user_agent()
        #print(ua)
        url = "http://app.gsxt.gov.cn/gsxt/cn/gov/saic/web/controller/PrimaryInfoIndexAppController/search?page=1"
        payload = {'searchword': str(S),
                   'conditions': '{"excep_tab": "0","ill_tab": "0","area": "0","cStatus": "0","xzxk": "0","xzcf": "0","dydj": "0"}',
                   'sourceType': 'A'}
        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Accept': 'application/json',
            'User-Agent': ua,
            'Host': 'app.gsxt.gov.cn'
        }
        response = requests.request("POST", url, headers=headers, data=payload)
        #print(response.text)
        info = json.loads(response.text)
        temp = info['data']['result']['recordsTotal']
        print(temp)
        return int(temp)


# 从每个文件夹下读取excel并进行如上计算后，将值全部存入一个list1中

# code=int(input("请输入股票代码"))

def getscore(ThePath, w_list, aim_path,p,code):
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
    #print(type(score))
    return score

def score_calculate(companyName,code):
    W = [[0, 4, 4, 4, 2, 3, 6, 3, 3, 1, 5], [0, 2, 3, 3, 4, 4, 3, 3, 6, -5.0, 6, 3], [0, 5, 2, 2, 2, 7, 3, 3, 2, 3, 2]]
    pathroot = os.path.dirname(os.path.dirname(__file__))
    ThePath1 = pathroot + r'\DATA SUPPORT\词频统计\三级指标\E'
    ThePath2 = pathroot + r'\DATA SUPPORT\词频统计\三级指标\S'
    ThePath3 = pathroot + r'\DATA SUPPORT\词频统计\三级指标\G'
    aimpath = pathroot + r"\DATA SUPPORT\得分\分数汇总.xlsx"
    p1 = pathroot + r'\DATA SUPPORT\E.xls'
    p2 = pathroot + r'\DATA SUPPORT\S.xls'
    p3 = pathroot + r'\DATA SUPPORT\G.xls'
    sE = getscore(ThePath1, W[0], aimpath, p1,code)
    sS = getscore(ThePath2, W[1], aimpath, p2,code)
    sG = getscore(ThePath3, W[2], aimpath, p3,code)

    server = gsxt()
    n = server.search(companyName)
    print(sE, sS, sG)
    print(sE + sS + sG)
    print(n)
    if n <= 20:
        sE += 2
    if n >= 40:
        sE -= 2

    S = sE + sS + sG
    print(S)
    return [sE,sS,sG]

