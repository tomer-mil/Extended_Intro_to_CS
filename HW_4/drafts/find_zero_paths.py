# def reach_end(m):
#     return True
# def capture(i, j, j_addition=0, i_addition=0):
#     index_list = []
#     index_list.append((i + i_addition, j + j_addition))
# def find_zero_paths(m):
#
#     if len(m) == 1 and len(m[0]) == 1:
#         print("done!")
#
#     i = 0
#     j = 0
#
#     if m[i + 1][j] == 0:
#         print("M:", m)
#         # capture(i + 1, j)
#         new_m = [x for x in m[1:]]
#         find_zero_paths(new_m)
#
#     if m[i][j + 1] == 0:
#         print("M2:", m)
#         while m[i][j + 1] == 0:
#             # CAPTURE
#             j += 1
#         new_m = [x[j:] for x in m[1:]]
#         find_zero_paths(new_m)
#
#     #
#     # if j > 0:
#     #     new_m = [x[j:] for x in m[1:]]
#     #     find_zero_paths(new_m)
# def find_zero_paths2(m):
#
#     if len(m) == 1:
#         print("done!")
#
#     for i in range(len(m)):
#         print("i:", i)
#         j = 0
#
#         if m[i + 1][j] == 0:
#             capture(i + 1, j)
#             # new_m = [x for x in m[1:]]
#
#             print("new_m:", new_m)
#             find_zero_paths2(new_m)
#
#         if m[i][j + 1] == 0:
#             while m[i][j + 1] == 0:
#                 #CAPTURE
#                 j += 1
#             new_m = [x[j:] for x in m[1:]]
#             print("new_M:", new_m)
#             find_zero_paths2(new_m)
#
#
#         #
#         # if j > 0:
#         #     new_m = [x[j:] for x in m[1:]]
#         #     find_zero_paths(new_m)
# def find_zero_paths1(m):
#     print("m:", m)
#     width = len(m[0])
#     height = len(m)
#
#     if len(m) == 1:
#         if m[0][0] == 0:
#             print("m is single: ", m)
#             return 1
#
#     result = 0
#
#     i = 0
#     if width == 1:
#         if m[1][0] == 0:
#             del m[0]
#             find_zero_paths1(m)
#         else:
#             return 0
#     elif height == 1:
#         if m[0][1] == 0:
#             for d in range(height):
#                 del m[d][0]
#                 find_zero_paths1(m)
#         else:
#             return 0
#
#     if m[i][i + 1] == 0:
#         for d in range(height):
#             print("column deletion")
#             # print("d:", d)
#             del m[d][0]
#             # print("m after collum deletion:", m)
#         find_zero_paths1(m)
#     elif m[i + 1][i] == 0:
#         print("row deletion")
#         del m[i]
#         # print("m after row deletion:", m)
#         find_zero_paths1(m)
#     else:
#         return "done"


# m = [[0, 0, 0, 2, 4, 6],[0, 4, 0, 2, 3, 4],[0, 0, 0, 3, 2, 4],[2, 4, 0, 0, 0, 0],[3, 6, 0, 4, 6, 0],[3, 0, 0, 0, 0, 0]]

# j

m1 = [[0, 0, 0, 2, 4, 6],
      [0, 4, 0, 2, 3, 4],
      [0, 0, 0, 3, 2, 4],
      [2, 4, 0, 0, 0, 0],
      [3, 6, 0, 4, 6, 0],
      [3, 5, 0, 0, 0, 0]]  # i


# 1. stop: if m[i][j] == m[0][0]
#       // if m[i+1][j] != 0 and m[i][j+1] != 0 and m[i-1][j] != 0 and m[i][j-1] != 0

