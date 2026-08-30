# Практическая ячейка 1. Цикл for и range()
# Данные из датасета: годы наблюдения с дополнительной информацией

print("=" * 50)
print("ДИНАМИКА ДЕМОГРАФИЧЕСКИХ ПОКАЗАТЕЛЕЙ ПО ГОДАМ")
print("=" * 50)

# Список годов из датасета (2000-2020 с шагом 5)
years = list(range(2000, 2021, 5))
print(f"Годы наблюдения: {years}")

# Создаем словарь с данными для каждого года (в промилле)
data_by_year = {
    2000: {"birth": 11.2, "death": 15.8, "pop": 146300000},
    2005: {"birth": 10.8, "death": 15.2, "pop": 146700000},
    2010: {"birth": 10.2, "death": 14.8, "pop": 147200000},
    2015: {"birth": 9.8, "death": 14.2, "pop": 147800000},
    2020: {"birth": 10.5, "death": 14.5, "pop": 146000000}
}

print("\nДанные по годам:")
print("-" * 50)

for year in years:
    if year in data_by_year:
        data = data_by_year[year]
        natural = data["birth"] - data["death"]
        status = "прирост" if natural > 0 else "убыль"
        print(f"Год {year}: рождаемость {data['birth']}‰, смертность {data['death']}‰, "
              f"естественный {status}: {abs(natural):.1f}‰, население {data['pop']:,} чел.")
    else:
        print(f"Год {year}: данные отсутствуют")

print("\n" + "=" * 50)
print(f"Всего обработано лет: {len(years)}")
print("=" * 50)


# Практическая ячейка 2. Цикл по списку значений
# Расширенный анализ стран с демографическими показателями

print("=" * 60)
print("ДЕМОГРАФИЧЕСКИЙ АНАЛИЗ СТРАН МИРА")
print("=" * 60)

# Расширенный список стран с данными (население, рождаемость, смертность, ВВП)
countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5, "gdp": 32000},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8, "gdp": 18000},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8, "gdp": 65000},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2, "gdp": 7000},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5, "gdp": 15000},
    {"name": "Германия", "continent": "Европа", "pop": 83200000, "birth": 7.8, "death": 11.8, "gdp": 52000},
    {"name": "Япония", "continent": "Азия", "pop": 126500000, "birth": 7.2, "death": 10.5, "gdp": 48000},
    {"name": "Нигерия", "continent": "Африка", "pop": 206000000, "birth": 34.5, "death": 12.8, "gdp": 5000},
    {"name": "Египет", "continent": "Африка", "pop": 100000000, "birth": 16.8, "death": 5.0, "gdp": 12000},
    {"name": "Мексика", "continent": "Америка", "pop": 128000000, "birth": 15.5, "death": 4.8, "gdp": 19000}
]

# Расчет и вывод информации по каждой стране
print("\n{:<15} {:<10} {:<15} {:<10} {:<10} {:<10} {:<10}".format(
    "Страна", "Континент", "Население", "Рождаемость", "Смертность", "Прирост", "ВВП"
))
print("-" * 80)

for country in countries_data:
    natural = country["birth"] - country["death"]
    status = "+" if natural > 0 else ""
    print("{:<15} {:<10} {:<15,} {:<10.1f} {:<10.1f} {:<+10.1f} {:<10,}".format(
        country["name"],
        country["continent"],
        country["pop"],
        country["birth"],
        country["death"],
        natural,
        country["gdp"]
    ))

print("-" * 80)
print(f"Всего проанализировано стран: {len(countries_data)}")

# Практическая ячейка 3. Накопление суммы
# Расширенный расчет статистических показателей

print("=" * 60)
print("СТАТИСТИКА НАСЕЛЕНИЯ СТРАН")
print("=" * 60)

# Данные из датасета (население стран)
population = [146000000, 1411000000, 331000000, 1380000000, 212000000, 83200000, 126500000, 206000000, 100000000, 128000000]
countries = ["Россия", "Китай", "США", "Индия", "Бразилия", "Германия", "Япония", "Нигерия", "Египет", "Мексика"]

