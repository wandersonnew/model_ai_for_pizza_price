import streamlit as st
import pandas as pd
# from sklearn.linear_model import LinearRegression
import pickle

with open('pizza_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# df = pd.read_csv('pizzas.csv')

# model = LinearRegression()
# X = df[['diametro']]
# y = df[['preco']]

# model.fit(X, y)

st.title('Prevendo o valor de uma Pizza')
st.divider()
diametro = st.number_input('Digite o diâmetro da pizza em cm', min_value=0)

if diametro:
    X_valor = pd.DataFrame({'diametro': [diametro]})
    preco_previsto = model.predict(X_valor)[0][0]
    st.write(f'O valor da pizza com diâmetro {diametro}cm é de R${preco_previsto:.2f}')
