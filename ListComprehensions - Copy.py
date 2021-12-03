if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    old_list = [x, y, z]

    # list_comp = [(i, j, k) for i in old_list for j in old_list for k in old_list
    #              if i <= x and j <=y and k <= z and i + j + k != n]
    list_comp = [[i, j, k]
                 for i in range(x+1)
                 for j in range(y+1)
                 for k in range(z+1)
                 if i <= x and j <= y and k <= z and i + j + k != n
                 ]

    print(list_comp)

## I had problem at first - because range actually doesn't take the digit's itself. I had to add 1 to input data
