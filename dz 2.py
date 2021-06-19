# Создать список, состоящий из кубов нечётных чисел от 1 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7. Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7. Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# * Решить задачу под пунктом b, не создавая новый список.

numbers_list = []

for number in range (0, 1001):
    if number % 2 != 0:
        numbers_list.append(number**3)
print (numbers_list)

count = 0
while count < 2:
    if count == 1:
        for i, number in enumerate(numbers_list):
            numbers_list[i] +=17

    summa = 0
    for number in numbers_list:
        num = number
        num_sum = 0
        while num % 10 != 0:
            num_sum += num % 10
            num = num // 10

        if num_sum % 7 == 0:
            print (number)
            summa += number

    print (summa)
    count += 1
