import time

#Q5-a
A = [20, 5, 10, 40, 15, 25] # price
W = [1, 2, 3, 8, 7, 4] # weights
k = 10 # sack weight limit
n = len(A) - 1 # length of A
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

def find_max_profit_with_dict(A, W, n, k, profit_dict):
    result = 0
    if (n, k) in profit_dict:
        print("in memo")
        return profit_dict[(n, k)]

    else:
        if n < 0 or k <= 0:
            return 0

        elif k < W[n]:
            result = find_max_profit_with_dict(A, W, n - 1, k, profit_dict)
            profit_dict[(n, k)] = result

        elif k >= W[n]:

            not_in_bag = find_max_profit_with_dict(A, W, n - 1, k, profit_dict)
            in_bag = A[n] + find_max_profit_with_dict(A, W, n - 1, k - W[n], profit_dict)
            result = max(not_in_bag, in_bag)
        profit_dict[(n, k)] = result

    return result



def find_max_profit_fast(A, W, n, k):
    profit_dict = {}
    result = find_max_profit_with_dict(A, W, n, k, profit_dict)
    print(profit_dict)
    return result


def time_profit():
    t0 = time.perf_counter()
    print(find_max_profit_fast(A, W, n, k))
    t1 = time.perf_counter()
    print("time:", t1 - t0)

time_profit()

