# Question 5
s0 = "a" * 100
s1 = "b" * 40 + "a" * 60
s2 = "c" * 50 + "b" * 40 + "a" * 10
s3 = "a" * 100

lst1 = [s0, s1, s2, s3]
k1 = 50


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





print(prefix_suffix_overlap(lst1, k1))