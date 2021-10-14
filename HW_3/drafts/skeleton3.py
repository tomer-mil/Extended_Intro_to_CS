# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = []

import random

print("working")
############
# QUESTION 2
############

def text_2_16bits(text):
    lst = []
    for c in text:
        bin_ord_c = bin(ord(c))[2:]
        if len(bin_ord_c) < 16:
            zeroes = "0" * (16 - len(bin_ord_c))
            padded = (bin_ord_c[::-1] + zeroes)[::-1]
            bin_ord_c = padded

        lst += bin_ord_c
    return "".join(lst)

# Q2 - A, b
def bits_2_text(b_text):
    lst = []
    for i in range(0, len(b_text), 16):
        lst += [chr(int(b_text[i:i+16], 2))]

    return "".join(lst)

# Q2 - B
def float_add(a, b):
    pass  # replace this with your code


############
# QUESTION 3
############

# a
def swap(lst, i, j):
    tmp = lst[i]
    lst[i] = lst[j]
    lst[j] = tmp


def selection_sort(lst):
    """ sort lst (in-place) """
    n = len(lst)
    for i in range(n):
        m_index = i
        for j in range(i + 1, n):
            if lst[m_index] > lst[j]:
                m_index = j
        swap(lst, i, m_index)
    return None


def generate_sorted_blocks(lst, k):

    sorted_lst = []
    len_lst = len(lst)
    modulo = len(lst) % k

    if len(lst) % k == 0:
        len_lst -= k

    no_remainder = len_lst - modulo

    for i in range(0, no_remainder + 1, k):

        chunk = lst[i:i + k]
        selection_sort(chunk)
        sorted_lst.append(chunk)

    return sorted_lst


def merge(A, B):
    """ merging two lists into a sorted list
        A and B must be sorted! """
    n = len(A)
    m = len(B)
    C = [0 for i in range(n + m)]

    a = 0
    b = 0
    c = 0
    while a < n and b < m:  # more element in both A and B
        if A[a] < B[b]:
            C[c] = A[a]
            a += 1
        else:
            C[c] = B[b]
            b += 1
        c += 1

    C[c:] = A[a:] + B[b:]  # append remaining elements (one of those is empty)

    return C


# c
def merge_sorted_blocks(lst):
    pass  # replace this with your code


def sort_by_block_merge(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))


############
# QUESTION 4
############

def find(lst, s):
    pass  # replace this with your code


def sort_from_almost(lst):
    pass  # replace this with your code

def find_local_min(lst):
    pass  # replace this with your code


############
# QUESTION 5
############

# a
def string_to_int(s):
    letters_value = {
        "a": 0,
        "b": 1,
        "c": 2,
        "d": 3,
        "e": 4
    }

    k = len(s)
    result = ""

    for i in range(k):
        result += str(letters_value[s[i]])

    int_result = int(result, 5)
    return int_result


# b

def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1

    letters_value = {
        "0": "a",
        "1": "b",
        "2": "c",
        "3": "d",
        "4": "e"
    }

    n_base5 = convert_base(n, 5)
    str_n = str(n_base5)
    result = ""

    for i in str_n:
        result += letters_value[i]

    return result


# c
def sort_strings1(lst, k):
    pass  # replace this with your code


# e
def sort_strings2(lst, k):
    pass  # replace this with your code


########
# Tester
########

def test():
    # q2 - a
    
    text = "Hi There"
    text_bits = text_2_16bits(text)
    if bits_2_text(text_bits) != text:
        print("error in text reconstruction")
        
    if text_bits.count("0") + text_bits.count("1") != len(text_bits):
        print("error: non binary characters in text_2_16bits")

    if len(text_bits) % 16 != 0:
        print("error wrong length for text_2_16bits output")

    # q2 - b
    a = "0100000000101000000000000000000000000000000000000000000000000000"
    b = "0011111111101000000000000000000000000000000000000000000000000000"
    res = "0100000000101001100000000000000000000000000000000000000000000000"
    if float_add(a, b) != res:
        print("error in float_add of 12 + 0.75")
        
    # q3
    lst = [610, 906, 308, 759, 15, 389, 892, 939, 685, 565]
    if generate_sorted_blocks(lst, 2) != \
            [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 3) != \
            [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]:
        print("error in generate_sorted_blocks")
    if generate_sorted_blocks(lst, 10) != \
            [[15, 308, 389, 565, 610, 685, 759, 892, 906, 939]]:
        print("error in generate_sorted_blocks")

    block_lst1 = [[610, 906], [308, 759], [15, 389], [892, 939], [565, 685]]
    if merge_sorted_blocks(block_lst1) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")
    block_lst2 = [[308, 610, 906], [15, 389, 759], [685, 892, 939], [565]]
    if merge_sorted_blocks(block_lst2) != \
            [15, 308, 389, 565, 610, 685, 759, 892, 906, 939]:
        print("error in merge_sorted_blocks")

    # q4
    almost_sorted_lst = [2, 1, 3, 5, 4, 7, 6, 8, 9]

    if find(almost_sorted_lst, 5) != 3:
        print("error in find")

    if find(almost_sorted_lst, 50) != None:
        print("error in find")

    if sort_from_almost(almost_sorted_lst) != sorted(almost_sorted_lst):
        print("error in sort_from_almost")
    
    lst = [5, 6, 7, 5, 1, 1, 99, 100]
    pos = find_local_min(lst)
    if pos not in (0, 4, 5):
        print("error in find_local_min")

    # q5
    lst_num = [random.choice(range(5 ** 4)) for i in range(15)]
    for i in lst_num:
        s = int_to_string(4, i)
        if s is None or len(s) != 4:
            print("error in int_to_string")
        if (string_to_int(s) != i):
            print("error in int_to_string or in string_to_int")

    lst1 = ['aede', 'adae', 'dded', 'deea', 'cccc', 'aacc', 'edea', 'becb', 'daea', 'ccea']
    if sort_strings1(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings1")

    if sort_strings2(lst1, 4) \
            != ['aacc', 'adae', 'aede', 'becb', 'cccc', 'ccea', 'daea', 'dded', 'deea', 'edea']:
        print("error in sort_strings2")