# Инициализация накопителей
total_population = 0
max_population = 0
min_population = float('inf')
max_country = ""
min_country = ""
sum_squared = 0  # для расчета дисперсии

print("\nПошаговое накопление суммы:")
print("-" * 40)

for i, pop in enumerate(population):
    total_population += pop
    sum_squared += pop ** 2
    print(f"Шаг {i+1}: {countries[i]} + {pop:,} = {total_population:,}")

    # Поиск максимума и минимума
    if pop > max_population:
        max_population = pop
        max_country = countries[i]
    if pop < min_population:
        min_population = pop
        min_country = countries[i]

# Расчет среднего
average_population = total_population / len(population)

# Расчет дисперсии и стандартного отклонения
mean = average_population
variance = (sum_squared / len(population)) - (mean ** 2)
std_dev = variance ** 0.5

print("\n" + "=" * 60)
print("РЕЗУЛЬТАТЫ РАСЧЕТОВ:")
print("=" * 60)
print(f"Общая численность населения: {total_population:,} чел.")
print(f"Количество стран: {len(population)}")
print(f"Среднее население: {average_population:,.2f} чел.")
print(f"Максимальное население: {max_population:,} чел. ({max_country})")
print(f"Минимальное население: {min_population:,} чел. ({min_country})")
print(f"Дисперсия: {variance:,.2f}")
print(f"Стандартное отклонение: {std_dev:,.2f}")
print(f"Размах: {max_population - min_population:,} чел.")


# Практическая ячейка 4. Подсчет количества элементов по условию
# Расширенный анализ с категориями стран

print("=" * 60)
print("КЛАССИФИКАЦИЯ СТРАН ПО РОЖДАЕМОСТИ И СМЕРТНОСТИ")
print("=" * 60)

countries_data = [
    {"name": "Россия", "birth": 10.5, "death": 14.5, "pop": 146000000},
    {"name": "Китай", "birth": 8.5, "death": 5.8, "pop": 1411000000},
    {"name": "США", "birth": 11.5, "death": 9.8, "pop": 331000000},
    {"name": "Индия", "birth": 18.5, "death": 7.2, "pop": 1380000000},
    {"name": "Бразилия", "birth": 14.5, "death": 5.5, "pop": 212000000},
    {"name": "Германия", "birth": 7.8, "death": 11.8, "pop": 83200000},
    {"name": "Япония", "birth": 7.2, "death": 10.5, "pop": 126500000},
    {"name": "Нигерия", "birth": 34.5, "death": 12.8, "pop": 206000000},
    {"name": "Египет", "birth": 16.8, "death": 5.0, "pop": 100000000},
    {"name": "Мексика", "birth": 15.5, "death": 4.8, "pop": 128000000}
]

# Пороги для классификации
birth_threshold_high = 15.0
birth_threshold_low = 10.0
death_threshold_high = 10.0

# Инициализация счетчиков
high_birth = []
medium_birth = []
low_birth = []
high_death = []
natural_growth = []
natural_decline = []

for country in countries_data:
    # Классификация по рождаемости
    if country["birth"] > birth_threshold_high:
        high_birth.append(country["name"])
    elif country["birth"] > birth_threshold_low:
        medium_birth.append(country["name"])
    else:
        low_birth.append(country["name"])

    # Классификация по смертности
    if country["death"] > death_threshold_high:
        high_death.append(country["name"])

    # Естественный прирост/убыль
    if country["birth"] > country["death"]:
        natural_growth.append(country["name"])
    else:
        natural_decline.append(country["name"])

print("\nКЛАССИФИКАЦИЯ ПО РОЖДАЕМОСТИ:")
print("-" * 40)
print(f"Высокая (> {birth_threshold_high}‰): {len(high_birth)} стран - {', '.join(high_birth)}")
print(f"Средняя ({birth_threshold_low}-{birth_threshold_high}‰): {len(medium_birth)} стран - {', '.join(medium_birth)}")
print(f"Низкая (< {birth_threshold_low}‰): {len(low_birth)} стран - {', '.join(low_birth)}")

