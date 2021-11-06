# Циклы While
# 1.Создать переменную count со значением 0
count = 0
# 2.Создать переменную range_count со значением 10
range_count = 10
# 3.Создать переменную for_count со значением 0
for_count = 0
# 4.Создать переменную run со значением True
run = True
# 5.Сделать цикл while, который будет работать, пока run
# 5.1 Выводить в консоль "Hello, Cycle"
while True:
    print("Hello, Cycle")
# 6.Сделать цикл while, который будет работать, пока run
# 6.1 Выводить в консоль (“Step =”, count)
# 6.2 Переменной count прибавлять 1 с присвоением
while True:
    print("Step =", count)
    count += 1
# 7.Сделать цикл while, который будет работать пока count < range_count
# 7.1 Выводить в консоль (“Step =”, count)
# 7.2 Переменной count прибавлять 1 с присвоением
while count < range_count:
    print("Step =", count)
    count += 1
# 8.Сделать цикл while, который будет работать пока run
# 8.1 Выводить в консоль (“Step =”, count)
# 8.2 Переменной count прибавлять 1 с присвоением
# 8.2 Сделать if с условием, если count равен range_count, то цикл остановится
# 8.3 В теле if вывести в консоль (“STOP”, count)
while True:
    print("Step =", count)
    count += 1
    if count == range_count:
        break
print("STOP", count)
# Циклы For
# 9.Сделать цикл for c переменной item, который будет работать,
# пока счётчик range досчитает от for_count до range_count
# 9.1 Вывести в консоль (‘Step =’, item)
for item in range(0, 10):
    print("Step =", item)
# 10.Сделать цикл for c переменной item, который будет работать,
# пока счётчик range досчитает от 0 до 30
# 10.1 Вывести в консоль (‘Step =’, item)
# 10.2 Сделать if с условием, если item равен 5, то вывести в консоль (‘Item =’, item)
# 10.3 Сделать if с условием, если item равен 10, то вывести в консоль (‘Item =’, item)
# 10.4 Сделать if с условием, если item меньше 4, то вывести в консоль (‘Item <’, item)
# 10.5 Сделать if с условием, если item больше или равно 27, то вывести в консоль (‘Item >=’, item)
for item in range(0, 30):
    print("Step =", item)
    if item == 5:
        print("Item =", item)
    if item == 10:
        print("Item =", item)
    if item < 4:
        print("Item <", item)
    if item >= 27:
        print("Item >=", item)
# 11.Сделать цикл for c переменной item, который будет работать,
# пока счётчик range досчитает от 0 до range_count +1
# 11.1 Вывести в консоль (‘Step =’, item)
# 11.2 Сделать if с условием, если item равен 7
# - В теле if создать переменную inner_count равную 0
# - В теле if вывести в консоль (-- inner_count =’, inner_count)
# - В теле if сделать ещё один цикл for с переменной inner_item,
# который будет работать пока счётчик range досчитает от 0 до item
# -- Вывести в консоль (‘-------- Inner_Step =’, inner_item)
# -- Сделать if, если inner_item равен 5, то в inner_count присвоить inner_item
# - За пределами тела предыдущего цикла вывести в консоль (-- inner_count =’, inner_count)
for item in range(0, range_count + 1):
    print("Step =", item)
    if item == 7:
        inner_count = 0
        print("-- inner_count =", inner_count)
    for inner_item in range(0, item):
        print("-------- Inner_Step =", inner_item)
        if inner_item == 5:
            inner_count = inner_item
            print("-- inner_count =", inner_count)
# 12.Сделать цикл for c переменной item, который будет работать,
# пока счётчик range досчитает от 0 до 20
# 12.1 Вывести в консоль (‘Step =’, item)
# 12.2 Сделать if с условием, если item больше 7 и item меньше 12
# - В теле if вывести (‘If_item =’, item)
# - В теле if поставить continue
# 12.3 Выйти з if. Вывести в консоль (End_iteration =’, item)
for item in range(0, 20):
    print("Step =", item)
    if 7 < item < 12:
        print("If_item =", item)
        continue
print("End_iteration =", item)








