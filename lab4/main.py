import mylib
def main():
    k = 20
    k1 = [4, 2, 2, 2]
    k2 = [5, 10, 5, 2]
    parities_groups = [[2, 3], [2, 3], [2, 3, 4, 5], [2, 3, 4, 5]]
    xk = mylib.generate_random_binary_sequence(k)

    print("Двумерная матрица \n")
    print("Исходное сообщение: " + ' '.join(map(str, xk)))

    for i in range(len(k1)):
        print(f'\n {i + 1}-я матрица \n')

        matrix = [xk[j * k2[i]:(j + 1) * k2[i]] for j in range(k1[i])]
        print(f'Матрица k1*k2 при k1={k1[i]} и k2={k2[i]}:')
        for row in matrix:
            print(' '.join(map(str, row)))

        print('Количество групп паритетов =' + ', '.join(map(str, parities_groups[i])))

        check_bits = mylib.calculate_check_bits(matrix, parities_groups[i], k1[i], k2[i])
        print('Проверочные биты: ' + ' '.join(map(str, check_bits)))

        codeword = xk + check_bits
        print('Кодовое слово: ' + ' '.join(map(str, codeword)))

        error_count_1d = 1
        received_matrix_1d = mylib.set_random_errors(matrix, k1[i], k2[i], error_count_1d)
        print('Матрица полученного сообщения:')
        for row in received_matrix_1d:
            print(' '.join(map(str, row)))

        received_check_bits_1d = mylib.calculate_check_bits(received_matrix_1d, parities_groups[i], k1[i], k2[i])
        print('Проверочные биты полученного слова: ' + ' '.join(map(str, received_check_bits_1d)))

        if check_bits == received_check_bits_1d:
            print('Xr и Yr одинаковые, ошибок не обнаружено')
        else:
            print('Xr и Yr не одинаковые')
            corrected_1d = mylib.find_errors(check_bits, received_check_bits_1d, k1[i], k2[i], received_matrix_1d)
            print('Исправленные ошибочные символы:')
            for row in corrected_1d:
                print(' '.join(map(str, row)))

        print(f'\n Корректирующая способность кода для {i + 1}-й матрицы \n')
        word_variants_count = 100
        correction_count_2d = 0
        error_count_3d = 2
        for _ in range(word_variants_count):
            received_matrix = mylib.set_random_errors(matrix, k1[i], k2[i], error_count_3d)
            received_check_bits = mylib.calculate_check_bits(received_matrix, parities_groups[i], k1[i], k2[i])
            corrected_matrix = mylib.find_errors(check_bits, received_check_bits, k1[i], k2[i], received_matrix)
            if ''.join(map(str, xk)) == ''.join(map(str, sum(corrected_matrix, []))):
                correction_count_2d += 1
        print(f'Корректирующая способность для 2 ошибок: {correction_count_2d / word_variants_count}')


if __name__ == "__main__":
    main()
