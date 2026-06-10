import random

print("=== Игра: Камень, Ножницы, Бумага ===")

choices = ["камень", "ножницы", "бумага"]

while True:
    user_choice = input(
        "\nВыберите: камень, ножницы, бумага "
        "(или 'выход' для завершения): "
    ).lower()

    if user_choice == "выход":
        print("Спасибо за игру!")
        break

    if user_choice not in choices:
        print("Ошибка! Введите правильный вариант.")
        continue

    computer_choice = random.choice(choices)

    print(f"Вы выбрали: {user_choice}")
    print(f"Компьютер выбрал: {computer_choice}")

    if user_choice == computer_choice:
        print("Ничья!")
    elif (
        (user_choice == "камень" and computer_choice == "ножницы") or
        (user_choice == "ножницы" and computer_choice == "бумага") or
        (user_choice == "бумага" and computer_choice == "камень")
    ):
        print("Вы победили!")
    else:
        print("Компьютер победил!")