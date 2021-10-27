# keyword - модуль, а значит, его нужно импортировать перед использованием
import keyword
# вывести список всех доступных ключевых слов
print(keyword.kwlist)
# или
help('keywords')
#вывести длину списка ключевых слов
print(len(keyword.kwlist))

# 1) Создать переменную типа String
variable_str = "I love QA"
print(variable_str)
# 2) Создать переменную типа Integer
variable_int = 35
print(variable_int)
# 3) Создать переменную типа Float
variable_float = 3.14
print(variable_float)
# 4) Создать переменную типа Bytes
variable_bytes = bytes(155)
print(variable_bytes)
# 5) Создать переменную типа List
variable_list = ["I love QA", 35, 3.14, "Python", True]
print(variable_list)
# 6) Создать переменную типа Tuple
variable_tuple = ("Python", 3.14, False, "I love QA", 35)
print(variable_tuple)
# 7) Создать переменную типа Set
variable_set = ["apple", "orange", "apple", "pear", "orange", "banana"]
print(set(variable_set))
# 8. Создать переменную типа Frozen set
variable_frozenset = "блаблабла"
print(frozenset(variable_frozenset))
# 9) Создать переменную типа Dict
variable_dict = {"name": "Sasha", "age": 35, "experience": 6, 282: "apartment"}
print(variable_dict)
# 10) Вывести в консоль все выше перечисленные переменные с добавлением типа данных
print(type(variable_str), variable_str)
print(type(variable_int), variable_int)
print(type(variable_float), variable_float)
print(type(variable_bytes), variable_bytes)
print(type(variable_list), variable_list)
print(type(variable_tuple), variable_tuple)
print(type(variable_set), variable_set)
print(type(variable_frozenset), variable_frozenset)
print(type(variable_dict), variable_dict)
# 11) Создать 2 переменные String. Создать переменную, в которой сконкатенируете эти переменные. Вывести в консоль
str1 = "Java"
str2 = "Script"
str3 = str1+str2
print(str3)
# 12) Вывести в одну строку переменные типа String и Integer используя “,”
a = 1
b = "ball"
print("I have", a, b)
print("I have", a, "ball")
# 13) Вывести в одну строку переменные типа String и Integer используя “+”
a = 1
b = "ball"
print("I have" + ' ' + str(a) + ' ' + b)

