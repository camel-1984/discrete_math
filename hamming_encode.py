def hamming_encode(data):

    # исходное сообщения
    m = len(data)

    # проверочные биты
    r = 0
    while 2**r < m + r + 1:
        r += 1

    # длина закодированного сообщения
    total_length = m + r

    # расположение проверочных битов
    encoded = ['_' for _ in range(total_length)]
    j = 0  # Индекс для исходных данных
    for i in range(1, total_length + 1):
        if (i & (i - 1)) == 0:
            encoded[i - 1] = 'P'
        else:
            encoded[i - 1] = data[j]
            j += 1

    # заполнение проверочные битов
    for i in range(r):
        parity_pos = 2**i - 1
        parity_sum = 0
        for j in range(parity_pos, total_length, 2**(i + 1)):
            parity_sum += sum(int(encoded[k]) for k in range(j, min(j + 2**i, total_length)) if encoded[k] != 'P')
        encoded[parity_pos] = '0' if parity_sum % 2 == 0 else '1'

    return ''.join(encoded)

data = "111000101110010010010111110010001110011011101001010011001110001101011011100100111111110"

encoded_message = hamming_encode(data)

print("закодированное сообщение методом Хэмминга:")
print(encoded_message, "(",len(encoded_message), "символа",")", "\n")
print("RATE =", len(data) / len(encoded_message))
