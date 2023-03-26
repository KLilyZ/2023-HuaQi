import json

import pandas as pd
from django.shortcuts import render
import sys
import os
import pandas

from api.download_pdf_annual_report_2.aim_compant import aim_company
from api.download_pdf_annual_report_2.merge import merge
from api.download_pdf_annual_report_2.下载年报 import download_annual_report
from api.pdf2txt_3.转换txt import transfer_pdf
from api.word_frequency_4.词频统计3_1 import word_frequency
from api.score_5.得分计算1 import score_calculate
from api.advice_6.得分匹配 import testing
from api.advice_6.得分匹配 import testing2
from api.Get_pdf_7.Trans import trans
from api.Get_pdf_7.W2P import generate_pdf
from .models import Company
from .serializer import CompanySerializer

# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
# sys.path.insert(0,os.path.dirname((os.path.dirname(os.path.abspath(__file__)))))
# sys.path.insert(0,os.path.dirname(os.getcwd()))
from rest_framework import viewsets
from django.http import JsonResponse


# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

    def postESGScore(self, request, companyName):
        # TODO:调取接口，读到ESG得分
        # 分别对应E S G
        comprehensive = ''
        part1=''
        part2=''
        part3=''
        path = (os.path.dirname(os.path.dirname(__file__))) + "\\api\\DATA SUPPORT\\companyName.txt"
        with open(path, 'r', encoding='utf-8') as f:
            name = f.readline()[:-1]
            score = (f.readline())[1:-2].split(',')
            while True:
                tmp = f.readline()
                if tmp == '-1\n' or tmp=='':
                    break
                else:
                    comprehensive += tmp
            while True:
                tmp = f.readline()
                if tmp == '-2\n' or tmp == '':
                    break
                else:
                    part1 += tmp
            while True:
                tmp = f.readline()
                if tmp == '-3\n' or tmp == '':
                    break
                else:
                    part2 += tmp
            while True:
                tmp = f.readline()
                if tmp == '-4\n' or tmp == '':
                    break
                else:
                    part3 += tmp
        if name == '' or name != companyName:
            code = aim_company(companyName)
            merge()
            download_annual_report()
            transfer_pdf()
            word_frequency()
            dict_number = score_calculate(companyName, code)
            dict = str(dict_number).replace(' ','')
            conclude = testing(dict_number[0], dict_number[1], dict_number[2])
            partLis = testing2()
            generate_pdf(companyName, dict_number)
            trans(companyName)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(companyName)
                f.write('\n')
                f.write(dict)
                f.write('\n')
                f.write(conclude)
                f.write('\n')
                f.write('-1\n')
                f.write(partLis[0])
                f.write('-2\n')
                f.write(partLis[1])
                f.write('-3\n')
                f.write(partLis[2])
                f.write('-4\n')

        else:
            dict = score
            conclude = comprehensive
            partLis = [part1,part2,part3]

        response = {}
        response['value'] = dict
        response['part'] = partLis
        response['conclude'] = conclude
        return JsonResponse(response)

    def getCompanyName(self, request, companyName):
        print("已收到前端信息，公司名称为:" + companyName)
        ans = aim_company(companyName)
        print(ans)
        if ans != -1:
            response = {}
            response['name'] = '已成功接受'
            response['code'] = ans
        else:
            response = {}
            response['name'] = '无该公司信息'
        return JsonResponse(response)

    def postEScore(self, request, companyName):
        path = (os.path.dirname(os.path.dirname(__file__))) + "\\api\\DATA SUPPORT\\E.xls"
        df=pd.read_excel(path,dtype=str)
        score = df['小分'].astype(str)
        print((score))
        category=df['项目'].astype(str)
        print(category)
        detailList=[]
        response = {}
        for i in range(len(score)):
            dic={}
            dic["c1"]=category[i]
            dic["c2"]=score[i]
            print(dic)
            detailList.append(dic)

        detailList.reverse()
        response['details'] = detailList
        response['category'] = category.tolist()
        response['scorePer'] = score.tolist()
        # response['details'] = []
        # response['category'] = []
        # response['scorePer'] = []
        return JsonResponse(response)

    def postSScore(self, request, companyName):
        path = (os.path.dirname(os.path.dirname(__file__))) + "\\api\\DATA SUPPORT\\S.xls"
        df = pd.read_excel(path, dtype=str)
        score = df['小分'].astype(str)
        print((score))
        category = df['项目'].astype(str)
        print(category)
        detailList = []
        response = {}
        for i in range(len(score)):
            dic = {}
            dic["c1"] = category[i]
            dic["c2"] = score[i]
            print(dic)
            detailList.append(dic)
        detailList.reverse()
        response['details'] = detailList
        response['category'] = category.tolist()
        response['scorePer'] = score.tolist()
        return JsonResponse(response)

    def postGScore(self, request, companyName):
        path = (os.path.dirname(os.path.dirname(__file__))) + "\\api\\DATA SUPPORT\\G.xls"
        df = pd.read_excel(path, dtype=str)
        score = df['小分'].astype(str)
        print((score))
        category = df['项目'].astype(str)
        print(category)
        detailList = []
        response = {}
        for i in range(len(score)):
            dic = {}
            dic["c1"] = category[i]
            dic["c2"] = score[i]
            print(dic)
            detailList.append(dic)
        detailList.reverse()
        response['details'] = detailList
        response['category'] = category.tolist()
        response['scorePer'] = score.tolist()
        return JsonResponse(response)
