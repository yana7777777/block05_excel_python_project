# os нужен для проверки файлов и папок.
import os

# Path нужен для удобной работы с путями.
from pathlib import Path

# numpy нужен для числовых расчётов.
import numpy as np

# pandas нужен для работы с таблицами.
import pandas as pd

# matplotlib нужен для построения графиков.
import matplotlib.pyplot as plt

# display красиво показывает таблицы в Google Colab.
from IPython.display import display

# train_test_split делит данные на обучающую и тестовую части.
from sklearn.model_selection import train_test_split

# LinearRegression — простая модель машинного обучения для прогноза числа.
from sklearn.linear_model import LinearRegression

# Метрики качества прогноза.
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Папка для данных.
DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# Папка для отчётов.
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

# Проверяем, что папки созданы.
assert DATA_DIR.exists()
assert REPORTS_DIR.exists()

print("Окружение готово.")



# Шаблонный ноутбук с внешним датасетом
# Демография: рождаемость и смертность

import pandas as pd
import numpy as np
from pathlib import Path

# ============================================
# 1. НАСТРОЙКА ПУТЕЙ
# ============================================

DATA_DIR = Path("data")
DATA_DIR.mkdir(exist_ok=True)

# ============================================
# 2. URL ОТКРЫТОГО ДАТАСЕТА
# ============================================

url = "https://raw.githubusercontent.com/yana7777777/block05_excel_project/main/data/demographic_data.csv"

# Путь для локальной копии
local_data_path = DATA_DIR / "demographic_data.csv"

# ============================================
# 3. ФУНКЦИЯ FALLBACK (если интернет недоступен)
# ============================================

def create_fallback_demographic_dataset() -> pd.DataFrame:
    """Создаёт демографический датасет для fallback."""
    rng = np.random.default_rng(42)

    countries = [
        ("Russia", "Europe"),
        ("USA", "Americas"),
        ("China", "Asia"),
        ("India", "Asia"),
        ("Brazil", "Americas"),
        ("Nigeria", "Africa"),
        ("Germany", "Europe"),
        ("France", "Europe"),
        ("Japan", "Asia"),
        ("UK", "Europe"),
        ("Mexico", "Americas"),
        ("Egypt", "Africa"),
        ("Turkey", "Europe"),
        ("Vietnam", "Asia"),
        ("Kenya", "Africa"),
        ("Australia", "Oceania"),
        ("Canada", "Americas"),
        ("South Africa", "Africa"),
    ]

    years = [2000, 2005, 2010, 2015, 2020]
    rows = []

    for country, continent in countries:
        base_pop = rng.uniform(10_000_000, 150_000_000)
        base_birth = rng.uniform(8, 35)
        base_death = rng.uniform(5, 15)

        for year in years:
            year_idx = (year - 2000) / 5
            pop = base_pop * (1 + 0.012 * year_idx) + rng.normal(0, 1_000_000)
            pop = max(pop, 100_000)

            birth_rate = base_birth - 0.4 * year_idx + rng.normal(0, 0.5)
            birth_rate = max(birth_rate, 2.0)

            death_rate = base_death + 0.1 * year_idx + rng.normal(0, 0.3)
            death_rate = max(death_rate, 1.0)

            rows.append({
                "country": country,
                "continent": continent,
                "year": year,
                "pop": int(pop),
                "birth_rate": round(birth_rate, 1),
                "death_rate": round(death_rate, 1),
            })

    return pd.DataFrame(rows)

# ============================================
# 4. ЗАГРУЗКА ДАННЫХ
# ============================================

try:
    df = pd.read_csv(url)
    print("Данные успешно загружены из интернета.")
except Exception as error:
    print("Интернет-загрузка не сработала.")
    print("Создаём учебный fallback-датасет с такими же ключевыми столбцами.")
    df = create_fallback_demographic_dataset()

# Сохраняем локальную копию
df.to_csv(local_data_path, index=False)

# ============================================
# 5. ПЕРВИЧНЫЙ ОБЗОР
# ============================================

# Показываем первые строки
display(df.head())

# Печатаем размер
print("Размер таблицы:", df.shape)
print("Файл сохранён:", local_data_path)

