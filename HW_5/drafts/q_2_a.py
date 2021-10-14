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


pq2 = PQueue()
pq = PQueue("abc", [2, 1, 4])
pq.insert("b1", 3)
pq.insert("c2", 4)
#
print(pq.pull())

print(pq.q)

