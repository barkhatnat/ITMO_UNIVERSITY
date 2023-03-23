def subsetSum(nums, total):
    n = len(nums)
    T = [[False for x in range(total + 1)] for y in range(n + 1)]
    for i in range(n + 1):
        T[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, total + 1):
            if nums[i - 1] > j:
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][j - nums[i - 1]]
    return T


a = subsetSum([5,6,3], 9)

for i in range(len(a)):
    print("[", end="")
    for j in range(len(a[i])):
        print(a[i][j], end = ',')
    print("]")