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
