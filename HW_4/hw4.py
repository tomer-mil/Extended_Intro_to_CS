# Skeleton file for HW4 - winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw4_ID.py).
SUBMISSION_IDS = ["316081355"]

############
# QUESTION 2
############

 # c
def rec_slice_binary_search(lst, key):
    n = len(lst)
    if n <= 0:
        return None

    if key == lst[n//2]:
        return lst

    elif key < lst[n//2]:
        return rec_slice_binary_search(lst[0:n//2], key)

    else:
        return rec_slice_binary_search(lst[n//2 + 1: n], key)

############
# QUESTION 3
############

# b
def had_local(n, i, j):

    def bin_lst(x, bin_len):

        bin_x = bin(x)
        bin_x_len = len(bin_x)
        bin_x_lst = []

        for bit in range(bin_x_len - 1, 1, -1):
            bin_x_lst.append(bin_x[bit])
        padding = ["0"] * (bin_len - (bin_x_len - 2))
        bin_x_lst.extend(padding)
        return bin_x_lst

    def check_for_bit(n, bin_i, bin_j):
        if n == 0:
            return 0

        i_bit_to_check = bin_i.pop()
        j_bit_to_check = bin_j.pop()

        n -= 1

        if j_bit_to_check == "1" and i_bit_to_check == "1":
            if check_for_bit(n, bin_i, bin_j) == 1:
                return 0
            else:
                return 1
        else:
            return check_for_bit(n, bin_i, bin_j)


    i_bin_lst = bin_lst(i, n)
    j_bin_lst = bin_lst(j, n)

    return check_for_bit(n, i_bin_lst, j_bin_lst)


# d
had_complete = lambda n: [[had_local(n, i, j) for j in range(pow(2, n))] for i in range(pow(2, n))]

############
# QUESTION 4
############

# a


def create_matrix(m, path):
    new_m = []

    for i in range(len(m)):
        row = [0 for x in m]
        new_m.append(row)

    for c in path:
        new_m[0][0] = path.count((len(m) - 1, len(m) - 1))
        new_m[c[0]][c[1]] += 1

    return new_m


def find_zero_paths(m):
    
    def find_zero_paths_with_index(m, i, j, path):

    if i == (len(m) - 1) and j == (len(m) - 1):
        if m[i][j] == 0:
            return 1

    if i < len(m) - 1:
        if m[i + 1][j] == 0:
            find_zero_paths_with_index(m, i + 1, j, path)
            path.append((i + 1, j))

    if j < len(m) - 1:
        if m[i][j + 1] == 0:
            find_zero_paths_with_index(m, i, j + 1, path)
            path.append((i, j + 1))

    else:
        return 0
    
    path = []
    find_zero_paths_with_index(m, 0, 0, path)
    new_m = create_matrix(m, path)
    return path.count((len(m) - 1, len(m) - 1)), new_m

############
# QUESTION 5
############

# a
def find_max_profit(A, W, n, k):
    result = 0

    if n < 0 or k <= 0:
        return 0

    elif k < W[n]:
        result = find_max_profit(A, W, n - 1, k)

    elif k >= W[n]:

        not_in_bag = find_max_profit(A, W, n - 1, k)
        in_bag = A[n] + find_max_profit(A, W, n - 1, k - W[n])
        result = max(not_in_bag, in_bag)

    return result

# c

def find_max_profit_fast(A, W, n, k):
    profit_dict = {}

    def find_max_profit_with_dict(A, W, n, k, profit_dict):
        result = 0
        if (n, k) in profit_dict:
            return profit_dict[(n, k)]

        else:
            if n < 0 or k <= 0:
                return 0

            elif k < W[n]:
                result = find_max_profit_with_dict(A, W, n - 1, k, profit_dict)

            elif k >= W[n]:

                not_in_bag = find_max_profit_with_dict(A, W, n - 1, k, profit_dict)
                in_bag = A[n] + find_max_profit_with_dict(A, W, n - 1, k - W[n], profit_dict)
                result = max(not_in_bag, in_bag)
            profit_dict[(n, k)] = result

        return result
    return find_max_profit_with_dict(A, W, n, k, profit_dict)



############
# QUESTION 6
############

def distance(s1, s2):

    if s1 == "":
        return len(s2)
    elif s2 == "":
        return len(s1)
    elif s1[-1] == s2[-1]:
        op = 0
    else:
        op = 1

    min_op = min([distance(s1[:-1], s2) + 1, distance(s1, s2[:-1]) + 1, distance(s1[:-1], s2[:-1]) + op])

    return min_op


def distance_fast(s1, s2):

    def create_matrix(s1, s2, cnt, m):

        if s1 == s2 == "":
            return m

        if len(m) == 0:
            first_row = list(" " + s1)
            m.append(first_row)
            return create_matrix("", s2, cnt, m)
        if len(m) == 1:
            second_row = [s2[0]] + list(range(len(m[0]) - 1))
            m.append(second_row)
            return create_matrix("", s2[1:], cnt, m)

        new_row = [s2[0]] + [cnt] + (len(m[0]) - 2) * [0]
        m.append(new_row)

        return create_matrix("", s2[1:], cnt + 1, m)

    def distance_with_indexes(i, j, m):

        if i == len(m) - 1 and j == len(m[0]) - 1:
            if m[0][j] == m[i][0]:
                m[i][j] = m[i - 1][i - 1]
            else:
                m[i][j] = min(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1]) + 1
            return m[i][j]

        if j == len(m[0]):
            return distance_with_indexes(i + 1, 2, m)

        if m[0][j] == m[i][0]:
            m[i][j] = m[i - 1][i - 1]
            return distance_with_indexes(i, j + 1, m)

        if m[0][j] != m[i][0]:
            m[i][j] = min(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1]) + 1
            return distance_with_indexes(i, j + 1, m)

    if s1 == "":
        return len(s2)
    if s2 == "":
        return len(s1)

    m = create_matrix(" " + s1, " " + s2, 1, [])
    return distance_with_indexes(2, 2, m)



########
# Tester
########

def test():
    # print matrix, use this function only to check your results.
    def print_matrix(A):
        print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                         for row in A]))

    # Q2-c
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    key = 8
    if(rec_slice_binary_search(lst, key) != 7):
        print("Error in rec_slice_binary_search")

    # Q3-b
    if(had_local(2,2,2) != 1):
        print("Error in had_local")

    # Q4-a
    m = [[0,0,0,2,4,6],
         [0,4,0,2,3,4],
         [0,0,0,3,2,4],
         [2,4,0,0,0,0],
         [3,6,0,4,6,0],
         [3,0,0,0,0,0]]
    rr, rm = find_zero_paths(m)
    if(rr != 4):
        print("Error in find_zero_path")
    print_matrix(rm)

    #Q5-a
    A = [20, 5, 10, 40, 15, 25]
    W = [1, 2, 3, 8, 7, 4]
    k = 10
    if(find_max_profit(A, W, len(A) -1, k) != 60):
        print("Error in find_max_profit")
    #Q5-c
    if (find_max_profit_fast(A, W, len(A) - 1, k) != 60):
        print("Error in find_max_profit_fast")

    #Q6
    if distance('computer', 'commuter') != 1 or \
            distance('sport', 'sort') != 1 or \
            distance('', 'ab') != 2 or distance('kitten', 'sitting') != 3:
        print("Error in distance")

    if distance_fast('computer', 'commuter') != 1 or \
            distance_fast('sport', 'sort') != 1 or \
            distance_fast('', 'ab') != 2 or distance_fast('kitten', 'sitting') != 3:
        print("Error in distance_fast")

test()
