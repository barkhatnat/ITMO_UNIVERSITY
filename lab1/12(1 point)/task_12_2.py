import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()


def isThereASubset(S, n, len_of_subset):
    table = [[False for x in range(len_of_subset + 1)] for y in range(n + 1)]
    for i in range(n + 1):
        table[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, len_of_subset + 1):
            if nums[i - 1] > j:
                table[i][j] = table[i - 1][j]
            else:
                table[i][j] = table[i - 1][j] or table[i - 1][j - nums[i - 1]]
    return table[n][len_of_subset]


def counter(S):
    first_part = []
    second_part = []
    for i in sorted(S, reverse=True):
        if sum(S) // 2 >= sum(first_part) + i:
            first_part.append(i)
        else:
            second_part.append(i)
    return first_part


input_file = open('input.txt')
n = int(input_file.readline())
nums = list(map(int, input_file.readline().split()))
with open('output.txt', 'w') as output_file:
    amount = sum(nums)
    if amount % 2 == 0:
        if isThereASubset(nums, n, amount // 2):
            print(len(counter(nums)), file=output_file)
            print(*counter(nums), file=output_file)
    else:
        print(-1, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
