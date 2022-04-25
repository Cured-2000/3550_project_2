# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import codecs
import sys


def decrypt(cypher_text):
    length = len(cypher_text)-1
    cypher_text_doubles = []
    plain_text = []
    n = 2

    #initialize array
    for t in cypher_text:
        plain_text.append('')

    #devide the lines of cipher text into pairs of 2 into a 2D array
    for i in cypher_text:
        cypher_text_doubles.append([i[j:j+n] for j in range(0, len(i), n)])
    num_rotate = len(cypher_text_doubles)

    #compare each double in the list of hex values
    for i in range(len(cypher_text_doubles)):
        for k in range(len(cypher_text_doubles[i])):
            space_count = 0
            fail_count = 0
            zero_count = 0
            found = ''
            for j in range(i+1,len(cypher_text_doubles)):
                # prevent comparison of the same 2 lists
                a = set(cypher_text_doubles[i])
                b = set(cypher_text_doubles[j])
                if a == b:
                    continue

                # covert string into hex values

                hex_val = int(cypher_text_doubles[i][k], 16) ^ int(cypher_text_doubles[j][k], 16)

                # xor two values together and decode the result into ascii

                if hex_val <= int('7F', 16) and len(hex(hex_val)[2:]) == 2:
                    binary_val = codecs.decode(hex(hex_val)[2:], 'hex')
                    ascii_str = str(binary_val, 'utf-8')

                elif hex_val == 0:
                    ascii_str = '\0'

                else:
                    ascii_str = '!'

                #decide if the result is a space

                if ord(ascii_str) >= 65 or ord(ascii_str) == 0:

                    if (ord(ascii_str) != 0):
                        #saves a potential found value
                        space_count += 1
                        found = ascii_str


                    elif (ord(ascii_str) == 0):
                        zero_count += 1

                else:
                    fail_count += 1

                #check what char should be appended to the text

                if fail_count + zero_count == length:
                    plain_text[i] += str('_')

                elif (space_count + zero_count == length):
                    plain_text[i] += str(' ')

                elif (space_count + zero_count + fail_count == length):
                    if found.islower():
                        plain_text[i] += str(found.capitalize())
                    else:
                        plain_text[i] += str(found.lower())



    #prints the found plain text
    print("found plaintext:")
    count = 0
    for i in plain_text[0]:
        if i.isalpha() or i.isspace():
            count += 1

    for j in plain_text:
        print(j)
    print("found" ,count , "characters out of", len(plain_text[0]))


def read_my_file():
    try:
        #open files
        d = input("enter ciphertext file name:")
        f = open(d, "r")
        read = f.readlines()
        cypher_text = []

        #remove newlines from cypher text
        for i in range(len(read)):
            cypher_text.append(read[i].rstrip('\n'))
        decrypt(cypher_text)
    except FileNotFoundError:
        print("could not open " )




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    read_my_file()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
