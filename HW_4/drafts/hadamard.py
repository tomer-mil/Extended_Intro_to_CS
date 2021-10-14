
n1 = 3
i = 1
j = 1



def had_local(n, i, j):

    def bin_lst(x, bin_len):

        bin_x = bin(x)
        bin_x_len = len(bin_x)  # always +2 over
        bin_x_lst = []

        for bit in range(bin_x_len - 1, 1, -1):
            bin_x_lst.append(bin_x[bit])
        padding = ["0"] * (bin_len - (bin_x_len - 2))
        bin_x_lst.extend(padding)
        return bin_x_lst

    def check_for_bit(n, bin_i, bin_j):
        if n == 0:
            return 0

        i_bit_to_check = bin_i.pop()
        j_bit_to_check = bin_j.pop()

        n -= 1

        if j_bit_to_check == "1" and i_bit_to_check == "1":
            if check_for_bit(n, bin_i, bin_j) == 1:
                return 0
            else:
                return 1
        else:
            return check_for_bit(n, bin_i, bin_j)


    i_bin_lst = bin_lst(i, n)
    j_bin_lst = bin_lst(j, n)

    return check_for_bit(n, i_bin_lst, j_bin_lst)


print(had_local(n1, i, j))