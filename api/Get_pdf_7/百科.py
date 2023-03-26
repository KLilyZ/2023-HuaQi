from playwright.sync_api import sync_playwright

def run(playwright):

    browser = playwright.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled", "--start-maximized"])

    context = browser.new_context(no_viewport=True)

    page = context.new_page()

    page.goto("https://baike.baidu.com/#home")

    page.wait_for_timeout(2000)


    page.fill('//*[@id="query"]', '云南白药公司')

    page.locator('//*[@id="search"]').click()

    page.wait_for_timeout(2000)

    ddlist = page.query_selector_all('//*[@id="body_wrapper"]/div[1]/dl/dd')

    count = 0

    for dd in ddlist[0:1]:

        dd.query_selector('//a').click()

        page.wait_for_timeout(3000)

        last_page: page = context.pages[1]

        count = str(count)

        file_name = count


        try:

            body = last_page.query_selector('//html/body/div[3]/div[2]/div/div[1]/div[4]').text_content()

        except:

            body = last_page.query_selector('//html/body/div[3]/div[1]/div/div[1]/div[1]/div[3]').text_content()

        with open('img\\' + file_name + '.txt', 'w', encoding='utf_8_sig') as f:  # 设置文件对象data.txt

            f.write(body)

            print('保存完成：', file_name)

        count = int(count)

        count = count + 1

        last_page.close()
        print(str(body))
        return str(body)

with sync_playwright() as playwright:
    run(playwright)