print("\nКЛАССИФИКАЦИЯ ПО СМЕРТНОСТИ:")
print("-" * 40)
print(f"Высокая (> {death_threshold_high}‰): {len(high_death)} стран - {', '.join(high_death)}")

print("\nЕСТЕСТВЕННЫЙ ПРИРОСТ:")
print("-" * 40)
print(f"Положительный: {len(natural_growth)} стран - {', '.join(natural_growth)}")
print(f"Отрицательный (убыль): {len(natural_decline)} стран - {', '.join(natural_decline)}")



# Практическая ячейка 5. Мини-задача: анализ списка стран с расширенной статистикой
# Полный демографический анализ

print("=" * 70)
print("КОМПЛЕКСНЫЙ ДЕМОГРАФИЧЕСКИЙ АНАЛИЗ СТРАН")
print("=" * 70)

countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5, "gdp": 32000},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8, "gdp": 18000},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8, "gdp": 65000},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2, "gdp": 7000},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5, "gdp": 15000},
    {"name": "Германия", "continent": "Европа", "pop": 83200000, "birth": 7.8, "death": 11.8, "gdp": 52000},
    {"name": "Япония", "continent": "Азия", "pop": 126500000, "birth": 7.2, "death": 10.5, "gdp": 48000},
    {"name": "Нигерия", "continent": "Африка", "pop": 206000000, "birth": 34.5, "death": 12.8, "gdp": 5000},
    {"name": "Египет", "continent": "Африка", "pop": 100000000, "birth": 16.8, "death": 5.0, "gdp": 12000},
    {"name": "Мексика", "continent": "Америка", "pop": 128000000, "birth": 15.5, "death": 4.8, "gdp": 19000}
]

# Инициализация накопителей
total_pop = 0
total_birth = 0
total_death = 0
total_gdp = 0
countries_count = 0
high_birth_count = 0
high_death_count = 0
growth_count = 0
decline_count = 0

# Списки для детального анализа
high_birth_list = []
high_death_list = []
growth_list = []
decline_list = []
gdp_high_list = []
gdp_low_list = []

# Пороги
birth_threshold = 15.0
death_threshold = 10.0
gdp_threshold = 20000

print("\nОБРАБОТКА ДАННЫХ ПО СТРАНАМ:")
print("-" * 70)

for country in countries_data:
    # Накопление сумм
    total_pop += country["pop"]
    total_birth += country["birth"]
    total_death += country["death"]
    total_gdp += country["gdp"]
    countries_count += 1

    # Естественный прирост
    natural = country["birth"] - country["death"]

    # Проверка условий
    if country["birth"] > birth_threshold:
        high_birth_count += 1
        high_birth_list.append(country["name"])
    if country["death"] > death_threshold:
        high_death_count += 1
        high_death_list.append(country["name"])
    if natural > 0:
        growth_count += 1
        growth_list.append(country["name"])
    else:
        decline_count += 1
        decline_list.append(country["name"])
    if country["gdp"] > gdp_threshold:
        gdp_high_list.append(country["name"])
    else:
        gdp_low_list.append(country["name"])

    # Вывод текущей обработки (каждый 2-й)
    if countries_count % 2 == 0:
        print(f"Обработано {countries_count} стран...")

# Расчет средних значений
avg_pop = total_pop / countries_count
avg_birth = total_birth / countries_count
avg_death = total_death / countries_count
avg_gdp = total_gdp / countries_count

print("\n" + "=" * 70)
print("ИТОГОВАЯ СТАТИСТИКА:")
print("=" * 70)

print(f"\n1. ОБЩИЕ ПОКАЗАТЕЛИ:")
print(f"   Всего стран: {countries_count}")
print(f"   Общее население: {total_pop:,} чел.")
print(f"   Среднее население: {avg_pop:,.2f} чел.")
print(f"   Средняя рождаемость: {avg_birth:.2f}‰")
print(f"   Средняя смертность: {avg_death:.2f}‰")
print(f"   Средний ВВП: ${avg_gdp:,.2f}")

