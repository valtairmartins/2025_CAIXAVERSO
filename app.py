import streamlit as st

st.set_page_config(page_title="CAIXA VERSO", layout="centered")

st.markdown("## CAIXA VERSO 2025")
st.markdown("#### Preditor Inteligente de Vendas")

# Entradas em duas colunas
col1, col2 = st.columns(2)
with col1:
    idade = st.text_input("Idade")
    estado_civil = st.text_input("Estado Civil")
    tempo_cliente = st.text_input("Tempo como Cliente")
    tem_seguro = st.text_input("Tem Seguro?")
    freq_acesso = st.text_input("Frequência no App")
with col2:
    renda = st.text_input("Renda")
    escolaridade = st.text_input("Escolaridade")
    usa_app = st.text_input("Usa App?")
    tem_cartao = st.text_input("Tem Cartão?")
    clicou_oferta = st.text_input("Clicou em Oferta?")

# Botão de previsão
if st.button("Prever"):
    if clicou_oferta.lower() == "sim":
        st.success("✅ Alta chance de compra!")
    else:
        st.warning("⚠️ Provavelmente não comprará.")

# Rodapé
st.markdown("---")
st.markdown("**Astronauta Valtair Martins de Oliveira**  \nCaixa Econômica Federal", unsafe_allow_html=True)
