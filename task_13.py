text = input("Введите числа через пробел: ")
parts = text.split()

numbers = [float(x) for x in parts]

unique = set(numbers)
print(f"Уникальные: {list(unique)}")

even = [x for x in numbers if x == int(x) and int(x) % 2 ==0]
odd = [x for x in numbers if x == int(x) and int(x) % 2 != 0]
negative =[x for x in numbers if x< 0]
floats = [x for x in numbers if x != int(x)]
sum_5 = sum(x for x in numbers if x == int(x) and x % 5 ==0)
print(f"Четные: {even}")
print(f"Нечетные: {odd}")
print(f"Отрицательные: {negative}")
print(f"Дробные: {floats}")
print(f"Сумма кратных 5: {sum_5}")
print(f"Максимум: {max(numbers)}")
print(f"Минимум: {min(numbers)}")