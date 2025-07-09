import streamlit as st
import numpy as np
import joblib

# Configuração da página
st.set_page_config(page_title="CAIXA VERSO", layout="centered")

# Carrega o modelo
modelo = joblib.load("modelo_treinado.pkl")

# Título
st.markdown("## CAIXA VERSO 2025")
st.markdown("#### Previsão Inteligente de Vendas")

# Entradas
idade = st.number_input("Idade", min_value=18, max_value=100, step=1)
usa_app = st.checkbox("Você usa o aplicativo da CAIXA? (marque se sim)")
usa_app_int = int(usa_app)

# Botão de previsão
if st.button("Prever"):
    entrada = np.array([[idade, usa_app_int]], dtype=float)

    try:
        # Previsão da classe e das probabilidades
        pred = modelo.predict(entrada)[0]
        probas = modelo.predict_proba(entrada)[0]
        prob_nao_compra = float(probas[0])
        prob_compra = float(probas[1])

        # Resultado
        if pred == 1:
            st.success(f"✅ Alta chance de compra! (confiança: {prob_compra:.0%})")
        else:
            st.warning(f"⚠️ Provavelmente não comprará. (confiança: {prob_nao_compra:.0%})")

        # Mostrar ambas as probabilidades
        st.markdown("### 🔍 Detalhes da previsão:")
        st.write(f"🛒 Probabilidade de **comprar**: `{prob_compra:.2%}`")
        st.write(f"🚫 Probabilidade de **não comprar**: `{prob_nao_compra:.2%}`")

    except Exception as e:
        st.error(f"Erro ao prever: {e}")

# Rodapé
st.markdown("---")
st.markdown("**Astronauta Valtair Martins de Oliveira**  \nCaixa Econômica Federal", unsafe_allow_html=True)
