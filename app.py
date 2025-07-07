import streamlit as st
import joblib
import numpy as np

# Título principal
st.markdown("<h2 style='text-align: center; color: #004AAD;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor CAIXA</h4>", unsafe_allow_html=True)

# Campos de entrada
idade = st.text_input("Idade:")
renda = st.text_input("Renda:")
estado_civil = st.text_input("Estado Civil:")  # Codificado no treino
escolaridade = st.text_input("Escolaridade:")  # Codificado no treino
tempo_cliente = st.text_input("Tempo Cliente:")
usa_app = st.text_input("Usa App?")  # 0 ou 1
tem_seguro = st.text_input("Tem Seguro?")  # 0 ou 1
tem_cartao = st.text_input("Tem Cartão?")  # 0 ou 1
freq_acesso = st.text_input("Freq. Acesso App:")
clicou_oferta = st.text_input("Clicou Oferta?")  # 0 ou 1

# Botão de previsão
if st.button("Prever"):
    try:
        # Coletar os dados como float
        entrada = np.array([[
            float(idade),
            float(renda),
            int(estado_civil),
            int(escolaridade),
            float(tempo_cliente),
            int(usa_app),
            int(tem_seguro),
            int(tem_cartao),
            float(freq_acesso),
            int(clicou_oferta)
        ]])

        # Carregar o modelo
        modelo = joblib.load('modelo_treinado.pkl')

        # Fazer a previsão
        pred = modelo.predict(entrada)

        # Interpretar resultado
        if pred[0] == 1:
            st.success("✅ O cliente **vai efetuar uma compra**.")
        else:
            st.warning("⚠️ O cliente **não vai efetuar uma compra**.")
    
    # Rodapé
st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)