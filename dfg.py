import math


def function(a,b,f):
   return (math.sqrt(a - b) / (a - b)) + math.sqrt(f)

def zal(a,b,f):
    try:
        result = function(a,b,f)
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