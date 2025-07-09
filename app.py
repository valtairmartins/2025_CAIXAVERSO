import streamlit as st
import numpy as np
import joblib

# Configuração da página
st.set_page_config(page_title="CAIXA VERSO 2025", layout="wide")

# === Caminho da imagem do robô (usar versão RAW do GitHub) ===
robo_url = "https://raw.githubusercontent.com/valtairmartins/CAIXAVERSO/main/robo.png"

# Dividir layout em colunas
col1, col2 = st.columns([1, 2])

# === Coluna da Imagem ===
with col1:
    st.image(robo_url, width=200)

# === Coluna do Conteúdo ===
with col2:
    st.markdown("## CAIXA VERSO 2025")
    st.markdown("### Previsão Inteligente de Vendas")

    # Entradas do usuário
    idade = st.number_input("Idade", min_value=18, max_value=100, value=30, step=1)
    usa_app = st.checkbox("Você usa o aplicativo da CAIXA? (marque se sim)")
    usa_app_int = int(usa_app)

    # Botão de previsão
    if st.button("Prever"):
        try:
            # Carregar modelo treinado
            modelo = joblib.load("modelo_treinado.pkl")

            # Criar entrada
            entrada = np.array([[idade, usa_app_int]])

            # Fazer previsão
            pred = modelo.predict(entrada)[0]
            probs = modelo.predict_proba(entrada)[0]
            prob_compra = probs[1]
            prob_nao_compra = probs[0]
            confianca = probs[pred]

            # Mensagem principal
            if pred == 1:
                st.success(f"✅ Alta chance de compra! (confiança: {confianca:.0%})")
            else:
                st.warning(f"⚠️ Provavelmente não comprará. (confiança: {confianca:.0%})")

            # Detalhes da previsão
            st.markdown("### 🔍 Detalhes da previsão:")
            st.markdown(f"""
                <p>🛒 Probabilidade de <b>comprar</b>: 
                <span style='color:green; font-weight:bold'>{prob_compra:.2%}</span></p>
                
                <p>🚫 Probabilidade de <b>não comprar</b>: 
                <span style='color:red; font-weight:bold'>{prob_nao_compra:.2%}</span></p>
            """, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"Erro ao carregar modelo ou prever: {e}")

# Rodapé
st.markdown("---")
st.markdown("Astronauta Valtair Martins de Oliveira  \nCaixa Econômica Federal")

