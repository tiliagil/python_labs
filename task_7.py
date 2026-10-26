minutes = int(input("Введите количество потраченных минут: "))
sms = int(input("Введите количество сообщений: "))
internet = int(input("Введите количество потраченных Мб: "))

if minutes > 60:
    extra_minutes_cost = (minutes - 60) * 0.89
else:
    extra_minutes_cost = 0

if sms > 30:
    extra_sms_cost = (sms - 30) * 0.59
else:
    extra_sms_cost = 0

if internet > 1024:
    extra_internet_cost = (internet - 1024) * 0.79
else:
    extra_internet_cost = 0

base = 24.99
subtotal = base + extra_minutes_cost + extra_sms_cost + extra_internet_cost
tax = subtotal * 0.02
total = subtotal + tax

print(f"Базовая сумма: {base:.2f}")
if extra_minutes_cost > 0:
    print(f"Доплата за минуты: {extra_minutes_cost:.2f}")
if extra_sms_cost > 0:
    print(f"Доплата за SMS: {extra_sms_cost:.2f}")
if extra_internet_cost > 0:
    print(f"Доплата за интернет: {extra_internet_cost:.2f}")
print(f"Налог: {tax:.2f}")
print(f"Итого к оплате: {total:.2f}")