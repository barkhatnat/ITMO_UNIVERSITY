import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
N, K = map(int, input_file.readline().split())
S = input_file.readline()
def isAlmostPalindrom(S, K, N):
    diff_count = 0
    for i in range(N // 2):
        if S[i] != S[-i - 1]:
            diff_count += 1
            if diff_count > K:
                return False
        # if i >= K:
        #     break
    return (True, diff_count)


answer = 0
for i in range(N):
    step = min(i + 1, N - 1 - i + 1)
    current_K_for_1, current_K_for_2 = 0, 1
    answer += 1
    answer += int(len(S[i:i + 2]) == 2 and isAlmostPalindrom(S[i:i + 2], K, len(S[i]))[0])
    for j in range(1, step):
        if S[i - j] == S[i + j]:
            answer += 1
        else:
            current_K_for_1 += 1
            if current_K_for_1 <= K:
                answer += 1
        if i < step -1:
            if len(S[i - j:i + j + 2]) >= 4 and S[i - j] == S[i + j + 1]:
                answer += 1
            elif len(S[i - j:i + j + 2]) >= 4:
                current_K_for_2 += 1
                if current_K_for_2 <= K:
                    answer += 1
with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)

print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()