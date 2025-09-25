number_words = {
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five"
}
try:
    number = int(input("Введите целое число от 1 до 5: \n"))
    if 1 <= number <= 5:
        print(f"Число {number} на английском: {number_words[number]}")
    else:
        print("Ошибка! Введите число от 1 до 5")
except ValueError:
    print("Ошибка! Введите целое число от 1 до 5")