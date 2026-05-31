# ==========================================================
# train.py
# Treinamento da RNA Sudoku 4x4
# ==========================================================

from dataset import load_dataset
from model import create_model

from sklearn.metrics import mean_squared_error
import joblib


# ==========================================================
# Carregar dados
# ==========================================================

X_train, Y_train = load_dataset("train.csv")
X_test, Y_test = load_dataset("test.csv")

print("Treinando rede neural...")


# ==========================================================
# Criar modelo
# ==========================================================

model = create_model()


# ==========================================================
# Treinar
# ==========================================================

model.fit(X_train, Y_train)


# ==========================================================
# Avaliar
# ==========================================================

predictions = model.predict(X_test)

mse = mean_squared_error(Y_test, predictions)

print(f"\nErro quadrático médio (MSE): {mse:.4f}")


# ==========================================================
# Salvar modelo
# ==========================================================

joblib.dump(model, "sudoku_model.pkl")

print("\nModelo salvo em sudoku_model.pkl")