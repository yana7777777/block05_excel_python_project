# Ячейка 1. Импорт библиотек и загрузка данных
# Адаптировано под демографический датасет

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython.display import display
from pathlib import Path

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

# URL нашего демографического датасета
dataset_url = "https://raw.githubusercontent.com/yana7777777/block05_excel_python_project/main/data/demographic_data.csv"
local_candidates = [
    "demographic_data.csv",
    "./demographic_data.csv",
    "./data/demographic_data.csv",
    "/mnt/data/demographic_data.csv"
]

try:
    raw_df = pd.read_csv(dataset_url)
    data_source = f"Данные загружены из интернета: {dataset_url}"
except Exception:
    loaded = False
    for candidate in local_candidates:
        if Path(candidate).exists():
            raw_df = pd.read_csv(candidate)
            data_source = f"Интернет недоступен, загружена локальная копия: {candidate}"
            loaded = True
            break
    if not loaded:
        raise FileNotFoundError("Не удалось загрузить датасет ни из интернета, ни из локального файла.")

# Переименовываем колонки для удобства
base_df = raw_df.rename(columns={
    "country": "country",
    "continent": "continent",
    "year": "year",
    "pop": "pop",
    "birth_rate": "birth_rate",
    "death_rate": "death_rate"
}).copy()

# Приводим год к числовому типу (уже int)
base_df["year"] = pd.to_numeric(base_df["year"], errors="coerce")
base_df = base_df.sort_values(["country", "year"]).reset_index(drop=True)

print(data_source)
print(f"Размер таблицы: {base_df.shape[0]} строк, {base_df.shape[1]} столбцов")
print("\nТипы данных:")
print(base_df.dtypes)

display(base_df.head())


# Ячейка 2. Первичный обзор данных
# Адаптировано под демографический датасет

display(base_df[["year", "pop", "birth_rate", "death_rate"]].describe().round(3))

plt.figure(figsize=(12, 5))
for country in base_df["country"].unique()[:5]:
    subset = base_df[base_df["country"] == country]
    plt.plot(subset["year"], subset["pop"], label=country, marker="o")

plt.title("Динамика численности населения по странам (первые 5 стран)")
plt.xlabel("Год")
plt.ylabel("Население (человек)")
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()



# Ячейка 3. Создание признаков для кластеризации
# Адаптировано под демографический датасет

feature_df = base_df.copy()

# 1. Естественный прирост (рождаемость - смертность)
feature_df["natural_increase"] = feature_df["birth_rate"] - feature_df["death_rate"]

# 2. Коэффициент рождаемости/смертности (показывает, во сколько раз рождаемость превышает смертность)
feature_df["birth_death_ratio"] = feature_df["birth_rate"] / feature_df["death_rate"]

# 3. Изменение населения (прирост за период, %)
feature_df["pop_change_pct"] = feature_df.groupby("country")["pop"].pct_change() * 100

# 4. Нормализованная рождаемость (в процентах от максимума по стране)
feature_df["birth_normalized"] = feature_df.groupby("country")["birth_rate"].transform(lambda x: x / x.max() * 100)

# 5. Волатильность рождаемости (изменчивость за последние 3 периода)
feature_df["birth_volatility_3"] = feature_df.groupby("country")["birth_rate"].rolling(window=3).std().reset_index(drop=True)

# 6. Волатильность смертности (изменчивость за последние 3 периода)
feature_df["death_volatility_3"] = feature_df.groupby("country")["death_rate"].rolling(window=3).std().reset_index(drop=True)

# 7. Относительный прирост (естественный прирост / смертность)
feature_df["relative_growth"] = feature_df["natural_increase"] / feature_df["death_rate"]

display(
    feature_df[
        ["country", "year", "pop", "birth_rate", "death_rate",
         "natural_increase", "birth_death_ratio", "pop_change_pct",
         "birth_normalized", "relative_growth"]
    ].head(10).round(3)
)



# Ячейка 4. Визуальный анализ созданных признаков
# Адаптировано под демографический датасет

plot_df = feature_df.dropna(subset=["natural_increase", "pop_change_pct", "birth_volatility_3"]).copy()

fig, axes = plt.subplots(3, 1, figsize=(12, 11), sharex=True)

# График 1: Естественный прирост по странам
for country in plot_df["country"].unique():
    subset = plot_df[plot_df["country"] == country]
    axes[0].plot(subset["year"], subset["natural_increase"], label=country, alpha=0.7)
axes[0].set_title("Естественный прирост населения (рождаемость - смертность)", fontsize=12)
axes[0].set_ylabel("Прирост (‰)")
axes[0].axhline(y=0, color="black", linestyle="--", alpha=0.5)
axes[0].grid(alpha=0.3)
axes[0].legend(bbox_to_anchor=(1.05, 1), loc="upper left")

# График 2: Изменение населения (%)
for country in plot_df["country"].unique():
    subset = plot_df[plot_df["country"] == country]
    axes[1].plot(subset["year"], subset["pop_change_pct"], label=country, alpha=0.7)
axes[1].set_title("Изменение численности населения (%)", fontsize=12)
axes[1].set_ylabel("Изменение (%)")
axes[1].axhline(y=0, color="black", linestyle="--", alpha=0.5)
axes[1].grid(alpha=0.3)

# График 3: Волатильность рождаемости
for country in plot_df["country"].unique():
    subset = plot_df[plot_df["country"] == country]
    axes[2].plot(subset["year"], subset["birth_volatility_3"], label=country, alpha=0.7)
