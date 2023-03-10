# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы
# расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма
# первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать
# программу, которая проверяет счастливость билета.

numbers = int(input("Введите номер билетика: "))

sumLeft = 0
sumRight = 0

for i in range(6):
    if i < 3:
        sumRight += numbers // 10 ** i % 10
    else:
        sumLeft += numbers // 10 ** i % 10

if sumLeft == sumRight:
    print(f"Билетик с номером {numbers} является счастливым")
else:
    print(f"Билетик с номером {numbers} не является счастливым")
