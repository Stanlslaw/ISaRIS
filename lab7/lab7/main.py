import time
import timeit
def print_matrix(matrix):
    for row in matrix:
        print(row)
    print()

def sorted_matrix(matrix):
    return sorted(matrix)

def create_matrix(input):
    matrix = []
    for _ in range(len(input)):
        matrix.append(input)
        input = input[1:] + input[0]
    return matrix

def get_the_last_column_from_matrix(matrix):
    the_last_column = ""
    for row in matrix:
        the_last_column += row[-1]
    return the_last_column

def get_row_number_from_matrix(input, matrix):
    for i, row in enumerate(matrix):
        if row == input:
            return i
    return -1

def add_decoding_matrix_rows(input, matrix):
    for i in range(len(matrix)):
        matrix[i] = input[i] + matrix[i]
    return matrix

def get_decoding_matrix(message):
    message_matrix = [""] * len(message)

    for _ in range(len(message)):
        add_decoding_matrix_rows(message, message_matrix)
        print_matrix(message_matrix)
        message_matrix.sort()

    return message_matrix

def main():
    input3Letters = "тел"
    output3Letters = ''.join(format(ord(char), 'b') for char in input3Letters)

    print("Строка в ASCII: " + output3Letters)

    input_messages = [
        "СТАС",
        "СКАЛКОВИЧ",   
        "телегаммааппарат",
        output3Letters
    ]

    for words in input_messages:
        print("\t\t\tСообщение: " + words)
        print("\nКодирование\n")

        start_encoding = timeit.default_timer()

        w1 = create_matrix(words)
        print("Матрица W1 - сдвиг строк")
        print_matrix(w1)
        w2 = sorted_matrix(w1)
        print("Матрица W2 - отсортированные строки")
        print_matrix(w2)

        input_encode = get_the_last_column_from_matrix(w2) + str(get_row_number_from_matrix(words, w2))
        getted_message = input_encode[:len(words)]

        print("Закодированное сообщение: " + getted_message)
        print("Номер строки содержащей корректное сообщение: " + str(get_row_number_from_matrix(words, w2)) + "\n")

        encoding_time = (timeit.default_timer() - start_encoding) * 1000

        print("\nДекодирование\n")
        start_decoding = timeit.default_timer()

        w2_for_decode = get_decoding_matrix(getted_message)
        print("Восстановленная матрица W2 - отсортировали")
        print_matrix(w2_for_decode)

        number_of_initial_message = int(input_encode[len(words):])
        print("Декодированное сообщение: " + w2_for_decode[number_of_initial_message])

        decoding_time = (timeit.default_timer() - start_decoding) * 1000

        output = w2_for_decode[number_of_initial_message]

        if output == words:
            print("Успешно!")
        else:
            print("Ничего не получилось...")

        print("Время кодирования: {:.4f} мс".format(encoding_time))
        print("Время декодирования: {:.4f} мс\n".format(decoding_time))

if __name__ == "__main__":
    main()
