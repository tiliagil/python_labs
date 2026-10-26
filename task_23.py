print("Программа для анализа личных финансов")
print("------------------------------------")

income = float(input("Введите ваш доход за месяц: "))

print("Введите расходы (если нет, введите 0):")
housing = float(input("Жилье: "))
food = float(input("Питание: "))
transport = float(input("Транспорт: "))
fun = float(input("Развлечения: "))
other = float(input("Прочее: "))

total_expenses = housing + food + transport + fun + other
balance = income - total_expenses

print("\nРезультаты:")
print("Общий доход:", income)
print("Общие расходы:", total_expenses)
print("Остаток:", balance)

print("\nРекомендации:")

if balance < 0:
    print("- Вы тратите больше, чем зарабатываете. Необходимо сократить расходы.")
elif balance < income * 0.1:
    print("- Ваш остаток очень мал. Рекомендуется откладывать хотя бы 10% дохода.")
else:
    print("- У вас есть свободные средства. Часть из них можно отложить на сбережения.")

if fun > income * 0.2:
    print("- Расходы на развлечения превышают 20% дохода. Стоит их сократить.")

if food > income * 0.3:
    print("- Расходы на питание превышают 30% дохода. Рекомендуется готовить дома чаще.")

if balance > 0 and fun <= income * 0.2 and food <= income * 0.3:
    print("- Ваш бюджет сбалансирован. Вы можете планировать крупные покупки.")