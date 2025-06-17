import math


def root(a,b,f):
    return (math.sqrt(a - b) / (a - b)) + math.sqrt(f)
def hand(a,b,f):
    try:
        result = root(a,b,f)
        print (result)

 

    except(ZeroDivisionError):
        print('Деление на ноль')
        result = 'Деление на ноль'
    except(TypeError):
        print('Ошибка типов данных')
        result = 'Ошибка типов данных'
    except(ValueError):
        print('Извлечение корня из отрицательного числа')
        result = 'Извлечение корня из отрицательного числа'
    except Exception as e:
        print(f"Тип ошибки {e}")
        result = (f"Тип ошибки {e}")

    return  result



"""
1. Деление на ноль при (a - b) == 0
2. Все нули
3. Отрицательное значение под корнем
4. Нормальный случай
5. Текст в аргументах
6. Пустой ввод
"""