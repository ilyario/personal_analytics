import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.write("# Курс рубля от событий")

currency = st.selectbox("Валюта", ["us", "ch", "euro"])

df = pd.read_excel(f"./ruble_analysis/data/{currency}.xlsx")

# Выбранные даты
selected_dates = [
    datetime(1996, 7, 3),
    datetime(2000, 3, 26),
    datetime(2004, 3, 24),
    datetime(2008, 4, 2),
    datetime(2012, 3, 4),
    datetime(2016, 3, 18),
]

# Определение интервала
interval_days = st.selectbox("Интервала до/после выборов?", (14, 30, 90, 180))

# Создание фигуры с подграфиками
fig, axs = plt.subplots(len(selected_dates), 1, figsize=(10, 6 * len(selected_dates)))

# Построение графиков для каждой даты
for i, date in enumerate(selected_dates):
    start_date = date - timedelta(days=interval_days)
    end_date = date + timedelta(days=interval_days)

    # Фильтрация данных по дате
    filtered_df = df[(df["data"] >= start_date) & (df["data"] <= end_date)]

    # Построение графиков для каждой даты на соответствующем подграфике
    axs[i].plot(filtered_df["data"], filtered_df["curs"], label=f"Курс {currency}")
    axs[i].axvline(x=date, color="r", linestyle="--", label=date.strftime("%d.%m.%Y"))

    axs[i].set_xlabel("Дата")
    axs[i].set_ylabel("Курс")
    axs[i].set_title(
        f'Графики курса пределах +/- {interval_days} дней от выборов презедента РФ {date.strftime("%d.%m.%Y")}'
    )
    axs[i].legend()
    axs[i].grid(True)
    axs[i].tick_params(axis="x", rotation=45)  # Поворот меток по оси X на 45 градусов

plt.tight_layout()

# Отображение графиков в Streamlit
st.pyplot()
