import pandas as pd
import plotly.express as px
import streamlit as st

# Leer los datos
car_data = pd.read_csv('vehicles_us.csv')

# Título de la aplicación
st.header('Análisis de datos de vehículos usados')

# Crear un botón para mostrar histograma
hist_button = st.button('Construir histograma')

# Si se hace clic en el botón
if hist_button:
    # Escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un histograma
    fig = px.histogram(car_data, x="odometer")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Crear un botón para mostrar gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')

# Si se hace clic en el botón
if scatter_button:
    # Escribir un mensaje
    st.write('Creación de un gráfico de dispersión para odómetro vs precio')
    
    # Crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
