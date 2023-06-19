import utils as Ex5
from bitarray import bitarray


def simple_bsc(path, error_probability):
    file = open(path, "r", encoding="ISO-8859-1")
    file_content = file.read()
    content_to_binary = Ex5.chars_to_binary(file_content).replace(" ", "")
    binary_content_bsc = Ex5.bsc(content_to_binary, error_probability)
    binary_bsc_to_content = Ex5.binary_to_chars(binary_content_bsc)
    different_chars = count_different_chars(file_content, binary_bsc_to_content)
    ber, different_bits = Ex5.ber_calculator(content_to_binary, binary_content_bsc)
    print("N of total bits = ", len(content_to_binary))
    print("N of different bits = ", different_bits)
    print("Bit error rate : " + str(ber))
    print("Number of different chars", different_chars)


def encode(text):
    d = {'1': bitarray('111'), '0': bitarray('000')}
    arr = bitarray()
    arr.encode(d, text)
    return arr


def decode(text):
    decoded_bits = bitarray()
    for i in range(0, len(text), 3):
        bit_slice = text[i:i + 3]
        if bit_slice.count('1') > 3 / 2:
            decoded_bits.append(True)
        else:
            decoded_bits.append(False)
    return decoded_bits


#  A) ii)
def repetition_code_bsc(path, error_probability):
    loops = 0
    media = 0
    file = open(path, "r", encoding="ISO-8859-1")
    file_content = file.read()
    content_to_binary = Ex5.chars_to_binary(file_content).replace(" ", "")
    bsc = Ex5.bsc

    binary_to_repetition = encode(content_to_binary)
    repetition_bsc = bsc(binary_to_repetition, error_probability)  # Ex5.bsc(enc_text, 0.001)
    binary_bsc = decode(repetition_bsc)

    ber, different_bits = Ex5.ber_calculator(str(content_to_binary), str(binary_bsc.to01()))
    different_chars = count_different_chars(file_content, Ex5.binary_to_chars(binary_bsc.to01()))
    file.close()
    print("N of total bits = ", len(binary_bsc.to01()))
    print("N of different bits = ", different_bits)
    print("Bit error rate : " + str(ber))
    print("Number of different chars", different_chars)


# B) ii)
def repetition_code_bsc_with_interleaving(path, error_probability, matrix_rows, matrix_cols):
    loops = 0
    media = 0
    file = open(path, "r", encoding="ISO-8859-1")
    file_content = file.read()
    content_to_binary = Ex5.chars_to_binary(file_content).replace(" ", "")
    interleave = Ex5.interleave(content_to_binary, matrix_rows, matrix_cols)

    bsc = Ex5.bsc

    binary_to_repetition = encode(interleave)
    repetition_bsc = bsc(binary_to_repetition, error_probability)  # Ex5.bsc(enc_text, 0.001)
    binary_bsc = decode(repetition_bsc)
    de_interleave = Ex5.interleave(str(binary_bsc.to01()), matrix_rows, matrix_cols)

    ber, different_bits = Ex5.ber_calculator(str(content_to_binary), str(de_interleave))
    different_chars = count_different_chars(file_content, Ex5.binary_to_chars(de_interleave))
    file.close()

    print("N of total bits = ", len(de_interleave))
    print("N of different bits = ", different_bits)
    print("Bit error rate : " + str(ber))
    print("Number of different chars", different_chars)


#  A) iii)
def encode_hamming(message):
    # Verify message length
    if len(message) != 4:
        raise ValueError("The binary message must have length of 4 bits")

    # Calculate bits p1, p2 and p4
    p1 = message[0] ^ message[1] ^ message[3]
    p2 = message[0] ^ message[2] ^ message[3]
    p4 = message[1] ^ message[2] ^ message[3]

    # Assemble the encoded message with the p bits and the message bits
    encoded_message = [p1, p2, message[0], p4, message[1], message[2], message[3]]

    return encoded_message


def decode_hamming(encoded_message):
    if len(encoded_message) != 7:
        raise ValueError("The message must have a length of 7 bits.")
    p1 = encoded_message[0] ^ encoded_message[2] ^ encoded_message[4] ^ encoded_message[6]
    p2 = encoded_message[1] ^ encoded_message[2] ^ encoded_message[5] ^ encoded_message[6]
    p4 = encoded_message[3] ^ encoded_message[4] ^ encoded_message[5] ^ encoded_message[6]
    error_bit = p4 * 4 + p2 * 2 + p1
    if error_bit != 0:
        encoded_message[error_bit - 1] = 1 - encoded_message[error_bit - 1]
    decoded_message = [encoded_message[2], encoded_message[4], encoded_message[5], encoded_message[6]]

    return decoded_message


