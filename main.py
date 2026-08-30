# Практическая ячейка 1. Список и доступ по индексу
# Данные из датасета: список стран

countries = ["Россия", "Китай", "США", "Индия", "Бразилия", "Германия", "Япония", "Нигерия", "Мексика", "Египет"]

print("=" * 50)
print("СПИСОК СТРАН ДЛЯ АНАЛИЗА")
print("=" * 50)

print("\nСписок стран:", countries)
print("Первая страна в списке:", countries[0])
print("Последняя страна в списке:", countries[-1])
print("Третья страна в списке:", countries[2])
print("Предпоследняя страна в списке:", countries[-2])
print("Количество стран в списке:", len(countries))

# Дополнительно: срез списка (первые 5 стран)
print("\nПервые 5 стран:", countries[:5])
# Срез списка (последние 3 страны)
print("Последние 3 страны:", countries[-3:])


# Практическая ячейка 2. Изменение списка и добавление элементов
# Данные из датасета: список стран

countries = ["Россия", "Китай", "США", "Индия", "Бразилия", "Германия", "Япония", "Нигерия", "Мексика", "Египет"]

print("=" * 50)
print("ИЗМЕНЕНИЕ СПИСКА СТРАН")
print("=" * 50)

print("\nИсходный список стран:", countries)

# Изменяем элемент по индексу
countries[1] = "Китай (КНР)"          # меняем "Китай" на "Китай (КНР)"
countries[4] = "Бразилия (ФР)"        # меняем "Бразилия" на "Бразилия (ФР)"
countries[-1] = "Египет (АРЕ)"        # меняем "Египет" на "Египет (АРЕ)"

print("\nПосле изменения элементов:", countries)

# Добавляем элементы в конец списка
countries.append("Аргентина")
countries.append("Таиланд")
countries.append("Чили")

print("После добавления новых стран:", countries)

# Вставляем элемент на конкретную позицию
countries.insert(2, "Великобритания")
print("После вставки на позицию 2:", countries)

# Удаляем элемент по индексу
removed_country = countries.pop(5)
print(f"Удалённая страна (позиция 5): {removed_country}")
print("После удаления:", countries)

# Удаляем элемент по значению
countries.remove("Германия")
print("После удаления 'Германия':", countries)

print(f"\nИтоговое количество стран: {len(countries)}")
print("Итоговый список стран:", countries)

# Практическая ячейка 3. Словарь и работа с ключами
# Данные из датасета: информация о стране

country_info = {
    "name": "Россия",
    "continent": "Европа",
    "population": 146000000,
    "birth_rate": 10.5,
    "death_rate": 14.5,
    "gdp": 32000,
    "capital": "Москва"
}

print("=" * 50)
print("СЛОВАРЬ СТРАНЫ")
print("=" * 50)

print("\nСловарь country_info:", country_info)
print("Название страны:", country_info["name"])
print("Континент:", country_info["continent"])
print("Население:", country_info["population"])
print("Рождаемость:", country_info["birth_rate"])
print("Смертность:", country_info["death_rate"])
print("Столица:", country_info["capital"])

# Получаем список ключей и значений
print("\nКлючи словаря:", list(country_info.keys()))
print("Значения словаря:", list(country_info.values()))

# Добавляем новый ключ
country_info["currency"] = "Рубль"
print("\nПосле добавления валюты:", country_info)

# Изменяем значение
country_info["population"] = 146500000
print("После изменения населения:", country_info)

# Проверка наличия ключа
if "gdp" in country_info:
    print(f"ВВП страны: {country_info['gdp']} USD")
else:
    print("Ключ 'gdp' отсутствует")

# Получение значения с дефолтным (если ключа нет)
unemployment = country_info.get("unemployment", "Нет данных")
print(f"Безработица: {unemployment}")


# Практическая ячейка 4. Список словарей как мини-таблица
# Данные из датасета: список стран с показателями

countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5},
]

print("=" * 50)
print("ТАБЛИЦА СТРАН (СПИСОК СЛОВАРЕЙ)")
print("=" * 50)

