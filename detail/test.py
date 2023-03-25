with open('companyName.txt', 'r', encoding='utf-8') as f:
    name = f.readline()
    score = f.readline()
with open('companyName.txt', 'w', encoding='utf-8') as f:
    f.write("云南白药")
    f.write('\n')
    dict=str([20.2,30,33])
    f.write(dict)