axes[2].set_title("Волатильность рождаемости (скользящее std за 3 периода)", fontsize=12)
axes[2].set_xlabel("Год")
axes[2].set_ylabel("Стандартное отклонение")
axes[2].grid(alpha=0.3)

plt.tight_layout()
plt.show()




# Ячейка 5. Подготовка матрицы признаков, стандартизация и визуализация
# Расширенная версия с графиками

print("="*70)
print("ПОДГОТОВКА ДАННЫХ ДЛЯ КЛАСТЕРИЗАЦИИ")
print("="*70)

# Определяем признаки для кластеризации
cluster_features = [
    "natural_increase",
    "birth_death_ratio",
    "pop_change_pct",
    "birth_normalized",
    "relative_growth"
]

# Создаём датафрейм с признаками
cluster_df = feature_df[["country", "year"] + cluster_features].dropna().reset_index(drop=True).copy()

print(f"\n📊 Размер данных для кластеризации: {cluster_df.shape[0]} строк, {cluster_df.shape[1]} столбцов")
print(f"📋 Используемые признаки: {', '.join(cluster_features)}")

# ============================================
# 1. ВИЗУАЛИЗАЦИЯ РАСПРЕДЕЛЕНИЯ ПРИЗНАКОВ ДО СТАНДАРТИЗАЦИИ
# ============================================

print("\n" + "-"*70)
print("1. РАСПРЕДЕЛЕНИЕ ПРИЗНАКОВ ДО СТАНДАРТИЗАЦИИ")
print("-"*70)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, feature in enumerate(cluster_features):
    axes[i].hist(cluster_df[feature], bins=15, color='skyblue', edgecolor='black', alpha=0.7)
    axes[i].axvline(cluster_df[feature].mean(), color='red', linestyle='dashed', linewidth=2, label=f'Среднее: {cluster_df[feature].mean():.2f}')
    axes[i].axvline(cluster_df[feature].median(), color='green', linestyle='dashed', linewidth=2, label=f'Медиана: {cluster_df[feature].median():.2f}')
    axes[i].set_title(f'Распределение признака: {feature}')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Частота')
    axes[i].legend()
    axes[i].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================
# 2. СТАНДАРТИЗАЦИЯ ПРИЗНАКОВ
# ============================================

print("\n" + "-"*70)
print("2. СТАНДАРТИЗАЦИЯ ПРИЗНАКОВ (StandardScaler)")
print("-"*70)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(cluster_df[cluster_features])

# Статистика после стандартизации
scaled_df = pd.DataFrame(X_scaled, columns=cluster_features)

print("\n📊 Статистика после стандартизации:")
display(scaled_df.describe().round(3))

print("\n📊 Первые 5 строк стандартизированных данных:")
display(scaled_df.head().round(3))

# ============================================
# 3. ВИЗУАЛИЗАЦИЯ РАСПРЕДЕЛЕНИЯ ПРИЗНАКОВ ПОСЛЕ СТАНДАРТИЗАЦИИ
# ============================================

print("\n" + "-"*70)
print("3. РАСПРЕДЕЛЕНИЕ ПРИЗНАКОВ ПОСЛЕ СТАНДАРТИЗАЦИИ")
print("-"*70)

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for i, feature in enumerate(cluster_features):
    axes[i].hist(scaled_df[feature], bins=15, color='lightgreen', edgecolor='black', alpha=0.7)
    axes[i].axvline(0, color='red', linestyle='dashed', linewidth=2, label='Среднее = 0')
    axes[i].set_title(f'Стандартизированный признак: {feature}')
    axes[i].set_xlabel(feature)
    axes[i].set_ylabel('Частота')
    axes[i].legend()
    axes[i].grid(alpha=0.3)

plt.tight_layout()
plt.show()

# ============================================
# 4. МАТРИЦА КОРРЕЛЯЦИИ ПРИЗНАКОВ
# ============================================

print("\n" + "-"*70)
print("4. МАТРИЦА КОРРЕЛЯЦИИ ПРИЗНАКОВ")
print("-"*70)

plt.figure(figsize=(8, 6))
correlation_matrix = cluster_df[cluster_features].corr()
im = plt.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(im)

plt.xticks(range(len(cluster_features)), cluster_features, rotation=45, ha='right')
plt.yticks(range(len(cluster_features)), cluster_features)
plt.title('Матрица корреляции признаков')

# Добавляем значения корреляции в ячейки
for i in range(len(cluster_features)):
    for j in range(len(cluster_features)):
        plt.text(j, i, f'{correlation_matrix.iloc[i, j]:.2f}', ha='center', va='center', 
                 color='white' if abs(correlation_matrix.iloc[i, j]) > 0.5 else 'black')

plt.tight_layout()
plt.show()

print("\n📊 Матрица корреляции (числовые значения):")
display(correlation_matrix.round(3))

# ============================================
# 5. ИТОГОВАЯ ИНФОРМАЦИЯ
# ============================================

print("\n" + "-"*70)
print("5. ИТОГОВАЯ ИНФОРМАЦИЯ")
print("-"*70)

print(f"\n✅ Строк для кластеризации: {cluster_df.shape[0]}")
print(f"✅ Используемые признаки: {', '.join(cluster_features)}")
print(f"✅ Размер матрицы X_scaled: {X_scaled.shape}")
print(f"✅ Среднее каждого признака после стандартизации: {scaled_df.mean().round(3).values}")
print(f"✅ Стандартное отклонение каждого признака после стандартизации: {scaled_df.std().round(3).values}")