print("\n{:<15} {:<12} {:<15} {:<12} {:<12}".format(
    "Страна", "Континент", "Население", "Рождаемость", "Смертность"
))
print("-" * 65)

for row in countries_data:
    natural = row["birth"] - row["death"]
    print("{:<15} {:<12} {:<15,} {:<12.1f} {:<12.1f}".format(
        row["name"],
        row["continent"],
        row["pop"],
        row["birth"],
        row["death"]
    ))

print("\n" + "=" * 50)
print("ДОПОЛНИТЕЛЬНЫЙ АНАЛИЗ")
print("=" * 50)

total_pop = 0
total_birth = 0
total_death = 0
count = 0

for row in countries_data:
    total_pop += row["pop"]
    total_birth += row["birth"]
    total_death += row["death"]
    count += 1

print(f"Всего стран: {count}")
print(f"Общее население: {total_pop:,} чел.")
print(f"Средняя рождаемость: {total_birth/count:.2f}‰")
print(f"Средняя смертность: {total_death/count:.2f}‰")


# Практическая ячейка 5. Мини-задача: анализ стран
# Данные из датасета: список стран с показателями

countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5},
    {"name": "Германия", "continent": "Европа", "pop": 83200000, "birth": 7.8, "death": 11.8},
    {"name": "Япония", "continent": "Азия", "pop": 126500000, "birth": 7.2, "death": 10.5},
    {"name": "Нигерия", "continent": "Африка", "pop": 206000000, "birth": 34.5, "death": 12.8},
]

print("=" * 60)
print("ДЕМОГРАФИЧЕСКИЙ АНАЛИЗ СТРАН")
print("=" * 60)

print("\n{:<15} {:<12} {:<15} {:<10} {:<10} {:<12}".format(
    "Страна", "Континент", "Население", "Рожд.", "Смерт.", "Прирост"
))
print("-" * 75)

total_pop = 0
total_birth = 0
total_death = 0
countries_count = 0
high_birth_count = 0
high_death_count = 0

for row in countries_data:
    natural = row["birth"] - row["death"]
    status = "📈" if natural > 0 else "📉"

    total_pop += row["pop"]
    total_birth += row["birth"]
    total_death += row["death"]
    countries_count += 1

    if row["birth"] > 15.0:
        high_birth_count += 1
    if row["death"] > 10.0:
        high_death_count += 1

    print("{:<15} {:<12} {:<15,} {:<10.1f} {:<10.1f} {:<12.1f} {}".format(
        row["name"],
        row["continent"],
        row["pop"],
        row["birth"],
        row["death"],
        natural,
        status
    ))

print("-" * 75)

avg_pop = total_pop / countries_count
avg_birth = total_birth / countries_count
avg_death = total_death / countries_count

print("\n" + "=" * 60)
print("ИТОГОВАЯ СТАТИСТИКА")
print("=" * 60)

print(f"Количество стран: {countries_count}")
print(f"Общее население: {total_pop:,} чел.")
print(f"Среднее население: {avg_pop:,.2f} чел.")
print(f"Средняя рождаемость: {avg_birth:.2f}‰")
print(f"Средняя смертность: {avg_death:.2f}‰")
print(f"Стран с высокой рождаемостью (>15‰): {high_birth_count}")
print(f"Стран с высокой смертностью (>10‰): {high_death_count}")


# Практическая ячейка 6. Тест и самопроверка
# Данные из датасета

print("=" * 50)
print("ЗАПУСК ТЕСТОВ")
print("=" * 50)

# 1. Список и индексы
countries = ["Россия", "Китай", "США", "Индия", "Бразилия"]
assert countries[0] == "Россия"
assert countries[-1] == "Бразилия"
assert len(countries) == 5
print("✅ Тест 1 пройден: список и индексы")

# 2. Изменение списка
countries[1] = "Китай (КНР)"
countries.append("Германия")
assert countries == ["Россия", "Китай (КНР)", "США", "Индия", "Бразилия", "Германия"]
print("✅ Тест 2 пройден: изменение списка")

