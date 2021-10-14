# Skeleton file for HW3 - Spring 2020 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw3_ID.py).

# Enter all IDs of participating students as strings, separated by commas.
# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["316081355", "318919123"]

import random


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
def split_bits(num):

    assert len(num) == 64

    number_dict = {
        "s" : num[:1],
        "e" : num[1:12],
        "e_10" : (int(num[1:12], 2) - 1023),
        "f" : num[12:],
        "f_10" : int(num[12:], 2)
    }
    return number_dict

def float_add(a, b):
    # splitting bits
    a_dict = split_bits(a)
    b_dict = split_bits(b)

    # checking if a = -b or b = -a
    if      (a_dict["e"] == b_dict["e"])\
            and (a_dict["f"] == b_dict["f"])\
            and (a_dict["s"] != b_dict["s"]):
        return "0" * 64

    final_res = {
        "s": "0",
        "e": "",
        "e_10": "",
        "f": "",
        "f_10": 0
    }

    a_dict["f"] = "1" + a_dict["f"]
    b_dict["f"] = "1" + b_dict["f"]

    if a_dict["e_10"] > b_dict["e_10"]:
        delta = a_dict["e_10"] - b_dict["e_10"]
        b_dict["f"] = ("0" * delta) + b_dict["f"]
        b_dict["f"] = b_dict["f"][:len(b_dict["f"]) - delta]
        b_dict["f_10"] = int(b_dict["f"], 2)


    elif a_dict["e_10"] < b_dict["e_10"]:
        delta = b_dict["e_10"] - a_dict["e_10"]
        b_dict["f"] = ("0" * delta) + a_dict["f"]
        b_dict["f"] = a_dict["f"][:len(a_dict["f"]) - delta]
        b_dict["f_10"] = int(a_dict["f"], 2)

    # checking for symbol
    if a_dict["s"] == "1":
        a_dict["f_10"] = int(("-" + str(a_dict["f_10"])))

    if b_dict["s"] == "1":
        b_dict["f_10"] = int(("-" + str(b_dict["f_10"])))

    final_res["f_10"] = a_dict["f_10"] + b_dict["f_10"]

    if final_res["f_10"] < 0:
        final_res["s"] = "1"

    final_res["f"] = str(bin(abs(final_res["f_10"])))[2:]

    if len(final_res["f"]) > 52:
        final_res["f"] = final_res["f"][1:]
        while len(final_res["f"]) > 52:
            final_res["f"] -= final_res["f"][-1:-2:-1]

    elif len(final_res["f"]) < 52:
        final_res["f"] = "0" * (52 - len(final_res["f"])) + final_res["f"]

    max_e = max(a_dict["e_10"], b_dict["e_10"])
    max_e += 1023
    max_e = str(bin(max_e))[2:]

    if len(max_e) < 11:
        max_e = ("0" * (11 - len(max_e))) + max_e

    final_res["e"] = max_e

    return final_res["s"] + final_res["e"] + final_res["f"]


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


def generate_sorted_blocks(lst, k) :
    sorted_lst = []
    for i in range(0, len(lst), k) :
        div_lst = lst[i:i + k] #seperate to n/k lists
        selection_sort(div_lst)
        sorted_lst.append(div_lst)
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
def merge_sorted_blocks_1(lst, left, right):   #aid func- binary_search
    if (right - left) == 1:
        return lst[left]
    if (right - left) == 2:
        return merge(lst[left], lst[left + 1])
    middle = (left + right) // 2
    return merge(merge_sorted_blocks_1(lst, left, middle), merge_sorted_blocks_1(lst, middle, right))


def merge_sorted_blocks_2(lst, k):
    return merge_sorted_blocks(generate_sorted_blocks(lst, k))  #aid func generate sorted blocks


def merge_sorted_blocks(lst):
    return merge_sorted_blocks_1(lst, 0, len(lst))






############
# QUESTION 4
############

#a


def find(lst, s):
    n = len(lst)
    left = 0
    right = n-1
    if n == 1:
        if s != lst[0]:
            return None
        return 0
    while left < right:
        mid = (left+right)//2
        if s == lst[mid]:
            return mid
        if s == lst[mid + 1]:
            return mid + 1
        if s == lst[mid - 1]:
            return mid - 1
        elif s < lst[mid]:
            right = mid-1
        else:
            left = mid+1
    return None

#b


def sort_from_almost(lst):
    for i in range(len(lst)-1):
        if lst[i] > lst[i+1]:
            temp = lst[i+1]
            lst[i+1] = lst[i]
            lst[i] = temp


#c


def find_local_min(lst):
    m = 0
    for i in range(len(lst) - 1):
        if lst[1] == 0:
            return i
        elif lst[i] < lst[i+1] or lst[i] == lst[i+1]:
            if lst[i] < lst[i-1] or lst[i] == lst[i-1]:
                m += i
        elif i == 0:
            if lst[0] < lst[1] or lst[0] == lst[1]:
                return 0
    return m



############
# QUESTION 5
############

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

def int_to_string(k, n):
    assert 0 <= n <= 5 ** k - 1

    letters_value = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e"
    }
    string_lst = []
    for i in range(k):
        num = n % 5
        string_lst.append(letters_value[num])
        n //= 5
    string_lst = string_lst[::-1]
    return "".join(string_lst)

def sort_strings1(lst, k):
    rank_lst = [0] * (5 ** k)
    sorted_list = []

    for elem in lst:
        rank_lst[string_to_int(elem)] = 1

    for rank in range(len(rank_lst)):
        if rank_lst[rank] == 1:
            sorted_list.append(int_to_string(k, rank))

    return sorted_list

def sort_strings2(lst, k):

    sorted_list = []

    for i in range(5 ** k):
        str_to_check = int_to_string(k, i)
        if str_to_check in lst:
            sorted_list.append(str_to_check)

    return sorted_list

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

    sort_from_almost(almost_sorted_lst)
    if almost_sorted_lst != sorted(almost_sorted_lst):
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

test()