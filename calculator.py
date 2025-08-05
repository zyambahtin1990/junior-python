try:
    a = int(input("Введите первое число: "))
    b = int(input("Введите второе число: "))
    amount = a + b
except ValueError:
    print("Введено не число")
else:
    print("Результат сложения:", amount)


try:
    c = int(input("Введите первое число: "))
    d = int(input("Введите второе число: "))
    difference = c - d
except ValueError:
    print("Введено не число")
else:
    print("Результат вычитания:", difference)


try:
    e = int(input("Введите первое число: "))
    f = int(input("Введите второе число: "))
    multiplication = e * f
except ValueError:
    print("Введено не число")
else:
    print("Результат умножения:", multiplication)


try:
    j = int(input("Введите первое число: "))
    h = int(input("Введите второе число: "))
    division = j / h
except ValueError:
    print("Введено не число")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print("Результат деления:", division)


