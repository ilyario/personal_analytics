import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.write("# Курс рубля и президентские выборы")

df_us = pd.read_excel("./ruble_analysis/data/us.xlsx")
df_ch = pd.read_excel("./ruble_analysis/data/ch.xlsx")
df_euro = pd.read_excel("./ruble_analysis/data/euro.xlsx")

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
    filtered_df_us = df_us[(df_us["data"] >= start_date) & (df_us["data"] <= end_date)]
    filtered_df_ch = df_ch[(df_ch["data"] >= start_date) & (df_ch["data"] <= end_date)]
    filtered_df_euro = df_euro[
        (df_euro["data"] >= start_date) & (df_euro["data"] <= end_date)
    ]

    # Построение графиков для каждой даты на соответствующем подграфике
    axs[i].plot(filtered_df_us["data"], filtered_df_us["curs"], label="Курс US")
    axs[i].plot(filtered_df_ch["data"], filtered_df_ch["curs"], label="Курс CH")
    axs[i].plot(filtered_df_euro["data"], filtered_df_euro["curs"], label="Курс EURO")
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
