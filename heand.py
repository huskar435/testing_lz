import math

def function(a, b, f):
    return (math.sqrt(a - b) / (a - b)) + math.sqrt(f)

def hand(a, b, f):
    try:
        a = float(a)
        b = float(b)
        f = float(f)
    except (ValueError, TypeError):
        print('Ошибка типов данных')
        return 'Ошибка типов данных'
    try:
        result = function(a, b, f)
        print(result)
    except ZeroDivisionError:
        print('Деление на ноль')
        return 'Деление на ноль'
    except ValueError:
        print('Извлечение корня из отрицательного числа')
        return 'Извлечение корня из отрицательного числа'
    except Exception as e:
        print(f"Тип ошибки {e}")
        return f"Тип ошибки {e}"

    return result



"""
1. Деление на ноль при (a - b) == 0
2. Все нули
3. Отрицательное значение под корнем
4. Нормальный случай
5. Текст в аргументах
6. Пустой ввод
"""