sales = [
    {"name": "Тушь", "price": 450, "count": 15},
    {"name": "Помада", "price": 300, "count": 25},
    {"name": "Тушь", "price": 450, "count": 5},
    {"name": "Крем", "price": 800, "count": 10},
    {"name": "Помада", "price": 300, "count": 10},
    {"name": "Тени", "price": 600, "count": 8}
]

itog = {}

for tovar in sales:
    name = tovar["name"]
    summa = tovar["price"] * tovar["count"]

    if name in itog:
        itog[name] = itog[name] + summa
    else:
        itog[name] = summa

print("Выручка по товарам:")
for name, total in itog.items():
    print(f"  {name}: {total} руб.")

best = ""
max_sum = 0

for name, total in itog.items():
    if total > max_sum:
        max_sum = total
        best = name

print(f"\nСамый прибыльный: {best} (выручка: {max_sum} руб.)")

count = len(itog)
print(f"Количество уникальных: {count}")