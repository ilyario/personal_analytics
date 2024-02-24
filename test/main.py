import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Генерируем данные для графиков
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Создаем первый график
fig1, ax1 = plt.subplots()
ax1.plot(x, y1)
ax1.set_title("График синуса")

# Отображаем первый график в Streamlit
st.pyplot(fig1)

# Создаем второй график
fig2, ax2 = plt.subplots()
ax2.plot(x, y2)
ax2.set_title("График косинуса")

# Отображаем второй график в Streamlit
st.pyplot(fig2)