print(f"\n2. АНАЛИЗ ПО УСЛОВИЯМ:")
print(f"   Стран с рождаемостью > {birth_threshold}‰: {high_birth_count} ({', '.join(high_birth_list)})")
print(f"   Стран со смертностью > {death_threshold}‰: {high_death_count} ({', '.join(high_death_list)})")
print(f"   Стран с естественным приростом: {growth_count} ({', '.join(growth_list)})")
print(f"   Стран с естественной убылью: {decline_count} ({', '.join(decline_list)})")
print(f"   Стран с высоким ВВП (> ${gdp_threshold}): {len(gdp_high_list)} ({', '.join(gdp_high_list)})")
print(f"   Стран с низким ВВП (< ${gdp_threshold}): {len(gdp_low_list)} ({', '.join(gdp_low_list)})")

print(f"\n3. ВЫВОДЫ:")
if growth_count > decline_count:
    print(f"   ✅ В большинстве стран ({growth_count}) наблюдается естественный прирост.")
else:
    print(f"   ⚠️ В большинстве стран ({decline_count}) наблюдается естественная убыль.")
if high_birth_count > high_death_count:
    print(f"   📈 Высокая рождаемость ({high_birth_count} стран) преобладает над высокой смертностью ({high_death_count} стран).")
else:
    print(f"   📉 Высокая смертность ({high_death_count} стран) преобладает над высокой рождаемостью ({high_birth_count} стран).")
if len(gdp_high_list) > len(gdp_low_list):
    print(f"   💰 Большинство стран ({len(gdp_high_list)}) имеют высокий ВВП.")
else:
    print(f"   💰 Большинство стран ({len(gdp_low_list)}) имеют низкий ВВП.")

print("\n" + "=" * 70)




# Практическая ячейка 6. Тест и самопроверка

print("=" * 60)
print("ЗАПУСК ТЕСТОВ ПО УРОКУ 4")
print("=" * 60)

# 1. range() с шагом
years = []
for y in range(2000, 2021, 5):
    years.append(y)
assert years == [2000, 2005, 2010, 2015, 2020]
print("✅ Тест 1 пройден: range() работает корректно")

# 2. Перебор списка и сумма (ВСЕ 10 СТРАН ИЗ ВАШЕГО ДАТАСЕТА)
population = [146000000, 1411000000, 331000000, 1380000000, 212000000, 206000000, 83200000, 126500000, 128000000, 100000000]
total = 0
for pop in population:
    total += pop
# Сумма всех 10 стран: 146000000 + 1411000000 + 331000000 + 1380000000 + 212000000 + 206000000 + 83200000 + 126500000 + 128000000 + 100000000 = 4123700000
assert total == 4123700000
print("✅ Тест 2 пройден: сумма населения рассчитана верно")

# 3. Подсчёт элементов по условию (рождаемость)
birth_rates = [10.5, 8.5, 11.5, 18.5, 14.5, 34.5, 7.8, 7.2, 15.5, 16.8]
count_high = 0
for rate in birth_rates:
    if rate > 12.0:
        count_high += 1
assert count_high == 5
print("✅ Тест 3 пройден: подсчет по условию работает")

# 4. Подсчёт элементов по условию (смертность)
death_rates = [14.5, 5.8, 9.8, 7.2, 5.5, 12.8, 11.8, 10.5, 4.8, 5.0]
count_high_death = 0
for rate in death_rates:
    if rate > 10.0:
        count_high_death += 1
assert count_high_death == 4
print("✅ Тест 4 пройден: подсчет смертности работает")

# 5. Мини-проверка среднего
population_avg = [146000000, 1411000000, 331000000, 1380000000, 212000000]
total_population_avg = 0
countries_count_avg = 0
for pop in population_avg:
    total_population_avg += pop
    countries_count_avg += 1
average_population = total_population_avg / countries_count_avg
assert average_population == 696000000.0
print("✅ Тест 5 пройден: среднее рассчитано верно")

print("\n" + "=" * 60)
print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО! Все проверки выполнены.")
print("=" * 60)



# Практическая ячейка 7. Итоговый отчет по уроку 4
# Полный демографический анализ с визуализацией данных

