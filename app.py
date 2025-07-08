import streamlit as st

# Estilo customizado para remover o espaço superior e ajustar layout
st.markdown("""
    <style>
        /* Remove espaço superior */
        .block-container {
            padding-top: 1rem;
        }
        .stTextInput > div > div > input {
            font-size: 14px;
            height: 32px;
        }
        .footer {
            margin-top: 5px; /* Aqui foi ajustado */
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho centralizado
st.markdown("<h2 style='text-align: center; color: #004AAD;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor Inteligente de Vendas CAIXA</h4>", unsafe_allow_html=True)

# Reduzir o formulário usando colunas
col1, col2 = st.columns(2)

with col1:
    idade = st.text_input("Idade (em anos)")
    estado_civil = st.text_input("Estado Civil (solteiro/casado)")
    tempo_cliente = st.text_input("Tempo como Cliente (em anos)")
    tem_seguro = st.text_input("Possui Seguro? (sim/não)")
    freq_acesso = st.text_input("Frequência de Acesso ao App")

with col2:
    renda = st.text_input("Renda Mensal (R$)")
    escolaridade = st.text_input("Escolaridade (Medio/Superior)")
    usa_app = st.text_input("Usa o App? (sim/não)")
    tem_cartao = st.text_input("Possui Cartão? (sim/não)")
    clicou_oferta = st.text_input("Clicou em Oferta? (sim/não)")

# Botão de previsão
if st.button("Prever"):
    st.success("Este cliente provavelmente realizará uma compra!")

# Rodapé logo abaixo do botão
st.markdown("""
    <div class='footer'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)
