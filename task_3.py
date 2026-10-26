summa = int(input("Введите сумму в рублях (целое число): "))

coins_100 = summa // 100
summa = summa % 100

coins_50 = summa // 50
summa = summa % 50

coins_10 = summa // 10
summa = summa % 10

coins_5 = summa // 5
summa = summa % 5

coins_2 = summa // 2
summa = summa % 2

coins_1 = summa

print(f"Купюр по 100: {coins_100}")
print(f"Купюр по 50: {coins_50}")
print(f"Купюр по 10: {coins_10}")
print(f"Купюр по 5: {coins_5}")
print(f"Монет по 2: {coins_2}")
print(f"Монет по 1: {coins_1}")
