alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

shift = 1
word = "hello"
word_decoded = "ifmmp"

#encode
for letter in word:
    if letter in alphabet:
        print(alphabet[alphabet.index(letter) + shift])

#decode
for letter in word_decoded:
    if letter in alphabet:
        print(alphabet[alphabet.index(letter) - shift])