per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму, которую планируете положить под проценты:"))
TKB = int((per_cent['ТКБ']) * (money/100))
SKB = int((per_cent['СКБ']) * (money/100))
VTB = int((per_cent['ВТБ']) * (money/100))
SBER = int((per_cent['СБЕР']) * (money/100))
deposit = {}
deposit['TKB'] = TKB
deposit['SKB'] = SKB
deposit['VTB'] = VTB
deposit['SBER'] = SBER

print("Накопленные средства за год вклада в каждом из банков =",deposit)
print("Максимальная сумма, которую вы можете заработать:", max(deposit.values()))