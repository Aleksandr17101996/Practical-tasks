per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}

money = int(input("Введите сумму которую планируете положить под проценты:"))

per = list(per_cent.values())
deposit = list(map(lambda x: x * money/100, per))
deposit_max = max(deposit)

print("Максимальная сумма, которую вы можете заработать", deposit_max)