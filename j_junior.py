try:
    a = int(input("Введите первое число:"))
    b = int(input("Введите второе число"))
    result = a / b
except ValueError:
    print("Введено не число")
except ZeroDivisionError:
    print("На ноль делить нельзя")
else:
    print(result)
finally:
    print("Работа программы завершена")
