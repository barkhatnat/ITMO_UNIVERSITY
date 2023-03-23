input_file = open('input.txt')
N, K = map(int, input_file.readline().split())
S = input_file.readline()
print(N, K, S)

all_words = []
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
for i in range(N):
    print('\n ONE LETTER\n')
    print(f'now is checking {S[i]} combinations')
    print(f'first combination: {S[i]}')
    print(f'first combination: {S[i:i + 2]}')
    # answer+=1
    # answer += int(isAlmostPalindrom(S[i],K,2))
    step = min(i+1, N-1-i+1)
    for j in range(1, step):
        # if len(S[i-j:i+j]) == j + 1:
        print(f'current combination for 1: {S[i-j:i+j+1]}')
        # if isAlmostPalindrom(S[i-j:i+j+1], K, len(S[i-j:i+j+1])):
        #     answer+=1
        #
        print(f'current combination for 2: {S[i - j:i + j + 2]}')
    # print('\n TWO LETTERS\n')
    # print(f'now is checking {S[i:i+2]} combinations')
    # print(f'first combination: {S[i:i+2]}')
    # for j in range(1, step):
    #     # if len(S[i-j:i+j]) == j + 1:
    #     print(f'current combination: {S[i - j:i + j + 2]}')



print(answer)
