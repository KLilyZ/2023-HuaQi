import sys
import os
# 把当前文件所在文件夹的父文件夹路径加入到PYTHONPATH
# sys.path.insert(0,(os.path.dirname(os.path.abspath(__file__))))
# print(sys.path)
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyViewSet


router = DefaultRouter()
urlpatterns = [
    path('',CompanyViewSet.as_view({"post":"getCompanyName","get":"postESGScore"})),
    path('Environment/',CompanyViewSet.as_view({"get":"postEScore"})),
    path('Social/', CompanyViewSet.as_view({"get": "postSScore"})),
    path('Governance/', CompanyViewSet.as_view({"get": "postGScore"})),
]