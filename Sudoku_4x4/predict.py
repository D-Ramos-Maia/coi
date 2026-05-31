# ==========================================================
# predict.py
# Teste da RNA Sudoku 4x4
# ==========================================================

import numpy as np
import joblib

from generator import generate_valid_board
from generator import create_puzzle
from validator import is_valid


# ==========================================================
# Imprimir tabuleiro formatado
# ==========================================================

def print_board(board):

    for row in board:
        print(" ".join(map(str, row)))

    print()


# ==========================================================
# Carregar modelo treinado
# ==========================================================

print("Carregando modelo...\n")

model = joblib.load("sudoku_model.pkl")

print("Modelo carregado com sucesso!\n")


# ==========================================================
# Gerar Sudoku aleatório
# ==========================================================

solution = generate_valid_board()

puzzle = create_puzzle(solution, holes=6)


# ==========================================================
# Mostrar Sudoku inicial
# ==========================================================

print("=" * 40)
print("TABULEIRO INICIAL")
print("=" * 40)

print_board(puzzle)


# ==========================================================
# Fazer previsão
# ==========================================================

X = puzzle.flatten().reshape(1, -1)

prediction = model.predict(X)

prediction = np.round(prediction)

prediction = np.clip(prediction, 1, 4)

prediction = prediction.astype(int)

prediction = prediction.reshape(4, 4)


# ==========================================================
# Mostrar solução prevista
# ==========================================================

print("=" * 40)
print("SOLUÇÃO GERADA PELA RNA")
print("=" * 40)

print_board(prediction)


# ==========================================================
# Mostrar solução correta
# ==========================================================

print("=" * 40)
print("SOLUÇÃO CORRETA")
print("=" * 40)

print_board(solution)


# ==========================================================
# Validação
# ==========================================================

print("=" * 40)
print("VALIDAÇÃO")
print("=" * 40)

valid = is_valid(prediction)

print(f"Sudoku válido? {valid}")

correct = np.array_equal(prediction, solution)

print(f"Solução idêntica à correta? {correct}")


# ==========================================================
# Estatísticas finais
# ==========================================================

print("\n" + "=" * 40)

if valid and correct:
    print("RESULTADO: SUCESSO TOTAL")
elif valid:
    print("RESULTADO: Sudoku válido, mas diferente da solução original")
else:
    print("RESULTADO: Sudoku inválido")

print("=" * 40)