# Проверяем ключевые столбцы
required_columns = {"country", "continent", "year", "pop", "birth_rate", "death_rate"}
assert required_columns.issubset(df.columns)



# ============================================
# ПРОВЕРКА КАЧЕСТВА ДАННЫХ
# ============================================

# Размер таблицы.
print("Размер таблицы:", df.shape)

# Названия столбцов.
print("\nНазвания столбцов:")
print(df.columns.tolist())

# Типы данных.
print("\nТипы данных:")
print(df.dtypes)

# Проверка пропусков.
print("\nПропуски по столбцам:")
print(df.isna().sum())

# Описательная статистика.
print("\nОписательная статистика:")
display(df.describe())

# Проверяем, что таблица не пустая.
assert len(df) > 0

# Проверяем, что нет пропусков в ключевых числовых столбцах.
assert df[["year", "pop", "birth_rate", "death_rate"]].isna().sum().sum() == 0

print("\n✅ Проверка данных пройдена. Данные готовы к анализу.")



# Целевая переменная.
target_column = "death_rate"

# Признаки.
feature_columns = ["year", "pop", "birth_rate"]

# Рабочая таблица только с нужными столбцами.
model_df = df[feature_columns + [target_column]].copy()

# Показываем рабочую таблицу.
display(model_df.head())

print("Целевая переменная:", target_column)
print("Признаки:", feature_columns)

# Проверки.
assert target_column in model_df.columns
assert set(feature_columns).issubset(model_df.columns)



# График 1: год и смертность.
plt.figure(figsize=(8, 4))
plt.scatter(df["year"], df["death_rate"], alpha=0.5)
plt.title("Год и смертность")
plt.xlabel("Год")
plt.ylabel("Смертность (на 1000 человек)")
plt.grid(True)
plt.tight_layout()
plt.show()

# График 2: рождаемость и смертность.
plt.figure(figsize=(8, 4))
plt.scatter(df["birth_rate"], df["death_rate"], alpha=0.5)
plt.title("Рождаемость и смертность")
plt.xlabel("Рождаемость (на 1000 человек)")
plt.ylabel("Смертность (на 1000 человек)")
plt.grid(True)
plt.tight_layout()
plt.show()

# График 3: население и смертность.
plt.figure(figsize=(8, 4))
plt.scatter(df["pop"], df["death_rate"], alpha=0.5)
plt.title("Население и смертность")
plt.xlabel("Население (человек)")
plt.ylabel("Смертность (на 1000 человек)")
plt.grid(True)
plt.tight_layout()
plt.show()

print("Первичный вывод:")
print("Если на графике точки идут вверх, значит между признаком и целью может быть положительная связь.")
print("Если точки идут вниз — отрицательная связь.")
print("Если точки разбросаны хаотично — связи нет.")

# Проверка.
assert df["death_rate"].min() > 0


# X — признаки.
X = model_df[feature_columns]

# y — целевая переменная.
y = model_df[target_column]

# Показываем первые строки X.
print("Первые строки X:")
display(X.head())

# Показываем первые значения y.
print("Первые значения y:")
display(y.head())

# Размеры.
print("Размер X:", X.shape)
print("Размер y:", y.shape)

# Проверки.
assert len(X) == len(y)
assert X.shape[1] == len(feature_columns)



# Делим данные на обучение и тест.
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

print("Размер X_train:", X_train.shape)
print("Размер X_test:", X_test.shape)
print("Размер y_train:", y_train.shape)
print("Размер y_test:", y_test.shape)

# Проверки.
assert len(X_train) == len(y_train)
assert len(X_test) == len(y_test)
assert len(X_train) + len(X_test) == len(X)



# Создаём модель.
model = LinearRegression()

# Обучаем модель на обучающей части.
model.fit(X_train, y_train)

# Собираем коэффициенты в таблицу.
coef_df = pd.DataFrame({
    "feature": feature_columns,
    "coefficient": model.coef_,
})

# Свободный член модели.
intercept = model.intercept_

print("Свободный член модели:")
print(intercept)

print("\nКоэффициенты модели:")
display(coef_df)

