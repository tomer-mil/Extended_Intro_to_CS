# Skeleton file for HW6 - Winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw6_ID.py).

# Enter all IDs of participating students as strings, separated by commas.

# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.

SUBMISSION_IDS = ["316081355"]


############
# QUESTION 1
############

# (a)
def take_only(gen, predicate, n):
    cnt = 0

    for g in gen:
        if predicate(g):
            cnt = 0
            yield g
        else:
            cnt += 1
        if cnt == n:
            break



# (b)
def blocks(gen, k):
    sub_lst = []
    for g in gen:
        sub_lst.append(g)
        if len(sub_lst) == k:
            yield sub_lst
            sub_lst = []

    if sub_lst != []:
        yield sub_lst


############
# QUESTION 5
############

# (b)
def CYK_d(st, rule_dict, start_var):

    ''' What is the minimal depth of a parse tree that generates st? '''
    n = len(st)

    # table for the dynamic programming algorithm
    table = [[None for j in range(n + 1)] for i in range(n)]
    # Initialize the relevant triangular region with empty sets
    for i in range(n):
        for j in range(i + 1, n + 1):
            table[i][j] = {}

    # Fill the table cells representing substrings of length 1
    fill_length_1_cells_d(table, rule_dict, st)

    # Fill the table cells representing substrings of length >=2
    for length in range(2, n + 1):
        for i in range(0, n - length + 1):
            j = i + length
            fill_cell_d(table, i, j, rule_dict)

    # Original CYK: return start_var in table[0][n]
    if start_var in table[0][n]:
        return table[0][n][start_var]
    return -1


def fill_length_1_cells_d(table, rule_dict, st):
    n = len(st)
    for i in range(n):
        for lhs in rule_dict:  # lhs is a single variable
            if st[i] in rule_dict[lhs]:
                table[i][i + 1][lhs] = 1


def fill_cell_d(table, i, j, rule_dict):

    for k in range(i + 1, j):  # non trivial partitions of s[i:j]
        for lhs in rule_dict:  # lhs is a single variable
            for rhs in rule_dict[lhs]:
                if len(rhs) == 2:  # rule like A -> XY (not like A -> a)
                    X, Y = rhs[0], rhs[1]
                    if X in table[i][k] and Y in table[k][j]:
                        max_value = max(table[i][k][X], table[k][j][Y])
                        if lhs in table[i][j]:
                            table[i][j][lhs] = min(table[i][j][lhs], max_value + 1)
                        else:
                            table[i][j][lhs] = max_value + 1

    
########
# Tester
########

def test():
    # Question 1
    import types
    # (a)
    if not isinstance(take_only((i for i in range(30)), lambda x: x % 3 == 1, 5), types.GeneratorType):
        print("Error in take_only")
    if list(take_only((i for i in range(30)), lambda x: x % 3 == 1, 5)) != [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]:
        print("Error in take_only")
    if list(take_only((i for i in range(30)), lambda x: x < 10 or x % 7 == 0, 5)) != [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 14]:
        print("Error in take_only")

    # (b)
    if not isinstance(blocks((i for i in range(10)), 5), types.GeneratorType):
        print("Error in blocks")
    if list(blocks((i for i in range(10)), 5)) != [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9]]:
        print("Error in blocks")
    if list(blocks((i for i in range(10)), 3)) != [[0, 1, 2], [3, 4, 5], [6, 7, 8], [9]]:
        print("Error in blocks")
    if list(blocks((i for i in range(9)), 3)) != [[0, 1, 2], [3, 4, 5], [6, 7, 8]]:
        print("Error in blocks")

    # Question 5
    rule_dict = {"S": {"AB", "BC"}, "A": {"BA", "a"}, "B": {"CC", "b"}, "C": {"AB", "a"}}
    if CYK_d("baaba", rule_dict, "S") != 4:
        print("Error in CYK_d")
    if CYK_d("baab", rule_dict, "S") != -1:
        print("Error in CYK_d")



