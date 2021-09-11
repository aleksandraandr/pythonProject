str = "Hello world!"
print(str)
#Hello world! напечатать всю строку
print(str[0]) #напечатать первый символ строки
print(str[2:5]) #напечатать символы с третьего по пятый
print(str[2:]) #напечатать символы с третьего до конца строки
print(str*2) #напечатать строку два раза
print(str+"TEST") #напечатать конкатенирующую (объединенную) строку
age = 35 #переменная типа int (целое число)
print(age)
normal_body_temp = 36.6
print(normal_body_temp) #переменная типа float
list_numbers = [1, 2, 3, 255] #список с именем list_numbers
the_bytes = bytes (list_numbers) #переменная типа bytes с именем the_bytes
print(the_bytes)
list_datatypes = ["Python", 19, 3.14, "tiger", 35]
print(list_datatypes) #напечатать полный список
print(list_datatypes[0]) #вывести первый элемент списка
print(list_datatypes[1:3]) #вывести элементы списка, начиная со второго и заканчивая третьим
print(list_datatypes[2:]) #вывести элементы списка, начиная со второго и до конца
tinylist = ["sasha", 35] #новый список
print(tinylist*2) #вывести все элементы списка два раза
print(list_datatypes+tinylist) #вывести объединенные списки
print(list_datatypes[-1]) #получение последнего элемента списка
tuple = ("Python", 19, 3.14, "tiger", 35)
print(tuple) #вывести все элементы кортежа
print(tuple[0]) #вывести первый элемент кортежа
print(tuple[1:3]) #вывести второй и третий элементы
print(tuple[2:]) #вывести все элементы, начиная с третьего
tinytuple = ("sasha", 35) # новый кортеж
print(tinytuple*2) #вывести все элементы два раза
print(tuple[1:3]*2) #вывести второй и третий элементы два раза
print(tuple+tinytuple) #вывести объединенные элементы кортежей
print(tuple[-1]) #вывести последний элемент кортежа
set()
print(set()) #создание пустых множеств
frozenset()
print(frozenset()) #создание пустых множеств
basket = {"apple", "orange", "apple", "pear", "orange", "banana"}
print(basket) #дубликаты будут удалены
x = set([1,2,3,4,5,6,7,8,9])
print(x)
x = "блаблабла"
print(set(x)) #преобразование str во множество
x = ("apple", "banana", "cherry")
print(set(x)) #преобразование tuple во множество
x = ["apple", "banana", "cherry"]
print(set(x)) #преобразование list во множество
x = frozenset("мама мыла раму")
print(x)
dict_ages = {"Сергей":37,"Саша":35,"Егор":19}
print(dict_ages) #вывести полное содержимое словаря
print(dict_ages.keys()) #вывести все ключи словаря
print(dict_ages.values()) #вывести все значения в словаре
str1 = "Py"
str2 = "thon"
str3 = str1+str2
print(str3)
int1 = 100
int2 = 50
int3 = int1+int2
print(int3)
int4 = int1/int2
print(int4)
int4 = int1//int2
print(int4)
int5 = int1*int2
print(int5)
int6 = int1%int2
print(int6)
int7 = 5
int7 %=3
print(int7)