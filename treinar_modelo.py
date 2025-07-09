import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import joblib

# Carrega a base real
df = pd.read_csv("C:/Users/Windows/Desktop/Carreira/CAIXAVERSO/deploy_app/MOCK_DATA.csv")  # substitua pelo caminho correto

# Garante que 'usa_app_caixa' está em formato binário
df["usa_app_caixa"] = df["usa_app_caixa"].map({"sim": 1, "não": 0})  # ajuste se necessário

# Seleciona apenas as colunas escolhidas
X = df[["idade", "usa_app_caixa"]]
y = df["aderiu_produto"]  # substitua pelo nome da sua variável alvo

# Treinamento
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
modelo = DecisionTreeClassifier(random_state=42)
modelo.fit(X_train, y_train)

# Salva modelo
joblib.dump(modelo, "modelo_treinado.pkl")

print("✅ Modelo treinado com sucesso usando apenas 'idade' e 'usa_app_caixa'.")
