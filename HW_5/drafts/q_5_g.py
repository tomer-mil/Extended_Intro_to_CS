import time

class Dict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """
        self.table = [[] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def insert(self, key, value):
        """ insert key,value into table
            Allow repetitions of keys """
        i = self.hash_mod(key)  # hash on key only
        item = [key, value]  # pack into one item
        self.table[i].append(item)

    def find(self, key):

        result = []

        i = self.hash_mod(key)
        cell = self.table[i]

        for elem in cell:
            if key == elem[0]:
                result.append(elem[1])

        return result

# Question 5
s0 = "a" * 1000
s1 = "b" * 400 + "a" * 600
s2 = "c" * 500 + "b" * 400 + "a" * 10
s3 = "a" * 1000

lst1 = [s0, s1, s2, s3] * 100
print(lst1)
k1 = 500

def elapsed(expression):
    t1 = time.perf_counter()
    eval(expression)
    t2 = time.perf_counter()
    return t2 - t1


def prefix_suffix_overlap(lst, k):

    result = []

    for i in range(len(lst)):
        prefix = lst[i][:k]
        for j in range(len(lst)):
            if i != j:
                suffix = lst[j][-k:]
                if prefix == suffix:
                    couple = (i, j)
                    result.append(couple)

    return result
def prefix_suffix_overlap_hash1(lst, k):

    result = []
    d = Dict(len(lst))

    for i in range(len(lst)): # n
        prefix = lst[i][:k]
        d.insert(prefix, i)

    for j in range(len(lst)):
        suffix = lst[j][-k:]
        for index in d.find(suffix):
            if j != index:
                result.append((index, j))

    return result
def prefix_suffix_overlap_hash2(lst, k):

    result = []
    d = dict()

    for i in range(len(lst)):
        prefix = lst[i][:k]

        if prefix not in d:
            d[prefix] = [i]
        else:
            d[prefix].append(i)

    for j in range(len(lst)):
        suffix = lst[j][-k:]
        if suffix in d:
            for n in d[suffix]:
                if j != n:
                    result.append((n, j))

    return result
print("regular:", elapsed("prefix_suffix_overlap(lst1,k1)"))
print("hash 1:", elapsed("prefix_suffix_overlap_hash1(lst1,k1)"))
print("hash 2:", elapsed("prefix_suffix_overlap_hash2(lst1,k1)"))
