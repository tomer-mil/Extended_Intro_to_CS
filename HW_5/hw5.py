# Skeleton file for HW5 - Winter 2021 - extended intro to CS

# Add your implementation to this file

# You may add other utility functions to this file,
# but you may NOT change the signature of the existing ones.

# Change the name of the file to include your ID number (hw5_ID.py).

# Enter all IDs of participating students as strings, separated by commas.

# For example: SUBMISSION_IDS = ["123456", "987654"] if submitted in a pair or SUBMISSION_IDS = ["123456"] if submitted alone.

SUBMISSION_IDS = ["316081355"]


############
# QUESTION 1
############

def printree(t, bykey=True):
    """Print a textual representation of t
        bykey=True: show keys instead of values"""
    # for row in trepr(t, bykey):
    #        print(row)
    return trepr(t, bykey)


def trepr(t, bykey=False):
    """Return a list of textual representations of the levels in t
        bykey=True: show keys instead of values"""
    if t == None:
        return ["#"]

    thistr = str(t.key) if bykey else str(t.val)

    return conc(trepr(t.left, bykey), thistr, trepr(t.right, bykey))


def conc(left, root, right):
    """Return a concatenation of textual represantations of
        a root node, its left node, and its right node
        root is a string, and left and right are lists of strings"""

    lwid = len(left[-1])
    rwid = len(right[-1])
    rootwid = len(root)

    result = [(lwid + 1) * " " + root + (rwid + 1) * " "]

    ls = leftspace(left[0])
    rs = rightspace(right[0])
    result.append(ls * " " + (lwid - ls) * "_" + "/" + rootwid * " " + "|" + rs * "_" + (rwid - rs) * " ")

    for i in range(max(len(left), len(right))):
        row = ""
        if i < len(left):
            row += left[i]
        else:
            row += lwid * " "

        row += (rootwid + 2) * " "

        if i < len(right):
            row += right[i]
        else:
            row += rwid * " "

        result.append(row)

    return result


def leftspace(row):
    """helper for conc"""
    # row is the first row of a left node
    # returns the index of where the second whitespace starts
    i = len(row) - 1
    while row[i] == " ":
        i -= 1
    return i + 1


def rightspace(row):
    """helper for conc"""
    # row is the first row of a right node
    # returns the index of where the first whitespace ends
    i = 0
    while row[i] == " ":
        i += 1
    return i


class Tree_node():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
        return "(" + str(self.key) + ":" + str(self.val) + ")"


class Binary_search_tree():

    def __init__(self):
        self.root = None

    def __repr__(self):  # no need to understand the implementation of this one
        out = ""
        for row in printree(self.root):  # need printree.py file
            out = out + row + "\n"
        return out

    def lookup(self, key):
        ''' return node with key, uses recursion '''

        def lookup_rec(node, key):
            if node == None:
                return None
            elif key == node.key:
                return node
            elif key < node.key:
                return lookup_rec(node.left, key)
            else:
                return lookup_rec(node.right, key)

        return lookup_rec(self.root, key)

    def insert(self, key, val):
        ''' insert node with key,val into tree, uses recursion '''

        def insert_rec(node, key, val):
            if key == node.key:
                node.val = val  # update the val for this key
            elif key < node.key:
                if node.left == None:
                    node.left = Tree_node(key, val)
                else:
                    insert_rec(node.left, key, val)
            else:  # key > node.key:
                if node.right == None:
                    node.right = Tree_node(key, val)
                else:
                    insert_rec(node.right, key, val)
            return

        if self.root == None:  # empty tree
            self.root = Tree_node(key, val)
        else:
            insert_rec(self.root, key, val)

    def diam(self):

        def longest_route_rec(node):
            if node == None:
                return 0, 0

            go_right = longest_route_rec(node.right)
            go_left = longest_route_rec(node.left)
            local_diam = max(go_left[0], go_right[0], go_right[1] + go_left[1] + 1)

            return local_diam, (max(go_right[1], go_left[1]) + 1)

        return longest_route_rec(self.root)[0]

    def is_min_heap(self):
        def heap_rec(node):
            if node.right == None and node.left == None:
                return True
            elif node.right == None:
                if node.left.val <= node.val:
                    return False
                return heap_rec(node.left)
            elif node.val >= node.right.val or node.left.val <= node.val:
                return False
            return heap_rec(node.right) and heap_rec(node.left)
        if self.root == None:
            return True
        return heap_rec(self.root)

############
# QUESTION 2
############

# Part A
class PNode():

    def __init__(self, val, p, nex=None):
        self.value = val
        self.next = nex
        self.priority = p

    def __repr__(self):
        return f"{self.value},{self.priority} ({id(self)})"
    # This shows pointers as well for educational purposes


