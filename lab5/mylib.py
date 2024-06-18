import random
class InfoMetrics:
    @staticmethod
    def generate_matrix(poly, n, k):
        matrix = [[0] * n for _ in range(k)]
        poly_length = len(poly)
        # Fill the first row with the polynomial
        for i in range(poly_length):
            matrix[0][i] = int(poly[i])
        # Fill other rows by shifting the polynomial one position to the right
        for i in range(1, k):
            matrix[i][0] = 0
            for j in range(1, poly_length):
                matrix[i][j] = matrix[i - 1][j - 1]
            for j in range(poly_length, n):
                matrix[i][j] = matrix[i - 1][j - 1]
        return matrix

    @staticmethod
    def to_canonical_form(matrix, n, k):
        for i in range(k):
            for j in range(i + 1, k):
                if matrix[i][j] == 1:
                    for l in range(n):
                        matrix[i][l] = (matrix[i][l] + matrix[j][l]) % 2
        return matrix

    @staticmethod
    def generate_check_matrix(generator_matrix, n, k):
        r = n - k
        check_matrix = [[0] * r for _ in range(n)]
        # Extract the last r columns and k rows from the generator matrix
        for i in range(k):
            check_matrix[i] = generator_matrix[i][k:]
        # Add a diagonal matrix of size r by r at the bottom
        for i in range(r):
            check_matrix[k + i][i] = 1
        return check_matrix

    @staticmethod
    def transpose_matrix(matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        transposed_matrix = [[0] * rows for _ in range(cols)]
        for i in range(rows):
            for j in range(cols):
                transposed_matrix[j][i] = matrix[i][j]
        return transposed_matrix

    @staticmethod
    def calculate_redundant_bits(info_word, check_matrix):
        r = len(check_matrix)
        redundant_bits = ""
        for i in range(r):
            sum_val = sum(int(info_word[j]) * check_matrix[i][j] for j in range(len(info_word)))
            redundant_bits += str(sum_val % 2)
        return redundant_bits

    @staticmethod
    def correct_error(code_word, correct_redundant_bits, check_matrix):
        n = len(check_matrix[0])
        r = len(check_matrix)
        error_red_bits = InfoMetrics.calculate_redundant_bits(code_word, check_matrix)
        error_vector = "".join(str((int(error_red_bits[i]) + int(correct_redundant_bits[i])) % 2) for i in range(r))
        print("syndrome: " + error_vector)
        for i in range(n):
            column = "".join(str(check_matrix[j][i]) for j in range(r))
            if column == error_vector:
                code_word = code_word[:i] + ('1' if code_word[i] == '0' else '0') + code_word[i + 1:]
                break
        return code_word

    @staticmethod
    def introduce_errors(word, num_errors):
        word_list = list(word)
        for _ in range(num_errors):
            error_pos = random.randint(0, len(word) - 1)
            word_list[error_pos] = '1' if word_list[error_pos] == '0' else '0'
        return ''.join(word_list)
