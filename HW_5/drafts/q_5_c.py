

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



d = Dict(3)
d.insert("aaaa", 56)
d.insert("aaaa", 40)
d.insert("bbbb", 56)
d.insert("cccc", 20)

print(d)
print(d.find("aaaa"))



