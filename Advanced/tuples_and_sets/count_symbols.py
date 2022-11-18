text = input()

dic = {}

for el in text:
    dic[el] = text.count(el)

sorted_dic = sorted(dic.keys(), key=lambda x: x)
for i in sorted_dic:
    values = dic[i]
    print(f"{i}: {values} time/s")
