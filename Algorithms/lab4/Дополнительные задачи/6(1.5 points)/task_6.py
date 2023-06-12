import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()
input_file = open('input.txt')
s = input_file.readline()


def z_func(s):
    n = len(s)
    z = [0] * n
    l = r = 0
    '''Текущий самый правый отрезок совпадения полагается равным [0:0], 
    т.е. заведомо маленький отрезок, в который не попадёт ни одно i'''
    for i in range(1, n):
        if i <= r:
            '''z[i] в [l:r] соответствует значение z[i-l] s [0:r-l]. Однако, 
            значение z[i-l] может оказаться большим и при применении к z[i] в [l:r]
            вылезти за границы r. Этого допустить нельзя, так как про символее правее r 
            мы ничего не знаем. Поэтому ищем минимум.'''
            z[i] = min(z[i - l], r - i + 1)
        while i + z[i] < n and s[i + z[i]] == s[z[i]]:
            z[i] += 1
            '''Тривиальный алгоритм. Также следим за тем, чтобы индексы не вышли за пределы строки'''
        # if z[i] > r - i:
        if i + z[i] - 1 > r:
            l, r = i, i + z[i] - 1
            '''Мы продлеваем отрезок совпадения до i + z[i] - 1, если требуется.'''
    return z


with open('output.txt', 'w') as output_file:
    print(*z_func(s)[1:], file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
