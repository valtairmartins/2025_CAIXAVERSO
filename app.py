import streamlit as st 

# Título principal
st.markdown("<h2 style='text-align: center; color: #004AAD;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor CAIXA</h4>", unsafe_allow_html=True)

# Formulário de entrada
idade = st.text_input("Idade:")
renda = st.text_input("Renda:")
estado_civil = st.text_input("Estado Civil:")
escolaridade = st.text_input("Escolaridade:")
tempo_cliente = st.text_input("Tempo Cliente:")
usa_app = st.text_input("Usa App?")
tem_seguro = st.text_input("Tem Seguro?")
tem_cartao = st.text_input("Tem Cartão?")
freq_acesso = st.text_input("Freq. Acesso App:")
clicou_oferta = st.text_input("Clicou Oferta?")

# Botão de previsão (sem lógica por enquanto)
if st.button("Prever"):
    st.success("Previsão realizada com sucesso! Verifique o resultado no sistema!")  # Placeholder

# Rodapé
st.markdown("""
    <div style='text-align: center; margin-top: 30px;'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)