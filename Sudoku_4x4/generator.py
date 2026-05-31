# ==========================================================
# generator.py
# Gerador de dados para treinamento de RNA Sudoku 4x4
# ==========================================================

import numpy as np
import random
import csv
from sklearn.model_selection import train_test_split

# ==========================================================
# Sudoku base válido
# ==========================================================

BASE_BOARD = np.array([
    [1, 2, 3, 4],
    [3, 4, 1, 2],
    [2, 1, 4, 3],
    [4, 3, 2, 1]
])


# ==========================================================
# Gera uma nova solução válida a partir da base
# ==========================================================

def generate_valid_board():
    board = BASE_BOARD.copy()

    # Troca números aleatoriamente
    mapping = [1, 2, 3, 4]
    random.shuffle(mapping)

    new_board = board.copy()

    for old_value in range(1, 5):
        new_board[board == old_value] = mapping[old_value - 1]

    return new_board


# ==========================================================
# Remove células aleatoriamente
# ==========================================================

def create_puzzle(solution, holes=6):
    puzzle = solution.copy()

    positions = [(r, c) for r in range(4) for c in range(4)]

    removed = random.sample(positions, holes)

    for row, col in removed:
        puzzle[row][col] = 0

    return puzzle


# ==========================================================
# Converte matriz em vetor
# ==========================================================

def flatten_board(board):
    return board.flatten().tolist()


# ==========================================================
# Gera dataset completo
# ==========================================================

def generate_dataset(num_samples=2000):

    data = []

    for _ in range(num_samples):

        solution = generate_valid_board()

        holes = random.randint(4, 8)

        puzzle = create_puzzle(solution, holes)

        input_data = flatten_board(puzzle)
        output_data = flatten_board(solution)

        row = input_data + output_data

        data.append(row)

    return data


# ==========================================================
# Salva CSV
# ==========================================================

def save_csv(filename, data):

    with open(filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(data)


# ==========================================================
# Programa principal
# ==========================================================

if __name__ == "__main__":

    print("Gerando exemplos...")

    dataset = generate_dataset(2000)

    train_data, test_data = train_test_split(
        dataset,
        test_size=0.2,
        random_state=42
    )

    save_csv("train.csv", train_data)
    save_csv("test.csv", test_data)

    print(f"Treino: {len(train_data)} exemplos")
    print(f"Teste : {len(test_data)} exemplos")

    print("Arquivos gerados com sucesso!")