# 3. Словарь
country_info = {"name": "Россия", "continent": "Европа", "population": 146000000}
assert country_info["name"] == "Россия"
assert country_info["continent"] == "Европа"
assert country_info["population"] == 146000000
print("✅ Тест 3 пройден: словарь")

# 4. Список словарей
countries_data = [
    {"pop": 146000000, "birth": 10.5},
    {"pop": 1411000000, "birth": 8.5},
    {"pop": 331000000, "birth": 11.5},
]

total_pop = 0
total_birth = 0
for row in countries_data:
    total_pop += row["pop"]
    total_birth += row["birth"]

assert total_pop == 1888000000
assert total_birth == 30.5
print("✅ Тест 4 пройден: список словарей")

# 5. Расчёт суммы
countries_data = [
    {"pop": 146000000, "birth": 10.5},
    {"pop": 1411000000, "birth": 8.5},
]

total_pop = 0
for row in countries_data:
    total_pop += row["pop"]

assert total_pop == 1557000000
print("✅ Тест 5 пройден: расчёт суммы")

print("\n" + "=" * 50)
print("✅ ТЕСТ ПРОЙДЕН УСПЕШНО! Все проверки выполнены.")
print("=" * 50)


# Практическая ячейка 7. Итоговый отчет по уроку 5 (исправленный)

countries_data = [
    {"name": "Россия", "continent": "Европа", "pop": 146000000, "birth": 10.5, "death": 14.5, "gdp": 32000, "area": 17125191, "density": 8.5},
    {"name": "Китай", "continent": "Азия", "pop": 1411000000, "birth": 8.5, "death": 5.8, "gdp": 18000, "area": 9596961, "density": 147.0},
    {"name": "США", "continent": "Америка", "pop": 331000000, "birth": 11.5, "death": 9.8, "gdp": 65000, "area": 9833517, "density": 33.7},
    {"name": "Индия", "continent": "Азия", "pop": 1380000000, "birth": 18.5, "death": 7.2, "gdp": 7000, "area": 3287263, "density": 419.8},
    {"name": "Бразилия", "continent": "Америка", "pop": 212000000, "birth": 14.5, "death": 5.5, "gdp": 15000, "area": 8515767, "density": 24.9},
    {"name": "Германия", "continent": "Европа", "pop": 83200000, "birth": 7.8, "death": 11.8, "gdp": 52000, "area": 357022, "density": 233.0},
    {"name": "Япония", "continent": "Азия", "pop": 126500000, "birth": 7.2, "death": 10.5, "gdp": 48000, "area": 377975, "density": 334.7},
    {"name": "Нигерия", "continent": "Африка", "pop": 206000000, "birth": 34.5, "death": 12.8, "gdp": 5000, "area": 923768, "density": 223.0},
    {"name": "Мексика", "continent": "Америка", "pop": 128000000, "birth": 15.5, "death": 4.8, "gdp": 19000, "area": 1964375, "density": 65.2},
    {"name": "Египет", "continent": "Африка", "pop": 100000000, "birth": 16.8, "death": 5.0, "gdp": 12000, "area": 1002450, "density": 99.8},
]

print("=" * 85)
print(" " * 25 + "ИТОГОВЫЙ ОТЧЕТ ПО УРОКУ 5")
print(" " * 18 + "СПИСКИ, СЛОВАРИ И ТАБЛИЧНОЕ МЫШЛЕНИЕ")
print("=" * 85)

print("\n" + "█" * 85)
print(" 1. ОБЩАЯ ИНФОРМАЦИЯ О ДАННЫХ")
print("█" * 85)

print(f"\n📊 В таблице представлены данные по {len(countries_data)} странам мира.")
print("📋 Колонки данных:")
print("   - name: название страны")
print("   - continent: континент")
print("   - pop: численность населения (человек)")
print("   - birth: рождаемость (на 1000 человек)")
print("   - death: смертность (на 1000 человек)")
print("   - gdp: ВВП на душу населения (USD)")
print("   - area: площадь территории (кв.км)")
print("   - density: плотность населения (чел/кв.км)")

