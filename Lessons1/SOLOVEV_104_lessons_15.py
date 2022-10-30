### Домашнее задание № 1 ###
import json
new_file = open('output.json', 'w', encoding='UTF-8', newline='')
a = []
b = []
di_ct = {}
while True:
    in_put = str(input("Введите название продукта: "))
    if in_put == 'стоп':
        break
    in_put_2 = int(input("Введите стоимость: "))
    a.append(in_put)
    b.append(in_put_2)
di_ct = dict(zip(a, b))
json.dump(di_ct, new_file)
### Домашнее задание № 2 ###
with open('output.json', 'r', encoding='UTF-8') as file:
    new_out = json.load(file)
    print(sum(new_out.values()), 'р.')