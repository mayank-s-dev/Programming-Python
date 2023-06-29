# https://practice.geeksforgeeks.org/problems/find-distinct-elements2054/1
def distinct(M, N):
    # code here

    dict = {}
    for i in range(0, N):
        for j in range(0, N):
            ele = M[i][j]
            if dict.get(ele) is None and i == 0:
                dict[ele] = 1
            elif dict.get(ele) == i:
                dict[ele] += 1

        print(i, dict)
    count = 0
    for i in dict:
        if dict[i] == N:
            count += 1

    return count


matrix = [[6, 4, 7, 3, 5, 3, 1, 1, 6, 3, 3, 3, 4, 3, 4, 8, 8],
          [3, 4, 6, 6, 6, 6, 2, 2, 6, 3, 2, 8, 3, 7, 6, 6, 5],
          [8, 2, 7, 1, 2, 4, 3, 4, 6, 6, 7, 1, 5, 6, 3, 8, 4],
          [8, 6, 1, 2, 7, 6, 4, 8, 6, 6, 6, 3, 4, 2, 2, 5, 8],
          [2, 7, 3, 5, 2, 8, 2, 8, 1, 7, 6, 3, 6, 1, 3, 3, 1],
          [4, 2, 7, 7, 1, 4, 4, 7, 6, 7, 8, 7, 4, 8, 1, 2, 2],
          [5, 3, 2, 6, 3, 2, 4, 8, 4, 2, 8, 6, 4, 8, 1, 5, 6],
          [7, 6, 1, 3, 4, 6, 1, 3, 5, 4, 2, 5, 5, 4, 1, 8, 5],
          [6, 2, 6, 2, 1, 1, 3, 8, 7, 6, 7, 7, 3, 5, 6, 8, 5],
          [8, 3, 3, 8, 5, 7, 4, 7, 3, 8, 2, 3, 7, 6, 8, 8, 3],
          [1, 8, 3, 3, 7, 1, 1, 6, 8, 3, 2, 5, 2, 6, 4, 4, 8],
          [3, 8, 6, 6, 6, 8, 6, 7, 2, 4, 4, 2, 4, 6, 2, 3, 1],
          [5, 2, 1, 5, 7, 8, 7, 8, 4, 8, 5, 7, 3, 5, 2, 2, 2],
          [7, 8, 2, 4, 6, 3, 8, 2, 4, 3, 7, 6, 5, 7, 2, 6, 8],
          [6, 4, 7, 4, 3, 3, 3, 8, 1, 5, 4, 2, 6, 5, 1, 5, 6],
          [4, 3, 1, 3, 4, 4, 5, 2, 1, 2, 1, 2, 7, 8, 7, 3, 6],
          [2, 5, 8, 4, 4, 1, 8, 7, 2, 6, 4, 2, 2, 1, 6, 4, 1]]
n = 17

print(distinct(matrix, n))

