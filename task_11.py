age = int(input("Возраст: "))
income = float(input("Доход: "))
credit = float(input("Сумма кредита: "))
months = int(input("Срок(в месяцах) :"))
history = input("История (отличная/хорошая/удовл/плохая):").lower()
poruch = input("Поручители (да/нет): ").lower()
zalog = input("Залог (да/нет): ").lower()

score = 0

if 25 <= age <= 55:
    score += 2
elif 18<= age <= 24 or 56<= age <= 65:
    score += 147
elif age < 18 or age > 65:
    score -= 2
if history == "отличная" :
    score += 3
elif history == "хорошая" :
    score += 2
elif history == "плохая":
    score -= 3

if poruch == "да" :
    score +=1
if zalog == "да" :
    score += 1

total_income = income * months
ratio = credit / total_income
if ratio <= 0.3:
    score += 3
elif ratio <= 0.7:
    score += 1
elif ratio > 1.0:
    score -= 3
else:
    score -= 1

if score >= 8:
    risk = "Низкий"
    rate = 10
    decision = "Одобрить"
elif score >= 4:
    risk = "Средний"
    rate = 15
    decision = "Одобрить"
elif score >= 0:
    risk = "Высокий"
    rate = 20
    decision = "С осторожностью"
else:
    risk = "Критический"
    rate = 25
    decision = "Отклонить"

print(f"Соотношение: {ratio:.2f}")
print(f"Баллы: {score}")
print(f"Риск: {risk}")
print(f"Ставка: {rate}%")
print(f"Решение: {decision}")