print("=" * 80)
print(" " * 25 + "ИТОГОВЫЙ ОТЧЕТ")
print(" " * 20 + "ПО УРОКУ 4: ЦИКЛЫ И ПОВТОРЯЮЩИЕСЯ РАСЧЕТЫ")
print("=" * 80)

# Данные (10 стран)
countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5, "gdp": 32000},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8, "gdp": 18000},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8, "gdp": 65000},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2, "gdp": 7000},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5, "gdp": 15000},
    {"name": "Нигерия", "continent": "Африка", "pop": 206000000, "birth": 34.5, "death": 12.8, "gdp": 5000},
    {"name": "Германия", "continent": "Европа", "pop": 83200000, "birth": 7.8, "death": 11.8, "gdp": 52000},
    {"name": "Япония", "continent": "Азия", "pop": 126500000, "birth": 7.2, "death": 10.5, "gdp": 48000},
    {"name": "Мексика", "continent": "Америка", "pop": 128000000, "birth": 15.5, "death": 4.8, "gdp": 19000},
    {"name": "Египет", "continent": "Африка", "pop": 100000000, "birth": 16.8, "death": 5.0, "gdp": 12000}
]

# ============================================
# 1. РАСЧЕТ СТАТИСТИК
# ============================================

print("\n" + "█" * 80)
print(" 1. СТАТИСТИЧЕСКИЙ АНАЛИЗ")
print("█" * 80)

total_pop = 0
total_birth = 0
total_death = 0
total_gdp = 0
country_count = 0

max_pop = 0
min_pop = float('inf')
max_pop_country = ""
min_pop_country = ""

max_birth = 0
min_birth = float('inf')
max_birth_country = ""
min_birth_country = ""

max_death = 0
min_death = float('inf')
max_death_country = ""
min_death_country = ""

for country in countries_data:
    total_pop += country["pop"]
    total_birth += country["birth"]
    total_death += country["death"]
    total_gdp += country["gdp"]
    country_count += 1

    if country["pop"] > max_pop:
        max_pop = country["pop"]
        max_pop_country = country["name"]
    if country["pop"] < min_pop:
        min_pop = country["pop"]
        min_pop_country = country["name"]

    if country["birth"] > max_birth:
        max_birth = country["birth"]
        max_birth_country = country["name"]
    if country["birth"] < min_birth:
        min_birth = country["birth"]
        min_birth_country = country["name"]

    if country["death"] > max_death:
        max_death = country["death"]
        max_death_country = country["name"]
    if country["death"] < min_death:
        min_death = country["death"]
        min_death_country = country["name"]

avg_pop = total_pop / country_count
avg_birth = total_birth / country_count
avg_death = total_death / country_count
avg_gdp = total_gdp / country_count

print(f"\n📊 ОБЩИЕ ПОКАЗАТЕЛИ:")
print(f"   Всего стран: {country_count}")
print(f"   Общее население: {total_pop:>15,} чел.")
print(f"   Среднее население: {avg_pop:>15,.2f} чел.")
print(f"   Максимальное население: {max_pop:>15,} чел. ({max_pop_country})")
print(f"   Минимальное население: {min_pop:>15,} чел. ({min_pop_country})")

print(f"\n📈 РОЖДАЕМОСТЬ:")
print(f"   Средняя рождаемость: {avg_birth:>15.2f}‰")
print(f"   Максимальная рождаемость: {max_birth:>15.1f}‰ ({max_birth_country})")
print(f"   Минимальная рождаемость: {min_birth:>15.1f}‰ ({min_birth_country})")

print(f"\n📉 СМЕРТНОСТЬ:")
print(f"   Средняя смертность: {avg_death:>15.2f}‰")
print(f"   Максимальная смертность: {max_death:>15.1f}‰ ({max_death_country})")
print(f"   Минимальная смертность: {min_death:>15.1f}‰ ({min_death_country})")

print(f"\n💰 ЭКОНОМИКА:")
print(f"   Средний ВВП: ${avg_gdp:>14,.2f}")

