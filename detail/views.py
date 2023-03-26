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

    def postESGScore(self, request, companyName):
        # TODO:调取接口，读到ESG得分
        # 分别对应E S G
        comprehensive = ''
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
        if name == '' or name != companyName:
            code = aim_company(companyName)
            merge()
            download_annual_report()
            transfer_pdf()
            word_frequency()
            dict = score_calculate(companyName, code)
            conclude = testing(dict[0], dict[1], dict[2])
            with open(path, 'w', encoding='utf-8') as f:
                f.write(companyName)
                f.write('\n')
                f.write(str(dict))
                f.write('\n')
                f.write(conclude)
                f.write('\n')
                f.write('-1')

        else:
            dict = score
            conclude = comprehensive

        response = {}
        response['value'] = dict
        response['part'] = [" hhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
                            "        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
                            "        hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh<br>\n" +
                            "        文がいくつか集まり、かつ、まとまった内容を表すもの。内容のうえで前の文と密接な関係をもつと考えられる文は、そのまま続いて書き継がれ、前の文と隔たりが意識されたとき、次の文は行を改めて書かれる。すなわち、段落がつけられるということであり、これは、書き手がまとまった内容を段落ごとにまとめようとするからである。この、一つの段落にまとめられる、いくつかの文の集まりを一文章というが、よりあいまいに、いくつかの文をまとめて取り上げるときにそれを文章と称したり、文と同意義としたりすることもあるなど文章はことばの単位として厳密なものでないことが多い。これに対して、時枝誠記(ときえだもとき)は、文章を語・文と並ぶ文法上の単位として考えるべきことを主張し、表現者が一つの統一体ととらえた、完結した言語表現を文章と定義した。これによれば、一編の小説は一つの文章であり、のちに続編が書き継がれた場合には、この続編をもあわせたものが一つの文章ということになる。俳句、和歌の一句・一首は、いずれも一つの文章であり、これをまとめた句集・歌集は、編纂(へんさん)者の完結した思想があることにおいて、それぞれ一つの文章ということになる。\n" +
                            "\n" +
                            "        ［山口明穂］\n" +
                            "\n" +
                            "        『時枝誠記著『日本文法　口語篇』（1950・岩波書店）』"]
        # response['conclude'] = "在日常的工作中，总有一些报表、图表的配色方案是值得我们参考的，但是因为没有颜色抓取工具导致大家没办法把配色给取下来。下面介绍一下大家平时可以怎么抓取颜色，快速获取颜色的RGB或十六进制代码：\n" + \
        #                   "        平时大家都会登录QQ或微信，可以利用截图功能，抓取颜色：\n" + \
        #                   "        ① 同时按住 Ctrl + Alt + A，进入截图；\n" + \
        #                   "        ② 按住 Ctrl 键，光标处会显示光标位置对应RGB的6位十六进制颜色码；（如：C0EAF7）\n" + \
        #                   "        ③ 松开 Ctrl 键，光标处会显示光标位置对应RGB的3串RGB颜色值。（如：192,234,247）\n" + \
        #                   "        用好上面的取色技巧，可以大大加快项目组的开发速度和配色技能。\n" + \
        #                   "      综合建议\n" + \
        #                   "      在日常的工作中，总有一些报表、图表的配色方案是值得我们参考的，但是因为没有颜色抓取工具导致大家没办法把配色给取下来。下面介绍一下大家平时可以怎么抓取颜色，快速获取颜色的RGB或十六进制代码：\n" + \
        #                   "        平时大家都会登录QQ或微信，可以利用截图功能，抓取颜色：\n" + \
        #                   "        ① 同时按住 Ctrl + Alt + A，进入截图；\n" + \
        #                   "        ② 按住 Ctrl 键，光标处会显示光标位置对应RGB的6位十六进制颜色码；（如：C0EAF7）\n" + \
        #                   "        ③ 松开 Ctrl 键，光标处会显示光标位置对应RGB的3串RGB颜色值。（如：192,234,247）\n" + \
        #                   "        用好上面的取色技巧，可以大大加快项目组的开发速度和配色技能。\n" + \
        #                   "      在日常的工作中，总有一些报表、图表的配色方案是值得我们参考的，但是因为没有颜色抓取工具导致大家没办法把配色给取下来。下面介绍一下大家平时可以怎么抓取颜色，快速获取颜色的RGB或十六进制代码：\n" + \
        #                   "        ① 同时按住 Ctrl + Alt + A，进入截图；\n" + \
        #                   "        ② 按住 Ctrl 键，光标处会显示光标位置对应RGB的6位十六进制颜色码；（如：C0EAF7）\n" + \
        #                   "        ③ 松开 Ctrl 键，光标处会显示光标位置对应RGB的3串RGB颜色值。（如：192,234,247）\n" + \
        #                   "        用好上面的取色技巧，可以大大加快项目组的开发速度和配色技能。\n" + \
        #                   "      在日常的工作中，总有一些报表、图表的配色方案是值得我们参考的，但是因为没有颜色抓取工具导致大家没办法把配色给取下来。下面介绍一下大家平时可以怎么抓取颜色，快速获取颜色的RGB或十六进制代码：\n"
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
