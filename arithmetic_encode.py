from decimal import Decimal, getcontext
from collections import Counter
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.width', None)

# 28 знаков после запятой
getcontext().prec = 28

def f(message):

    # частоты символов
    frequencies = Counter(message)
    total_symbols = Decimal(sum(frequencies.values()))
    probabilities = {char: Decimal(freq) / total_symbols for char, freq in frequencies.items()}
    sorted_characters = sorted(probabilities.items(), key=lambda item: item[1], reverse=True)

    # начальные отрезки
    ranges = {}
    low = Decimal(0)
    for char, prob in sorted_characters:
        high = low + prob
        ranges[char] = (low, high)
        low = high

    # кодирование
    intervals = []
    low, high = Decimal(0), Decimal(1)
    for char in message:
        char_low, char_high = ranges[char]
        range_width = high - low
        high = low + range_width * char_high
        low = low + range_width * char_low
        intervals.append({"символ": char, "левая граница": str(low), "правая граница": str(high)})

    code = (low + high) / 2

    return probabilities, ranges, intervals, code

message = "МОЛЧАНОВРОСТИСЛАВАНДРЕЕВИЧ"

probabilities, ranges, intervals, code = f(message)

ranges_table = pd.DataFrame(
    [{"символ": char,
      "вероятность": f"{probabilities[char]:.28f}",
      "левая граница": f"{ranges[char][0]:.28f}",
      "правая граница": f"{ranges[char][1]:.28f}"}
     for char in probabilities]
).sort_values(by="вероятность", ascending=False)

intervals_table = pd.DataFrame(intervals)

print("начальная таблица отрезков:")
print(ranges_table)
print("\nтаблица кодирования:")
print(intervals_table, "\n")

value = Decimal(2) ** 87 * Decimal("0.8863005509837524454901952543")
binary_representation = bin(int(value))
print("двоичное представление:", binary_representation, "(", len(binary_representation) - 2, "символов", ")")