# ============================================
# 2. ДЕТАЛЬНЫЙ АНАЛИЗ ПО СТРАНАМ
# ============================================

print("\n" + "█" * 80)
print(" 2. ДЕТАЛЬНЫЙ АНАЛИЗ ПО СТРАНАМ")
print("█" * 80)

print("\n{:<15} {:<12} {:<15} {:<10} {:<10} {:<12} {:<12}".format(
    "Страна", "Континент", "Население", "Рожд.", "Смерт.", "Прирост", "ВВП"
))
print("-" * 85)

for country in countries_data:
    natural = country["birth"] - country["death"]
    status = "📈" if natural > 0 else "📉"
    print("{:<15} {:<12} {:<15,} {:<10.1f} {:<10.1f} {:<12.1f} {:<12,}".format(
        country["name"],
        country["continent"],
        country["pop"],
        country["birth"],
        country["death"],
        natural,
        country["gdp"]
    ))

# ============================================
# 3. КЛАССИФИКАЦИЯ СТРАН
# ============================================

print("\n" + "█" * 80)
print(" 3. КЛАССИФИКАЦИЯ СТРАН")
print("█" * 80)

# По рождаемости
high_birth = []
medium_birth = []
low_birth = []
for country in countries_data:
    if country["birth"] > 15.0:
        high_birth.append(country["name"])
    elif country["birth"] > 10.0:
        medium_birth.append(country["name"])
    else:
        low_birth.append(country["name"])

print(f"\n👶 РОЖДАЕМОСТЬ:")
print(f"   Высокая (>15‰): {len(high_birth)} стран → {', '.join(high_birth)}")
print(f"   Средняя (10-15‰): {len(medium_birth)} стран → {', '.join(medium_birth)}")
print(f"   Низкая (<10‰): {len(low_birth)} стран → {', '.join(low_birth)}")

# По смертности
high_death = []
medium_death = []
low_death = []
for country in countries_data:
    if country["death"] > 10.0:
        high_death.append(country["name"])
    elif country["death"] > 7.0:
        medium_death.append(country["name"])
    else:
        low_death.append(country["name"])

print(f"\n💀 СМЕРТНОСТЬ:")
print(f"   Высокая (>10‰): {len(high_death)} стран → {', '.join(high_death)}")
print(f"   Средняя (7-10‰): {len(medium_death)} стран → {', '.join(medium_death)}")
print(f"   Низкая (<7‰): {len(low_death)} стран → {', '.join(low_death)}")

# По ВВП
high_gdp = []
medium_gdp = []
low_gdp = []
for country in countries_data:
    if country["gdp"] > 30000:
        high_gdp.append(country["name"])
    elif country["gdp"] > 15000:
        medium_gdp.append(country["name"])
    else:
        low_gdp.append(country["name"])

print(f"\n💵 ВВП:")
print(f"   Высокий (>$30000): {len(high_gdp)} стран → {', '.join(high_gdp)}")
print(f"   Средний ($15000-$30000): {len(medium_gdp)} стран → {', '.join(medium_gdp)}")
print(f"   Низкий (<$15000): {len(low_gdp)} стран → {', '.join(low_gdp)}")

# ============================================
# 4. ЕСТЕСТВЕННЫЙ ПРИРОСТ
# ============================================

print("\n" + "█" * 80)
print(" 4. ЕСТЕСТВЕННЫЙ ПРИРОСТ НАСЕЛЕНИЯ")
print("█" * 80)

growth = []
decline = []
for country in countries_data:
    natural = country["birth"] - country["death"]
    if natural > 0:
        growth.append((country["name"], natural))
    else:
        decline.append((country["name"], abs(natural)))

print(f"\n✅ Страны с естественным приростом ({len(growth)}):")
if growth:
    for name, val in growth:
        print(f"   {name}: +{val:.1f}‰")
else:
    print("   Нет стран с естественным приростом")

print(f"\n❌ Страны с естественной убылью ({len(decline)}):")
if decline:
    for name, val in decline:
        print(f"   {name}: -{val:.1f}‰")
else:
    print("   Нет стран с естественной убылью")

