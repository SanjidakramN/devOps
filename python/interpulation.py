lang = "python"
lst = list(lang)
print(type(lst))
print(lst)

lst1 = [i for i in lang]
print(lst1)
print(type(lst1))

lst2 = [i for i in range (20)]
print(lst2)

lst3 = [i * i for i in range(20)]
print(lst3)

lst4 = [(i, i*i) for i in range(20)]
print(lst4)
print(type(lst4))
print(lst4[5])  # 5th element of the list   (5, 25)

lst5 = [i for i in range(20) if i % 2 == 0]
print(lst5)

lst6 = [i for i in range(20) if i % 2 != 0]
print(lst6)

lst7 = [i for i in range(3, 20) if i % 5 == 0 if i % 2 == 0 ]
print(lst7)

lst8 = [[1,2,3], [4,5,6], [7,8,9]]
flat_lst = [number for row in lst8 for number in row]
print(flat_lst)



