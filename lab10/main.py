from collections import defaultdict

class InfoMetrics:
    ranges = {}

    @staticmethod
    def main():
        #word = "телегаммааппарат"
        word = "телегаммааппаратполуторапроцентный"
        InfoMetrics.calculate_initial_ranges(word)
        encoded_value = InfoMetrics.perform_arithmetic_encoding(word)
        print(f"Закодированное значение: {encoded_value}")
        decoded_word = InfoMetrics.perform_arithmetic_decoding(encoded_value, len(word))
        print(f"Декодированное слово: {decoded_word}")

    @staticmethod
    def calculate_initial_ranges(word):
        probabilities = defaultdict(float)
        total_length = len(word)

        # Вычисляем вероятности для каждого символа
        for ch in word:
            probabilities[ch] += 1
        for k in probabilities:
            probabilities[k] /= total_length

        # Инициализируем начальные границы
        lower = 0.0

        # Вычисляем диапазоны для каждого символа
        for ch, prob in probabilities.items():
            upper = lower + prob
            InfoMetrics.ranges[ch] = (lower, upper)
            lower = upper

        print("Шаг 0")
        for k, v in InfoMetrics.ranges.items():
            print(f"Для символа '{k}' диапазон: [{v[0]}, {v[1]}]")

    @staticmethod
    def perform_arithmetic_encoding(word):
        lower = 0.0
        upper = 1.0

        for i, ch in enumerate(word):
            current_range = InfoMetrics.ranges[ch]
            range_width = upper - lower

            # Вычисляем новые границы для текущего символа
            new_lower = lower + range_width * current_range[0]
            new_upper = lower + range_width * current_range[1]

            # Обновляем рабочий диапазон
            lower = new_lower
            upper = new_upper

            print(f"Шаг {i + 1} ----------------------------------------------------")
            print(f"{ch}' диапазон: [{new_lower}, {new_upper}]")

        # Возвращаем среднее значение между верхней и нижней границей как закодированное значение
        return (lower + upper) / 2.0

    @staticmethod
    def perform_arithmetic_decoding(code, length):
        word = []

        for i in range(length):
            # Находим символ, соответствующий текущему коду
            for ch, (lower, upper) in InfoMetrics.ranges.items():
                if lower <= code < upper:
                    word.append(ch)
                    # Обновляем код для следующего символа
                    code = (code - lower) / (upper - lower)
                    break
            else:
                raise RuntimeError("Не удалось декодировать символ")

        return ''.join(word)

if __name__ == "__main__":
    InfoMetrics.main()
