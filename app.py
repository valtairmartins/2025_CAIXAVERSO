import streamlit as st

# Estilo customizado para reduzir a largura do formulário
st.markdown("""
    <style>
        .stTextInput > div > div > input {
            font-size: 14px;
            height: 32px;
        }
        .container {
            max-width: 600px;
            margin: auto;
        }
        .footer {
            margin-top: 20px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho centralizado
st.markdown("<h2 style='text-align: center; color: #004AAD;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor CAIXA</h4>", unsafe_allow_html=True)

# Reduzir o formulário usando colunas
col1, col2 = st.columns(2)

with col1:
    idade = st.text_input("Idade:")
    estado_civil = st.text_input("Estado Civil:")
    tempo_cliente = st.text_input("Tempo Cliente:")
    tem_seguro = st.text_input("Tem Seguro?")
    freq_acesso = st.text_input("Freq. Acesso App:")

with col2:
    renda = st.text_input("Renda:")
    escolaridade = st.text_input("Escolaridade:")
    usa_app = st.text_input("Usa App?")
    tem_cartao = st.text_input("Tem Cartão?")
    clicou_oferta = st.text_input("Clicou Oferta?")

# Botão de previsão
if st.button("Prever"):
    st.success("Previsão realizada com sucesso! Verifique o resultado no sistema!")

# Rodapé logo abaixo do botão
st.markdown("""
    <div class='footer'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)