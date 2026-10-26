import random

secret = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Ваша догадка: "))
    attempts += 1

    if guess < secret:
        print("Загаданное число больше")
    elif guess > secret:
        print("Загаданное число меньше")
    else:
        print(f"Угадали, попыток: {attempts}")
        break