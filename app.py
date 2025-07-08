import streamlit as st

# Estilo customizado para remover o espaço superior e ajustar layout
st.markdown("""
    <style>
        .block-container {
            padding-top: 1rem;
        }
        .stTextInput > div > div > input {
            font-size: 14px;
            height: 32px;
        }
        .footer {
            margin-top: 5px;
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
    escolaridade = st.text_input("Escolaridade (medio/superior)")
    usa_app = st.text_input("Usa o App? (sim/não)")
    tem_cartao = st.text_input("Possui Cartão? (sim/não)")
    clicou_oferta = st.text_input("Clicou em Oferta? (sim/não)")

# Botão de previsão
if st.button("Prever"):
    if all([idade, renda, estado_civil, escolaridade, tempo_cliente, freq_acesso,
            tem_seguro, usa_app, tem_cartao, clicou_oferta]):
        if clicou_oferta.lower() == "sim":
            st.success("✅ Este cliente tem alta chance de comprar o produto!")
        else:
            st.warning("⚠️ Este cliente provavelmente **não** comprará o produto.")
    else:
        st.error("Por favor, preencha **todos os campos** para fazer a previsão.")

# Rodapé
st.markdown("""
    <div class='footer'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)
