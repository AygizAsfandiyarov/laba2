def valid_date(day, month, year):
    if not (1 <= month <= 12):
        return False
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 1 <= day <= 31
    if month in [4, 6, 9, 11]:
        return 1 <= day <= 30
    if month == 2:
        if (year % 4 == 0 and year % 100 !=0) or (year % 400 ==0):
            return 1 <= day <= 29
        else:
            return 1 <= day <= 28 
    return False

def calculate_age():
    while True:
        birth_date_str = input("Введите дату рождения (дд/мм/гггг): ")
        try:
            day, month, year = map(int, birth_date_str.split('/'))
            if not valid_date(day, month, year):
                print("Некорректная дата.")
            break
        except ValueError:
            print("Ошибка: введите дату в правильном формате (дд/мм/гггг) и убедитесь, что числа в пределах диапазона.")

    while True:
        today_date_str = input("Введите текущую дату (дд/мм/гггг): ")
        try:
            today_day, today_month, today_year = map(int, today_date_str.split('/'))
            if not valid_date(today_day, today_month, today_year):
                print("Ошибка: некорректная текущая дата.")
                continue
            break
        except ValueError:
            print("Ошибка: введите дату в правильном формате (дд.мм.гггг) и убедитесь, что числа в пределах диапазона.")

    age = today_year - year

    if (today_month, today_day) < (month, day):
        age -= 1

    print(f"Ваш возраст: {age} лет")

calculate_age()