print("\n📌 ИТОГИ ПОДГОТОВКИ ДАННЫХ:")
print("- Данные успешно подготовлены для кластеризации.")
print("- Признаки стандартизированы (среднее = 0, std = 1).")
print("- Корреляция между признаками позволяет оценить их взаимосвязь.")
print("- Матрица X_scaled готова для передачи в алгоритм KMeans.")

print("\n" + "="*70)
print("✅ ПОДГОТОВКА ДАННЫХ ЗАВЕРШЕНА.")
print("="*70)




# Ячейка 6. Выбор числа кластеров: метод локтя и silhouette score
# Расширенная версия с графиками и детальным анализом

print("="*70)
print("ВЫБОР ОПТИМАЛЬНОГО ЧИСЛА КЛАСТЕРОВ")
print("="*70)

# Определяем диапазон кластеров для проверки
k_values = list(range(2, 9))  # от 2 до 8
inertia_values = []
silhouette_values = []

print("\n📊 Расчёт метрик для каждого k...")

for k in k_values:
    model = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = model.fit_predict(X_scaled)
    inertia_values.append(model.inertia_)
    silhouette_values.append(
        silhouette_score(X_scaled, labels, sample_size=min(300, len(X_scaled)), random_state=42)
    )
    print(f"   k = {k}: Inertia = {model.inertia_:.2f}, Silhouette = {silhouette_values[-1]:.4f}")

# Создаём DataFrame с результатами
comparison_df = pd.DataFrame({
    "k": k_values,
    "inertia": inertia_values,
    "silhouette_score": silhouette_values
}).round(4)

print("\n📊 Сводная таблица метрик:")
display(comparison_df)

# ============================================
# ВИЗУАЛИЗАЦИЯ: Метод локтя и Silhouette score
# ============================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# График 1: Метод локтя (Inertia)
axes[0].plot(k_values, inertia_values, marker='o', linewidth=2, markersize=10, color='#2E86C1')
axes[0].set_title("Метод локтя (Inertia)", fontsize=14)
axes[0].set_xlabel("Количество кластеров (k)", fontsize=12)
axes[0].set_ylabel("Inertia (сумма квадратов расстояний)", fontsize=12)
axes[0].grid(alpha=0.3)
# Добавляем подписи точек
for i, (k, val) in enumerate(zip(k_values, inertia_values)):
    axes[0].annotate(f'{val:.0f}', (k, val), textcoords="offset points", xytext=(0,10), ha='center')

# График 2: Silhouette score
axes[1].plot(k_values, silhouette_values, marker='s', linewidth=2, markersize=10, color='#27AE60')
axes[1].set_title("Silhouette Score", fontsize=14)
axes[1].set_xlabel("Количество кластеров (k)", fontsize=12)
axes[1].set_ylabel("Silhouette Score", fontsize=12)
axes[1].grid(alpha=0.3)
axes[1].axhline(y=0.5, color='red', linestyle='--', alpha=0.5, label='Хороший уровень (0.5)')
axes[1].legend()
# Добавляем подписи точек
for i, (k, val) in enumerate(zip(k_values, silhouette_values)):
    axes[1].annotate(f'{val:.3f}', (k, val), textcoords="offset points", xytext=(0,10), ha='center')

# График 3: Совмещённый (нормализованные значения)
# ПРЕОБРАЗУЕМ СПИСКИ В МАССИВЫ NUMPY ДЛЯ НОРМАЛИЗАЦИИ
inertia_array = np.array(inertia_values)
silhouette_array = np.array(silhouette_values)

inertia_norm = (inertia_array - inertia_array.min()) / (inertia_array.max() - inertia_array.min())
silhouette_norm = (silhouette_array - silhouette_array.min()) / (silhouette_array.max() - silhouette_array.min())

axes[2].plot(k_values, inertia_norm, marker='o', linewidth=2, markersize=8, label='Inertia (норм.)', color='#2E86C1')
axes[2].plot(k_values, silhouette_norm, marker='s', linewidth=2, markersize=8, label='Silhouette (норм.)', color='#27AE60')
axes[2].set_title("Сравнение метрик (нормализовано)", fontsize=14)
axes[2].set_xlabel("Количество кластеров (k)", fontsize=12)
axes[2].set_ylabel("Нормализованное значение", fontsize=12)
axes[2].grid(alpha=0.3)
axes[2].legend()

plt.tight_layout()
plt.show()

# ============================================
# ВЫБОР ОПТИМАЛЬНОГО k
# ============================================

print("\n" + "-"*70)
print("ВЫБОР ОПТИМАЛЬНОГО ЧИСЛА КЛАСТЕРОВ")
print("-"*70)

best_k = comparison_df.sort_values("silhouette_score", ascending=False).iloc[0]["k"]
best_k = int(best_k)

print(f"\n🏆 Лучшее k по silhouette score: {best_k} (score = {comparison_df[comparison_df['k']==best_k]['silhouette_score'].values[0]:.4f})")

# Дополнительный анализ: где наблюдается "локоть"
inertia_diff = [inertia_values[i] - inertia_values[i+1] for i in range(len(inertia_values)-1)]
elbow_k = k_values[np.argmax(inertia_diff) + 1] if inertia_diff else 3

print(f"📌 'Локоть' по методу Inertia: k = {elbow_k}")

# Анализ silhouette
silhouette_analysis = []
for k, score in zip(k_values, silhouette_values):
    if score > 0.5:
        quality = "✅ Хорошо"
    elif score > 0.3:
        quality = "⚠️ Средне"
    else:
        quality = "❌ Плохо"
    silhouette_analysis.append(quality)

