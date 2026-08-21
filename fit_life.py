# Проект FitLife - MVP версия 1.0


# 1. Знакомство
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
user_name = input('Как вас зовут?\n')
# TODO: Спроси возраст и сохрани в переменную user_age (не забудь преобразовать в число)
exit_loop = True
while exit_loop:
    try:
        user_age = int(input('Введите ваш возраст:\n'))
        exit_loop = False
    except ValueError, TypeError:
        print('Некорректное значение! Повторите ввод')
# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
exit_loop = True
while exit_loop:
    try:
        user_weight = float(input('Введите ваш вес, кг:\n'))
        exit_loop = False
    except ValueError, TypeError:
        print('Некорректное значение! Повторите ввод')
# TODO: Запроси рост (в метрах, например 1.75) и сохрани в user_height (тип float)
exit_loop = True
while exit_loop:
    try:
        user_height = float(input('Введите ваш рост, в метрах:\n'))
        exit_loop = False
    except ValueError, TypeError:
        print('Некорректное значение! Повторите ввод')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
def bmi_calculation(weight, height):
    bmi = round(weight / (height ** 2), 1)
    return bmi


bmi = bmi_calculation(user_weight, user_height)


# Подсчет воды: вес * 30 мл
# TODO: Рассчитай water_needed
def water_needed(weight):
    water_ml = weight * 30
    water_l = round(water_ml / 1000, 2)
    return water_l


water_l = water_needed(user_weight)

# 4. Вывод красивого результата
# TODO: Используй f-строку, чтобы вывести приветствие, например: "Привет, Иван!"
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f"Привет, {user_name}! Ваш возраст {user_age}, ваш индекс массы тела {bmi}, ваша норма потребления воды в сутки {water_l} литров")
print("Расчет окончен. Будьте здоровы!")