# ============================================
# 5. ДЕМОГРАФИЧЕСКИЙ РИСК
# ============================================

print("\n" + "█" * 80)
print(" 5. АНАЛИЗ ДЕМОГРАФИЧЕСКОГО РИСКА")
print("█" * 80)

risk_countries = []
stable_countries = []
for country in countries_data:
    natural = country["birth"] - country["death"]
    if natural < 0:
        risk_countries.append(country["name"])
    elif country["birth"] > 25.0 and country["death"] > 10.0:
        risk_countries.append(country["name"])
    else:
        stable_countries.append(country["name"])

print(f"\n⚠️ Страны с демографическим риском ({len(risk_countries)}):")
if risk_countries:
    for name in risk_countries:
        print(f"   {name}")
else:
    print("   Нет")

print(f"\n✅ Стабильные страны ({len(stable_countries)}):")
if stable_countries:
    for name in stable_countries:
        print(f"   {name}")
else:
    print("   Нет")

# ============================================
# 6. ВЫВОДЫ И РЕКОМЕНДАЦИИ
# ============================================

print("\n" + "█" * 80)
print(" 6. ВЫВОДЫ И РЕКОМЕНДАЦИИ")
print("█" * 80)

print("\n📌 ОСНОВНЫЕ ВЫВОДЫ:")

if len(growth) > len(decline):
    print(f"   ✅ В {len(growth)} странах наблюдается естественный прирост населения.")
    print(f"      Демографическая ситуация в целом благоприятная.")
else:
    print(f"   ⚠️ В {len(decline)} странах наблюдается естественная убыль населения.")
    print(f"      Требуется проведение демографической политики.")

if len(high_birth) > len(low_birth):
    print(f"   📈 Высокая рождаемость ({len(high_birth)} стран) преобладает над низкой ({len(low_birth)}).")
else:
    print(f"   📉 Низкая рождаемость ({len(low_birth)} стран) преобладает над высокой ({len(high_birth)}).")

if len(high_gdp) > len(low_gdp):
    print(f"   💰 В {len(high_gdp)} странах высокий уровень ВВП.")
else:
    print(f"   💰 В {len(low_gdp)} странах низкий уровень ВВП.")

print("\n📌 РЕКОМЕНДАЦИИ:")

if len(risk_countries) > 0:
    print(f"   - Обратить внимание на страны с демографическим риском:")
    for name in risk_countries:
        print(f"     * {name}")

if len(decline) > 0:
    print(f"   - Разработать меры поддержки рождаемости в странах с убылью:")
    for name, val in decline:
        print(f"     * {name} (убыль {val:.1f}‰)")

if len(low_gdp) > 0:
    print(f"   - Стимулировать экономический рост в странах с низким ВВП:")
    for name in low_gdp:
        print(f"     * {name}")

# ============================================
# 7. ИТОГОВАЯ СТАТИСТИКА
# ============================================

print("\n" + "█" * 80)
print(" 7. ИТОГОВАЯ СТАТИСТИКА")
print("█" * 80)

print(f"""
┌─────────────────────────────────────────────────────────────────────────────┐
│                        СВОДНАЯ СТАТИСТИКА                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│  Всего стран                     {country_count:>10}                                    │
│  Общее население                 {total_pop:>15,} чел.                     │
│  Среднее население               {avg_pop:>15,.2f} чел.                   │
│  Средняя рождаемость             {avg_birth:>15.2f}‰                      │
│  Средняя смертность              {avg_death:>15.2f}‰                      │
│  Средний ВВП                     ${avg_gdp:>14,.2f}                       │
│  Стран с приростом               {len(growth):>10}                                   │
│  Стран с убылью                  {len(decline):>10}                                   │
│  Стран с демографическим риском  {len(risk_countries):>10}                           │
└─────────────────────────────────────────────────────────────────────────────┘
""")

print("=" * 80)
print(" " * 30 + "✅ ОТЧЕТ СФОРМИРОВАН")
print(" " * 25 + "ДАННЫЕ ГОТОВЫ К АНАЛИЗУ")
print("=" * 80)