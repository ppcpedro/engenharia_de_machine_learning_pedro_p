import streamlit as st
import pandas as pd
import mlflow.pyfunc

# Carregar o modelo
model = mlflow.pyfunc.load_model("file:///C:/Pedro/posgrad/Engenharia de Machine Learning [23E1_3]/file/133641983168627663/cdbdfe5ac65f40f8ae02665b92448373/artifacts/best-model")

# Crie o aplicativo Streamlit
st.title("Previsão de Arremessos do Kobe Bryant")
st.write("Insira os seguintes detalhes para prever se Kobe acertou ou errou a cesta.")

# Crie campos de entrada para o usuário
lat = st.number_input("Latitude")
lon = st.number_input("Longitude")
minutes_remaining = st.number_input("Minutos Restantes")
period = st.number_input("Período")
playoffs = st.selectbox("Playoffs?", ["Sim", "Não"])
shot_distance = st.number_input("Distância do Arremesso")

# Converta a entrada do usuário em um DataFrame
user_input = pd.DataFrame({
    'lat': [lat],
    'lon': [lon],
    'minutes_remaining': [minutes_remaining],
    'period': [period],
    'playoffs': [playoffs == "Sim"],
    'shot_distance': [shot_distance]
})

# Use o modelo para fazer uma previsão
prediction = model.predict(user_input)

# Exiba a previsão para o usuário
if prediction[0] == 1:
    st.write("Kobe acertou a cesta!")
else:
    st.write("Kobe errou a cesta.")