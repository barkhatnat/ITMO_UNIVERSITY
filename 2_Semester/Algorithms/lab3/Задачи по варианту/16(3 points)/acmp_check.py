input_file = open('input.txt')
n = int(input_file.readline().strip())
graph = {}
for _ in range(n):
    p_id = input_file.readline().strip()
    p_calls = int(input_file.readline().strip())
    graph[p_id] = []
    if p_calls != 0:
        for _ in range(p_calls):
            called_prog = input_file.readline().strip()
            graph[p_id].append(called_prog)
    input_file.readline()


def dfs(v, visited, start_v):
    if v in visited:
        return v == start_v
    visited.append(v)
    for neighbor in graph[v]:
        if dfs(neighbor, visited, start_v):
            return True
    return False


result = ''

for p_id in list(graph.keys()):
    visited = []
    if dfs(p_id, visited, p_id) and graph[p_id] is not None:
        result += 'YES\n'
    else:
        result += 'NO\n'

with open('output.txt', 'w') as output_file:
    print(result, file=output_file)
