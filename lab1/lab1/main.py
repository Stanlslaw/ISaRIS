import entropy

latysh_alphabet = ['a', 'ā', 'b', 'c', 'č', 'd', 'e', 'ē', 'f', 'g',
                   'ģ', 'h', 'i', 'ī', 'j', 'k', 'ķ', 'l', 'ļ', 'm',
                   'n', 'ņ', 'o', 'p', 'r', 's', 'š', 't', 'u', 'ū',
                   'v', 'z', 'ž']
tadjik_alphabet = ['а', 'б', 'в', 'г', 'ғ', 'д', 'е', 'ё', 'ж', 'з',
                   'и', 'й', 'к', 'қ', 'л', 'м', 'н', 'о', 'п', 'р',
                   'с', 'т', 'у', 'ф', 'х', 'ҳ', 'ч', 'ш', 'ъ', 'ы',
                   'ь', 'э', 'ю', 'я']

binary_alphabet = ['0', '1']
if __name__ == '__main__':
    print("Лабораторная работа №2")
    menu_flag = True
    entropy.calculate_alphabet_frequency(open("tadjik.txt", "r", encoding="utf-8").read(), tadjik_alphabet)
    #entropy.calculate_alphabet_frequency(open("latysh.txt", "r", encoding="utf-8").read(), latysh_alphabet)
    while(menu_flag):
        print("Выберите задание:")
        print("1 - энтропия для таджитского алфавита\n"
              "2 - энтропия для латышского алфавита\n"
              "3 - энтропия для бинарного представления\n"
              "4 - расчет количества информации\n"
              "5 - выход")
        choosed = int(input("Выбор: "))
        if choosed == 1:
            print("Энтропия таджикского: ",
                  entropy.calculate_shannon_entropy(open("tadjik.txt", "r", encoding="utf-8").read(), tadjik_alphabet))
        elif choosed == 2:
            print("Энтропия латышского: ",
                  entropy.calculate_shannon_entropy(open("latysh.txt", "r", encoding="utf-8").read(), latysh_alphabet))
        elif choosed == 3:
            print("Энтропия бинарного: ",
                  entropy.calculate_shannon_entropy(entropy.binary("Kobrin is one of the best cities"), binary_alphabet))
        elif choosed == 4:
            print("Таджикский - количество информации: ",
                  entropy.count_information("Skalkovich Stanislaw Leonidovich",
                  entropy.calculate_shannon_entropy(open("tadjik.txt", "r", encoding="utf-8").read(), tadjik_alphabet)))
            print("Латышский - количество информации: ",
                  entropy.count_information("Skalkovich Stanislaw Leonidovich",
                                            entropy.calculate_shannon_entropy(open("latysh.txt", "r", encoding="utf-8").read(),
                                                                              latysh_alphabet)))
            print("Бинарный - количество информации: ",
                  entropy.count_information(entropy.binary("Skalkovich Stanislaw Leonidovich"),
                                            entropy.calculate_shannon_entropy(entropy.binary("Skalkovich Stanislaw Leonidovich"),
                                                                              binary_alphabet)))
            b1 = entropy.with_error(0.1)
            binary_string = entropy.binary('Skalkovich Stanislaw Leonidovich')
            information1 = entropy.count_information(binary_string, b1)
            print("Энтропия при вероятности ошибочной передачи = 0.1:", b1)
            print("Количество информации:", information1)

            b2 = entropy.with_error(0.5)
            information2 = entropy.count_information(binary_string, b2)
            print("Энтропия при вероятности ошибочной передачи = 0.5:", b2)
            print("Количество информации:", information2)

            b3 = entropy.with_error(0.9999999999999999)
            information3 = entropy.count_information(binary_string, b3)
            print("Энтропия при вероятности ошибочной передачи = 1.0:", b3)
            print("Количество информации:", information3)

            s1 = entropy.with_error(0.1)
            text = "Skalkovich Stanislaw Leonidovich"
            information4 = entropy.count_information(text, s1)
            print("Для латышского")
            print("Энтропия при вероятности ошибочной передачи = 0.1:", s1)
            print("Количество информации:", information4)

            s2 = entropy.with_error(0.5)
            information5 = entropy.count_information(text, s2)
            print("Энтропия при вероятности ошибочной передачи = 0.5:", s2)
            print("Количество информации:", information5)

            s3 = entropy.with_error(0.9999999999999999)
            information6 = entropy.count_information(text, s3)
            print("Энтропия при вероятности ошибочной передачи = 1.0:", s3)
            print("Количество информации:", information6)
        elif choosed == 5:
            menu_flag = False
            break
        else:
            continue

input("press enter to close")