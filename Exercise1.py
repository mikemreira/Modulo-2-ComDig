import Exercise5 as Ex5
from bitarray import bitarray
import pycrc


""" A) i)
1.1 - texto "alice29.txt" -> BER (0.0995, 0.1, 0.1, 0.1, 0.099) -> n de bits (1187856)
1.2 - texto "Person.java" -> BER (0.0901, 0.0989, 0.1029, 0.0942, 0.0995) -> n de bits (50720)
1.3 - texto "progc.c" -> BER (0.1004, 0.0981, 0.100, 0.101, 0.102) -> n de bits (316896)
1.4 - texto "cp.htm" -> BER (0.0984, 0.105, 0.0997, 0.0984, 0.0963) -> n de bits (196824)

2.1 - texto "alice29.txt" -> BER (0.0097, 0.0095, 0.01, 0.00993, 0.0096) com BER 10^-2
2.2 - texto "Person.java" -> BER (0.0115, 0.0110, 0.0084, 0.0101, 0.0101) com BER 10^-2
2.3 - texto "progc.c" -> BER (0.010059) com BER 10^-2
2.4 - texto "cp.htm" -> BER (0.009897) com BER 10^-2

3.1 - texto "alice29.txt -> BER (0.00099849)
3.2 - texto "Person.java -> BER (0.0011456)
3.3 - texto "progc.c" -> BER (0.0009694)
3.4 - texto "cp.htm" -> BER (0.000975)

4.1 - texto "alice29.txt" -> BER (0.00010035)
4.2 - texto "Person.java" -> BER (0.0001322)
4.3 - texto "progc.c" -> BER (0.00009178)
4.4 - texto "cp.htm" -> BER (0.0001208)

5.1 - texto "alice29.txt" -> BER (0.00000836)
5.2 - texto "Person.java" -> BER (0.00004406)
5.3 - texto "progc.c" -> BER (0.00004406)
5.4 - texto "cp.htm" -> BER (0.0000258866)
"""

""" A) ii)
1.1 - texto "alice29.txt" -> BER (0.01586) com BER 10^-1
1.2 - texto "Person.java" -> BER (0.017133) com BER 10^-1
1.3 - texto "progc.c" -> BER (0.016297) com BER 10^-1 
1.4 - texto "cp.htm" -> BER (0.014459) com BER 10^-1

2.1 - texto "alice29.txt" -> BER (0.0001694) com BER 10^-2
2.2 - texto "Person.java" -> BER (0.0002011) com BER 10^-2
2.3 - texto "progc.c" -> BER (0.0001616) com BER 10^-2
2.4 - texto "cp.htm" -> BER (0.0001677) com BER 10^-2

3.1 - texto "alice29.txt -> BER (0.0000023572)
3.2 - texto "Person.java -> BER (0.000003943)
3.3 - texto "progc.c" -> BER (0.0000018934)
3.4 - texto "cp.htm" -> BER (0.0000020323)

4.1 - texto "alice29.txt" -> BER (0.0)
4.2 - texto "Person.java" -> BER (0.0)
4.3 - texto "progc.c" -> BER (0.0)
4.4 - texto "cp.htm" -> BER (0.0)

5.1 - texto "alice29.txt" -> BER (0.0)
5.2 - texto "Person.java" -> BER (0.0)
5.3 - texto "progc.c" -> BER (0.0)
5.4 - texto "cp.htm" -> BER (0.0)

"""

d = {'1': bitarray('111'), '0': bitarray('000')}


def encode(text):
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


def repetition_code_bsc():
    loops = 0
    media = 0
    file = open("./TestFilesCD/alice29.txt", "r", encoding="ISO-8859-1")
    text = Ex5.to_binary(file.read()).replace(" ", "")
    while loops < 1:
        enc_text = encode(text)
        interference = Ex5.bsc(enc_text, 0.001)
        dec_text = decode(interference)
        media, counter = Ex5.ber_calculator(str(text), str(dec_text.to01()))
        loops += 1
    file.close()
    print("N of total bits = ", len(dec_text.to01()))
    print("N of different bits = ", counter)
    print(media / loops)


def hamming_coding_encoding_bsc():
    print("hamming")
    encoder = pycrc.hamming.Hamming74.encode('1010')
    print(encoder)
    encoder.encode()


def main():
    # repetition_code_bsc()
    hamming_coding_encoding_bsc()


if __name__ == "__main__":
    main()