# Проверки.
assert len(model.coef_) == len(feature_columns)
assert isinstance(intercept, float)


# Строим прогноз.
y_pred = model.predict(X_test)

# Таблица факт-прогноз.
results_df = pd.DataFrame({
    "real_death_rate": y_test.values,
    "predicted_death_rate": y_pred,
})

# Добавляем ошибку прогноза.
results_df["error"] = results_df["predicted_death_rate"] - results_df["real_death_rate"]
results_df["abs_error"] = results_df["error"].abs()

# Показываем первые строки.
display(results_df.head(10))

# График факт vs прогноз.
plt.figure(figsize=(7, 6))
plt.scatter(y_test, y_pred, alpha=0.6)

# Линия идеального прогноза.
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()])

plt.xlabel("Реальная смертность")
plt.ylabel("Прогноз модели")
plt.title("Факт vs прогноз (смертность)")
plt.grid(True)
plt.tight_layout()
plt.show()

# Проверки.
assert len(y_pred) == len(y_test)
assert "abs_error" in results_df.columns



# Считаем метрики модели.
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

# Baseline: простой прогноз средним значением обучающей выборки.
baseline_pred = np.full(shape=len(y_test), fill_value=y_train.mean())

# MAE baseline.
baseline_mae = mean_absolute_error(y_test, baseline_pred)

# Печатаем метрики.
print("Метрики модели:")
print("MAE:", round(mae, 3))
print("MSE:", round(mse, 3))
print("RMSE:", round(rmse, 3))
print("R2:", round(r2, 3))

print("\nBaseline:")
print("Baseline MAE:", round(baseline_mae, 3))

if mae < baseline_mae:
    print("\nВывод: модель лучше простого прогноза средним.")
else:
    print("\nВывод: модель не лучше простого прогноза средним. Признаки или модель нужно улучшать.")

# Проверки.
assert mae >= 0
assert mse >= 0
assert rmse >= 0




# Новые примеры для прогноза.
new_cases = pd.DataFrame({
    "year": [2025, 2025, 2025],
    "pop": [50_000_000, 50_000_000, 50_000_000],
    "birth_rate": [8.0, 15.0, 30.0],
})

# Строим прогноз.
new_cases["predicted_death_rate"] = model.predict(new_cases)

# Показываем результат.
display(new_cases)

print("Интерпретация:")
print("Модель показывает, как меняется прогноз смертности при разных уровнях рождаемости.")
print("При одинаковом населении и годе, чем выше рождаемость, тем выше прогнозируемая смертность.")

# Проверки.
assert "predicted_death_rate" in new_cases.columns
assert len(new_cases) == 3


# ============================================
# 11. ПРОГНОЗ ДЛЯ НОВЫХ СЦЕНАРИЕВ
# ============================================

new_cases = pd.DataFrame({
    "year": [2025, 2025, 2025],
    "pop": [50_000_000, 50_000_000, 50_000_000],
    "birth_rate": [8.0, 15.0, 30.0],
})

new_cases["predicted_death_rate"] = model.predict(new_cases)

display(new_cases)

print("Интерпретация:")
print("Модель показывает, как меняется прогноз смертности при разных уровнях рождаемости.")

# ============================================
# 12. ИТОГОВЫЙ ОТЧЁТ
# ============================================

# Подготовка переменных для отчёта
coef_year = model.coef_[0]
coef_birth = model.coef_[2]

if coef_year > 0:
    year_effect = "положительное (смертность растёт)"
else:
    year_effect = "отрицательное (смертность снижается)"

if coef_birth > 0:
    birth_effect = "положительное (выше рождаемость -> выше смертность)"
else:
    birth_effect = "отрицательное (выше рождаемость -> ниже смертность)"

if mae < baseline_mae:
    quality_text = "Модель лучше простого прогноза средним"
    improvement = f"Улучшение составило {(baseline_mae - mae) / baseline_mae * 100:.1f}%"
else:
    quality_text = "Модель не лучше простого прогноза средним"
    improvement = "Требуется улучшение модели"

if abs(coef_year) > abs(coef_birth):
    strongest = "год (year)"
