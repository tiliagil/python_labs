summa = int(input("Введите сумму покупки: "))
age = int(input("Введите возраст: "))
birthday = input("У вас сегодня день рождения? (да/нет): ").lower()
vip = input("Вы VIP-клиент? (да/нет): ").lower()

discount = 0

if summa > 1000:
    discount += 10
if age >= 63:
    discount += 5
if birthday == "да":
    discount += 5

if vip == "да":
    discount = max(discount, 15)

if discount > 25:
    discount = 25

total = summa - summa * discount / 100

print(f"Скидка: {discount}%")
print(f"Итоговая сумма: {total:.2f}")