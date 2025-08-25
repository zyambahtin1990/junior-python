

age = int(input("Введите Ваш возраст: \n"))
nation_rf = input("Есть ли у Вас гражданство РФ: \n")
responsibility = input("Привлекались ли Вы к уголовной и иным видам ответсвенности? \n")
if age >=18 and nation_rf == "да" and responsibility == "нет":
    print("Вы можете участвовать в голосовании")
else:
    print("Вы не можете участвовать в голосовании")


