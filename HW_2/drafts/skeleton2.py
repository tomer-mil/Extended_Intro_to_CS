#Skeleton file for HW2 - Winter 2021 - extended intro to CS

#Add your implementation to this file

#you may NOT change the signature of the existing functions.

#Change the name of the file to include your ID number (hw2_ID.py).

#Enter all IDs of participating students as strings, separated by commas.
#For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.
SUBMISSION_IDS = ["318919123", "316081355"]
import random


############
# QUESTION 1
############


def convert_values(symbols):
    converted = []
    for s in symbols:
        if s == "T":
            converted.append("10")
        elif s == "J":
            converted.append("11")
        elif s == "Q":
            converted.append("12")
        elif s == "K":
            converted.append("13")
        elif s == "A":
            converted.append("14")
        else:
            converted.append(s)

    return converted


def check_straight(values):
    for v in range(0, 5):
        values[v] = int(values[v])
    values.sort()

    i = 0
    while values[i] + 1 == values[i + 1]:
        i += 1
        if i == 4:
            return 5
    else:
        return 0


def check_flush(symbols):
    j = 0
    while symbols[j] == symbols[j + 1]:
        j += 1
        if j == 4:
            return 6
    else:
        return 0


def check_pairs(values):
    for i in range(0, 5):
        counter = values.count(values[i])

        if counter == 4:
            return 8

        elif counter == 3:
            if i == 0:
                if values[3] == values[4]:
                    return 7
                else:
                    return 4
            elif i > 0:
                return 4

        elif counter == 2:
            if i == 0:
                for j in range(2, 5):
                    cnt = values.count(values[j])
                    if cnt == 1:
                        if values[3] == values[4]:
                            return 3
                        else:
                            return 2
                    elif cnt == 2:
                        return 3
                    elif cnt == 3:
                        return 7
            if i == 1:
                if values[3] == values[4]:
                    return 3
            if i > 1:
                return 2

        elif counter == 1:
            if i == 3:
                return 1


def poker_hand(hand):
    rank = 0
    # Retrieving data from str-hand
    hand_split = hand.split()

    hand_symbols = [s[-1] for s in hand_split]
    values = [v[0] for v in hand_split]
    values_converted = convert_values(values)

    # Checking for rank
    is_straight = check_straight(values_converted)
    is_flush = check_flush(hand_symbols)
    is_pair = check_pairs(values_converted)

    # Checking if straight flush or royal straight flush
    if is_straight and is_flush:
        if values_converted[0] == 10:
            rank = 10
        else:
            rank = 9

    # Checking what to print
    if rank < 9:
        rank = max(is_pair, is_flush, is_straight, 1)

    ranks_titles = ["Error", "High Card", "One Pair", "Two Pairs", "Three of a Kind", "Straight", "Flush",
                    "Full House", "Four of a Kind", "Straight Flush", "Royal Flush"]

    print(ranks_titles[rank])




############
# QUESTION 2
############

# 2a
def coin():
    chance = random.random()
    if chance >= 0.5:
        return True
    else:
        return False

# 2b 
def uniform(a,b):
    rnd = random.random()
    return a + (b-a) * rnd

# 2c
def choice(seq):
    rnd = random.random()
    a = len(seq)
    chance = (a - 1) * rnd
    return seq[round(chance)]

# 2d
def weighted_choice(seq, weights):
    rnd = uniform(0, len(seq))

    rnd / len(seq)
    b = len(seq)
    for i in range(0, len(seq)):
        chance = (weights[i] * (b - 1)) * rnd
    r_chance = round(chance)

    return seq[r_chance]

# 2e
def get_biased_coin(p):

    return lambda p: random.random() <= p

# 2f
def test_biased_coin(p, num_flips):
    cnt = 0
    tester = get_biased_coin(p)
    for i in range(num_flips):
        if tester(p):
            cnt += 1
    return cnt / num_flips


############
# QUESTION 3
############

# 3a
def has_repeat1(s, k):
    s_list = list(s)
    segments_list = []

    for j in range(0, (len(s) - k) + 1):
        separator = ""
        segments = separator.join(s_list[j:k + j:])
        segments_list.append(segments)

    for i in range(0, len(segments_list)):
        if segments_list.count(segments_list[i]) > 1:
            return True
        else:
            return False

# 3b
def has_repeat2(s, k):
    for i in range(0, len(s) - (k - 1)):
        segment = s[i:i + k]
        for j in range(i + 1, len(s) - (k - 1)):
            compared_segment = s[j:j + k]
            if segment == compared_segment:
                return True
    return False


############
# QUESTION 4
############

def interpolate(xy, x_hat):
    def interpolate(xy, x_hat):

        new_values = []

        for i in range(0, len(x_hat)):

            tmp_right = []
            tmp_left = []

            for j in range(0, len(xy)):  # Sorting xy
                if x_hat[i] >= xy[j][0]:
                    tmp_left.append(xy[j])
                else:
                    tmp_right.append(xy[j])

            max_left = max(tmp_left)  # Finding closest (x,y) points from right and left
            min_right = min(tmp_right)

            m = (min_right[1] - max_left[1]) / (min_right[0] - max_left[0])  # Parameters for equation
            c = min_right[1] - (m * min_right[0])

            y_hat = m * float(x_hat[i]) + c  # Creating the equation and finding y_hat

            new_point = (x_hat[i], y_hat)
            new_values.append(new_point)

        return new_values


############
# QUESTION 5
############