# 2. small problems:
def find_zero_paths_with_index2(m, i, j, path):

    if i == (len(m) - 1) and j == (len(m) - 1):
        path.append((i, j))
        return 1

    if m[i][j] == 0:
        path.append((i, j))

    if j != len(m) - 1 and i != len(m) - 1:
        if (m[i][j + 1] == 0) and (m[i + 1][j]) == 0:
            # path.append((i, j))
            find_zero_paths_with_index2(m, i, j + 1, path)
            find_zero_paths_with_index2(m, i + 1, j, path)
        elif m[i][j + 1] == 0:
            # path.append((i, j))
            print("right. appended:", (i, j))
            find_zero_paths_with_index2(m, i, j + 1, path)
        elif m[i + 1][j] == 0:
            # path.append((i, j))
            print("down. appended:", (i, j))
            find_zero_paths_with_index2(m, i + 1, j, path)

    if i == len(m) - 1:
        if m[i][j + 1] == 0:
            # path.append((i, j))
            print("right. appended:", (i, j))
            find_zero_paths_with_index2(m, i, j + 1, path)

    if j == len(m) - 1:
        if m[i + 1][j] == 0:
            # path.append((i, j))
            print("down. appended:", (i, j))
            find_zero_paths_with_index2(m, i + 1, j, path)

    return 0


def find_zero_paths_with_index(m, i, j, path):
    if i == (len(m) - 1) and j == (len(m) - 1):
        if m[i][j] == 0:
            path.append((i, j))
            # print("appended:", (i, j))
            return 1

    # if (i, j < len(m) - 1) and ()

    if i < len(m) - 1:
        if m[i + 1][j] == 0:
            path.append((i, j))
            # print("appended:", (i, j))
            find_zero_paths_with_index(m, i + 1, j, path)
        # if j < len(m) - 1 and m[i][j] == 0:
        #     path.append((i, j))

    # if j < len(m) - 1 and m[i][j + 1] == 0:
    #     path.append((i, j + 1))
    #     find_zero_paths_with_index(m, i, j + 1, path)

    # elif m[i + 1][j] == 0:
    #     find_zero_paths_with_index(m, i + 1, j, path)
    #     path.append((i + 1, j))

    elif j < len(m) - 1:
        if m[i][j + 1] == 0:
            path.append((i, j))
            find_zero_paths_with_index(m, i, j + 1, path)

    #
    # if (i > 1) and ((i - 1, j) not in path):
    #     if m[i - 1][j] == 0:
    #         path.append((i - 1, j))
    #         find_zero_paths_with_index(m, i - 1, j, path)
    #
    # if (j > 1) and ((i, j - 1) not in path):
    #     if m[i][j - 1] == 0:
    #         path.append((i, j - 1))
    #         find_zero_paths_with_index(m, i, j - 1, path)

    else:
        return 0

def find_zero_path_with_route(m, i, j, route, total_routes):
    print(route)
    index = (i, j)

    if m[i][j] == 0:
        route.append(index)

    if i == (len(m) - 1) and j == (len(m) - 1):
        if route not in total_routes:
            total_routes.append(route)
            route.clear()
            return 1
        else:
            route.clear()
            return 0



    if j != len(m) - 1 and i != len(m) - 1:
        if m[i + 1][j] == m[i][j + 1] == 0:
            find_zero_path_with_route(m, i, j + 1, route, total_routes)
            find_zero_path_with_route(m, i + 1, j, route, total_routes)

    if j != len(m) - 1:
        if m[i][j + 1] == 0:
            find_zero_path_with_route(m, i, j + 1, route, total_routes)
        else:
            if i != len(m) - 1:
                if m[i + 1][j] == 0:
                    find_zero_path_with_route(m, i + 1, j, route, total_routes)

    if i != len(m) - 1:
        if m[i + 1][j] == 0:
            find_zero_path_with_route(m, i + 1, j, route, total_routes)


def create_matrix(m, path):
    new_m = [[0 for j in m] for i in m]

    for l in path:
        if (len(m) - 1, len(m) - 1) in l:
            for c in l:
                i = c[0]
                j = c[1]
                new_m[i][j] += 1

    return new_m


# def find_zero_paths(m):
#     path = []
#     find_zero_paths_with_index2(m, 0, 0, path)
#     print("tzomet:", path.count((3, 2)))
#     new_m = create_matrix(m, path)
#     return path.count((len(m) - 1, len(m) - 1)), new_m


def find_zero_paths(m):
    path = []
    find_zero_path_with_route(m, 0, 0, [], path)
    print("tzomet:", path.count((3, 2)))
    new_m = create_matrix(m, path)
    return path.count((len(m) - 1, len(m) - 1)), new_m

def print_matrix(A):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row])
                     for row in A]))


rr, rm = find_zero_paths(m1)

print_matrix(rm)
print("number of paths:", rr)

# find_zero_paths2(m1)