print("\n" + "█" * 85)
print(" 2. ДЕТАЛЬНАЯ ТАБЛИЦА ПО СТРАНАМ")
print("█" * 85)

print("\n{:<15} {:<12} {:<15} {:<10} {:<10} {:<12} {:<8} {:<12}".format(
    "Страна", "Континент", "Население", "Рожд.", "Смерт.", "Прирост", "ВВП", "Плотность"
))
print("-" * 100)

total_pop = 0
total_birth = 0
total_death = 0
total_gdp = 0
total_area = 0
total_density = 0
country_count = 0
growth_count = 0
decline_count = 0
gdp_high = 0
gdp_low = 0
asia_count = 0
europe_count = 0
america_count = 0
africa_count = 0

birth_rates = []
death_rates = []
gdp_rates = []
density_rates = []

growth_list = []
decline_list = []
high_birth = []
low_birth = []
high_death = []
low_death = []
high_gdp = []
low_gdp = []
dense_countries = []
sparse_countries = []

for row in countries_data:
    natural = row["birth"] - row["death"]
    status = "📈" if natural > 0 else "📉"

    total_pop += row["pop"]
    total_birth += row["birth"]
    total_death += row["death"]
    total_gdp += row["gdp"]
    total_area += row["area"]
    total_density += row["density"]
    country_count += 1

    birth_rates.append(row["birth"])
    death_rates.append(row["death"])
    gdp_rates.append(row["gdp"])
    density_rates.append(row["density"])

    if natural > 0:
        growth_count += 1
        growth_list.append((row["name"], natural))
    else:
        decline_count += 1
        decline_list.append((row["name"], abs(natural)))

    if row["gdp"] > 30000:
        gdp_high += 1
        high_gdp.append(row["name"])
    else:
        gdp_low += 1
        low_gdp.append(row["name"])

    if row["continent"] == "Азия":
        asia_count += 1
    elif row["continent"] == "Европа":
        europe_count += 1
    elif row["continent"] == "Америка":
        america_count += 1
    elif row["continent"] == "Африка":
        africa_count += 1

    if row["birth"] > 15.0:
        high_birth.append(row["name"])
    elif row["birth"] < 10.0:
        low_birth.append(row["name"])

    if row["death"] > 10.0:
        high_death.append(row["name"])
    elif row["death"] < 7.0:
        low_death.append(row["name"])

    if row["density"] > 100:
        dense_countries.append((row["name"], row["density"]))
    else:
        sparse_countries.append((row["name"], row["density"]))

    print("{:<15} {:<12} {:<15,} {:<10.1f} {:<10.1f} {:<12.1f} {:<8,} {:<12.1f} {}".format(
        row["name"],
        row["continent"],
        row["pop"],
        row["birth"],
        row["death"],
        natural,
        row["gdp"],
        row["density"],
        status
    ))

print("-" * 100)

avg_pop = total_pop / country_count
avg_birth = total_birth / country_count
avg_death = total_death / country_count
avg_gdp = total_gdp / country_count
avg_area = total_area / country_count
avg_density = total_density / country_count

# Сортировка по населению
sorted_by_pop = sorted(countries_data, key=lambda x: x["pop"], reverse=True)
max_pop_country = sorted_by_pop[0]
min_pop_country = sorted_by_pop[-1]

# Сортировка по рождаемости
sorted_by_birth = sorted(countries_data, key=lambda x: x["birth"], reverse=True)
max_birth_country = sorted_by_birth[0]
min_birth_country = sorted_by_birth[-1]

# Сортировка по смертности
sorted_by_death = sorted(countries_data, key=lambda x: x["death"], reverse=True)
max_death_country = sorted_by_death[0]
min_death_country = sorted_by_death[-1]

