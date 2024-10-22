import random

def find_multiples():
    # Генерируем список случайных чисел от 0 до 200, размером 10
    numbers = [random.randint(0, 200) for _ in range(10)]
    
    # Выводим сгенерированные числа
    print(f"Сгенерированные числа: {numbers}")
    
    # Фильтруем числа, кратные x с помощью лямбда-функции
    multiples = list(filter(lambda num: num % x == 0, numbers))
    
    return multiples

def valid_input():
    while True:
        user_input = input("Введите положительное целое число X: ")
        try:
            x = int(user_input)
            if x <= 0:
                print("Ошибка: число должно быть положительным.")
            else:
                return x
        except ValueError:
            print("Ошибка: ввод должен быть целым положительным числом.")

x = valid_input()
result = find_multiples()
print(f"Числа, кратные {x}: {result}")
