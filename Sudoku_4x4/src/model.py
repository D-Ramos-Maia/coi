# ==========================================================
# model.py
# Definição da Rede Neural Multicamadas (MLP)
# ==========================================================

from sklearn.neural_network import MLPRegressor


def create_model():
    """
    Cria e retorna uma RNA Multicamadas.
    """

    model = MLPRegressor(
        hidden_layer_sizes=(128, 256, 128),
        activation="relu",
        solver="adam",
        max_iter=1000,
        random_state=42
    )

    return model


# ==========================================================
# Teste simples
# ==========================================================

if __name__ == "__main__":

    model = create_model()

    print(model)
