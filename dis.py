import numpy as np


def solve_system(matrix):
    rows = matrix.shape[0]

    # Прямой ход метода Гаусса
    for i in range(rows):
        max_row_idx = np.argmax(np.abs(matrix[i:, i])) + i
        if matrix[max_row_idx][i] == 0:
            if np.all(matrix[i:, -1] == 0):
                raise ValueError("Система имеет бесконечно много решений.")
            else:
                raise ValueError("Нет решений для данной системы.")
        matrix[[i, max_row_idx]] = matrix[[max_row_idx, i]]
        for j in range(i + 1, rows):
            multiplier = matrix[j][i] / matrix[i][i]
            matrix[j] -= multiplier * matrix[i]

    # Обратный ход метода Гаусса
    result = np.zeros(rows)
    for i in range(rows - 1, -1, -1):
        if matrix[i][i] != 0:
            result[i] = (matrix[i][-1] - np.dot(matrix[i][:-1], result)) / matrix[i][i]

    return result
