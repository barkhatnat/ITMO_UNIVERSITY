import time
import tracemalloc


def gorner_scheme(text):
    result = ord(text[0])
    base_x = 31
    for i in range(1, len(text)):
        result = result * base_x + ord(text[i])
    return result


def calculate_hash(text):
    q = 2 ** 31 - 1
    return gorner_scheme(text) % q


start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
p = input_file.readline()[:-1]
t = input_file.readline()
len_p, len_t = len(p), len(t)
p_hash = calculate_hash(p)
base_x = 31
q = 2 ** 31 - 1
i = 0
count = 0
start_points = []
current_hash = calculate_hash(t[0:len_p])
while True:
    if p_hash == current_hash:
        if p == t[i:i + len_p]:
            count += 1
            start_points.append(i + 1)
    if i >= len_t - len_p:
        break
    current_hash = ((current_hash - ord(t[i]) * base_x ** (len_p - 1)) * base_x + ord(t[i + len_p])) % q
    i += 1
with open('output.txt', 'w') as output_file:
    print(count, file=output_file)
    print(*start_points, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
