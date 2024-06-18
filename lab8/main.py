class ShannonFanoSymbol:
    def __init__(self, symbol, count, viorite, code):
        self.symbol = symbol
        self.count = count
        self.viorite = viorite
        self.code = code

    @staticmethod
    def add_symbols(symbols, line):
        for character in line:
            symbol = next((x for x in symbols if x.symbol == character), None)
            if symbol is None:
                symbols.append(ShannonFanoSymbol(character, 1, 0.0, ""))
            else:
                symbol.count += 1
        return symbols

    @staticmethod
    def show(symbols):
        for symbol in symbols:
            print(f"Символ: {symbol.symbol}  Кол-во: {symbol.count}", end=" ")
            if symbol.viorite != 0:
                print(f"Вероятность: {symbol.viorite}", end="")
            if symbol.code != "":
                print(f"  Код: {symbol.code}", end="")
            print()
        print()

    @staticmethod
    def add_codes(symbols):
        counter = 0
        probability = 0.0
        first = []
        second = []

        while probability < (sum(x.viorite for x in symbols) / 2):
            probability += symbols[counter].viorite
            counter += 1

        for i in range(counter):
            symbols[i].code += "0"
            first.append(symbols[i])

        for i in range(counter, len(symbols)):
            symbols[i].code += "1"
            second.append(symbols[i])

        if len(symbols) > 1:
            first = ShannonFanoSymbol.add_codes(first)
            second = ShannonFanoSymbol.add_codes(second)
            first.extend(second)
            symbols = first
        return symbols


symbols = []
with open("text.txt", "r", encoding="utf-8") as file:
    for line in file:
        symbols = ShannonFanoSymbol.add_symbols(symbols, line)

print("\nТаблица символов на основе данных, полученных в лабораторной работе № 2:\n")
ShannonFanoSymbol.show(symbols)

symbolssum = sum(x.count for x in symbols)
print("Сумма всех символов текста на латинском языке:", symbolssum)

for symbol in symbols:
    symbol.viorite = symbol.count / symbolssum

print("Сумма вероятностей всех символов таблицы:", sum(x.viorite for x in symbols), "\n")

symbols = sorted(symbols, key=lambda x: x.viorite, reverse=True)
ShannonFanoSymbol.show(symbols)

print("\nТаблица с кодом для каждого символа:\n")
symbols = ShannonFanoSymbol.add_codes(symbols)
for symbol in symbols:
    symbol.code = symbol.code[:-1]
ShannonFanoSymbol.show(symbols)

block_of_FIO = "Skalkovich Stanislau Leonidovich"
decoding_of_FIO = ""
for char_FIO in block_of_FIO:
    decoding_of_FIO += next((x.code for x in symbols if x.symbol == char_FIO), "")

print("Исходное сообщение:")
print(block_of_FIO)
print("Сообщение после кодировки:")
print(decoding_of_FIO)
print("Количество битов в кодах ASCII:", len(block_of_FIO) * 8)
print("Количество битов по таблице Шеннон-Фано:", len(decoding_of_FIO))
print("_____________________________________________")
print("\nДекодирование:\n")

encoded = ""
FIO_decoded = ""
for i in range(len(decoding_of_FIO)):
    encoded += decoding_of_FIO[i]
    symbol = next((x for x in symbols if x.code == encoded), None)
    if symbol is not None:
        FIO_decoded += symbol.symbol
        encoded = ""

print(FIO_decoded)

print("_____________________________________________")
print("\nДинамически, на основе анализа сжимаемого сообщения:\n")

symbols.clear()

message = "Skalkovich"
symbols = ShannonFanoSymbol.add_symbols(symbols, message)
ShannonFanoSymbol.show(symbols)

symbolssum = sum(x.count for x in symbols)
print("Сумма всех символов текста на латинском языке:", symbolssum)

for symbol in symbols:
    symbol.viorite = symbol.count / symbolssum

print("Сумма вероятностей всех символов таблицы:", sum(x.viorite for x in symbols), "\n")

symbols = sorted(symbols, key=lambda x: x.viorite, reverse=True)
ShannonFanoSymbol.show(symbols)

print("\nТаблица с кодом для каждого символа:\n")
symbols = ShannonFanoSymbol.add_codes(symbols)
for symbol in symbols:
    symbol.code = symbol.code[:-1]

ShannonFanoSymbol.show(symbols)

block_of_FIO = "Skalkovich"
decoding_of_FIO = ""
for char_FIO in block_of_FIO:
    decoding_of_FIO += next((x.code for x in symbols if x.symbol == char_FIO), "")

print("Исходное сообщение:")
print(block_of_FIO)
print("Сообщение после кодировки:")
print(decoding_of_FIO)
print("Количество битов в кодах ASCII:", len(block_of_FIO) * 8)
print("Количество битов по таблице Шеннон-Фано:", len(decoding_of_FIO))
print("____________________________________")
print("\nДекодирование")

encoded = ""
FIO_decoded = ""
for i in range(len(decoding_of_FIO)):
    encoded += decoding_of_FIO[i]
    symbol = next((x for x in symbols if x.code == encoded), None)
    if symbol is not None:
        FIO_decoded += symbol.symbol
        encoded = ""
print(FIO_decoded)