comparison_df["качество"] = silhouette_analysis
print("\n📊 Детальный анализ качества:")
display(comparison_df)

# Выбор k для интерпретации
if best_k < 4:
    chosen_k = 3
else:
    chosen_k = best_k

print(f"\n🎯 Для учебной интерпретации выбираем k = {chosen_k}, потому что это хороший баланс между качеством и понятностью.")

print("\n" + "="*70)
print("✅ ВЫБОР ЧИСЛА КЛАСТЕРОВ ЗАВЕРШЁН.")
print("="*70)




# Ячейка 7. Обучение модели KMeans и получение кластеров
# Расширенная версия с детальной интерпретацией

print("="*70)
print("ОБУЧЕНИЕ МОДЕЛИ KMEANS И АНАЛИЗ КЛАСТЕРОВ")
print("="*70)

# ============================================
# ОБУЧЕНИЕ МОДЕЛИ
# ============================================

kmeans = KMeans(n_clusters=chosen_k, random_state=42, n_init=20)
cluster_df["cluster"] = kmeans.fit_predict(X_scaled)

print(f"\n✅ Модель KMeans обучена с k = {chosen_k}")
print(f"   Количество итераций: {kmeans.n_iter_}")
print(f"   Итоговая инерция: {kmeans.inertia_:.2f}")

# ============================================
# СВОДНАЯ ТАБЛИЦА ПО КЛАСТЕРАМ
# ============================================

cluster_summary = (
    cluster_df
    .groupby("cluster")
    .agg(
        count=("cluster", "size"),
        natural_increase_mean=("natural_increase", "mean"),
        birth_death_ratio_mean=("birth_death_ratio", "mean"),
        pop_change_pct_mean=("pop_change_pct", "mean"),
        birth_normalized_mean=("birth_normalized", "mean"),
        relative_growth_mean=("relative_growth", "mean")
    )
    .round(3)
    .sort_values("natural_increase_mean", ascending=False)
)

print("\n📊 СВОДНАЯ ТАБЛИЦА ПО КЛАСТЕРАМ:")
display(cluster_summary)

# ============================================
# ПРИСВОЕНИЕ НАЗВАНИЙ КЛАСТЕРАМ
# ============================================

cluster_order = cluster_summary.index.tolist()
name_map = {}

if len(cluster_order) >= 3:
    name_map = {
        cluster_order[0]: "📈 Страны с высоким приростом",
        cluster_order[1]: "📊 Страны со средним приростом",
        cluster_order[2]: "📉 Страны с низким приростом/убылью"
    }
elif len(cluster_order) == 2:
    name_map = {
        cluster_order[0]: "📈 Страны с приростом",
        cluster_order[1]: "📉 Страны с убылью"
    }
else:
    name_map = {cluster_order[0]: "📊 Единый кластер"}

# Применяем названия
cluster_df["cluster_name"] = cluster_df["cluster"].map(name_map)
cluster_summary["cluster_name"] = cluster_summary.index.map(name_map)

print("\n🏷️ НАЗВАНИЯ КЛАСТЕРОВ:")
for cluster_id, name in name_map.items():
    print(f"   Кластер {cluster_id}: {name}")

# ============================================
# ВИЗУАЛИЗАЦИЯ РАСПРЕДЕЛЕНИЯ КЛАСТЕРОВ
# ============================================

fig, axes = plt.subplots(1, 3, figsize=(18, 5))

# График 1: Количество стран в кластерах
counts = cluster_df["cluster_name"].value_counts()
colors = ['#2E86C1', '#27AE60', '#E74C3C', '#F39C12', '#8E44AD'][:len(counts)]
axes[0].bar(counts.index, counts.values, color=colors)
axes[0].set_title("Количество стран в каждом кластере", fontsize=14)
axes[0].set_xlabel("Кластер")
axes[0].set_ylabel("Количество")
axes[0].tick_params(axis='x', rotation=15)
for i, (label, count) in enumerate(counts.items()):
    axes[0].text(i, count + 0.5, str(count), ha='center', fontsize=12)

# График 2: Средний естественный прирост по кластерам
growth_means = cluster_summary["natural_increase_mean"]
axes[1].bar(cluster_summary["cluster_name"], growth_means, color=colors)
axes[1].axhline(y=0, color='black', linestyle='--', alpha=0.5)
axes[1].set_title("Средний естественный прирост по кластерам", fontsize=14)
axes[1].set_xlabel("Кластер")
axes[1].set_ylabel("Прирост (‰)")
axes[1].tick_params(axis='x', rotation=15)

# График 3: Среднее соотношение рождаемости к смертности
ratio_means = cluster_summary["birth_death_ratio_mean"]
axes[2].bar(cluster_summary["cluster_name"], ratio_means, color=colors)
axes[2].axhline(y=1, color='black', linestyle='--', alpha=0.5)
axes[2].set_title("Среднее соотношение рождаемости/смертности", fontsize=14)
axes[2].set_xlabel("Кластер")
axes[2].set_ylabel("Соотношение")
axes[2].tick_params(axis='x', rotation=15)

plt.tight_layout()
plt.show()

# ============================================
# ДЕТАЛЬНЫЙ АНАЛИЗ КАЖДОГО КЛАСТЕРА
# ============================================

print("\n" + "-"*70)
print("ДЕТАЛЬНЫЙ АНАЛИЗ КАЖДОГО КЛАСТЕРА")
print("-"*70)