# Сортировка по ВВП
sorted_by_gdp = sorted(countries_data, key=lambda x: x["gdp"], reverse=True)
max_gdp_country = sorted_by_gdp[0]
min_gdp_country = sorted_by_gdp[-1]

print("\n" + "█" * 85)
print(" 3. СТАТИСТИЧЕСКИЕ ПОКАЗАТЕЛИ")
print("█" * 85)

print(f"\n📊 ОБЩАЯ СТАТИСТИКА:")
print(f"   Всего стран: {country_count}")
print(f"   Общее население: {total_pop:,} чел.")
print(f"   Среднее население: {avg_pop:,.2f} чел.")
print(f"   Средняя рождаемость: {avg_birth:.2f}‰")
print(f"   Средняя смертность: {avg_death:.2f}‰")
print(f"   Средний ВВП: ${avg_gdp:,.2f}")
print(f"   Средняя плотность населения: {avg_density:.1f} чел/кв.км")

print(f"\n📈 МАКСИМАЛЬНЫЕ ПОКАЗАТЕЛИ:")
print(f"   Максимальное население: {max_pop_country['name']} ({max_pop_country['pop']:,} чел.)")
print(f"   Максимальная рождаемость: {max_birth_country['name']} ({max_birth_country['birth']:.1f}‰)")
print(f"   Максимальная смертность: {max_death_country['name']} ({max_death_country['death']:.1f}‰)")
print(f"   Максимальный ВВП: {max_gdp_country['name']} (${max_gdp_country['gdp']:,})")

print(f"\n📉 МИНИМАЛЬНЫЕ ПОКАЗАТЕЛИ:")
print(f"   Минимальное население: {min_pop_country['name']} ({min_pop_country['pop']:,} чел.)")
print(f"   Минимальная рождаемость: {min_birth_country['name']} ({min_birth_country['birth']:.1f}‰)")
print(f"   Минимальная смертность: {min_death_country['name']} ({min_death_country['death']:.1f}‰)")
print(f"   Минимальный ВВП: {min_gdp_country['name']} (${min_gdp_country['gdp']:,})")

print("\n" + "█" * 85)
print(" 4. РАСПРЕДЕЛЕНИЕ ПО КОНТИНЕНТАМ")
print("█" * 85)

print(f"\n🌍 КОНТИНЕНТЫ:")
print(f"   Азия: {asia_count} стран")
print(f"   Европа: {europe_count} стран")
print(f"   Америка: {america_count} стран")
print(f"   Африка: {africa_count} стран")

# Группировка по континентам
continents_data = {}
for row in countries_data:
    continent = row["continent"]
    if continent not in continents_data:
        continents_data[continent] = []
    continents_data[continent].append(row)

print(f"\n📊 СВОДКА ПО КОНТИНЕНТАМ:")
print("\n{:<12} {:<8} {:<15} {:<12} {:<12} {:<10}".format(
    "Континент", "Стран", "Население", "Рождаемость", "Смертность", "ВВП"
))
print("-" * 75)

for continent, rows in continents_data.items():
    cont_pop = sum([r["pop"] for r in rows])
    cont_birth = sum([r["birth"] for r in rows]) / len(rows)
    cont_death = sum([r["death"] for r in rows]) / len(rows)
    cont_gdp = sum([r["gdp"] for r in rows]) / len(rows)
    print("{:<12} {:<8} {:<15,} {:<12.2f} {:<12.2f} {:<10,.0f}".format(
        continent,
        len(rows),
        cont_pop,
        cont_birth,
        cont_death,
        cont_gdp
    ))

print("\n" + "█" * 85)
print(" 5. КЛАССИФИКАЦИЯ СТРАН ПО ПОКАЗАТЕЛЯМ")
print("█" * 85)

print(f"\n👶 КЛАССИФИКАЦИЯ ПО РОЖДАЕМОСТИ:")
print(f"   Высокая (>15‰): {len(high_birth)} стран → {', '.join(high_birth) if high_birth else 'нет'}")
print(f"   Низкая (<10‰): {len(low_birth)} стран → {', '.join(low_birth) if low_birth else 'нет'}")

