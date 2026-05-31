# ==========================================================
# validator.py
# Verifica se um Sudoku 4x4 é válido
# ==========================================================

def is_valid(board):

    # ==========================
    # Verificar linhas
    # ==========================

    for row in board:

        if sorted(row) != [1, 2, 3, 4]:
            return False

    # ==========================
    # Verificar colunas
    # ==========================

    for col in range(4):

        column = []

        for row in range(4):
            column.append(board[row][col])

        if sorted(column) != [1, 2, 3, 4]:
            return False

    # ==========================
    # Verificar blocos 2x2
    # ==========================

    for start_row in [0, 2]:
        for start_col in [0, 2]:

            block = []

            for r in range(start_row, start_row + 2):
                for c in range(start_col, start_col + 2):
                    block.append(board[r][c])

            if sorted(block) != [1, 2, 3, 4]:
                return False

    return True


# ==========================================================
# Teste
# ==========================================================

if __name__ == "__main__":

    board = [
        [4, 3, 2, 1],
        [2, 1, 4, 3],
        [3, 4, 1, 2],
        [1, 2, 3, 4]
    ]

    print("Sudoku válido?", is_valid(board))
