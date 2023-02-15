# шифр
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def shift_encode(string):

    string_encoded = ''
    for letter in string:

        position = alphabet.find(letter)
        position_next = (position + 1) % len(alphabet)
        next_latter = alphabet[position_next]
        string_encoded += next_latter

    return string_encoded

sifr = shift_encode("абзаца")
print(sifr) # зашифровывает

def shift_decode(string):

    string_encoded = ''
    for letter in string:

        position = alphabet.find(letter)
        position_next = (position - 1 + 33) % len(alphabet)
        next_latter = alphabet[position_next]
        string_encoded += next_latter

    return string_encoded

print(shift_decode(sifr))