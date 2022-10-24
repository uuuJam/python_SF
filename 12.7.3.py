per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
Money = float(input("Сколько вы готовы вложить? : "))
TKB = round(Money / 100 * per_cent['ТКБ'],2)
SKB = round(Money / 100 * per_cent['СКБ'],2)
VTB = round(Money / 100 * per_cent['ВТБ'],2)
SBER = round(Money / 100 * per_cent['СБЕР'],2)

deposit = [TKB, SKB, VTB, SBER]
print("Доход в каждом банке:", deposit)

max_number = max(deposit)
print("Максимальная сумма, которую вы можете заработать - ", max_number)