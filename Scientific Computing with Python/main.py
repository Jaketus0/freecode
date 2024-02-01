# text = 'Hello World'
# shift = 3
# alphabet = 'abcdefghijklmnopqrstuvwxyz'

# for char in text:
#     index = alphabet.find(char)
#     print(char, index)

text = 'Hello World'
shift = 3
alphabet = 'abcdefghijklmnopqrstuvwxyz'
encrypted_text = ''
for char in text.lower():
    index = alphabet.find(char) #text itu index ke brp di alphabet
    new_index = index + shift
    encrypted_text += alphabet[new_index]
    print('char:', char, 'encrypted text:', encrypted_text)
