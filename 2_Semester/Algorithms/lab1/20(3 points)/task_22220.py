

# N, K = map(int, input().split())
# S = input()
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
    return True


answer = 0
for i in range(len(S)):
    for j in range(i + 1, N + 1):
        if isAlmostPalindrom(S[i:j], K, j - i):
            print(S[i:j])
            answer += 1
print(answer)
with open('output_2.txt', 'w') as output_file:
    print(answer, file=output_file)