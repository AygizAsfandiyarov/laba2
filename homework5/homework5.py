def get_number():
    for num in range(30):
        if num % 2 != 0:
            yield num

# Создаем генератор
numbers = get_number()

numbers_list = list(numbers)

first = numbers_list[0] # Первое значение
fifth = numbers_list[4] # Пятое значение
last = numbers_list[-1] # Последнее значение

print("Первое нечетное число:", first)
print("Пятое нечетное число:", fifth)
print("Последнее нечетное число:", last)