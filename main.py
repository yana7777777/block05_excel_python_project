# Загрузка данных из локальной папки data
import pandas as pd
from pathlib import Path

# Путь к CSV файлу в папке data
csv_path = Path("data/demographic_data.csv")

# Проверяем, что файл существует
if not csv_path.exists():
    raise FileNotFoundError(f"Файл не найден: {csv_path}")

# Читаем CSV файл
df = pd.read_csv(csv_path)

# Проверяем, что загрузилось
print("Размер таблицы:", df.shape)
print("\nПервые 5 строк:")
print(df.head())
print("\nНазвания столбцов:")
print(list(df.columns))

# Сохраняем как XLSX в ту же папку data
xlsx_path = Path("data/demographic_data.xlsx")
df.to_excel(xlsx_path, index=False, sheet_name="demographic_data")

print(f"\n✅ Файл успешно конвертирован и сохранен как: {xlsx_path}")

# Проверяем, что файл создался
if xlsx_path.exists():
    print(f"✅ Файл {xlsx_path.name} успешно создан в папке {xlsx_path.parent}")
else:
    print("❌ Что-то пошло не так, файл не создан")




# Ячейка 2. Фильтрация по одному условию
# Адаптировано под демографический датасет

print("="*70)
print("ФИЛЬТРАЦИЯ ПО ОДНОМУ УСЛОВИЮ")
print("="*70)

# Проверяем уникальные значения континентов
print("\n🌍 УНИКАЛЬНЫЕ КОНТИНЕНТЫ В ДАННЫХ:")
print(df["continent"].unique())

# TODO:
# 1. Отберите только строки, где continent == "Europe"
# 2. Сохраните результат в europe_df
# 3. Выведите количество строк после фильтра
# 4. Покажите результат

europe_df = df[df["continent"] == "Europe"]

print(f"\n📊 Количество строк в датасете: {len(df)}")
print(f"📊 Количество строк с континентом 'Europe': {len(europe_df)}")
print(f"📊 Процент европейских стран: {len(europe_df) / len(df) * 100:.1f}%")

print("\n📋 ПЕРВЫЕ 5 СТРОК ОТФИЛЬТРОВАННОЙ ТАБЛИЦЫ:")
print(europe_df.head())

print("\n📊 СТАТИСТИКА ПО ЕВРОПЕЙСКИМ СТРАНАМ:")
print(europe_df[["pop", "birth_rate", "death_rate"]].describe())


# Ячейка 3. Фильтрация по нескольким условиям
# Адаптировано под демографический датасет

print("="*70)
print("ФИЛЬТРАЦИЯ ПО НЕСКОЛЬКИМ УСЛОВИЯМ")
print("="*70)

# TODO:
# 1. Создайте фильтр для строк, где continent == "Europe"
# 2. Добавьте второе условие: year >= 2010
# 3. Сохраните результат в europe_recent_df
# 4. Выведите количество строк и саму таблицу

europe_recent_df = df[(df["continent"] == "Europe") & (df["year"] >= 2010)]

print(f"\n📊 Количество строк в датасете: {len(df)}")
print(f"📊 Количество строк с континентом 'Europe' и годом >= 2010: {len(europe_recent_df)}")
print(f"📊 Процент от общего датасета: {len(europe_recent_df) / len(df) * 100:.1f}%")

print("\n📋 ПЕРВЫЕ 5 СТРОК ОТФИЛЬТРОВАННОЙ ТАБЛИЦЫ:")
print(europe_recent_df.head())

print("\n📊 СТАТИСТИКА ПО ОТФИЛЬТРОВАННЫМ ДАННЫМ:")
print(europe_recent_df[["pop", "birth_rate", "death_rate"]].describe())


# Ячейка 4. Сортировка таблицы
# Адаптировано под демографический датасет

print("="*70)
print("СОРТИРОВКА ТАБЛИЦЫ")
print("="*70)

# TODO:
# 1. Отсортируйте таблицу по столбцу pop (население) по убыванию
# 2. Сохраните результат в sorted_by_pop
# 3. Покажите первые 5 строк результата

sorted_by_pop = df.sort_values(by="pop", ascending=False)

print("\n📊 ТОП-5 СТРАН ПО НАСЕЛЕНИЮ (ВСЕ ГОДЫ):")
print(sorted_by_pop[["country", "continent", "year", "pop"]].head(5))

print("\n📊 ТОП-5 СТРАН ПО НАСЕЛЕНИЮ (ТОЛЬКО 2020 ГОД):")
df_2020 = df[df["year"] == 2020]
sorted_by_pop_2020 = df_2020.sort_values(by="pop", ascending=False)
print(sorted_by_pop_2020[["country", "continent", "pop"]].head(5))


# Ячейка 5. Вычисляемый столбец и мини-задача
print("="*70)
print("ВЫЧИСЛЯЕМЫЙ СТОЛБЕЦ И МИНИ-ЗАДАЧА")
print("="*70)

df_calc = df.copy()
df_calc["natural_increase"] = df_calc["birth_rate"] - df_calc["death_rate"]

