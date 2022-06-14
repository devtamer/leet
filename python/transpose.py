# m = [[1, 5],[3, 4],[5, 6]]
# for row in m :
#     print(row)
# print(range(len(m[0])))
# rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
# print("\n")
# for row in rez:
#     print(row)


def transpose(matrix):
    print(range(len(matrix)), matrix[0], len(matrix[0]))

    res = []
    for i in range(len(matrix[0])): # looping through the length of the first row
        tmp =[]
        for j in range(len(matrix)): # looping through the le
            # print("i: ", i, "j: ", j, "\n")
            tmp.append(matrix[j][i])

        res.append(tmp)
    return res

print(transpose([[1,2,3],[4,5,6],[7,8,9],[7,8,9]]))

