import streamlit as st
import numpy as np
import joblib

# Carrega o modelo
modelo = joblib.load("modelo_treinado.pkl")

# Dicionários de mapeamento
map_binario = {"sim": 1, "não": 0}
map_estado_civil = {"solteiro": 0, "casado": 1}
map_escolaridade = {"medio": 0, "superior": 1}

# Estilo customizado
st.set_page_config(page_title="Preditor de Vendas CAIXA", layout="centered")
st.markdown("""
    <style>
        .block-container { padding-top: 1.5rem; }
        .stTextInput > div > div > input { font-size: 14px; height: 36px; }
        .footer { margin-top: 20px; text-align: center; font-size: 14px; color: #666; }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho
st.markdown("<h2 style='text-align: center; color: #004AAD;'>CAIXA VERSO 2025</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Preditor Inteligente de Vendas CAIXA</h4>", unsafe_allow_html=True)

# Formulário dividido
col1, col2 = st.columns(2)

with col1:
    idade = st.number_input("Idade", min_value=18, max_value=100, step=1)
    estado_civil = st.selectbox("Estado Civil", ["solteiro", "casado"])
    tempo_cliente = st.number_input("Tempo como Cliente (anos)", min_value=0.0, max_value=50.0, step=0.1)
    tem_seguro = st.selectbox("Possui Seguro?", ["sim", "não"])
    freq_acesso = st.number_input("Frequência de Acesso ao App (mês)", min_value=0.0, max_value=100.0, step=0.1)

with col2:
    renda = st.number_input("Renda Mensal (R$)", min_value=0.0, step=100.0)
    escolaridade = st.selectbox("Escolaridade", ["medio", "superior"])
    usa_app = st.selectbox("Usa o App?", ["sim", "não"])
    tem_cartao = st.selectbox("Possui Cartão?", ["sim", "não"])
    clicou_oferta = st.selectbox("Clicou em Oferta?", ["sim", "não"])

# Botão de previsão
if st.button("Prever"):
    try:
        # Organiza os dados conforme o modelo
        entrada = np.array([[
            idade,
            renda,
            map_estado_civil[estado_civil],
            map_escolaridade[escolaridade],
            tempo_cliente,
            map_binario[usa_app],
            map_binario[tem_seguro],
            map_binario[tem_cartao],
            freq_acesso,
            map_binario[clicou_oferta]
        ]])

        # Faz a previsão
        pred = modelo.predict(entrada)[0]
        prob = modelo.predict_proba(entrada)[0][pred]

        # Mostra o resultado
        if pred == 1:
            st.success(f"✅ Este cliente tem alta chance de comprar o produto (confiança: {prob:.0%})!")
        else:
            st.warning(f"⚠️ Este cliente provavelmente **não** comprará o produto (confiança: {prob:.0%}).")

    except Exception as e:
        st.error(f"Erro na previsão: {str(e)}")

# Rodapé
st.markdown("""
    <div class='footer'>
        <strong>Astronauta Valtair Martins de Oliveira</strong><br>
        <span style='color: #004AAD;'>Caixa Econômica Federal</span>
    </div>
""", unsafe_allow_html=True)
