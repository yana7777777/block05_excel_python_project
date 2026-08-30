# Практическая ячейка 1. Сравнения и логические значения
# Данные из датасета: Россия, 2020 год

population = 146000000
birth_rate = 10.5
death_rate = 14.5

# TODO:
# 1. Выведите население, рождаемость и смертность
# 2. Проверьте, больше ли рождаемость смертности
# 3. Проверьте, равна ли рождаемость смертности
# 4. Проверьте, не равна ли смертность нулю
# 5. Проверьте, не больше ли смертность 15

is_birth_more_than_death = birth_rate > death_rate
is_birth_equal_death = birth_rate == death_rate
death_not_zero = death_rate != 0
death_not_more_than_15 = death_rate <= 15

print("Население:", population)
print("Рождаемость:", birth_rate)
print("Смертность:", death_rate)
print("Рождаемость больше смертности?", is_birth_more_than_death)
print("Рождаемость равна смертности?", is_birth_equal_death)
print("Смертность не равна нулю?", death_not_zero)
print("Смертность не больше 15?", death_not_more_than_15)


# Практическая ячейка 2. Простое условие if / else
# Данные из датасета: Россия, 2020 год

birth_rate = 10.5
death_rate = 14.5

# TODO:
# Если рождаемость больше или равна смертности,
# присвойте status значение "Естественный прирост",
# иначе "Естественная убыль"

if birth_rate >= death_rate:
    status = "Естественный прирост"
else:
    status = "Естественная убыль"

print("Рождаемость:", birth_rate)
print("Смертность:", death_rate)
print("Статус:", status)


# Практическая ячейка 3. Несколько веток: if / elif / else
# Данные из датасета: Россия, 2020 год

birth_rate = 10.5
death_rate = 14.5
natural_increase = birth_rate - death_rate

# TODO:
# 1. Если естественный прирост >= 5, статус "Высокий прирост"
# 2. Если естественный прирост >= 0, статус "Положительный прирост"
# 3. Если естественный прирост >= -5, статус "Небольшая убыль"
# 4. Иначе статус "Высокая убыль"

growth_status = ""

if natural_increase >= 5:
    growth_status = "Высокий прирост"
elif natural_increase >= 0:
    growth_status = "Положительный прирост"
elif natural_increase >= -5:
    growth_status = "Небольшая убыль"
else:
    growth_status = "Высокая убыль"

print("Рождаемость:", birth_rate)
print("Смертность:", death_rate)
print("Естественный прирост:", natural_increase)
print("Статус прироста:", growth_status)

# Практическая ячейка 4. Сложные условия: and, or, not
# Данные из датасета: Россия, 2020 год

population = 146000000
birth_rate = 10.5
death_rate = 14.5
is_developing = False
has_crisis = True
is_large_population = population > 100000000

# TODO:
# 1. Создайте переменную demographic_risk
# 2. Демографический риск есть, если:
#    - смертность > 15 И население > 100 млн
#      ИЛИ
#    - есть кризис
# 3. Также выведите, что страна не развивающаяся через not

demographic_risk = False
not_developing = False

if (death_rate > 15 and is_large_population) or has_crisis:
    demographic_risk = True

not_developing = not is_developing

print("Население:", population)
print("Рождаемость:", birth_rate)
print("Смертность:", death_rate)
print("Развивающаяся страна:", is_developing)
print("Кризис:", has_crisis)
print("Демографический риск?", demographic_risk)
print("Страна не развивающаяся?", not_developing)



# Практическая ячейка 5. Мини-задача: обработка демографических данных
# Данные из датасета: Россия, 2020 год

country = "Россия"
population = 146000000
birth_rate = 10.5
death_rate = 14.5
life_expectancy = 73.0
has_healthcare_crisis = False
has_funding = True

# TODO:
# Определите demographic_status по правилам:
# 1. Если смертность > 15 -> "Критический уровень"
# 2. Если смертность > 12 и birth_rate < 11 -> "Неблагоприятная ситуация"
# 3. Если продолжительность жизни > 70 и смертность < 12 -> "Благоприятная ситуация"
# 4. Если есть финансирование и нет кризиса в здравоохранении -> "Стабильная ситуация"
# 5. Иначе -> "Требуется анализ"

demographic_status = ""

print("Страна:", country)
print("Население:", population)
print("Рождаемость:", birth_rate)
print("Смертность:", death_rate)
print("Продолжительность жизни:", life_expectancy)
print("Кризис в здравоохранении:", has_healthcare_crisis)
print("Наличие финансирования:", has_funding)
print("Итоговый статус:", demographic_status)



# Практическая ячейка 6. Тест и самопроверка

