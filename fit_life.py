# Проект FitLife - MVP версия 1.0


# 1. Знакомство
while True:
    try:
        user_name = input('Как вас зовут?\n').strip()
        # Можно завести список допустимых имен, но словарь сюда не вместить
        if not user_name:
            raise ValueError
        break
    except ValueError:
        print('Введите непустое имя')
while True:
    try:
        user_age = int(input('Введите ваш возраст:\n'))
        # Ограничим возраст с нуля, младенцы не в счет
        if user_age <= 0:
            raise ValueError
        break
    except ValueError:
        print('Некорректное значение! Повторите ввод')
# 2. Сбор данных
while True:
    try:
        user_weight = float(input('Введите ваш вес, кг:\n'))
        # Человек должен что-то весит, сверху не будем ограничивать
        if user_weight <= 0:
            raise ValueError
        break
    except ValueError:
        print('Некорректное значение! Повторите ввод')
while True:
    try:
        user_height = float(input('Введите ваш рост, в метрах:\n'))
        # Есть деление на нуль в функции, границы роста человека
        if (user_height <= 0) or (user_height > 3):
            raise ValueError
        break
    except ValueError:
        print('Некорректное значение! Повторите ввод')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
def bmi_calculation(weight, height):
    """Функция для расчета ИМТ"""
    try:
        return round(weight / (height ** 2), 1)
    except ZeroDivisionError:
        print('YOU SHALL NOT PASS')


bmi = bmi_calculation(user_weight, user_height)


WATER_PER_KG = 30
MLITER_TO_LITER = 1000


# Подсчет воды: вес * 30 мл
def water_needed(weight):
    """Функция расчета воды для синтаксического сахара"""
    water_ml = weight * WATER_PER_KG
    return round(water_ml / MLITER_TO_LITER, 2)


water_l = water_needed(user_weight)

# 4. Вывод красивого результата
print(f"Привет, {user_name}!\nВаш возраст: {user_age}\n\
Ваш индекс массы тела: {bmi}\n\
Ваша норма потребления воды в сутки: {water_l} литров\n")
print("Расчет окончен. Будьте здоровы!")
