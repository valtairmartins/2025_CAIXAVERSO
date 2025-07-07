import streamlit as st

st.markdown("""
    <style>
        /* Layout geral */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
            max-width: 900px;
            margin: auto;
            background-color: #F9FAFC;
            border-radius: 12px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        /* Inputs */
        .stTextInput > div > div > input {
            font-size: 15px;
            height: 36px;
            border: 1px solid #ccc;
            border-radius: 8px;
            padding: 6px 10px;
        }

        /* Botão */
        button[kind="primary"] {
            background-color: #004AAD;
            color: white;
            border-radius: 10px;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
            font-weight: bold;
        }
        button[kind="primary"]:hover {
            background-color: #00337f;
            transform: scale(1.02);
        }

        /* Rodapé */
        .footer {
            margin-top: 30px;
            text-align: center;
            color: #666;
            font-size: 0.9rem;
        }

        /* Títulos */
        h2, h4 {
            color: #004AAD;
            font-family: 'Segoe UI', sans-serif;
        }
    </style>
""", unsafe_allow_html=True)

# ======= Título =======
st.markdown("<h2 style='text-align: center;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor Inteligente de Vendas CAIXA</h4>", unsafe_allow_html=True)
st.write("")

# ======= Formulário de entrada =======
col1, col2 = st.columns(2)

with col1:
    idade = st.text_input("Idade")
    estado_civil = st.text_input("Estado Civil")
    tempo_cliente = st.text_input("Tempo como Cliente (em anos)")
    tem_seguro = st.text_input("Possui Seguro? (Sim/Não)")
    freq_acesso = st.text_input("Frequência de Acesso ao App")

with col2:
    renda = st.text_input("Renda Mensal (R$)")
    escolaridade = st.text_input("Escolaridade")
    usa_app = st.text_input("Usa o App? (Sim/Não)")
    tem_cartao = st.text_input("Possui Cartão? (Sim/Não)")
    clicou_oferta = st.text_input("Clicou em Oferta? (Sim/Não)")

# ======= Botão de previsão =======
if st.button("Prever"):
    # Aqui vai a lógica de modelo (simulação abaixo)
    st.markdown("""
        <div style="text-align:center; padding:20px;">
            <span style='font-size: 1.2rem; color: green; font-weight: bold;'>Este cliente provavelmente realizará uma compra.</span>
        </div>
    """, unsafe_allow_html=True)

# ======= Rodapé =======
st.markdown("""
    <div class='footer'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        Caixa Econômica Federal • CAIXAVERSO 2025
    </div>
""", unsafe_allow_html=True)
