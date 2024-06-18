import math

import mylib


def main():
    input_data = open('input.txt', 'r', encoding="ascii").read()
    input_data_binary = mylib.to_binary(input_data)
    k = len(input_data_binary)  # длина сообщения
    r = int(math.log2(k) + 1)  # избыточность сообщения
    n = r + k  # кодовое слово
    d = 4  # расстояние Хэминга
    hamming_matrix = mylib.get_hamming_matrix(k, r)
    Xr = mylib.calc_redundant_bits(hamming_matrix, mylib.to_binary(input_data), k, r)
    print(input_data)
    print("Xk:\n", input_data_binary)
    print("k = ", k)
    print("r = ", r)
    print("n = ", n)
    print("d = ", d)
    print("Проверочная матрица Хэмминга")
    for row in hamming_matrix:
        print(mylib.get_bits_str(row))
    print(f"Избыточные биты Xr: {mylib.get_bits_str(Xr)}", end=" ")

    for num_of_errors in range(3):
        binary_with_error = mylib.gen_err(input_data_binary, num_of_errors)
        print(f"Сообщение с {num_of_errors} ошибками: {binary_with_error}")
        Xr_with_error = mylib.calc_redundant_bits(hamming_matrix, binary_with_error, k, r)
        print(f"Избыточные биты Xr с {num_of_errors} ошибками: {mylib.get_bits_str(Xr_with_error)}", end=" ")
        S = mylib.calc_syndrome(Xr, Xr_with_error, r)
        print(f"Синдром: {mylib.get_bits_str(S)}")

        if any(S):
            En = mylib.gen_err_vector(S, hamming_matrix)
            print(f"Вектор ошибок: {mylib.get_bits_str(En)}")

            corrected_binary = mylib.correct_err(binary_with_error, En, r)
            print(f"Исправленное сообщение: {corrected_binary}")

            corrected_text = mylib.from_binary(corrected_binary)
            print(f"Исправленное сообщение в ascii: {corrected_text}")
        else:
            print("Нет ошибок для исправления.")


if __name__ == '__main__':
    main()
