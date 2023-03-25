with open('companyName.txt', 'r', encoding='utf-8') as f:
    name = f.readline()
    score = f.readline()
print(name)
print(score)