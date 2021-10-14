s2 = ""
s1 = "ab"







def distance_fast(s1, s2):

    def create_matrix(s1, s2, cnt, m):

        if s1 == s2 == "":
            return m

        if len(m) == 0:
            first_row = list(" " + s1)
            m.append(first_row)
            return create_matrix("", s2, cnt, m)
        if len(m) == 1:
            second_row = [s2[0]] + list(range(len(m[0]) - 1))
            m.append(second_row)
            return create_matrix("", s2[1:], cnt, m)

        new_row = [s2[0]] + [cnt] + (len(m[0]) - 2) * [0]
        m.append(new_row)

        return create_matrix("", s2[1:], cnt + 1, m)

    def distance_with_indexes(i, j, m):

        if i == len(m) - 1 and j == len(m[0]) - 1:
            if m[0][j] == m[i][0]:
                m[i][j] = m[i - 1][i - 1]
            else:
                m[i][j] = min(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1]) + 1
            return m[i][j]

        if j == len(m[0]):
            return distance_with_indexes(i + 1, 2, m)

        if m[0][j] == m[i][0]:
            m[i][j] = m[i - 1][i - 1]
            return distance_with_indexes(i, j + 1, m)

        if m[0][j] != m[i][0]:
            m[i][j] = min(m[i][j - 1], m[i - 1][j], m[i - 1][j - 1]) + 1
            return distance_with_indexes(i, j + 1, m)

    if s1 == "":
        return len(s2)
    if s2 == "":
        return len(s1)

    m = create_matrix(" " + s1," " + s2, 1, [])
    return distance_with_indexes(2, 2, m)


# def distance_mem():


# def distance_fast(s1, s2):





# print("my_m:", my_m)
# print("sliced my_m:", len(my_m[0][:3]))
print("distance:", distance(s1, s2))


m2: [
    [' ', ' ', 's', 'i', 't', 't', 'i', 'n', 'g'],
    [' ', 0, 1, 2, 3, 4, 5, 6, 7],
    ['k', 1, 0, 0, 0, 0, 0, 0, 0],
    ['i', 2, 0, 0, 0, 0, 0, 0, 0],
    ['t', 3, 0, 0, 0, 0, 0, 0, 0],
    ['t', 4, 0, 0, 0, 0, 0, 0, 0],
    ['e', 5, 0, 0, 0, 0, 0, 0, 0],
    ['n', 6, 0, 0, 0, 0, 0, 0, 0]]