import base64lib
import entropy
import textwrap
latysh_alphabet = ['a', 'ā', 'b', 'c', 'č', 'd', 'e', 'ē', 'f', 'g',
                   'ģ', 'h', 'i', 'ī', 'j', 'k', 'ķ', 'l', 'ļ', 'm',
                   'n', 'ņ', 'o', 'p', 'r', 's', 'š', 't', 'u', 'ū',
                   'v', 'z', 'ž']
base64_alphabet = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
    'w', 'x', 'y', 'z', '0', '1', '2', '3',
    '4', '5', '6', '7', '8', '9', '+', '/'
]
binary_alphabet = ['0', '1']
if __name__ == '__main__':
    a = "Skalkovich"
    b = "Stanislau"
    menu_flag = True
    while menu_flag:
        print("Выберите задание:")
        print("1 - Документ в base64\n"
              "2 - распределение частотных свойств алфавитов по документам\n"
              "3 - XOR в кодах ASCII\n"
              "4 - XOR в кодах base64\n"
              "5 - выход")
        choosed = int(input("Выбор: "))
        if choosed == 1:
            output = base64lib.encode_document_to_base64("latysh.txt")
            open('latysh_base64.txt', "w", encoding="utf-8").write(output)
            for line in textwrap.wrap(output, width=64):
                print(line)
            continue
        elif choosed == 2:
            b_doc = base64lib.encode_document_to_base64("latysh.txt")
            entropy_shannon_a = entropy.calculate_shannon_entropy(
                      open("latysh.txt", "r", encoding="utf-8").read().lower(),
                      latysh_alphabet)
            print("Энропия по Шеннону документа a: ", entropy_shannon_a)
            entropy_hartley_a = entropy.calculate_hartley_entropy(
                      open("latysh.txt", "r", encoding="utf-8").read().lower(),
                      latysh_alphabet)
            print("Энропия по Хартли документа a: ", entropy_hartley_a)

            print("избыточность документа a", entropy.calculate_redundancy(entropy_shannon_a, entropy_hartley_a))
            print("избыточность документа a по другой формуле", entropy.calculate_redundancy_alt(entropy_shannon_a, latysh_alphabet))

            entropy_shannon_b = entropy.calculate_shannon_entropy(
                      b_doc,
                      base64_alphabet)
            print("Энропия по Шеннону документа b: ", entropy_shannon_b)
            entropy_hartley_b = entropy.calculate_hartley_entropy(
                      b_doc,
                      base64_alphabet)
            print("Энропия по Хартли документа b: ", entropy_hartley_b)

            print("избыточность документа b", entropy.calculate_redundancy(entropy_shannon_b, entropy_hartley_b))
            print("избыточность документа b по другой формуле",
                  entropy.calculate_redundancy_alt(entropy_shannon_b, base64_alphabet))
            continue
        elif choosed == 3:
            xor_res, a_full, b_full = base64lib.xor_buffers(a.encode("ascii"), b.encode("ascii"))
            print(f"a: {a_full}\n"
                  f"b: {b_full}\n"
                  f"r: {xor_res}")
            continue
        elif choosed == 4:
            xor_res, a_full, b_full = base64lib.xor_buffers(
                base64lib.string_to_base64(a.encode("utf-8")).encode("utf-8"),
                base64lib.string_to_base64(b.encode("utf-8")).encode("utf-8"))
            print(f"a: {a_full}\n"
                  f"b: {b_full}\n"
                  f"r: {xor_res}")
            continue
        elif choosed == 5:
            menu_flag = False
            continue
        else:
            continue

