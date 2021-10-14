SUBMISSION_IDS = ["316081355", "318919123"]
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

    return ranks_titles[rank]




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
                print("x_hat[i]: ", x_hat[i])
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




def test():
    # 1
    if poker_hand("5H 5C 6S 7S KD") != 'One Pair' or \
            poker_hand("5D 8C 9S JS AC") != 'High Card' or \
            poker_hand("3D 6D 7D TD QD") != 'Flush' or \
            poker_hand("3C 3D 3S 9S 9D") != 'Full House' or \
            poker_hand("AC TC JC KC QC") != 'Royal Flush' or \
            poker_hand("AC TC JC KC QD") != 'Straight':
        print("error in poker_hand")

    # 2a
    if coin() not in [True, False]:
        print("error in coin")

    # 2b
    if not (-0.2 <= uniform(-0.2, 1.3) < 1.3):
        print("error in uniform")

    # 2c
    if choice(range(7)) not in range(7):
        print("error in choice")

    # 2d
    # if weighted_choice([1, 2, 3], [0.1, 0.1, 0.8]) not in [1, 2, 3]:
    #    print("error in weighted_choice")

    # 2e
    #if not callable(get_biased_coin(0.8)) or get_biased_coin(0.3)() not in [True, False]:
     #   print("error in get_biased_coin")

    # 2f
    #if abs(test_biased_coin(0.3, 100000) - 0.3) > 0.01:
    #    print("error in test_biased_coin")

    # 3a
    if not has_repeat1("ababa", 3) or \
            has_repeat1("ababa", 4) or \
            not has_repeat1("aba",1):
        print("error in has_repeat1()")

    # 3b
    if not has_repeat2("ababa", 3) or \
            has_repeat2("ababa", 4) or \
            not has_repeat2("aba",1):
        print("error in has_repeat2()")

    # 4
    if interpolate([(1, 10), (4, 40)], [4, 2, 3]) != [(4, 40), (2, 20.0), (3, 30.0)] or \
            interpolate([(-3, 9), (-2, 4), (-1, 1), (0, 0), (1, 1), (2, 4), (3, 9)], [-2.5, -1.5, 0.5, 1.5, 2.5]) != [(-2.5, 6.5), (-1.5, 2.5), (0.5, 0.5), (1.5, 2.5), (2.5, 6.5)]:
        print("error in interpolate")

    # 5a
    if not check_goldbach_for_num(10, {2, 3, 5, 7}) or \
            check_goldbach_for_num(10, {2, 3}):
        print("error in check_goldbach_for_num()")

    # 5b
    if not check_goldbach_for_range(20, {2, 3, 5, 7, 11}) or \
            check_goldbach_for_range(21, {2, 3, 5, 7, 11}):
        print("error in check_goldbach_for_range()")

    # 5c
    primes_set = parse_primes('primes.txt')
    if check_goldbach_for_num_stats(20, primes_set) != 2 or \
            check_goldbach_for_num_stats(10, primes_set) != 2:
        print("error in check_goldbach_for_num_stats()")

    if check_goldbach_stats(11, primes_set) != {1: 3, 2: 1}:
        print("error in check_goldbach_stats")

    # 6a
    if add("10", "0") != "10" or \
            add("0", "0") != "0" or \
            add("1001", "11") != "1100":
        print("error in add")

    # 6b
    if sub("10", "0") != "10" or \
            sub("0", "0") != "0" or \
            sub("1000", "11") != "101":
        print("error in sub")

    # 6c
    if inc("0") != "1" or \
            inc("1") != "10" or \
            inc("101") != "110" or \
            inc("111") != "1000" or \
            inc(inc("111")) != "1001":
        print("error in inc")

    # 6d
    if dec("1") != "0" or \
            dec("101") != "100" or \
            dec("100") != "11" or \
            dec(dec("100")) != "10":
        print("error in dec")

    # 6e
    if mult("0", "10") != "0" or \
            mult("0", "0") != "0" or \
            mult("10", "1010") != "10100" or \
            mult("1", "1011") != "1011" or \
            mult("11", "111") != "10101":
        print("error in mult")

