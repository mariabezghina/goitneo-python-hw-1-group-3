from collections import defaultdict
from datetime import datetime, timedelta

users = [
    {"name": "Bill Rickson", "birthday": datetime(1955, 10, 28)},
    {"name": "Jill Valentine", "birthday": datetime(1974, 11, 30)},
    {"name": "Kim Jelly", "birthday": datetime(1980, 10, 21)},
    {"name": "Jan Koum", "birthday": datetime(1976, 2, 24)},
    {"name": "Bill Campbell", "birthday": datetime(1955, 10, 20)},
    {"name": "Robert Washer", "birthday": datetime(1955, 10, 20)},
    {"name": "Rick Davis", "birthday": datetime(1955, 10, 19)},
    {"name": "Bob Morton", "birthday": datetime(1955, 10, 19)},
    {"name": "Anna Styles", "birthday": datetime(1955, 10, 15)},
]

def get_birthdays_per_week(users):
    # Підготовка Даних
    birthday_dict = defaultdict(list)

    # Отримання Поточної Дати
    today = datetime.today().date()

    # Перебір Користувачів
    for user in users:
        # Конвертація Дати
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        # Оцінка Дати на Цей Рік
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        # Порівняння з Поточною Датою
        delta_days = (birthday_this_year - today).days

        # Визначення Дня Тижня
        if delta_days < 7:
            # Якщо це вихідний, переносимо на понеділок
            birthday_day = (today + timedelta(days=delta_days)).strftime("%A")
            if birthday_day in ["Saturday", "Sunday"]:
                birthday_day = "Monday"

            # Зберігання Результату
            birthday_dict[birthday_day].append(name)

    # Виведення Результату
    for day, names in birthday_dict.items():
        print(f"{day}: {', '.join(names)}")

# Приклад виклику функції

get_birthdays_per_week(users)
