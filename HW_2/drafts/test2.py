import time


def parse_primes(filename):
    primes = []
    with open(filename, "r") as f:
        for line in f:
            primes += [int(num_str) for num_str in line.split(" ")[:-1] if num_str]
    return set(primes)



def check_goldbach_for_num(n, primes_set):

    for i in primes_set:
        if n - i in primes_set:
            return True
    return False


def check_goldbach_for_range(limit, primes_set):

    range_to_check = [n for n in range(4, limit, 2)]
    for n in range_to_check:
        if not check_goldbach_for_num(n, primes_set):
            return False
    return True

def check_goldbach_for_num_stats(n, primes_set):
    cnt = 0
    for i in primes_set:
        if i < n:
            if n - i in primes_set:
                cnt += 1
    if cnt == 0:
        return 0
    elif cnt % 2 == 0:
        if cnt == 52:
            print(n)
            return cnt // 2
        return cnt // 2
    
    else:
        return (cnt + 1) // 2

   
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



def goldbach_with_time():
    t0 = time.perf_counter()
    my_dict = check_goldbach_stats(1000, parse_primes("primes.txt"))
    print(my_dict)
    t1 = time.perf_counter()
    print("running time: ", t1-t0, "sec")