class PQueue():

    def __init__(self, vals=None, ps=None):
        self.next = None
        self.len = 0
        self.q = []

        if vals != None:
            for val, p in zip(vals, ps):
                self.insert(val, p)

    def __len__(self):
        return self.len

    def __repr__(self):
        out = ""
        p = self.next
        while p != None:
            out += str(p) + ", "  # str(p) envokes __repr__ of class PNode
            p = p.next
        return "[" + out[:-2] + "]"

    def add_node_at_start(self, val, p):
        ''' add node with value val at the list head '''
        pointer = self
        tmp = pointer.next
        pointer.next = PNode(val, p)
        pointer.next.next = tmp
        self.len += 1

    def __getitem__(self, loc):
        assert 0 <= loc <= len(self)
        pointer = self.next
        for i in range(0, loc):
            pointer = pointer.next
        return pointer

    def reverse(self):
        prev = None
        curr = self.next
        while curr != None:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        self.next = prev

    def find(self, pr):
        ''' find (first) node with value val in list '''
        pointer = self.next
        loc = 0
        while pointer != None:
            if pointer.priority == pr:
                return loc
            else:
                pointer = pointer.next
                loc = loc + 1
        return None

    def insert(self, val, p):

        def insert_at_loc(val, pr, loc):
            pointer = self
            for i in range(0, loc):
                pointer = pointer.next
            tmp = pointer.next
            pointer.next = PNode(val, pr)
            pointer.next.next = tmp
            self.len += 1

        if self.q != []:
            max_priority = max(self.q)

            if p > max_priority:
                self.q.append(p)
                insert_at_loc(val, p, self.len)

            elif p == max_priority:
                self.q.append(p)
                loc = self.find(p)
                insert_at_loc(val, p, loc)

            elif p not in self.q:
                self.q.append(p)
                self.q.sort()
                loc = self.q.index(p)
                insert_at_loc(val, p, loc)

            else:
                loc = self.find(p)
                insert_at_loc(val, p, loc - 1)

        else:
            self.q.append(p)
            self.add_node_at_start(val, p)

    def pull(self):
        if self.q == []:
            return None, None
        else:
            self.reverse()
            node = self.next
            return node.value, node.priority


#  Part B
class Node():
    def __init__(self, val):
        self.value = val
        self.next = None

    def __repr__(self):
        # return str(self.value)
        # This shows pointers as well for educational purposes:
        return "(" + str(self.value) + ", next: " + str(id(self.next)) + ")"


class Linked_list():
    def __init__(self, seq=None):
        self.next = None
        self.len = 0
        if seq != None:
            for x in seq[::-1]:
                self.add_at_start(x)

    def __repr__(self):
        out = ""
        p = self.next
        while p != None:
            out += str(p) + ", "  # str(p) envokes __repr__ of class Node
            p = p.next
        return "[" + out[:-2] + "]"

    def __len__(self):
        ''' called when using Python's len() '''
        return self.len

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        p = self
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1

    def reverse_start_end(self, k):
        '''
        fill-in your code below here according to the instructions
        '''
        assert 0 <= k <= self.len / 2


############
# QUESTION 4
############

# a
def power_new(a, b):
    result = 1

    b_bin = bin(b)[2:]

    reverse_b_bin = b_bin[::-1]

    for bit in reverse_b_bin:
        if bit == "1":
            result = result * a
        a = a * a

    return result

# b
def power_with_base(a, b, base=2):

    assert base >= 2
    result = 1

    while b > 0:

        x = 1

        residual = b % base

        for i in range(residual):
            x *= a

        result *= x

        for i in range(base - residual):
            x *= a

        a = x
        b = b // base

    return result


############
# QUESTION 5
############
# a
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


# c
#########################################
### Dict class ###
#########################################

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

#########################################
### End Dict class ###
#########################################    

# d
def prefix_suffix_overlap_hash1(lst, k):

    result = []
    d = Dict(len(lst))

    for i in range(len(lst)):
        prefix = lst[i][:k]
        d.insert(prefix, i)

    for j in range(len(lst)):
        suffix = lst[j][-k:]
        for index in d.find(suffix):
            if j != index:
                result.append((index, j))

    return result


# f
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


########
# Tester
########

def test():
    # Question 1 - a

    t2 = Binary_search_tree()
    t2.insert('c', 10)
    t2.insert('a', 10)
    t2.insert('b', 10)
    t2.insert('g', 10)
    t2.insert('e', 10)
    t2.insert('d', 10)
    t2.insert('f', 10)
    t2.insert('h', 10)
    if t2.diam() != 6:
        print("error in Binary_search_tree.diam")

    t3 = Binary_search_tree()
    t3.insert('c', 1)
    t3.insert('g', 3)
    t3.insert('e', 5)
    t3.insert('d', 7)
    t3.insert('f', 8)
    t3.insert('h', 6)
    t3.insert('z', 6)
    if t3.diam() != 5:
        print("error in Binary_search_tree.diam")

    # Question 1 - b
    """ Construct below binary tree
               1
             /   \
            /     \
           2       3
          / \     / \
         /   \   /   \
        17   19 36    7
    """
    t1 = Binary_search_tree()
    t1.insert('d', 1)
    t1.insert('b', 2)
    t1.insert('a', 17)
    t1.insert('c', 19)
    t1.insert('f', 3)
    t1.insert('e', 36)
    t1.insert('g', 7)

    if not t1.is_min_heap():
        print("Error in is_min_heap")

    # Question 2 - a
    pq = PQueue("abc", [2, 1, 3])
    if pq.pull()[0] != "c":
        print("error in PQueue.pull")
    if pq.pull()[0] != "a":
        print("error in PQueue.pull")

    # Question 2 - b
    q = Linked_list("abcde")
    q.reverse_start_end(2)
    q_str = []
    p = q.next
    while p != None:
        q_str += [p.value]
        p = p.next
    q_str = "".join(q_str)

    if q_str != "baced":
        print("error in reverse_start_end")

    # Question 4
    if power_new(2, 3) != 8:
        print("error in power_new()")

    if power_with_base(2, 3, 3) != 8:
        print("error in power_with_base()")

    # Question 5
    s0 = "a" * 100
    s1 = "b" * 40 + "a" * 60
    s2 = "c" * 50 + "b" * 40 + "a" * 10
    lst = [s0, s1, s2]
    k = 50
    if prefix_suffix_overlap(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap")
    if prefix_suffix_overlap_hash1(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap_hash1(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash1")
    if prefix_suffix_overlap_hash2(lst, k) != [(0, 1), (1, 2)] and \
            prefix_suffix_overlap_hash2(lst, k) != [(1, 2), (0, 1)]:
        print("error in prefix_suffix_overlap_hash2")
