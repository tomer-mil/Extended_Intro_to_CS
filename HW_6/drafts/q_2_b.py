def letters():
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    i = 0
    while i <= len(alphabet):
        for l in alphabet:
            yield l
            i += 1

    if i > len(alphabet):
        for g in range(len(alphabet), 256):
            g = alphabet[g] + alphabet[g]
            yield g
            i += 1


def huffman():
    mila = ""
    for i in range(256, 512):
        my_letters = letters()
        n = next(my_letters)
        print("n:", n)
        mila += n * i

    return mila


word = huffman()

def bad_coding(x):
    z = (x[0] + x[1]) % 2
    return (x + [z]) * 4

p = [1, 0]
# p2 = [0, 1]

print("code:", p, "|", bad_coding(p))
print("code:", p2, "|", bad_coding(p2))