print(f"\n💀 КЛАССИФИКАЦИЯ ПО СМЕРТНОСТИ:")
print(f"   Высокая (>10‰): {len(high_death)} стран → {', '.join(high_death) if high_death else 'нет'}")
print(f"   Низкая (<7‰): {len(low_death)} стран → {', '.join(low_death) if low_death else 'нет'}")

print(f"\n💰 КЛАССИФИКАЦИЯ ПО ВВП:")
print(f"   Высокий (>$30000): {len(high_gdp)} стран → {', '.join(high_gdp) if high_gdp else 'нет'}")
print(f"   Низкий (<$30000): {len(low_gdp)} стран → {', '.join(low_gdp) if low_gdp else 'нет'}")

print(f"\n🏙️ КЛАССИФИКАЦИЯ ПО ПЛОТНОСТИ НАСЕЛЕНИЯ:")
print(f"   Высокая (>100 чел/кв.км): {len(dense_countries)} стран → {', '.join([c[0] for c in dense_countries]) if dense_countries else 'нет'}")
print(f"   Низкая (<100 чел/кв.км): {len(sparse_countries)} стран → {', '.join([c[0] for c in sparse_countries]) if sparse_countries else 'нет'}")

print("\n" + "█" * 85)
print(" 6. ЕСТЕСТВЕННЫЙ ПРИРОСТ НАСЕЛЕНИЯ")
print("█" * 85)

print(f"\n✅ СТРАНЫ С ЕСТЕСТВЕННЫМ ПРИРОСТОМ ({len(growth_list)}):")
if growth_list:
    for name, val in growth_list:
        print(f"   {name}: +{val:.1f}‰")
else:
    print("   Нет стран с естественным приростом")

print(f"\n❌ СТРАНЫ С ЕСТЕСТВЕННОЙ УБЫЛЬЮ ({len(decline_list)}):")
if decline_list:
    for name, val in decline_list:
        print(f"   {name}: -{val:.1f}‰")
else:
    print("   Нет стран с естественной убылью")

print("\n" + "█" * 85)
print(" 7. ВЫВОДЫ И РЕКОМЕНДАЦИИ")
print("█" * 85)

print("\n📌 ОСНОВНЫЕ ВЫВОДЫ:")

# Вывод по приросту
if growth_count > decline_count:
    print(f"   ✅ В {growth_count} странах ({growth_count/country_count*100:.0f}%) наблюдается естественный прирост населения.")
    print(f"      Страны с приростом: {', '.join([c[0] for c in growth_list])}")
    print(f"      Страны с убылью: {', '.join([c[0] for c in decline_list])}")
else:
    print(f"   ⚠️ В {decline_count} странах ({decline_count/country_count*100:.0f}%) наблюдается естественная убыль населения.")
    print(f"      Страны с убылью: {', '.join([c[0] for c in decline_list])}")
    print(f"      Страны с приростом: {', '.join([c[0] for c in growth_list])}")

# Вывод по рождаемости
print(f"\n   👶 По рождаемости:")
print(f"      Высокая рождаемость (>15‰) в {len(high_birth)} странах: {', '.join(high_birth) if high_birth else 'нет'}")
print(f"      Низкая рождаемость (<10‰) в {len(low_birth)} странах: {', '.join(low_birth) if low_birth else 'нет'}")

# Вывод по смертности
print(f"\n   💀 По смертности:")
print(f"      Высокая смертность (>10‰) в {len(high_death)} странах: {', '.join(high_death) if high_death else 'нет'}")
print(f"      Низкая смертность (<7‰) в {len(low_death)} странах: {', '.join(low_death) if low_death else 'нет'}")

# Вывод по ВВП
print(f"\n   💰 По ВВП:")
print(f"      Высокий ВВП (>$30000) в {len(high_gdp)} странах: {', '.join(high_gdp) if high_gdp else 'нет'}")
print(f"      Низкий ВВП (<$30000) в {len(low_gdp)} странах: {', '.join(low_gdp) if low_gdp else 'нет'}")

