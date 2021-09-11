#Сделать скрипт, используя функцию input():
#-функция должна на вход принимать целое число;
#-внутри функции должно сгенерироваться рандомное целое число (import random)...(random.randint(1, 100));
#-выводить должна "Вы ввели число = (введённое число), которое (меньше/больше/равно) сгенерированного числа"
import random
random_value = random.randint(1, 100)
user_value = int(input("Введите целое число: "))
if user_value == random_value:
    print("Вы ввели число = ", user_value, "которое равно сгенерированному числу", random_value)
elif user_value > random_value:
    print("Вы ввели число = ", user_value, "которое больше сгенерированного числа", random_value)
else:
    print("Вы ввели число = ", user_value, "которое меньше сгенерированного числа", random_value)