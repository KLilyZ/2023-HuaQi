import docx
from playwright.sync_api import sync_playwright
import sys
import os

from ..advice_6.得分匹配 import testing3


def run2(playwright, name):
    browser = playwright.chromium.launch(headless=True,
                                         args=["--disable-blink-features=AutomationControlled", "--start-maximized"])

    context = browser.new_context(no_viewport=True)

    page = context.new_page()

    page.goto("https://baike.baidu.com/#home")

    page.wait_for_timeout(200)

    page.fill('//*[@id="query"]', name)

    page.locator('//*[@id="search"]').click()

    page.wait_for_timeout(200)

    ddlist = page.query_selector_all('//*[@id="body_wrapper"]/div[1]/dl/dd')

    count = 0

    for dd in ddlist[0:1]:

        dd.query_selector('//a').click()

        page.wait_for_timeout(300)

        last_page: page = context.pages[1]

        count = str(count)

        file_name = count

        try:

            body = last_page.query_selector('//html/body/div[3]/div[2]/div/div[1]/div[4]').text_content()

        except:

            body = last_page.query_selector('//html/body/div[3]/div[1]/div/div[1]/div[1]/div[3]').text_content()

        with open(os.path.dirname(__file__)+'\\img\\' + file_name + '.txt', 'w', encoding='utf-8') as f:  # 设置文件对象data.txt

            f.write(body)

            print('保存完成：', file_name)

        count = int(count)

        count = count + 1

        last_page.close()
        print(str(body).replace('\xa0', ' '))
        return str(body).replace('\xa0', ' ')


def generate_pdf(companyName, score):
    S1 = companyName
    with sync_playwright() as playwright:
        S2 = run2(playwright, str(S1 + '公司'))
    S3 = score
    S4 = testing3(score[0], score[1], score[2])
    doc = docx.Document(os.path.dirname(__file__)+'\\ESG框架.docx')
    for paragraph in doc.paragraphs:
        tmp = ''
        runs = paragraph.runs
        for i, run in enumerate(runs):
            tmp += run.text  # 合并run字符串

            if 'XXX' in tmp:
                # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
                run.text = run.text.replace(run.text, tmp)
                run.text = run.text.replace('XXX', '云南白药ESG框架')
                tmp = S1 + 'ESG框架'

            if '这里是简介' in tmp:
                # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
                run.text = run.text.replace(run.text, tmp)
                run.text = run.text.replace('这里是简介', '云南白药ESG框架')
                tmp = S2

            if '这里是评分' in tmp:
                # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
                run.text = run.text.replace(run.text, tmp)
                run.text = run.text.replace('这里是评分', '云南白药ESG框架')
                tmp = S3

            if '这点是改进建议' in tmp:
                # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
                run.text = run.text.replace(run.text, tmp)
                run.text = run.text.replace('这点是改进建议', '云南白药ESG框架')
                tmp = S4

            else:
                # 如果没匹配到目标字符串则把当前run置空
                run.text = run.text.replace(run.text, '')
            if i == len(runs) - 1:
                # 如果是当前段落一直没有符合规则得字符串直接将当前run替换为tmp
                run.text = run.text.replace(run.text, str(tmp))
    doc.save(os.path.dirname(__file__) + "\\Picture.docx")
