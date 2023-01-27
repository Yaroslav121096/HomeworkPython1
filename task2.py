# Задача 2: Найдите сумму цифр трехзначного числа

numbers = int(input("Введите число: "))
sum = 0

while numbers > 0:
    number = numbers % 10
    sum = sum + number
    numbers = numbers // 10

print("Сумма цифр числа:", sum)