import time
import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


# 尝试传参
s = Service("chromedriver.exe")


browser = webdriver.Chrome(service=s)
browser.get("http://www.ipe.org.cn/IndustryRecord/Regulatory.html?keycode=4543j9f9ri334233r3rixxxyyo12")

# 登录
cookie = {'name':'.ASPXAUTH','value':'0813571358B067E5DFDB89AB122E99FAEB789948A110C914127877C92A8B0C7E0E31D51C455FCFED23D5B20CA62C7FBF7CD59BEE183C77A4CC44F3EA12EDAE1F217487E43A365DB04BB04726D26DFC16420FF08054950EC95A1EC8E1EC54991BBDC4A708576EBDCD0932945E16B0D24B7218DA025CB6B2E9C8C4D2C2992985F49345005E8107D1CA05D6533FA050BE846A286BAA773ADC00DACD9448B63BA23B49D7EB749904E9D00608DEEC'}
browser.add_cookie(cookie)

time.sleep(3)

li_list = browser.find_elements(By.XPATH,r'//*[@id="table_con0"]/div[2]/table/tbody/tr')
#li_list = browser.find_elements_by_xpath('//*[@id="table_con0"]/div[2]/table/tbody/tr')

for i in li_list:
    raw_name = i.text
    name = re.search('.*? (.*?) .*?', raw_name).group(1)
    print(name)
    i.click()

    # 切换到新开的网页
    windows = browser.window_handles
    browser.switch_to.window(windows[-1])

    time.sleep(3)

    # 获取往年报告
    li_list2 = browser.find_elements(By.XPATH,'//*[@id="uitab_con"]/div[1]/div[1]/ul/li')
    for li in li_list2:
        li.click()
        time.sleep(2)
        a_list = li.find_elements(By.XPATH,'./div/a')
        first = 1
        for a in a_list:
            if first:
                a.click()
                time.sleep(2)
                first = 0
            else:
                li.click()
                time.sleep(1)
                a.click()
                time.sleep(2)

            # 提取数据
            html = browser.page_source
            soup = BeautifulSoup(html, 'lxml')

            div_box  = soup.find('div', class_='record-content record-information record-content_j')

            # 数据内容
            html = div_box.prettify()
            print(html)

            # 附件
            try:
                attachment = div_box.find('a').attrs['href']
            except:
                attachment = ''
            print(attachment)

            # 来源
            source = soup.find('h2').text[2:]
            print('来源', source)

            # 保存数据
            conn = MongoClient('localhost', 27017)
            db = conn.test_database
            collection = db.test_database
            item = {
                'name':name,
                'html':html,
                'attachment':attachment,
                'source':source
            }

            result=collection.insert_one(item)

            # break
        # break
    # break

    # 切换到上一个窗口
    windows = browser.window_handles
    browser.switch_to.window(windows[0])

browser.quit()