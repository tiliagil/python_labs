word = input("Введите строку: ")
reversed_word = word[::-1]

if word == reversed_word:
    print("Строка является палиндромом")
else:
    print("Строка не является палиндромом")
