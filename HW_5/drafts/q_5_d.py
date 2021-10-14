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
s0 = "a" * 100
s1 = "b" * 40 + "a" * 60
s2 = "c" * 50 + "b" * 40 + "a" * 1
s3 = "a" * 100

lst1 = [s0, s1, s2, s3]
k1 = 50

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

print(prefix_suffix_overlap_hash1(lst1, k1))
