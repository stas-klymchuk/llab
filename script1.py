def main():
    # Словник з даними користувачів (мінімум 4 користувачі)
    # Формат: "логін": {"password": "пароль", "grades": [оцінки]}
    users_db = {
        "student1": {
            "password": "123",
            "grades": [10, 8, 3, 12, 4, 7]
        },
        "student2": {
            "password": "abc",
            "grades": [2, 3, 4, 1, 5]
        },
        "student3": {
            "password": "pass",
            "grades": [11, 9, 10, 12, 8, 6, 5]
        },
        "student4": {
            "password": "qwerty",
            "grades": [4, 3, 2, 5, 6]
        }
    }

    print("=== АВТОРИЗАЦІЯ КОРИСТУВАЧА ===")
    input_login = input("Введіть логін: ").strip()
    input_password = input("Введіть пароль: ").strip()

    # Перевірка правильності логіна та пароля
    if input_login in users_db and users_db[input_login]["password"] == input_password:
        print(f"\n Вітаємо, {input_login}! Авторизація успішна.\n")

        grades = users_db[input_login]["grades"]

        # Виведення переліку всіх оцінок
        print(f"Перелік ваших оцінок: {grades}")

        # Підрахунок кількості задовільних (5-12) та незадовільних (1-4)
        satisfactory_count = 0
        unsatisfactory_count = 0

        for grade in grades:
            if 5 <= grade <= 12:
                satisfactory_count += 1
            elif 1 <= grade <= 4:
                unsatisfactory_count += 1

        # Виведення результатів аналізу
        print("-" * 35)
        print(f"Кількість задовільних оцінок (від 5 до 12): {satisfactory_count}")
        print(f"Кількість незадовільних оцінок (від 1 до 4): {unsatisfactory_count}")
        print("-" * 35)

    else:
        print("\n Помилка: Неправильний логін або пароль!")


if __name__ == "main":
    main()
