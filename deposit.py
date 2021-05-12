# создаем словарь с процентами депозитов
per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0}
# вводим сумму депозита
money = int(input("Please enter the deposit amount: "))
deposit = []

for value in per_cent.values():
    deposit.append(round(float(money/100 * value))) #создаем список с выплатами

print("The deposits payments = ", deposit)
deposit.sort()# сортировка списка по возрастанию значений
print("The maximum deposit payments = ", deposit[-1]) # выводим последний элемент списка