# 1. Простое сравнение
population = 146000000
assert population > 100000000

# 2. if / else
death_rate = 14.5
health_status = ""
if death_rate > 15:
    health_status = "Критический"
else:
    health_status = "Нормальный"
assert health_status == "Нормальный"

# 3. if / elif / else
birth_rate = 10.5
demographic_level = ""
if birth_rate > 20:
    demographic_level = "Высокий"
elif birth_rate > 10:
    demographic_level = "Средний"
else:
    demographic_level = "Низкий"
assert demographic_level == "Средний"

# 4. and / or / not
has_crisis = False
has_funding = True
is_stable = False
if not has_crisis and has_funding:
    is_stable = True
assert is_stable is True

# 5. Комплексное правило
life_expectancy = 73.0
death_rate = 14.5
has_healthcare_crisis = False
status = ""
if life_expectancy > 70 and death_rate < 12:
    status = "Благоприятная"
elif not has_healthcare_crisis and death_rate < 15:
    status = "Стабильная"
else:
    status = "Требуется анализ"
assert status == "Стабильная"

print("Тест пройден успешно. Все проверки выполнены.")


# Практическая ячейка 7. Итоговый отчет по уроку 3
# Данные из датасета: Россия, 2020 год

print("=" * 60)
print("ИТОГОВЫЙ ОТЧЕТ ПО УРОКУ 3 - УСЛОВИЯ И ЛОГИКА")
print("=" * 60)

# Исходные данные
country = "Россия"
population = 146000000
birth_rate = 10.5
death_rate = 14.5
life_expectancy = 73.0
has_healthcare_crisis = False
has_funding = True

print("\n1. ИСХОДНЫЕ ДАННЫЕ:")
print(f"   Страна: {country}")
print(f"   Население: {population:,} чел.")
print(f"   Рождаемость: {birth_rate} на 1000 чел.")
print(f"   Смертность: {death_rate} на 1000 чел.")
print(f"   Продолжительность жизни: {life_expectancy} лет")

# Расчет естественного прироста
natural_increase = birth_rate - death_rate
print(f"\n2. ЕСТЕСТВЕННЫЙ ПРИРОСТ:")
print(f"   Естественный прирост: {natural_increase:.1f} на 1000 чел.")

# Определение статуса прироста
if natural_increase >= 5:
    growth_status = "Высокий прирост"
elif natural_increase >= 0:
    growth_status = "Положительный прирост"
elif natural_increase >= -5:
    growth_status = "Небольшая убыль"
else:
    growth_status = "Высокая убыль"
print(f"   Статус прироста: {growth_status}")

# Определение статуса демографической ситуации
print(f"\n3. ДЕМОГРАФИЧЕСКАЯ СИТУАЦИЯ:")

if death_rate > 15:
    demographic_status = "Критический уровень"
elif death_rate > 12 and birth_rate < 11:
    demographic_status = "Неблагоприятная ситуация"
elif life_expectancy > 70 and death_rate < 12:
    demographic_status = "Благоприятная ситуация"
elif has_funding and not has_healthcare_crisis:
    demographic_status = "Стабильная ситуация"
else:
    demographic_status = "Требуется анализ"
print(f"   Статус: {demographic_status}")

# Демографический риск
is_large_population = population > 100000000
demographic_risk = (death_rate > 15 and is_large_population) or has_healthcare_crisis
print(f"\n4. ДЕМОГРАФИЧЕСКИЙ РИСК:")
print(f"   Наличие риска: {'Есть' if demographic_risk else 'Нет'}")

# Сравнение показателей
print(f"\n5. СРАВНЕНИЕ ПОКАЗАТЕЛЕЙ:")
print(f"   Рождаемость больше смертности? {'Да' if birth_rate > death_rate else 'Нет'}")
print(f"   Рождаемость равна смертности? {'Да' if birth_rate == death_rate else 'Нет'}")
print(f"   Смертность не равна нулю? {'Да' if death_rate != 0 else 'Нет'}")
print(f"   Смертность не больше 15? {'Да' if death_rate <= 15 else 'Нет'}")

print("\n" + "=" * 60)
print("ИТОГОВЫЙ ВЫВОД:")
print("=" * 60)
if growth_status == "Высокий прирост" or growth_status == "Положительный прирост":
    print("Демографическая ситуация в стране положительная.")
elif growth_status == "Небольшая убыль":
    print("Демографическая ситуация требует внимания, но критической не является.")
else:
    print("Демографическая ситуация критическая, требуются меры поддержки.")

if demographic_risk:
    print("Имеется демографический риск, требующий мониторинга.")
else:
    print("Демографические риски не выявлены.")

print(f"Общий статус: {demographic_status}")
print("=" * 60)