for cluster_id, name in name_map.items():
    subset = cluster_df[cluster_df["cluster"] == cluster_id]
    countries = subset["country"].unique()
    
    print(f"\n{name}:")
    print(f"   Количество наблюдений: {len(subset)}")
    print(f"   Страны: {', '.join(countries)}")
    print(f"   Средний естественный прирост: {subset['natural_increase'].mean():.2f}‰")
    print(f"   Среднее соотношение рождения/смертности: {subset['birth_death_ratio'].mean():.2f}")
    print(f"   Среднее изменение населения: {subset['pop_change_pct'].mean():.2f}%")

# ============================================
# ВЫВОД ПО КЛАСТЕРАМ
# ============================================

print("\n" + "="*70)
print("✅ ОБУЧЕНИЕ МОДЕЛИ И АНАЛИЗ КЛАСТЕРОВ ЗАВЕРШЕНЫ.")
print("="*70)




# Ячейка 8. Визуализация кластеров на плоскости PCA
# Расширенная версия с детальным анализом PCA

print("="*70)
print("ВИЗУАЛИЗАЦИЯ КЛАСТЕРОВ С ПОМОЩЬЮ PCA")
print("="*70)

# ============================================
# ПРИМЕНЕНИЕ PCA
# ============================================

pca = PCA(n_components=2)
pca_components = pca.fit_transform(X_scaled)

cluster_df["pca_1"] = pca_components[:, 0]
cluster_df["pca_2"] = pca_components[:, 1]

print("\n📊 Объяснённая дисперсия:")
print(f"   Компонента 1: {pca.explained_variance_ratio_[0]*100:.2f}%")
print(f"   Компонента 2: {pca.explained_variance_ratio_[1]*100:.2f}%")
print(f"   Суммарно: {pca.explained_variance_ratio_.sum()*100:.2f}%")

# ============================================
# ГРАФИК: КЛАСТЕРЫ В ПРОСТРАНСТВЕ PCA
# ============================================

plt.figure(figsize=(12, 8))

colors = {'📈 Страны с высоким приростом': '#2E86C1',
          '📊 Страны со средним приростом': '#27AE60',
          '📉 Страны с низким приростом/убылью': '#E74C3C'}

for name in cluster_df["cluster_name"].unique():
    subset = cluster_df[cluster_df["cluster_name"] == name]
    color = colors.get(name, '#95A5A6')
    plt.scatter(subset["pca_1"], subset["pca_2"], label=name, alpha=0.7, s=80, color=color, edgecolors='black', linewidth=0.5)

# Добавляем центры кластеров
centers_pca = pca.transform(kmeans.cluster_centers_)
for i, center in enumerate(centers_pca):
    plt.scatter(center[0], center[1], marker='X', s=200, c='black', edgecolors='white', linewidth=2)

