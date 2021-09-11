#cоздать 2 переменные типа String с разными значениями
country = "Belarus"
age = "35"
#cоздать 4 переменные типа Integer с разными значениями
weight = 52
height = 167
salary = 500
pet = 1
#cоздать 3 переменные типа Float с разными значениями
body_temp = 36.6
pi_value = 3.14
air_temp = 18.5
#реализовать 15 вариантов сравнения int переменных с операторами >, <, >=, <=, !=
print(weight > height)
print(salary > pet)
print(height > salary)
print(salary < height)
print(pet < salary)
print(weight < pet)
print(salary >= weight)
print(weight >= height)
print(pet >= weight)
print(pet <= weight)
print(height <= weight)
print(salary <= pet)
print(weight != height)
print(pet != salary)
print(height != pet)
#реализовать 9 вариантов сравнения Float переменных с операторами >, <, >=, <=, !=
print(body_temp > pi_value)
print(air_temp > body_temp)
print(pi_value < air_temp)
print(air_temp < pi_value)
print(pi_value >= air_temp)
print(body_temp >= pi_value)
print(body_temp <= air_temp)
print(pi_value <= body_temp)
print(body_temp != air_temp)
# реализовать 10 вариантов сравнения int переменных с операторами >, <, >=, <=, !=
# и условными выражениями (and, or, not)
result_1 = weight > 50 and height > 160
print(result_1)
result_2 = salary < 400 and height < 160
print(result_2)
result_3 = pet >= 3 and height >= 150
print(result_3)
result_4 = pet <= 1 and height <= 170
print(result_4)
result_5 = pet != 2 and salary != 400
print(result_5)
result_6 = salary > 499 or pet > 1
print(result_6)
result_7 = weight < 50 or height < 160
print(result_7)
result_8 = not pet > 1
print(result_8)
result_9 = not salary >= 500
print(result_9)
result_10 = not weight != 52
print(result_10)