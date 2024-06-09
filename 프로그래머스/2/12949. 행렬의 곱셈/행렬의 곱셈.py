# solve 4
# import numpy as np

# def solution(arr1, arr2):
#     res = np.dot(arr1, arr2).tolist()
#     return res

def solution(arr1, arr2):
    res = [[0] * (len(arr2[0])) for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            temp = 0
            for k in range(len(arr1[0])):
                temp += (arr1[i][k] * arr2[k][j])
            res[i][j] = temp
    return res