def process_matrix(matrix):
    processed_matrix = []

    for i in range(len(matrix)):
        processed_row = []

        for j in range(len(matrix[i])):
            neighbors = []
            element = matrix[i][j]

            # Left neighbor
            if j > 0:
                neighbors.append(matrix[i][j - 1])
            # Right neighbor
            if j < len(matrix[i]) - 1:
                neighbors.append(matrix[i][j + 1])
            # Upper neighbor
            if i > 0:
                neighbors.append(matrix[i - 1][j])
            # Lower neighbor
            if i < len(matrix) - 1:
                neighbors.append(matrix[i + 1][j])

            
            average = sum(neighbors + [element]) / (len(neighbors) + 1)
            processed_row.append(average)

        processed_matrix.append(processed_row)

    return processed_matrix


matrix = [
    [1, 2, 3, 4],
    [4, 5, 6, 7],
    [7, 8, 9, 0],
    [7, 8, 9, 6]
]

processed_matrix = process_matrix(matrix)
for row in processed_matrix:
    print(row)

