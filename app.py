import streamlit as st
import pandas as pd
import plotly.express as px


car_data = pd.read_csv("data/vehicles_us.csv")

st.title("EL MERCADO DE AUTOS USADOS Y SUS TENDENCIAS")

st.header("Breve explicación del Mercado de Autos:")

st.write("La compra de un automóvil está motivada por diversas razones, entre ellas están:")

st.write("Productivos: Ya sean carros de carga o transporte, involucrados en las diversas áreas de la producción, su valor tiende a ser depreciado a lo largo de 10 años, para recuperar algo de lo invertido la empresa vende al mercado el valor residual.")

st.write("Personales: Este abarca la selección del vehículo, para su uso individual motivado por la movilidad, en este sector de uso se ve influenciado por gustos, presupuesto y situación, se pueden encontrar carros que tienen apenas 1 años de haber salido, así como carros clásicos, que a pesar de la tendencia natural de bajar su valor con el paso del tiempo estos lo mantienen y hasta lo elevan")

st.subheader(
    "Histograma: Comportamiento de los precios en el mercado de autos usados.")

st.write("Muestra la concentración de los precios.")

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

sca_checkbox = st.checkbox('Construir grafico de dispersión')  # crear un botón

if sca_checkbox:  # al hacer clic en el botón
    # escribir un mensaje

    st.write('Creación de Grafico de Dispersión para el conjunto de datos donde nos muestra la correlación entre las variables precio y año del modelo.')

    # crea un grafico de dispersión
    fig1 = px.scatter(car_data, x="price", y="model_year")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig1, use_container_width=True)