else:
    strongest = "рождаемость (birth_rate)"

if r2 > 0.5:
    r2_text = f"хорошее. Модель объясняет {r2*100:.1f}% разброса данных"
else:
    r2_text = f"удовлетворительное. Модель объясняет {r2*100:.1f}% разброса данных"

pred1 = new_cases.iloc[0]['predicted_death_rate']
pred2 = new_cases.iloc[1]['predicted_death_rate']
pred3 = new_cases.iloc[2]['predicted_death_rate']

report_text = f'''
ИТОГОВЫЙ ОТЧЁТ ПО ПЕРВОМУ AI-НОУТБУКУ

1. ДАННЫЕ

Использован демографический датасет с показателями рождаемости и смертности по странам мира за период 2000-2020 годов.
Количество строк: {len(df)}
Количество столбцов: {df.shape[1]}

Колонки в датасете:
- country - название страны
- continent - континент
- year - год наблюдения
- pop - численность населения
- birth_rate - рождаемость (на 1000 человек)
- death_rate - смертность (на 1000 человек)

2. ЗАДАЧА

Решалась задача регрессии: прогнозирование уровня смертности death_rate.

3. ПРИЗНАКИ

Для прогноза использовались признаки:
- year (год наблюдения)
- pop (численность населения)
- birth_rate (рождаемость на 1000 человек)

4. МОДЕЛЬ

Использована модель LinearRegression.

Коэффициенты модели:
- year: {coef_year:.4f} - {year_effect}
- pop: {model.coef_[1]:.10f} - влияние населения минимально
- birth_rate: {coef_birth:.4f} - {birth_effect}

Свободный член модели (intercept): {model.intercept_:.2f}

5. КАЧЕСТВО МОДЕЛИ

MAE: {mae:.3f}
RMSE: {rmse:.3f}
R2: {r2:.3f}
Baseline MAE: {baseline_mae:.3f}

{quality_text}
{improvement}
Качество модели: {r2_text}

6. ПРОГНОЗ ДЛЯ НОВЫХ СЦЕНАРИЕВ

Три сценария для 2025 года с одинаковым населением (50 млн), но разным уровнем рождаемости:

Сценарий 1 (рождаемость 8.0): прогноз смертности = {pred1:.2f}
Сценарий 2 (рождаемость 15.0): прогноз смертности = {pred2:.2f}
Сценарий 3 (рождаемость 30.0): прогноз смертности = {pred3:.2f}

7. ВЫВОДЫ

1. Наиболее сильное влияние на смертность оказывает {strongest}
2. Модель {'лучше' if mae < baseline_mae else 'не лучше'} простого прогноза средним
3. R2 = {r2:.3f} - {r2_text}

8. ИТОГОВОЕ ЗАКЛЮЧЕНИЕ

В ходе работы был выполнен полный цикл анализа данных и машинного обучения.

Модель {'показывает' if mae < baseline_mae else 'не показывает'} улучшение на {(baseline_mae - mae) / baseline_mae * 100:.1f}%.
Наиболее сильное влияние на смертность оказывает {strongest}.

Дата выполнения: 2026-08-29
Автор: Чувакова Я.А.
Блок: 5 - Excel и Python. AI-факультатив
'''

# Сохраняем отчёт
REPORTS_DIR = Path("reports")
REPORTS_DIR.mkdir(exist_ok=True)

report_path = REPORTS_DIR / "lesson_01_ai_beginner_report.md"
report_path.write_text(report_text, encoding="utf-8")

# Сохраняем дополнительные файлы
predictions_path = REPORTS_DIR / "lesson_01_ai_predictions.csv"
results_df.to_csv(predictions_path, index=False)

coef_path = REPORTS_DIR / "lesson_01_model_coefficients.csv"
coef_df.to_csv(coef_path, index=False)

# Печатаем отчёт
print(report_text)

print("\n" + "="*60)
print("✅ Отчёт сформирован.")
print("📁 Отчёт сохранён:", report_path)
print("📁 Прогнозы сохранены:", predictions_path)
print("📁 Коэффициенты сохранены:", coef_path)
print("="*60)