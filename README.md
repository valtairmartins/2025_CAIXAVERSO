# Previsão de Vendas — CAIXAVERSO

![banner](https://github.com/valtairmartins/CAIXAVERSO/blob/main/banner_caixaverso.png)

> Projeto desenvolvido como parte do processo seletivo para a **Imersão CAIXAVERSO**, demonstrando domínio prático de **Machine Learning** aplicado a um contexto bancário realista, com foco em **open finance**, **fidelização de clientes** e **campanhas personalizadas**.

---

# Deploy da Aplicação
O sistema foi publicado na plataforma Streamlit Cloud e pode ser acessado aqui:
[Acesse a aplicação](https://astronautacaixaverso.streamlit.app/)

## Objetivo

Apresentar, de forma prática e funcional, o conhecimento completo sobre as etapas do ciclo de vida de um projeto de **Machine Learning em produção**, com ênfase em:

- Preparação de dados sintéticos simulando um banco público em transformação digital;
- Construção e avaliação de modelos de classificação;
- Deploy de uma aplicação interativa via **Streamlit Cloud**;
- Demonstração de boas práticas em ambientes de desenvolvimento com **conda** e **pip**.

---

## Contexto e Base de Dados

- Os dados foram gerados no [Mockaroo](https://www.mockaroo.com/), contendo **1.000 registros** com variáveis simuladas de um banco público em fase de modernização.
- O dataset simula o comportamento de clientes, produtos, vendas e características relevantes para análise preditiva.

---

## Tecnologias e Bibliotecas

| Categoria         | Ferramentas                           |
|------------------|----------------------------------------|
| Linguagem        | Python 3.10 / 3.13                     |
| Machine Learning | Scikit-learn, Joblib                   |
| Web App          | Streamlit                             |
| Manipulação de dados | Pandas, NumPy                     |
| Ambiente         | Conda, Pip                             |

---

## Modelos Treinados
Foram testados e comparados diversos algoritmos de classificação com ajuste de hiperparâmetros:

K-Nearest Neighbors (KNN)

Decision Tree

Support Vector Machine (SVM)

Random Forest

Gradient Boosting

AdaBoost

BaggingClassifier

## Técnicas Aplicadas
SelectKBest para seleção de atributos

StandardScaler para normalização

LabelEncoder para tratamento de variáveis categóricas

GridSearchCV para otimização dos modelos
