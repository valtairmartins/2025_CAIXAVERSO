import streamlit as st
import numpy as np
import joblib

# Configuração da página
st.set_page_config(page_title="CAIXA VERSO", layout="centered")

# Carrega o modelo
modelo = joblib.load("modelo_treinado.pkl")

# Título
st.markdown("## CAIXA VERSO 2025")
st.markdown("#### Preditor Inteligente de Vendas")

# Entradas
idade = st.number_input("Idade", min_value=18, max_value=100, step=1)
usa_app = st.checkbox("Usa o App da CAIXA?")  # Retorna True ou False

# Botão de previsão
if st.button("Prever"):
    entrada = np.array([[idade, usa_app]], dtype=object)

    try:
        pred = modelo.predict(entrada)[0]
        prob = modelo.predict_proba(entrada)[0][pred]

        if pred == 1:
            st.success(f"✅ Alta chance de compra! (confiança: {prob:.0%})")
        else:
            st.warning(f"⚠️ Provavelmente não comprará. (confiança: {prob:.0%})")
    except Exception as e:
        st.error(f"Erro ao prever: {e}")

# Rodapé
st.markdown("---")
st.markdown("**Astronauta Valtair Martins de Oliveira**  \nCaixa Econômica Federal", unsafe_allow_html=True)