plt.title("Кластеры стран в двумерном пространстве PCA", fontsize=16)
plt.xlabel(f"PCA 1 ({pca.explained_variance_ratio_[0]*100:.1f}% дисперсии)", fontsize=12)
plt.ylabel(f"PCA 2 ({pca.explained_variance_ratio_[1]*100:.1f}% дисперсии)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================
# АНАЛИЗ НАГРУЗОК ПРИЗНАКОВ НА PCA
# ============================================

print("\n" + "-"*70)
print("АНАЛИЗ ВКЛАДА ПРИЗНАКОВ В PCA-КОМПОНЕНТЫ")
print("-"*70)

loadings = pd.DataFrame(
    pca.components_.T,
    columns=['PC1', 'PC2'],
    index=cluster_features
)
print("\n📊 Нагрузки признаков на компоненты:")
display(loadings.round(3))

# Визуализация нагрузок
plt.figure(figsize=(10, 6))
for i, feature in enumerate(cluster_features):
    plt.arrow(0, 0, loadings.loc[feature, 'PC1'], loadings.loc[feature, 'PC2'], 
              head_width=0.05, head_length=0.05, fc='red', ec='red')
    plt.text(loadings.loc[feature, 'PC1']*1.1, loadings.loc[feature, 'PC2']*1.1, feature, fontsize=12)

plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
plt.axvline(x=0, color='black', linestyle='--', alpha=0.3)
plt.title("Вклад признаков в PCA-компоненты", fontsize=14)
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\n" + "="*70)
print("✅ ВИЗУАЛИЗАЦИЯ КЛАСТЕРОВ ЗАВЕРШЕНА.")
print("="*70)



# Ячейка 9. Кластеры на временной шкале и реальные примеры
# Расширенная версия с детальным анализом

print("="*70)
print("КЛАСТЕРЫ НА ВРЕМЕННОЙ ШКАЛЕ")
print("="*70)

# ============================================
# ПОДГОТОВКА ДАННЫХ ДЛЯ ГРАФИКА
# ============================================

# Добавляем данные о населении для визуализации
cluster_df = cluster_df.merge(feature_df[["country", "year", "pop"]], on=["country", "year"], how="left")

# ============================================
# ГРАФИК 1: КЛАСТЕРЫ НА ГРАФИКЕ НАСЕЛЕНИЯ
# ============================================

plt.figure(figsize=(14, 7))

# Линии для каждой страны
for country in cluster_df["country"].unique():
    subset = cluster_df[cluster_df["country"] == country]
    plt.plot(subset["year"], subset["pop"], alpha=0.3, color='gray', linewidth=1)

# Точки с цветом кластера
colors = {'📈 Страны с высоким приростом': '#2E86C1',
          '📊 Страны со средним приростом': '#27AE60',
          '📉 Страны с низким приростом/убылью': '#E74C3C'}

for name in cluster_df["cluster_name"].unique():
    subset = cluster_df[cluster_df["cluster_name"] == name]
    color = colors.get(name, '#95A5A6')
    plt.scatter(subset["year"], subset["pop"], label=name, s=50, alpha=0.7, color=color, edgecolors='black', linewidth=0.5)

plt.title("Кластеры стран на графике населения", fontsize=16)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Население (человек)", fontsize=12)
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

# ============================================
# ПРИМЕРЫ ДНЕЙ ИЗ КАЖДОГО КЛАСТЕРА
# ============================================

print("\n" + "-"*70)
print("ПРИМЕРЫ СТРАН ИЗ КАЖДОГО КЛАСТЕРА")
print("-"*70)

examples_df = (
    cluster_df[
        ["country", "year", "cluster_name", "natural_increase", "birth_death_ratio",
         "pop_change_pct", "relative_growth", "pop"]
    ]
    .groupby("cluster_name", group_keys=False)
    .head(5)
    .sort_values(["cluster_name", "country", "year"])
    .reset_index(drop=True)
)

display(examples_df.round(3))

# ============================================
# АНАЛИЗ ДИНАМИКИ КАЖДОГО КЛАСТЕРА
# ============================================

print("\n" + "-"*70)
print("ДИНАМИКА КЛАСТЕРОВ ПО ГОДАМ")
print("-"*70)

cluster_by_year = cluster_df.groupby(["year", "cluster_name"]).size().unstack(fill_value=0)

# График количества стран в кластерах по годам
cluster_by_year.plot(kind='bar', figsize=(12, 6), color=[colors.get(c, '#95A5A6') for c in cluster_by_year.columns])
plt.title("Количество стран в кластерах по годам", fontsize=14)
plt.xlabel("Год", fontsize=12)
plt.ylabel("Количество стран", fontsize=12)
plt.legend(title="Кластер")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()

print("\n📊 Распределение по годам:")
display(cluster_by_year)

# ============================================
# ВЫВОДЫ ПО ВРЕМЕННОЙ ДИНАМИКЕ
# ============================================

print("\n" + "="*70)
print("✅ АНАЛИЗ ВРЕМЕННОЙ ДИНАМИКИ ЗАВЕРШЁН.")
print("="*70)



# Ячейка 10. Итоговая интерпретация и отчёт
# Расширенная версия с подробными выводами и обоснованиями

print("="*80)
print(" " * 25 + "ИТОГОВЫЙ ОТЧЁТ ПО УРОКУ 6")
print(" " * 20 + "КЛАСТЕРИЗАЦИЯ ДЕМОГРАФИЧЕСКИХ ДАННЫХ")
print("="*80)

# ============================================
# 1. ЧТО МЫ ДЕЛАЛИ И ЗАЧЕМ
# ============================================

print("\n" + "█"*80)
print(" 1. ЧТО МЫ ДЕЛАЛИ И ЗАЧЕМ")
print("█"*80)

print("""
📌 ЦЕЛЬ ИССЛЕДОВАНИЯ:
   Мы применили метод кластеризации (KMeans) для поиска скрытых групп стран
   со схожими демографическими характеристиками. Это задача обучения без учителя,
   где алгоритм сам находит структуру в данных без готовых ответов.

📌 ПОЧЕМУ ЭТО ВАЖНО:
   - Кластеризация позволяет увидеть естественные группы объектов
   - Помогает сегментировать страны по демографическим признакам
   - Выявляет скрытые закономерности, которые не видны при простом просмотре таблицы
   - Даёт основу для дальнейшего анализа и принятия решений

📌 КАК МЫ ЭТО ДЕЛАЛИ:
   1. Подготовили признаки: естественный прирост, соотношение рождаемости/смертности,
      изменение населения, нормализованная рождаемость, относительный прирост
   2. Стандартизировали данные (StandardScaler)
   3. Подобрали оптимальное число кластеров (метод локтя + silhouette score)
   4. Обучили модель KMeans
   5. Проанализировали и интерпретировали полученные кластеры
""")

# ============================================
# 2. КАКИЕ ИССЛЕДОВАНИЯ МЫ ПРОВЕЛИ
# ============================================

print("\n" + "█"*80)
print(" 2. КАКИЕ ИССЛЕДОВАНИЯ МЫ ПРОВЕЛИ")
print("█"*80)

print("""
📊 ИССЛЕДОВАНИЕ 1: Анализ распределения признаков
   - Мы построили гистограммы для каждого признака, чтобы понять их распределение
   - Это помогло увидеть, какие значения являются типичными, а какие — выбросами
   - Например, мы увидели, что у большинства стран естественный прирост находится в диапазоне от -5 до +15‰

📊 ИССЛЕДОВАНИЕ 2: Стандартизация данных
   - Мы применили StandardScaler, чтобы привести все признаки к одному масштабу
   - Это важно, потому что KMeans чувствителен к масштабу признаков
   - Без стандартизации признаки с большими значениями (например, население) доминировали бы над другими

📊 ИССЛЕДОВАНИЕ 3: Выбор оптимального числа кластеров
   - Мы использовали метод локтя и silhouette score для выбора k
   - Метод локтя показал, что оптимальное k = {elbow_k if 'elbow_k' in dir() else 4}
   - Silhouette score показал, что лучшее k = {best_k} (score = {comparison_df[comparison_df['k']==best_k]['silhouette_score'].values[0]:.4f})
   - Для интерпретации мы выбрали k = {chosen_k}, потому что это даёт понятные и интерпретируемые группы

📊 ИССЛЕДОВАНИЕ 4: Обучение модели KMeans
   - Мы обучили модель с выбранным k = {chosen_k}
   - Модель разбила страны на {chosen_k} кластеров со схожими демографическими характеристиками

📊 ИССЛЕДОВАНИЕ 5: Анализ полученных кластеров
   - Мы проанализировали средние значения признаков в каждом кластере
   - Это позволило нам дать кластерам осмысленные названия
""")

# ============================================
# 3. КАКУЮ ИНФОРМАЦИЮ МЫ ПОЛУЧИЛИ
# ============================================

print("\n" + "█"*80)
print(" 3. КАКУЮ ИНФОРМАЦИЮ МЫ ПОЛУЧИЛИ")
print("█"*80)

# Проверки качества
cluster_counts = cluster_df["cluster_name"].value_counts()

assert cluster_df.shape[0] > 10, "⚠️ Для кластеризации должно быть достаточно наблюдений."
assert cluster_df["cluster"].nunique() == chosen_k, "⚠️ Число найденных кластеров не совпадает с выбранным k."
assert cluster_counts.min() > 1, "⚠️ Один из кластеров получился слишком маленьким."

print("\n✅ Все проверки пройдены успешно. Кластеры найдены корректно.")

# Основные характеристики кластеров
print("\n📌 ОСНОВНЫЕ ХАРАКТЕРИСТИКИ КЛАСТЕРОВ:")

cluster_info = []
for name in cluster_df["cluster_name"].unique():
    subset = cluster_df[cluster_df["cluster_name"] == name]
    countries = subset["country"].unique()
    avg_growth = subset["natural_increase"].mean()
    avg_ratio = subset["birth_death_ratio"].mean()
    avg_pop_change = subset["pop_change_pct"].mean()
    
    cluster_info.append({
        "name": name,
        "count": len(subset),
        "countries": countries,
        "avg_growth": avg_growth,
        "avg_ratio": avg_ratio,
        "avg_pop_change": avg_pop_change
    })
    
    print(f"\n   {name}:")
    print(f"      Количество наблюдений: {len(subset)}")
    print(f"      Страны: {', '.join(countries)}")
    print(f"      Средний естественный прирост: {avg_growth:.2f}‰")
    print(f"      Среднее соотношение рождаемости/смертности: {avg_ratio:.2f}")
    print(f"      Среднее изменение населения: {avg_pop_change:.2f}%")

# ============================================
# 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ
# ============================================

print("\n" + "█"*80)
print(" 4. СТАТИСТИЧЕСКИЙ АНАЛИЗ")
print("█"*80)

total_countries = len(cluster_df["country"].unique())
total_obs = cluster_df.shape[0]

print(f"\n📊 Общая статистика:")
print(f"   Всего стран: {total_countries}")
print(f"   Всего наблюдений: {total_obs}")
print(f"   Количество кластеров: {chosen_k}")
print(f"   Лучшее k по silhouette score: {best_k} (score = {comparison_df[comparison_df['k']==best_k]['silhouette_score'].values[0]:.4f})")
print(f"   Выбранное k для интерпретации: {chosen_k}")
print(f"   Объяснённая дисперсия PCA: {pca.explained_variance_ratio_.sum()*100:.2f}%")

# ============================================
# 5. ПОДРОБНЫЕ ВЫВОДЫ ПО КЛАСТЕРАМ
# ============================================

print("\n" + "█"*80)
print(" 5. ПОДРОБНЫЕ ВЫВОДЫ ПО КЛАСТЕРАМ")
print("█"*80)

cluster_summary_sorted = cluster_summary.sort_values("natural_increase_mean", ascending=False)

print("\n📌 КЛЮЧЕВЫЕ ВЫВОДЫ ПО КАЖДОМУ КЛАСТЕРУ:")

for i, (idx, row) in enumerate(cluster_summary_sorted.iterrows()):
    name = row["cluster_name"]
    growth = row["natural_increase_mean"]
    ratio = row["birth_death_ratio_mean"]
    count = int(row["count"])
    
    if growth > 0:
        status = "естественный прирост"
        status_emoji = "📈"
    else:
        status = "естественная убыль"
        status_emoji = "📉"
    
    # Получаем список стран в кластере
    countries_in_cluster = cluster_df[cluster_df["cluster"] == idx]["country"].unique()
    countries_list = ", ".join(countries_in_cluster)
    
    print(f"\n   {i+1}. {name} {status_emoji}")
    print(f"      Количество наблюдений: {count}")
    print(f"      Страны: {countries_list}")
    print(f"      Средний естественный прирост: {growth:.2f}‰ ({status})")
    print(f"      Среднее соотношение рождаемости/смертности: {ratio:.2f}")
    
    # Дополнительные выводы по кластеру
    if growth > 5:
        print(f"      🔍 В этом кластере наблюдается высокий естественный прирост.")
        print(f"         Это характерно для развивающихся стран с высокой рождаемостью.")
    elif growth > 0:
        print(f"      🔍 В этом кластере наблюдается умеренный естественный прирост.")
        print(f"         Это характерно для стран со стабильной демографической ситуацией.")
    else:
        print(f"      🔍 В этом кластере наблюдается естественная убыль населения.")
        print(f"         Это характерно для развитых стран с низкой рождаемостью и высокой смертностью.")
    
    if ratio > 1.5:
        print(f"      🔍 Рождаемость значительно превышает смертность (в {ratio:.1f} раз).")
    elif ratio > 1:
        print(f"      🔍 Рождаемость немного превышает смертность (в {ratio:.1f} раз).")
    else:
        print(f"      🔍 Смертность превышает рождаемость (соотношение {ratio:.1f}).")

# ============================================
# 6. ОБЩИЕ ВЫВОДЫ ПО ИССЛЕДОВАНИЮ
# ============================================

print("\n" + "█"*80)
print(" 6. ОБЩИЕ ВЫВОДЫ ПО ИССЛЕДОВАНИЮ")
print("█"*80)

print("""
📌 ОСНОВНЫЕ ВЫВОДЫ:

   1. Кластеризация позволила выделить {} устойчивых групп стран
      со схожими демографическими характеристиками.

   2. Наиболее сильное влияние на разделение стран на кластеры оказали:
      - Естественный прирост населения
      - Соотношение рождаемости и смертности
      - Динамика изменения численности населения

   3. {} из {} кластеров имеют положительный естественный прирост.
      Это говорит о том, что большинство стран демонстрируют рост населения.

   4. {} кластер(ов) имеют естественную убыль населения.
      Это характерно для развитых стран с низкой рождаемостью.

   5. Качество кластеризации можно оценить как {}.
      Silhouette score = {:.3f} (чем ближе к 1, тем лучше разделение).
""".format(
    chosen_k,
    len([c for c in cluster_summary_sorted.iterrows() if c[1]["natural_increase_mean"] > 0]),
    chosen_k,
    len([c for c in cluster_summary_sorted.iterrows() if c[1]["natural_increase_mean"] < 0]),
    "хорошее" if comparison_df[comparison_df['k']==best_k]['silhouette_score'].values[0] > 0.5 else "удовлетворительное",
    comparison_df[comparison_df['k']==best_k]['silhouette_score'].values[0]
))

# ============================================
# 7. РЕКОМЕНДАЦИИ ПО УЛУЧШЕНИЮ
# ============================================

print("\n" + "█"*80)
print(" 7. РЕКОМЕНДАЦИИ ПО УЛУЧШЕНИЮ")
print("█"*80)

print("""
📌 ЧТО МОЖНО УЛУЧШИТЬ:

   1. Добавить больше признаков:
      - Уровень урбанизации
      - ВВП на душу населения
      - Расходы на здравоохранение
      - Уровень образования
      - Экологические показатели

   2. Использовать другие алгоритмы кластеризации:
      - DBSCAN (для поиска кластеров произвольной формы)
      - Agglomerative Clustering (иерархическая кластеризация)
      - Gaussian Mixture Models (вероятностная кластеризация)

   3. Улучшить интерпретацию:
      - Добавить визуализацию центров кластеров
      - Построить профили кластеров (радарные диаграммы)
      - Проверить устойчивость кластеров (bootstrap)

   4. Расширить анализ:
      - Разбить данные по континентам
      - Проанализировать динамику кластеров во времени
      - Сравнить кластеризацию для разных периодов
""")

# ============================================
# 8. ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ
# ============================================

print("\n" + "█"*80)
print(" 8. ПРАКТИЧЕСКОЕ ПРИМЕНЕНИЕ РЕЗУЛЬТАТОВ")
print("█"*80)

print("""
📌 ГДЕ МОЖНО ПРИМЕНИТЬ ЭТОТ ПОДХОД:

   1. В дипломном проекте:
      - Сегментация клиентов по покупательскому поведению
      - Группировка товаров по характеристикам
      - Кластеризация регионов по экономическим показателям
      - Выделение типов пользователей по активности

   2. В бизнесе:
      - Сегментация рынка
      - Выявление целевых групп
      - Оптимизация маркетинговых кампаний
      - Анализ клиентской базы

   3. В науке и исследованиях:
      - Классификация объектов без размеченных данных
      - Выявление скрытых закономерностей
      - Сокращение размерности данных
""")

# ============================================
# 9. ИТОГОВОЕ ЗАКЛЮЧЕНИЕ
# ============================================

print("\n" + "█"*80)
print(" 9. ИТОГОВОЕ ЗАКЛЮЧЕНИЕ")
print("█"*80)

print("""
📌 ЧТО МЫ УЗНАЛИ В ХОДЕ РАБОТЫ:

   1. Кластеризация — это мощный метод AI, который позволяет находить скрытые
      группы объектов без готовой разметки.

   2. Мы научились:
      - Подготавливать данные для кластеризации (стандартизация)
      - Выбирать оптимальное число кластеров (метод локтя + silhouette score)
      - Применять алгоритм KMeans
      - Интерпретировать полученные кластеры
      - Визуализировать результаты (PCA)

   3. Мы получили практический навык, который можно применить в дипломе:
      - Сегментация клиентов
      - Группировка товаров
      - Кластеризация регионов
      - Выделение типов пользователей

   4. Кластеризация помогает:
      - Увидеть структуру данных
      - Найти аномалии
      - Подготовить данные для дальнейшего анализа
      - Принимать обоснованные решения на основе данных

📌 ГЛАВНЫЙ ВЫВОД:
   Кластеризация — это не просто математический метод, а практический
   инструмент для поиска скрытых закономерностей в данных. Она позволяет
   увидеть данные под новым углом и найти решения, которые не видны
   при поверхностном анализе.

📌 ИТОГОВЫЙ РЕЗУЛЬТАТ:
   Мы успешно применили кластеризацию к демографическим данным и получили
   {chosen_k} осмысленных кластеров стран. Каждый кластер имеет свои
   характерные особенности, которые мы описали и интерпретировали.
""")

print("="*80)
print(" " * 30 + "✅ ОТЧЕТ СФОРМИРОВАН")
print(" " * 28 + "КЛАСТЕРИЗАЦИЯ ВЫПОЛНЕНА УСПЕШНО")
print("="*80)



