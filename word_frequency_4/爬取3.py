import time
import sys
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from pymongo import MongoClient
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


def spider_3(companyName):
    # 尝试传参
    s = Service("chromedriver.exe")
    browser = webdriver.Chrome(service=s)
    browser.get('https://www.ipe.org.cn/IndustryRecord/Regulatory.html')

    cookie = {'name': '.ASPXAUTH',
              'value': '1C63749167824CA1C06CF47CFB3125FC988EF1693A816DD8C920B110907B7E82913075B459276B22081CB54360578D6437DB34F5FCA91DDD95DEDB020B99B8D73F7D9F37FD6CEB6699707B4073BF403377839DF375066EDE63C5209DC3B7A74EBE1C2A5335F70CF335D4CA2518353EC3E5A7A7CC6273AD993914DB09BACAB0CBBBF3255DAC5E03B7C0D96EEE1BCFCE10CD9BCDD54DFAA93066F79980DFF934E9DAC48BBE91E9B89689C41C02'}
    browser.add_cookie(cookie)

    time.sleep(3)
    # content_to_process = driver.find_element_by_link_text('企业环境信息').click()s = Service("chromedriver.exe")

    # str = input("Enter your input: ")
    str=companyName
    # browser.find_elements(By.CLASS_NAME,'bg-gray').click()
    browser.find_element(By.XPATH, "//input[@id='search_input']").send_keys(str)
    browser.find_element(By.XPATH, "//button[@class='button button-primary']").send_keys(Keys.ENTER)

    time.sleep(3)

    li_list = browser.find_elements(By.XPATH, r'//*[@id="table_con0"]/div[2]/table/tbody/tr')
    # li_list = browser.find_elements_by_xpath('//*[@id="table_con0"]/div[2]/table/tbody/tr')

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
        li_list2 = browser.find_elements(By.XPATH, '//*[@id="uitab_con"]/div[1]/div[1]/ul/li')
        for li in li_list2:
            li.click()
            time.sleep(2)
            a_list = li.find_elements(By.XPATH, './div/a')
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

                div_box = soup.find('div', class_='record-content record-information record-content_j')

                # 数据内容
                html = div_box.prettify()
                print(html.split())

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
                    'name': name,
                    'html': html,
                    'attachment': attachment,
                    'source': source
                }

                result = collection.insert_one(item)

                # break
            # break
        # break

        # 切换到上一个窗口
        windows = browser.window_handles
        browser.switch_to.window(windows[0])

    browser.quit()


