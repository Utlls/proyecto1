import streamlit as st
import pandas as pd
import plotly.express as px
import os
# print("Directorio de trabajo actual:", os.getcwd())

car_data = pd.read_csv("data/vehicles_us.csv")

st.title("EL MERCADO DE AUTOS USADOS Y SUS TENDENCIAS")

st.header("Breve explicación del Mercado de Autos:")

st.write("La compra de un automovil esta motivada por diversas razones, entre ellas estan:")

st.write("Productivos: Ya sean carros de carga o transporte, involucrados en las diversas áreas de la producción, su valor tiende a ser depreciado a lo largo de 10 años, \n para recuperar algo de lo invertido la empresa vende al mercado el valor residual. ")

st.write("Personales: Este abarca la selección del vehiculo, para su uso individual motivado por la movilidad, en este sector de uso se ve influenciado por gustos, presupuesto y situación, \n se pueden encontrar carros que tienen  apenas 1 años de aver salido así como carros clasicos, que a pesar de la tendencia natural de bajar suvalor con el paso del tiempo estos lo mantienen y hasta lo elevan")

st.subheader(
    "Histograma: Comportamiento de los precios en el mercado de autos usados.")

st.write("Muestra la concentración de los precios, y la distribucción")

hist_checkbox = st.checkbox('Construir histograma')  # crear un botón

if hist_checkbox:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Dispersión: Precios en el mercado de autos usados.")

st.write("Muestra la concentración de los precios, y la distribucción")

sca_checkbox = st.checkbox('Construir histograma')  # crear un botón

if sca_checkbox:  # al hacer clic en el botón
    # escribir un mensaje

    st.write('Creación de Geafico de Dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
