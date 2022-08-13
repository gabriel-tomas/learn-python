list = []
list1 = []
for c in range(0, 2):
    list1.append(str(input('Nome: ')))
    list1.append(int(input('Idade: ')))
    list.append(list1[:])
    list1.clear()
print(list)

