for i in range(1, 11):
    print(i)



n = int(input("Введите число N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Сумма чисел от 1 до {n}: {total}")



num = int(input("Введите число для таблицы умножения: "))
for i in range(1, 11):
    print(f"{num} × {i} = {num * i}")



count = 10
while count > 0:
    print(count)
    count -= 1
print("Старт!")



start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
count = 0
for i in range(start, end + 1):
    if i % 2 == 0:
        count += 1
print(f"Количество чётных чисел: {count}")



import random

secret = random.randint(1, 10)
guess = 0
while guess != secret:
    guess = int(input("Угадайте число от 1 до 10: "))
    if guess < secret:
        print("Больше!")
    elif guess > secret:
        print("Меньше!")
print("Поздравляем! Вы угадали!")



n = int(input("Введите число n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")



num = input("Введите целое число: ")
total = 0
for digit in num:
    if digit.isdigit():
        total += int(digit)
print(f"Сумма цифр: {total}")



n = int(input("Введите высоту треугольника: "))
for i in range(1, n + 1):
    print("*" * i)



import random

correct = 0
for _ in range(5):
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = int(input(f"{a} + {b} = "))
    if answer == a + b:
        print("Верно!")
        correct += 1
    else:
        print("Ошибка!")
print(f"Правильных ответов: {correct}")


