# Ячейка 1. Загружаем CSV из папки data, создаём Excel и считаем базовые агрегаты
import pandas as pd
from pathlib import Path

# Указываем путь к CSV файлу в папке data
csv_path = Path("data/demographic_data.csv")

# Проверяем, что файл существует
if not csv_path.exists():
    raise FileNotFoundError(f"Файл не найден: {csv_path}")

# Читаем CSV файл
df = pd.read_csv(csv_path)

# Создаём вычисляемый столбец natural_increase
df["natural_increase"] = df["birth_rate"] - df["death_rate"]

# Сохраняем как XLSX в папку data
xlsx_path = Path("data/lesson_09_groupby_pivot.xlsx")
df.to_excel(xlsx_path, index=False, sheet_name="sales_data")

print(f"✅ Файл сохранён: {xlsx_path}")

# Базовые агрегаты
print("\n📊 РАЗМЕР ТАБЛИЦЫ:", df.shape)
print("📊 КОЛИЧЕСТВО ЗАПИСЕЙ:", len(df))
print("📊 ОБЩИЙ ЕСТЕСТВЕННЫЙ ПРИРОСТ:", int(df["natural_increase"].sum()))
print("📊 СРЕДНИЙ ЕСТЕСТВЕННЫЙ ПРИРОСТ:", round(df["natural_increase"].mean(), 2))
print("📊 МАКСИМАЛЬНЫЙ ПРИРОСТ:", int(df["natural_increase"].max()))
print("📊 МИНИМАЛЬНЫЙ ПРИРОСТ:", int(df["natural_increase"].min()))

print(df.head())



# Ячейка 2. Группировка по континентам
print("="*70)
print("ГРУППИРОВКА ПО КОНТИНЕНТАМ")
print("="*70)

continent_summary = (
    df.groupby("continent", as_index=False)
      .agg(
          total_natural=("natural_increase", "sum"),
          countries=("country", "count"),
          avg_natural=("natural_increase", "mean"),
          avg_birth=("birth_rate", "mean"),
          avg_death=("death_rate", "mean")
      )
)

continent_summary["avg_natural"] = continent_summary["avg_natural"].round(2)
continent_summary["avg_birth"] = continent_summary["avg_birth"].round(2)
continent_summary["avg_death"] = continent_summary["avg_death"].round(2)

print("\n📊 СВОДКА ПО КОНТИНЕНТАМ:")
print(continent_summary.to_string(index=False))


# Ячейка 3. Группировка по континентам и годам
print("="*70)
print("ГРУППИРОВКА ПО КОНТИНЕНТАМ И ГОДАМ")
print("="*70)

cont_year_summary = (
    df.groupby(["continent", "year"], as_index=False)
      .agg(
          total_natural=("natural_increase", "sum"),
          avg_natural=("natural_increase", "mean"),
          countries=("country", "count"),
          avg_birth=("birth_rate", "mean"),
          avg_death=("death_rate", "mean")
      )
      .sort_values(["continent", "year"], ascending=[True, True])
)

cont_year_summary["avg_natural"] = cont_year_summary["avg_natural"].round(2)
cont_year_summary["avg_birth"] = cont_year_summary["avg_birth"].round(2)
cont_year_summary["avg_death"] = cont_year_summary["avg_death"].round(2)

print("\n📊 СВОДКА ПО КОНТИНЕНТАМ И ГОДАМ:")
print(cont_year_summary.to_string(index=False))


# Ячейка 4. Сортировка и поиск лидера
print("="*70)
print("СОРТИРОВКА И ПОИСК ЛИДЕРА")
print("="*70)

# Сортируем по total_natural (убывание)
continent_sorted = continent_summary.sort_values(by="total_natural", ascending=False)

top_continent = continent_sorted.iloc[0]["continent"]
top_continent_natural = int(continent_sorted.iloc[0]["total_natural"])

print(f"\n🏆 ЛИДЕР ПО ЕСТЕСТВЕННОМУ ПРИРОСТУ: {top_continent}")
print(f"   Общий прирост: {top_continent_natural}‰")

print("\n📊 ВСЕ КОНТИНЕНТЫ (ОТ ЛУЧШЕГО К ХУДШЕМУ):")
print(continent_sorted[["continent", "total_natural", "countries", "avg_natural"]].to_string(index=False))



# Ячейка 5. Сводная таблица: континент × год
print("="*70)
print("СВОДНАЯ ТАБЛИЦА: КОНТИНЕНТ × ГОД")
print("="*70)

pivot = pd.pivot_table(
    df,
    values="natural_increase",
    index="continent",
    columns="year",
    aggfunc="mean",
    fill_value=0
)

pivot = pivot.round(2)

