import docx

S1=input('请输入公司名称：')
S2=input('请输入简介')
S3=input('请输入评分')
S4=input('请输入建议')



doc = docx.Document('ESG框架.docx')
for paragraph in doc.paragraphs:
    tmp = ''
    runs = paragraph.runs
    for i, run in enumerate(runs):
        tmp += run.text # 合并run字符串

        if 'XXX' in tmp:
            # 如果存在匹配得字符串，那么将当前得run替换成合并后得字符串
            run.text = run.text.replace(run.text, tmp)
            run.text = run.text.replace('XXX', '云南白药ESG框架')
            tmp = S1+'ESG框架'

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
            run.text = run.text.replace(run.text, tmp)
doc.save(r"Picture.docx")