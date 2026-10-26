fullname = input("Введите ФИО: ")
words = fullname.split()
surname = words[0]
name = words[1]
patronymic = words[2]
print(f"Фамилия И.О. - {surname} {name[0]}.{patronymic[0]}.")