avg_natural = df_calc["natural_increase"].mean()
high_growth = df_calc[df_calc["natural_increase"] > 5].sort_values(by="natural_increase", ascending=False)
decline = df_calc[df_calc["natural_increase"] < 0].sort_values(by="natural_increase", ascending=True)

print(f"\nСредний прирост: {avg_natural:.2f}‰")
print(f"Стран с приростом > 5‰: {len(high_growth)}")
print(f"Стран с убылью: {len(decline)}")

print("\nТоп-10 по приросту:")
print(high_growth[["country", "year", "natural_increase"]].head(10))


# Ячейка 6. Тесты
print("="*50)
print("ТЕСТЫ")
print("="*50)

test_df = df.copy()

# 1. Размер таблицы
assert test_df.shape == (len(df), len(df.columns))
print("✅ Размер OK")

# 2. Фильтрация по континенту
test_europe = test_df[test_df["continent"] == "Europe"]
assert len(test_europe) > 0
print(f"✅ Europe: {len(test_europe)}")

# 3. Фильтрация по нескольким условиям
test_recent = test_df[(test_df["continent"] == "Europe") & (test_df["year"] >= 2010)]
assert len(test_recent) > 0
print(f"✅ Europe>=2010: {len(test_recent)}")

# 4. Сортировка (проверяем, что есть данные)
test_sorted = test_df.sort_values(by="pop", ascending=False)
assert len(test_sorted) > 0, "Таблица пуста"
print(f"✅ Лидер по населению: {test_sorted.iloc[0]['country']} ({test_sorted.iloc[0]['pop']:,} чел.)")

# 5. Вычисляемый столбец
test_calc = test_df.copy()
test_calc["natural_increase"] = test_calc["birth_rate"] - test_calc["death_rate"]
assert "natural_increase" in test_calc.columns
print("✅ natural_increase OK")

# 6. Фильтрация по вычисляемому столбцу
test_high = test_calc[test_calc["natural_increase"] > 5]
assert len(test_high) > 0
print(f"✅ Прирост >5: {len(test_high)}")

print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")



# Ячейка 7. Итоговый отчет по уроку 8
print("="*70)
print("ИТОГОВЫЙ ОТЧЕТ ПО УРОКУ 8")
print("ФИЛЬТРАЦИЯ, СОРТИРОВКА И ВЫЧИСЛЯЕМЫЕ СТОЛБЦЫ")
print("="*70)

# 1. Общая статистика
print("\n1. ОБЩАЯ СТАТИСТИКА")
print("-"*40)
print(f"Всего строк: {len(df)}")
print(f"Всего столбцов: {len(df.columns)}")
print(f"Стран: {df['country'].nunique()}")
print(f"Континентов: {df['continent'].nunique()}")
print(f"Годов: {df['year'].nunique()}")

print(f"\nСредняя рождаемость: {df['birth_rate'].mean():.2f}‰")
print(f"Средняя смертность: {df['death_rate'].mean():.2f}‰")
print(f"Средний прирост: {(df['birth_rate'] - df['death_rate']).mean():.2f}‰")

# 2. Фильтрация
print("\n2. ФИЛЬТРАЦИЯ")
print("-"*40)
europe_df = df[df["continent"] == "Europe"]
print(f"Европа: {len(europe_df)} записей ({len(europe_df)/len(df)*100:.1f}%)")

europe_recent = df[(df["continent"] == "Europe") & (df["year"] >= 2010)]
print(f"Европа (год >= 2010): {len(europe_recent)} записей")

high_growth = df[(df["birth_rate"] - df["death_rate"]) > 5]
print(f"С приростом > 5‰: {len(high_growth)} записей")

# 3. Сортировка
print("\n3. ТОП-5 ПО НАСЕЛЕНИЮ (2020)")
print("-"*40)
df_2020 = df[df["year"] == 2020]
top5 = df_2020.nlargest(5, "pop")
for i, (_, row) in enumerate(top5.iterrows(), 1):
    print(f"{i}. {row['country']}: {row['pop']:,} чел.")

# 4. Топ по приросту
print("\n4. ТОП-5 ПО ЕСТЕСТВЕННОМУ ПРИРОСТУ")
print("-"*40)
df_calc = df.copy()
df_calc["natural_increase"] = df_calc["birth_rate"] - df_calc["death_rate"]
top_natural = df_calc.nlargest(5, "natural_increase")
for i, (_, row) in enumerate(top_natural.iterrows(), 1):
    print(f"{i}. {row['country']} ({row['year']}): {row['natural_increase']:.1f}‰")

# 5. Итоговый вывод
print("\n5. ВЫВОДЫ")
print("="*70)
print("""✅ Фильтрация позволяет отбирать данные по условиям (континент, год)
✅ Сортировка выделяет лидеров по населению и другим показателям
✅ Вычисляемые столбцы помогают анализировать прирост населения
✅ Данные готовы для дальнейшего анализа и визуализации""")

print("="*70)
print("ОТЧЕТ СФОРМИРОВАН")
print("="*70)


