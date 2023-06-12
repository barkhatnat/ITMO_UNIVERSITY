import timeit


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
    return (True, diff_count)


starttime = timeit.default_timer()
print("The start time is :",starttime)

answer = 0
for i in range(N):

    print(f'now is checking {S[i]} combinations')
    print(f'first combination: {S[i]}')
    print(f'second combination: {S[i:i + 2]}')
    step = min(i+1, N-1-i+1)
    current_K_for_1, current_K_for_2 = 0, 1
    # isPalindrom, current_K = isAlmostPalindrom(S[i:i+2], K, len(S[i]))
    #

    answer+=1
    print("+ plus because start is palindrom")
    answer+= int(len(S[i:i+2])==2 and isAlmostPalindrom(S[i:i+2], K, len(S[i]))[0])
    print(f"+ plus because double start is palindrom: {int(len(S[i:i+2]) and isAlmostPalindrom(S[i:i+2], K, len(S[i]))[0])}")
    for j in range(1, step):
        print('\n ONE LETTER\n')
        print(f'current combination for 1: {S[i-j:i+j+1]}')
        if S[i-j]==S[i+j]:
            answer+=1
            print("+ plus because next is uncorrected palindrom")
            print(f'it is palindrom for {current_K_for_1}')
        else:
            current_K_for_1 +=1
            print(f'it is palindrom for {current_K_for_1}, global K is {K}')
            if current_K_for_1<=K:
                answer+=1
                print("+ plus because next is corrected palindrom")
            else:
                continue
        if i < step - 1:
            print('\n TWO LETTER\n')
            print(f'current combination for 2: {S[i - j:i + j + 2]}')
            print(len(S[i - j:i + j + 2]))
            print(i,j)
            print(S[i - j] == S[i + j + 1])
            if len(S[i - j:i + j + 2]) >=4 and S[i - j] == S[i + j + 1]:
                answer += 1
                print("+ plus because next is uncorrected palindrom")
                print(f'it is palindrom for {current_K_for_2}')
            elif len(S[i - j:i + j + 2]) >=4:
                current_K_for_2 += 1
                print(f'it is palindrom for {current_K_for_2}, global K is {K}')
                if current_K_for_2 <= K:
                    answer += 1
                    print("+ plus because next is corrected palindrom")
                else:
                    continue
print(answer)


