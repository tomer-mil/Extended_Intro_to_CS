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

    def __getitem__(self, loc):
        ''' called when using L[i] for reading
            return node at location 0<=loc<len '''
        assert 0 <= loc < len(self)
        p = self.next
        for i in range(0, loc):
            p = p.next
        return p

    def add_at_start(self, val):
        ''' add node with value val at the list head '''
        p = self
        tmp = p.next
        p.next = Node(val)
        p.next.next = tmp
        self.len += 1



    def reverse_start_end(self, k):
        assert 0 <= k <= self.len / 2

        def reverse_local(linlst, m, index=0):

            prev = None
            curr = linlst.next
            for i in range(m):
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            linlst.next = prev

        leftover = self.len - (2 * k)
        reverse_local(self, k)
        reverse_local(self, k, k + leftover)



ls = Linked_list("12345678")
ls.reverse_start_end(3)
print(ls)





