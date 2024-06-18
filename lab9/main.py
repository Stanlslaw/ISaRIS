def find_chars(dictionary, buf_word):
    index_in_array = 0
    length = 0
    last_element = buf_word[0]

    while buf_word[:length + 1] in dictionary:
        index_in_array = dictionary.index(buf_word[:length + 1]) + 1
        length += 1
        if length == len(buf_word):
            last_element = '|'
            break
        else:
            last_element = buf_word[length]

    return index_in_array, length, last_element


def send_chars(first_buf, second_buf, chars_count):
    chars_count = min(chars_count, len(second_buf))
    if chars_count > 0:
        first_buf += second_buf[:chars_count]
        second_buf = second_buf[chars_count:]
    return first_buf, second_buf


def minimize(buf, size):
    if len(buf) > size:
        buf = buf[-size:]
    return buf


def main():
    dictionary_length = 8
    word_length = 8

    input_message = "Скалкович Станислав Леонидович"
    result_message = ""
    word = input_message[:word_length]
    message = input_message[word_length:]

    dictionary = '0' * dictionary_length
    kod_word = ""
    iteration_count = 0
    total_iterations = len(input_message) // word_length

    while word:
        p, q, c = find_chars(dictionary, word)
        dictionary, word = send_chars(dictionary, word, q + 1)
        word, message = send_chars(word, message, q + 1)

        dictionary = minimize(dictionary, dictionary_length)
        word = minimize(word, word_length)

        kod_word += f"{p}{q}{c}"
        print(f"Словарь:             {dictionary}")
        print(f"Слово(буфер данных): {word}")
        print(f"Кодовое слово:       {kod_word}")
        print("-------------------------------")

        length_before_compression = len(input_message)
        length_after_compression = len(kod_word)
        compression_ratio_before = length_before_compression / length_after_compression
        compression_ratio_after = (1 - compression_ratio_before) * 100
        print(f"Степень сжатия: {compression_ratio_after:.2f}%")
        # if iteration_count == 16:


        iteration_count += 1

    dictionary = '0' * dictionary_length
    for i in range(0, len(kod_word), 3):
        p = int(kod_word[i])
        q = int(kod_word[i + 1])
        c = kod_word[i + 2]
        if p == 0 and q == 0:
            result_message += c
            dictionary += c
        else:
            str_part = dictionary[p - 1:p - 1 + q] + c
            result_message += str_part
            dictionary += str_part

        dictionary = minimize(dictionary, dictionary_length)
        print(f"Код:       {p} {q} {c}")
        print(f"Результат: {result_message}")
        print(f"Словарь:   {dictionary}")
        print("-------------------------------")


if __name__ == "__main__":
    main()
