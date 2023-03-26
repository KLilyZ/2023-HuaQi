import os.path

from django.shortcuts import render

# Create your views here.
from django.http import FileResponse


def download_file_ch(request):
    path = os.path.dirname(os.path.dirname(__file__))+"\\api\\DATA SUPPORT\\companyName.txt"
    with open(path,'r',encoding='utf-8') as f:
        companyName = f.readline()[:-1]
    file_path = os.path.dirname(os.path.dirname(__file__))+"\\api\\Get_pdf_7\\"+\
                companyName+"ESG框架.pdf"
    name = companyName+"ESG框架.pdf"
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename='+name
    return response

def download_company(request):
    file_path = os.path.dirname(os.path.dirname(__file__)) + "\\api\\DATA SUPPORT\\" + \
                "公司名称.xlsx"
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename=公司名称.xlsx'
    return response