def parse_primes(filename):
    primes = []
    with open(filename, "r") as f:
        for line in f:
            primes += [int(num_str) for num_str in line.split(" ")[:-1] if num_str]
    return set(primes)


# 5a
def check_goldbach_for_num(n, primes_set):

    for i in primes_set:
        if n - i in primes_set:
            return True
    return False

# 5b
def check_goldbach_for_range(limit, primes_set):

    range_to_check = [n for n in range(4, limit, 2)]
    for n in range_to_check:
        if not check_goldbach_for_num(n, primes_set):
            return False
    return True


# 5c1
def check_goldbach_for_num_stats(n, primes_set):
    cnt = 0
    for i in primes_set:
        if i < n:
            if n - i in primes_set:
                cnt += 1
    if cnt == 0:
        return 0
    elif cnt % 2 == 0:
        return cnt // 2
    else:
        return (cnt + 1) // 2

# 5c2    
def check_goldbach_stats(limit, primes_set):
    range_for_check = [n for n in range(4, limit, 2)]
    stats_dict = {}

    for n in range_for_check:

        cnt = check_goldbach_for_num_stats(n, primes_set)
        if cnt in stats_dict.keys():
            stats_dict[cnt] += 1

        else:
            d = {cnt: 1}
            stats_dict.update(d)

    return stats_dict

############
# QUESTION 6
############

# 6a
def add(bin1, bin2):

    result = ""
    carry = "0"

    l_bin1 = len(bin1)
    l_bin2 = len(bin2)

    if l_bin1 == l_bin2:

        bin1 = list(bin1[::-1])
        bin2 = list(bin2[::-1])

    elif l_bin1 > l_bin2:

        bin2 = bin2[::-1] + ("0" * (l_bin1 - l_bin2))
        bin2 = list(bin2)
        bin1 = list(bin1[::-1])

    else:
        bin1 = bin1[::-1] + ("0" * (l_bin2 - l_bin1))

        bin1 = list(bin1)
        bin2 = list(bin2[::-1])

    for i in range(max(l_bin1, l_bin2)):
        if bin1[i] == "1":
            if bin2[i] == "0":
                if carry == "0":
                    result += "1"
                    carry = "0"
                else:
                    result += "0"
                    carry = "1"
            else:
                if carry == "0":
                    result += "0"
                    carry = "1"
                else:
                    result += "1"
                    carry = "1"
        elif bin1[i] == "0":
            if bin2[i] == "0":
                if carry == "0":
                    result += "0"
                    carry = "0"
                else:
                    result += "1"
                    carry = "0"
            elif bin2[i] == "1":
                if carry == "0":
                    result += "1"
                    carry = "0"
                else:
                    result += "0"
                    carry = "1"

    carry_result = result + carry
    carry_result = carry_result[::-1]

    if carry_result[0] == "0":
        carry_result = carry_result[1::]
        return carry_result
    else:
        return carry_result


# 6b
def sub(bin1, bin2):

    if bin1 == bin2:
        return "0"

    result = ""

    l_bin1 = len(bin1)
    l_bin2 = len(bin2)

    if l_bin1 == l_bin2:

        bin1 = list(bin1[::-1])
        bin2 = list(bin2[::-1])

    elif l_bin1 > l_bin2:
        bin2 = bin2[::-1] + ("0" * (l_bin1 - l_bin2))

        bin2 = list(bin2)
        bin1 = list(bin1[::-1])

    else:
        bin1 = bin1[::-1] + ("0" * (l_bin2 - l_bin1))

        bin1 = list(bin1)
        bin2 = list(bin2[::-1])

    for i in range(max(l_bin1, l_bin2)):

        if bin1[i] == "1":
            if bin2[i] == "0":
                result += "1"
            else:
                result += "0"

        elif bin1[i] == "0":
            if bin2[i] == "0":
                result += "0"
            else:
                result += "1"
                j = i
                while bin1[j + 1] == "0":
                    bin1[j + 1] = "1"
                    j += 1
                if j == i:
                    bin1[j + 1] = "0"
                else:
                    bin1[j + 1] = "0"

    result = result[::-1]

    while result[0] == "0":
        result = result[1::]

    return result


# 6c
def inc(binary):
    return add(binary, "1")

# 6d
def dec(binary):
    return sub(binary, "1")

# 6e
def mult(bin1, bin2):

    if bin1 == "0" or bin2 == "0":
        return "0"
    elif bin1 == "1":
        return bin2
    elif bin2 == "1":
        return bin1

    tmp_list = []

    l_bin1 = len(bin1)
    l_bin2 = len(bin2)

    bin1 = bin1[::-1]
    bin2 = bin2[::-1]

    if l_bin1 >= l_bin2:
        min_bin = bin2
        max_bin = bin1
    else:
        min_bin = bin1
        max_bin = bin2


    for i in range(len(min_bin)):
        result = ""
        for k in range(len(max_bin)):

            if min_bin[i] == "1":

                if max_bin[k] == "0":
                    result += "0"
                else:

                    result += "1"
            else:
                result += "0" * k

        pad = lambda tmp_result: (tmp_result[::-1] + ("0" * i))
        pad_result = pad(result)
        tmp_list.append(pad_result)

    i = 0
    b1 = tmp_list[0]
    while i < len(tmp_list) - 1:
        b2 = tmp_list[i + 1]

        b3 = add(b1, b2)
        b1 = b3
        i += 2

    add(b1, tmp_list[len(tmp_list) - 1])
    return b1


