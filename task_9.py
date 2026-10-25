measure = input("Тип измерения (длина/масса/температура): ").lower()
from_unit = input("Из какой единицы: ").lower()
to_unit = input("В какую единицу: ").lower()
value = float(input("Значение: "))

result = None

if measure == "длина":
    if from_unit == "мм":
        value_in_m = value / 1000
    elif from_unit == "см":
        value_in_m = value / 100
    elif from_unit == "м":
        value_in_m = value
    elif from_unit == "км":
        value_in_m = value * 1000

    if to_unit == "мм":
        result = value_in_m * 1000
    elif to_unit == "см":
        result = value_in_m * 100
    elif to_unit == "м":
        result = value_in_m
    elif to_unit == "км":
        result = value_in_m / 1000

elif measure == "масса":
    if from_unit == "г":
        value_in_kg = value / 1000
    elif from_unit == "кг":
        value_in_kg = value
    elif from_unit == "т":
        value_in_kg = value * 1000

    if to_unit == "г":
        result = value_in_kg * 1000
    elif to_unit == "кг":
        result = value_in_kg
    elif to_unit == "т":
        result = value_in_kg / 1000

elif measure == "температура":
    if from_unit == "c":
        celsius = value
    elif from_unit == "f":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "k":
        celsius = value - 273.15

    if to_unit == "c":
        result = celsius
    elif to_unit == "f":
        result = celsius * 9 / 5 + 32
    elif to_unit == "k":
        result = celsius + 273.15

if result is not None:
    print(f"{value} {from_unit} = {result:.2f} {to_unit}")
else:
    print("Неизвестный тип измерения или единица")