# Вывод по плотности
print(f"\n   🏙️ По плотности населения:")
print(f"      Высокая плотность (>100 чел/кв.км) в {len(dense_countries)} странах: {', '.join([c[0] for c in dense_countries]) if dense_countries else 'нет'}")
print(f"      Низкая плотность (<100 чел/кв.км) в {len(sparse_countries)} странах: {', '.join([c[0] for c in sparse_countries]) if sparse_countries else 'нет'}")

print("\n📌 РЕКОМЕНДАЦИИ:")

if decline_list:
    print("   - Разработать меры поддержки рождаемости в странах с убылью:")
    for name, val in decline_list:
        print(f"     * {name} (убыль {val:.1f}‰)")

if low_gdp:
    print("   - Стимулировать экономический рост в странах с низким ВВП:")
    for name in low_gdp:
        print(f"     * {name}")

if dense_countries:
    print("   - Учитывать высокую плотность населения при планировании инфраструктуры:")
    for name, val in dense_countries:
        print(f"     * {name} ({val:.1f} чел/кв.км)")

print("\n" + "█" * 85)
print(" 8. ИТОГОВАЯ СВОДНАЯ СТАТИСТИКА")
print("█" * 85)

print(f"""
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              СВОДНАЯ СТАТИСТИКА                                    │
├─────────────────────────────────────────────────────────────────────────────────────┤
│  Всего стран                     {country_count:>10}                                        │
│  Общее население                 {total_pop:>15,} чел.                              │
│  Среднее население               {avg_pop:>15,.2f} чел.                            │
│  Средняя рождаемость             {avg_birth:>15.2f}‰                               │
│  Средняя смертность              {avg_death:>15.2f}‰                               │
│  Средний ВВП                     ${avg_gdp:>14,.2f}                                │
│  Средняя плотность               {avg_density:>15.1f} чел/кв.км                   │
│  Стран с приростом               {growth_count:>10}                                        │
│  Стран с убылью                  {decline_count:>10}                                        │
│  Стран с высоким ВВП             {gdp_high:>10}                                          │
│  Стран с низким ВВП              {gdp_low:>10}                                           │
│  Стран с высокой плотностью      {len(dense_countries):>10}                                  │
│  Стран с низкой плотностью       {len(sparse_countries):>10}                                 │
└─────────────────────────────────────────────────────────────────────────────────────┘
""")

print("\n" + "█" * 85)
print(" 9. ИТОГОВОЕ ЗАКЛЮЧЕНИЕ")
print("█" * 85)

print(f"""
В ходе выполнения урока 5 были изучены и отработаны следующие темы:
1. Создание списков и доступ к элементам по индексу
2. Изменение списков и добавление элементов
3. Создание словарей и работа с ключами
4. Список словарей как мини-таблица
5. Анализ данных на основе списка словарей

На основе данных по {country_count} странам мира получены следующие результаты:
- Общее население: {total_pop:,} человек
- Средняя рождаемость: {avg_birth:.2f}‰
- Средняя смертность: {avg_death:.2f}‰
- В {growth_count} странах наблюдается естественный прирост населения
- В {decline_count} странах наблюдается естественная убыль населения
- Максимальное население: {max_pop_country['name']} ({max_pop_country['pop']:,} чел.)
- Минимальное население: {min_pop_country['name']} ({min_pop_country['pop']:,} чел.)
- Максимальный ВВП: {max_gdp_country['name']} (${max_gdp_country['gdp']:,})
- Минимальный ВВП: {min_gdp_country['name']} (${min_gdp_country['gdp']:,})

Полученные навыки являются основой для работы с табличными данными и
подготовкой к изучению библиотеки pandas.
""")

print("=" * 85)
print(" " * 30 + "✅ ОТЧЕТ СФОРМИРОВАН")
print(" " * 28 + "ДАННЫЕ ГОТОВЫ К АНАЛИЗУ")
print("=" * 85)