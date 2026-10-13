# task = int(input("Решите пример 4*100-54: "))
# print("Ваш ответ: ",task, "Правильный ответ: ",4*100-54)

# a = int(input("Введите ваше первое число: "))
# b = int(input("Введите ваше второе число: "))
# c = int(input("Введите ваше третье число: "))
# d = int(input("Введите ваше четвертое число: "))
# sum1 = a + b
# sum2 = c + d
# print("Ответ: ", round(sum1 / sum2,2))
# name = input("Введите свое имя: ")
# year = int(input("Введите ваш год рождения: "))
# print("Имя пользователя:", name, 2026-year, "лет")

# var = input()
# var_int=int(var)
# var_float=float(var)
# var_str=str(var)
# print(type(var_int),var_int)
# print(type(var_float),var_float)
# print(type(var_str),var_str)

# var1=1
# var2=0
# print(bool(var1), bool(var2))

# var1=True
# var2=False
# print(int(var1), int(var2))




# a = int(input("Вудите диаметр окружности"))
# radius = a//2
# r = (3.14*a**2)/4
# s = 3.14*radius**2
# print(a,s , r**2*3.14)

# a = int(input("ведите а сторону"))
# b = int(input("ведите б сторону"))
# s = (2*a+2*b)
# print (s)

# st  = 'Hello'
# print(st+"  "+st)
# print(st, st)  


# print((st+" ")*5)

# print(lang[0:2])
# print(lang[0:])
# print(lang[2:])
# lang = "Phyton"

lang = "Hello world"
# print|(lang[0:-1:1])
# print|(lang[0::1])
# print|(lang[::2])
# print|(lang[::-1])

# word = input('выведите строку')
# print(lang[3])
# print(lang[:-2])
# print(lang[5])
# print(lang[:-2])
# print(lang[0::2])
# print(lang[1::2])
# print(lang[::-1])
# print(lang[::-2])
# print(len(lang))

# phone_num = "+1-234-567-89-10"
#  print (phone_num.replace('-',' '))
# print(phone_num.replace("++","  ",2))


# word = "Hello World"
# print (word.replace('Hello','BuyBuy'))
# print(phone_num.replace("++","  ",2))

# st = "Дляперео пределения порядка вычислений мы можем использовать"
# print(st.split(' '))

# st = "Дляперео пределения порядка вычислений мы можем использовать"
# st_split = st.split()
# print(st.split(' '))
# sorted_strings = sorted(st_split, key=len)
# print(sorted(st_split,key=len))
# st2 = " ".join(sorted_strings)
# print(st2)


# st="hello"
# print("  ".join(st))

# st=["hello","world"]
# print("  ".join(st))

# st = "Вводится строка состоящая из слов разделенных пробелами"
# print(st.split( ))

# print("Длина строки:",len(st))

# print("Текст в нижнем регистре:\n",st.lower())

# st_fix = st.replace("WALLE","WALL-E")
# print(st_fix)


# earth_count = st.count("Earth")
# print(f"\nСлово 'earth' встречается раз: {earth_count}")
# a = int(input("Введите ваше ferst число: "))
# b = int(input("Введите ваше second число: "))
# if a % 2 == 0 , b % 2 == 0:
#     print(True)
# else:
#     print(False)
  

# grade = int(input("Введите ваше ferst число: "))
# if grade < 25:
#     print('F')
# elif grade < 25 or grade < 45:
#     print('E')
# elif grade < 45 or grade < 50:
#     print('d')
# elif grade < 50 or grade < 60:
#     print('c')
# elif grade < 60 or grade < 80:
#     print('b')



lst = list()
lst = [1, 2, 7, 'Hello', True, 'Hi']
# print(lst)# print(lst[2])# print(lst[2:5])# print(lst[2:-1])# print(lst[::2])

lst.append(False)
print(lst)
lst.insert(12, True)
print(lst)


lst.append(False)
print(lst)
lst.insert(2, True)
lst.remove(7)
print(lst)
# del lst
# print(lst)
# lst.clear()
# print(lst)
lst_idx = lst.index('Hello')
print(lst_idx)
lst_pop = lst.pop(0)
print(lst)
print(lst_pop)