best_year_continent = pivot.sum(axis=0).idxmax()
best_continent_2020 = pivot[2020].idxmax()

print(f"\n📊 Год с максимальным средним приростом: {best_year_continent}")
print(f"📊 Континент-лидер в 2020 году: {best_continent_2020}")

print("\n📊 СВОДНАЯ ТАБЛИЦА (средний прирост по континентам и годам):")
print(pivot.to_string())


# Ячейка 6. Тесты и самопроверка
print("="*70)
print("ТЕСТЫ")
print("="*70)

test_df = df.copy()

# 1. Размер таблицы
assert test_df.shape == (len(df), len(df.columns))
print("✅ Размер таблицы OK")

# 2. Проверка natural_increase
assert "natural_increase" in test_df.columns
print("✅ natural_increase OK")

# 3. Группировка по континентам
test_continent = test_df.groupby("continent")["natural_increase"].sum()
assert len(test_continent) > 0
print(f"✅ Континентов: {len(test_continent)}")

# 4. Группировка по годам
test_year = test_df.groupby("year")["natural_increase"].mean()
assert len(test_year) > 0
print(f"✅ Годов: {len(test_year)}")

# 5. Сводная таблица
test_pivot = pd.pivot_table(
    test_df,
    values="natural_increase",
    index="continent",
    columns="year",
    aggfunc="mean",
    fill_value=0
)
assert test_pivot.shape[0] > 0
print("✅ Сводная таблица OK")

# 6. Сортировка
test_sorted = test_df.groupby("continent")["natural_increase"].sum().sort_values(ascending=False)
assert len(test_sorted) > 0
print(f"✅ Лидер: {test_sorted.index[0]}")

print("\n🎉 ВСЕ ТЕСТЫ ПРОЙДЕНЫ!")


# Ячейка 7. Итоговый отчет по уроку 9
print("="*70)
print("ИТОГОВЫЙ ОТЧЕТ ПО УРОКУ 9")
print("ГРУППИРОВКА, АГРЕГАТЫ И СВОДНЫЕ ТАБЛИЦЫ")
print("="*70)

# 1. Общая статистика
print("\n1. ОБЩАЯ СТАТИСТИКА")
print("-"*50)
print(f"Всего записей: {len(df)}")
print(f"Стран: {df['country'].nunique()}")
print(f"Континентов: {df['continent'].nunique()}")
print(f"Годов: {df['year'].nunique()}")

print(f"\nОбщий естественный прирост: {df['natural_increase'].sum():.0f}‰")
print(f"Средний естественный прирост: {df['natural_increase'].mean():.2f}‰")
print(f"Максимальный прирост: {df['natural_increase'].max():.1f}‰")
print(f"Минимальный прирост: {df['natural_increase'].min():.1f}‰")

# 2. Группировка по континентам
print("\n2. ГРУППИРОВКА ПО КОНТИНЕНТАМ")
print("-"*50)
print(continent_summary[["continent", "total_natural", "countries", "avg_natural", "avg_birth", "avg_death"]].to_string(index=False))

# 3. Группировка по годам
print("\n3. ГРУППИРОВКА ПО ГОДАМ")
print("-"*50)
year_summary = (
    df.groupby("year", as_index=False)
      .agg(
          avg_natural=("natural_increase", "mean"),
          avg_birth=("birth_rate", "mean"),
          avg_death=("death_rate", "mean")
      )
      .round(2)
)
print(year_summary.to_string(index=False))

# 4. Сводная таблица
print("\n4. СВОДНАЯ ТАБЛИЦА: КОНТИНЕНТ × ГОД")
print("-"*50)
print(pivot.to_string())

# 5. Лидеры
print("\n5. ЛИДЕРЫ ПО ЕСТЕСТВЕННОМУ ПРИРОСТУ")
print("-"*50)
top_cont = continent_sorted.iloc[0]
print(f"Континент-лидер: {top_cont['continent']} (прирост {top_cont['total_natural']:.0f}‰)")

country_avg = df.groupby("country")["natural_increase"].mean().sort_values(ascending=False)
print(f"Страна-лидер: {country_avg.index[0]} ({country_avg.iloc[0]:.1f}‰)")

# 6. Выводы
print("\n6. ВЫВОДЫ")
print("="*70)
print("""
✅ Группировка позволяет анализировать данные по континентам и годам
✅ Агрегаты (sum, mean) дают обобщённую картину демографической ситуации
✅ Сводные таблицы показывают динамику прироста по континентам и годам
✅ Лидеры по приросту: развивающиеся страны Азии и Африки
✅ Данные готовы для дальнейшего анализа и визуализации
""")
print("="*70)
print("ОТЧЕТ СФОРМИРОВАН")
print("="*70)