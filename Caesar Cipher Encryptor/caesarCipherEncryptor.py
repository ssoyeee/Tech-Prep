def caesarCipherEncryptor(string, key):
    # ascii 97-122
    answer = []
    askiistring=0
    for letter in string:
        askiistring = ((ord(letter)-97)+key)%26
        answer.append(chr(97+askiistring))
    return ''.join(answer)