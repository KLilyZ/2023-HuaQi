import xlwt
import os
import re
import xlsxwriter
# 读取txt 并提取指定字符
def readTXT(ThePath,aim_path):
    dir_list = os.listdir(ThePath)
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('年报数据统计', cell_overwrite_ok=True)

    index = 0
    for dir in dir_list:
        dir_path = ThePath + '\\' + dir
        files = os.listdir(dir_path)
        for file in files:
            if os.path.splitext(file)[-1] == ".txt":
                txt_path = os.path.join(dir_path, file)
                print(f'正在统计 1 {dir}-{file}')
                with open(txt_path, "r", encoding='utf-8', errors='ignore') as fp:
                    text = fp.readlines()
                    ind = 0
                    for line in text:
                        if line.find("人民币")!=-1:
                            print(line)
                            result1 = re.findall(r"人民币 (.*) 元",str(line))  # 提取指定字符  表示提取 time: ~ ms之间的字符
                            result2 = re.findall(r"人民币(.*)亿元", str(line))
                            #print(line)
                            print(result2)
                    sheet.write(index + 1, ind + 3, str(result1))
                index += 1
    book.save(aim_path)




ThePath= r'D:\first_01\词频统计\年报txt版本'
aim_path=r'D:\first_01\2'

readTXT(ThePath, f'{aim_path}\词频统计2.xls')