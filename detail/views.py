from django.shortcuts import render
import sys
import os

from api.download_pdf_annual_report_2.aim_compant import aim_company
from api.download_pdf_annual_report_2.merge import merge
from api.download_pdf_annual_report_2.下载年报 import download_annual_report
from api.pdf2txt_3.转换txt import transfer_pdf
from api.word_frequency_4.词频统计3_1 import word_frequency
from api.score_5.得分计算1 import score_calculate

# from api.word_frequency_4.爬取3 import spider_3
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

    def postESGScore(self,request,companyName):
        #TODO:调取接口，读到ESG得分
        # 分别对应E S G
        code =aim_company(companyName)
        merge()
        download_annual_report()
        transfer_pdf()
        word_frequency()
        dict=score_calculate(companyName,code)
        response={}
        response['value']=dict
        return JsonResponse(response)

    def getCompanyName(self,request,companyName):
        print("已收到前端信息，公司名称为:"+companyName)
        ans=aim_company(companyName)
        print(ans)
        if ans!=-1:
            #正常返回
            # spider_3(companyName)
            response = {}
            response['name'] = '已成功接受'
            response['code']=ans
        else:
            response = {}
            response['name'] = '无该公司信息'
        # if request.method == 'POST':
        #     if len(request.data['name']) > 0:
        #         response['name'] = request.data['name']
        return JsonResponse(response)

    def postEScore(self,request,companyName):
        response={}
        response['details'] = [{"c1": '大气排放', "c2": 12},{"c1":'扬尘',"c2":14}]
        response['category'] = ['大气排放','扬尘']
        response['scorePer'] = [12,14]
        return JsonResponse(response)

    def postSScore(self,request,companyName):
        response={}
        response['details'] = [{"c1": '大气排放', "c2": 12}, {"c1": '扬尘', "c2": 14}]
        response['category'] = ['大气排放', '扬尘']
        response['scorePer'] = [12, 14]
        return JsonResponse(response)

    def postGScore(self,request,companyName):
        response={}
        response['details'] = [{"c1": '这是一个特别长的公司名称，会有多长我也不知道，是否可以自己转行，为啥英文不行lllllllll', "c2": 12}, {"c1": '扬尘', "c2": 14}]
        response['category'] = ['这是一个特别长的公司名称，会有多长我也不知道，是否可以自己转行，为啥英文不行lllllllll', '扬尘']
        response['scorePer'] = [12, 14]
        return JsonResponse(response)
