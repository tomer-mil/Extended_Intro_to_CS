########################################################
#### HUFFMAN CODE
########################################################

def char_count(corpus):
    """ Counts the number of each character in text.
        Returns a dictionary, with keys being the observed characters,
        values being the counts """
    d = {}
    for ch in corpus:
        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1
    return d



def build_huffman_tree(char_count_dict):
    """ Recieves dictionary with char:count entries
        Generates Huffman tree represented as a tuple (left, right) """
    queue = char_count_dict.copy() #keep input intact

    while len(queue) > 1:
        #print(queue)
        # Extract minimum twice
        A, cntA = extract_min_cnt(queue) # key, val with minimal val
        B, cntB = extract_min_cnt(queue) # next minimal
        # Combine two into one and insert
        AB = (A,B)
        cntAB = cntA + cntB
        queue.update({AB: cntAB})

    # now queue has only one pair {htree: total_cnt}
    htree, total_cnt = queue.popitem() # total count must be sum(queue)
    #print(htree)
    return htree   # a tuple representing the tree structure

def extract_min_cnt(d):
    min_node = min(d, key=lambda k: d[k])
    min_cnt = d[min_node]
    d.pop(min_node)
    return min_node, min_cnt


def generate_hcode(htree, prefix=""):
    """ Receives a Huffman tree (tuple) with embedded encoding,
        and a prefix of encodings.
        Returns a dictionary where characters are
        keys and associated binary strings are values."""

    if isinstance(htree, str):  # a leaf in the tree = a single char
        return {htree: prefix}
    else:
        left_tree, right_tree = htree[0], htree[1]
        hcode = {}

        hcode.update(generate_hcode(left_tree, prefix + '0'))
        hcode.update(generate_hcode(right_tree, prefix + '1'))
        # oh, the beauty of recursion...

        return hcode


def compress(text, hcode):
    """ compress text using encoding dictionary """
    assert isinstance(text, str)
    return "".join((hcode[ch] for ch in text))


def decompress(bits, htree):
    """ get a bit string representing compressed text,
        and the Huffman tree (tuple) used to compress it.
        Return original text """
    node = htree  # htree = (htree_left, htree_right)
    result = []

    for bit in bits:
        node = node[int(bit)]  # left or right?
        if isinstance(node, str):  # a leaf in the tree = a single char
            result.append(node)
            node = htree  # restart, back to root

    return "".join(result)  # converts list of chars to a string


def ascii2bits(text):
    """ Translates ASCII text to binary reprersentation using
        7 bits per character. Assume only ASCII chars """
    return "".join([bin(ord(c))[2:].zfill(7) for c in text])


def full_cycle(corpus, text):
    # generate Huffman code from corpus
    print("corpus:\n", corpus, end="\n\n")
    counts = char_count(corpus)
    print(counts, end="\n\n")
    tree = build_huffman_tree(counts)
    print(tree, end="\n\n")
    code = generate_hcode(tree)
    print(code, end="\n\n")

    # compress text using code
    print("text:\n", text, end="\n\n")
    print("text len in bits, no compression:", len(ascii2bits(text)), end="\n\n")
    print(ascii2bits(text), end="\n\n")
    comp = compress(text, code)
    print("compressed len in bits:", len(comp), end="\n\n")
    print(comp, end="\n\n")
    print("compression ratio:", len(comp) / len(ascii2bits(text)), end="\n\n")

    # decompression, back to original code
    decomp = decompress(comp, tree)
    print(decomp, end="\n\n")

    assert decomp == text  # just making sure


####################################################
#### EXECUTIONS WITH VARIOUS TEXTS
####################################################

# <<<<<<<<<<<<<<<<<<<
# short sample texts
# >>>>>>>>>>>>>>>>>>>

corpus = """Selected Alan Perlis Quotations:
      (1) It is easier to write an incorrect program
            than understand a correct one.
      (2) One man's constant is another man's variable. """

text = "fun"

asci = "".join(chr(i) for i in range(128))

##full_cycle(corpus, text) #will raise an error, 'f' is missing from corpus
##full_cycle(corpus + "f", text)
##full_cycle(corpus + asci, text)  #add all ascii chars


# <<<<<<<<<<<<<<
# random texts
# >>>>>>>>>>>>>>
import random


def random_string(n):
    """ Generate a random ascii sequence of length n """
    return "".join(chr(random.randrange(128)) for i in range(n))


def rand_compression_test(n):
    print("compressing a random text of lengrh", n, "by itself")
    rand_text = random_string(n)
    corpus = text = rand_text
    code = generate_hcode(build_huffman_tree(char_count(corpus)))
    comp = compress(text, code)  # best possible corpus is text itself
    print("compression ratio:", len(comp) / len(ascii2bits(text)))






fib_huf = {"a": 1,
           "b": 1,
           "c": 2,
           "d": 3,
           "e": 5,
           "f": 8,
           "g": 13,
           "h": 21}
two_huf = {"a": 1,
           "b": 1,
           "c": 2,
           "d": 3,
           "e": 5,
           "f": 8,
           "g": 13,
           "h": 21}

def my_corpus(number):
    d = {}
    for i in range(number, number * 2):
        d[str(i)] = i
    return d

weird_corpus = my_corpus(300)

a_corpus = char_count("hello my friend")
print(generate_hcode(build_huffman_tree(weird_corpus)))
fib_corpus = "".join([l for l in [k*fib_huf[k] for k in fib_huf]])
print("corpus:", fib_corpus)
fib_tree = build_huffman_tree(fib_huf)
print("fib_tree:", fib_tree)
print("huf_code:", generate_hcode(fib_tree))

# {1: 1011, 2: 1011, 3: 1010, 4: 1001, 5: 1000 ... ,12: 0}