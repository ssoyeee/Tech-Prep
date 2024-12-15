def caesarCipherEncryptor(string, key):
    # ascii 97-122
    answer = []
    asciistring=0
    for letter in string:
        asciistring = ((ord(letter)-97)+key)%26
        answer.append(chr(97+asciistring))
    return ''.join(answer)
