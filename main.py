print("КАЛЬКУЛЯТОР".center(30))

while True:
    try:
        a, b = tuple(map(int, input("Введіть два числа через пропуск: ").split()))
    except:
        print("Некоректне введення.")
        continue
    print(f"""
    Оберіть дію для числа {a} та {b}:
        0. Вихід
        1. Додавання числа {a} + {b}
        2. Віднімання {a} - {b}
        3. Множення числа {a} * {b}
        3. Ділення числа {a} : {b}
        5. Піднесення числа {a} до сепеня числа {b}
        6. Сума квадратів чисел {a} та {b}
        7.Різниця квадратів чисел {a} та {b}
        8. Квадрат суми чисел {a} та {b}
        9. Квадрат різниці чисел {a} та {b}
        10. Усі парні числа між числами {a} та {b}
        11. Усі непарні числа між числами {a} та {b}
        12. Залишок від ділення числа {a} на число {b}
    """)

    user_choice = input('Ваш вибір: ')

    if user_choice == '0':
        break