def hamming_coding_encoding_bsc(path, errorProbability):
    file = open(path, "r", encoding="ISO-8859-1")
    file_content = file.read()
    text = Ex5.chars_to_binary(file_content).replace(" ", "")
    enc_text = bitarray()  # here you append the parts of the encoding
    dec_text = bitarray()  # here you append the parts of the decoding
    i = 0
    while i < len(text):
        message = [int(text[i]), int(text[i + 1]), int(text[i + 2]), int(text[i + 3])]
        chunk_to_encode = encode_hamming(message)
        for j in range(0, 7):  # the encoding has 7 bits
            enc_text.append(chunk_to_encode[j])
        i += 4
    interference = Ex5.bsc(enc_text, errorProbability)
    i = 0
    while i < len(interference):
        encoded_interference = [int(interference[i]), int(interference[i + 1]), int(interference[i + 2]),
                                int(interference[i + 3]), int(interference[i + 4]), int(interference[i + 5]),
                                int(interference[i + 6])]
        chunk_to_decode = decode_hamming(encoded_interference)
        for j in range(0, 4):
            dec_text.append(chunk_to_decode[j])
        i += 7
    media, counter = Ex5.ber_calculator(str(text), str(dec_text.to01()))
    file.close()
    string_difference = count_different_chars(file_content, Ex5.binary_to_chars(str(dec_text.to01())))
    print("N of total bits = ", len(dec_text.to01()))
    print("N of different bits = ", counter)
    print("Bit Error Rate = ", media)
    print("Number of different chars", string_difference)
    return media


# B) iii)
def hamming_coding_encoding_bsc_with_interleaving(path ,errorProbability, matrx_rows, matrix_cols):
    file = open(path, "r", encoding="ISO-8859-1")
    file_content = file.read()

    # Conversão para binário do texto recebido
    binary = Ex5.chars_to_binary(file_content).replace(" ", "")

    # Interleave aplicado no código binário do texto recebido
    interleave = Ex5.interleave(binary, matrx_rows, matrix_cols)
    enc_text = bitarray()  # here you append the parts of the encoding
    dec_text = bitarray()  # here you append the parts of the decoding
    i = 0

    # Encoding aplicando o algoritmo Hamming

    while i < len(interleave):
        message = [int(interleave[i]), int(interleave[i + 1]), int(interleave[i + 2]), int(interleave[i + 3])]
        chunk_to_encode = encode_hamming(message)
        for j in range(0, 7):  # the encoding has 7 bits
            enc_text.append(chunk_to_encode[j])
        i += 4

    # Canal BSC
    interference = Ex5.bsc(enc_text, errorProbability)
    i = 0

    # Decoding aplicando o algoritmo Hamming

    while i < len(interference):
        encoded_interference = [int(interference[i]), int(interference[i + 1]), int(interference[i + 2]),
                                int(interference[i + 3]), int(interference[i + 4]), int(interference[i + 5]),
                                int(interference[i + 6])]
        chunk_to_decode = decode_hamming(encoded_interference)
        for j in range(0, 4):
            dec_text.append(chunk_to_decode[j])
        i += 7
    media, counter = Ex5.ber_calculator(str(binary), str(dec_text.to01()))
    # print(Ex5.binary_to_chars(str(dec_text.to01())))



    # De-interleaving do código binário
    de_interleave = Ex5.interleave(str(dec_text.to01()), matrx_rows, matrix_cols)

    string_difference = count_different_chars(file_content, Ex5.binary_to_chars(de_interleave))
    file.close()

    print("N of total bits = ", len(dec_text.to01()))
    print("N of different bits = ", counter)
    print("Bit Error Rate = ", media)
    print("Number of different chars", string_difference)
    return media


def count_different_chars(str1, str2):
    count = 0
    for c1, c2 in zip(str1, str2):
        if c1 != c2:
            count += 1
    return count


def main():
    path = "./TestFilesCD/cp.htm"
    ber = 0.001
    matrix_rows = 10000
    matrix_cols = 1000
    """
    print("\n No error control : ")
    simple_bsc(path, ber)
    print("\n Repetition : ")
    repetition_code_bsc(path, ber)
    """
    print("\n Repetition with Interleaved : ")
    repetition_code_bsc_with_interleaving(path, ber, matrix_rows, matrix_cols)
    """
    print("\n Hamming : ")
    hamming_coding_encoding_bsc(path, ber)
    """
    print("\n Hamming Interleaved : ")
    hamming_coding_encoding_bsc_with_interleaving(path, ber, matrix_rows, matrix_cols)


if __name__ == "__main__":
    main()

