#Сделать скрипт, используя функцию input():
#-функция должна на вход принимать целое число;
#-внутри функции должно сгенерироваться рандомных два целых числа (import random)...(random.randint(1, 100));
#-выводить должна "Вы ввели число = (введённое число), которое (меньше/больше/равно и меньше/больше/равно)
# сгенерированному числу"
import random
random_value_1 = random.randint(1, 100)
random_value_2 = random.randint(1, 100)
user_value = int(input("Введите целое число: "))
if user_value > random_value_1:
    if user_value > random_value_2:
        print("Вы ввели число = ", user_value, "которое больше сгенерированного числа", random_value_1)
        print("Вы ввели число = ", user_value, "которое больше сгенерированного числа", random_value_2)
elif user_value <= random_value_1 and user_value <= random_value_2:
    print("Вы ввели число = ", user_value, "которое меньше сгенерированного числа", random_value_1)
    print("Вы ввели число = ", user_value, "которое меньше сгенерированного числа", random_value_2)
else:
    print("Вы ввели число = ", user_value, "которое меньше/больше/равно сгенерированному числу", random_value_1)
    print("Вы ввели число = ", user_value, "которое меньше/больше/равно сгенерированному числу", random_value_2)