
def all_nat():
    n = 0
    while True:
        yield n
        n += 1


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


def blocks(gen, k):
    sub_lst = []
    for g in gen:
        sub_lst.append(g)
        if len(sub_lst) == k:
            yield sub_lst
            sub_lst = []

    if sub_lst != []:
        yield sub_lst


print(list(blocks((i for i in range(12)), 5)))

# [[0,1,2,3,4],[5,6,7,8,9]]

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



l2 = lambda x: x < 10 or x % 7 == 0
l3 = lambda x: x == 3 or x + 7 == 22
# n1 = all_nat()

# print(next(n1))
# print(next(n1))
# for i in range(7):
print(list(take_only((i for i in range(30)), l2, 20)))
test()
# [1, 4, 7, 10, 13, 16, 19, 22, 25, 28]