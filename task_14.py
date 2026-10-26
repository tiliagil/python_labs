text1 = input("Введите первый набор чисел через пробел: ")
text2 = input("Введите второй набор чисел через пробел: ")

set1 = set(float(x) for x in text1.split())
set2 = set(float(x) for x in text2.split())

common = set1 & set2
only_first = set1 - set2
only_second = set2 - set1
exclusive = set1 ^ set2
print(f"\n1. Числа в обоих наборах: {common}")
print(f"2. Числа только в первом наборе: {only_first}")
print(f"3. Числа только во втором наборе: {only_second}")
print(f"4. Числа из обоих наборов, кроме общих: {exclusive}")