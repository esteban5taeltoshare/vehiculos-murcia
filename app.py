"""
app.py

Este archivo realiza un Análisis Exploratorio de Datos (EDA) sobre anuncios de vehículos usando Streamlit para la visualización interactiva.

Funcionalidades:
- Carga datos desde un archivo CSV.
- Muestra histogramas y gráficos de dispersión para variables relevantes.
"""

import streamlit as st  # Importa la librería Streamlit para crear la interfaz web interactiva
import pandas as pd  # Importa pandas para manipulación de datos
import plotly.express as px  # Importa plotly.express para crear gráficos interactivos

data = pd.read_csv("vehicles_us.csv")  # Lee el archivo CSV y lo almacena en un DataFrame

st.header("EDA de los anuncios de coches 🚗")  # Agrega un título principal a la app

fig = px.histogram(data, x="odometer")  # Genera el histograma del kilometraje
st.plotly_chart(fig)  # Muestra el histograma en la interfaz

fig2 = px.scatter(data, x="odometer", y="price")  # Genera el gráfico de dispersión entre kilometraje y precio
st.plotly_chart(fig2)  # Muestra el gráfico de dispersión en la interfaz