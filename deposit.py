per_cent = {'ТКБ': 5.6,
            'СКБ': 5.9,
            'ВТБ': 4.28,
            'СБЕР': 4.0}
money = int(input("Please enter the deposit amount: "))
deposit = []

for value in per_cent.values():
    deposit.append(round(float(money/100 * value)))

print("The deposits payments = ", deposit)
deposit.sort()
print("The maximum deposit payments = ", deposit[-1])


