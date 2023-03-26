import os.path

from django.shortcuts import render

# Create your views here.
from django.http import FileResponse
from api.Get_pdf_7.Trans import trans
from api.Get_pdf_7.W2P import generate_pdf


def download_file_ch(request):
    path = os.path.dirname(os.path.dirname(__file__))+"\\api\\DATA SUPPORT\\companyName.txt"
    with open(path,'r',encoding='utf-8') as f:
        companyName = f.readline()[:-1]
        score = f.readline()[1:-2].split(',')
    generate_pdf(companyName,score)
    trans()
    file_path = os.path.dirname(os.path.dirname(__file__))+"\\api\\Get_pdf_7\\Picture.pdf"
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="picture.pdf"'
    return response

def download_file_en(request):
    file_path = os.path.dirname(__file__)+'\\test.pdf'
    response = FileResponse(open(file_path, 'rb'))
    response['Content-Disposition'] = 'attachment; filename="test.pdf"'
    return response
