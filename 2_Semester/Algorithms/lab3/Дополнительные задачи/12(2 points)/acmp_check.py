from collections import defaultdict, deque
input_file = open('input.txt')
rooms, corridor = map(int, input_file.readline().split())
graph = defaultdict(list)
for i in range(corridor):
    from_room, to_room, color = input_file.readline().split()
    graph[from_room].append([to_room, color])
    graph[to_room].append([from_room, color])
moves_number = input_file.readline()
moves = list(map(str, input_file.readline().split()))
current = '1'
way = [current]
answer = "CORRECT"

for move in moves:
    for neighbor in graph[current]:
        if neighbor[1] == move:
            current = neighbor[0]
            way.append(current)
            break
    else:
        answer = "INCORRECT"
if answer == "CORRECT":
    answer = way[-1]
with open("output.txt", "w") as output_file:
    output_file.write(answer)
