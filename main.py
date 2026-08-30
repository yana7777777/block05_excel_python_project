# Практическая ячейка 1. Строки и длина текста
# Данные из датасета: Россия, 2020 год

country = "  Россия  "
continent = "Европа"
year = "2020"

# TODO:
# 1. Выведите country, continent и year
# 2. Создайте переменные country_length и continent_length

country_length = len(country)
continent_length = len(continent)

print("Исходное название страны:", repr(country))
print("Длина строки country:", country_length)
print("Континент:", continent)
print("Длина строки continent:", continent_length)
print("Год:", year)



# Практическая ячейка 2. Индексация и срезы
# Данные из датасета: Россия, Европа, 2020

country = "Россия"
continent = "Европа"
year = "2020"

# TODO:
# 1. Получить первый символ страны
# 2. Получить последний символ страны
# 3. Получить первые 3 буквы континента
# 4. Получить последние 2 цифры года

first_symbol = country[0]
last_symbol = country[-1]
continent_prefix = continent[0:3]
year_part = year[-2:]

print("Первый символ страны:", first_symbol)
print("Последний символ страны:", last_symbol)
print("Первые 3 буквы континента:", continent_prefix)
print("Последние 2 цифры года:", year_part)

