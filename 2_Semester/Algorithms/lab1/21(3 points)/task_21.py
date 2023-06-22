import time
import tracemalloc

start_time = time.perf_counter()
tracemalloc.start()

input_file = open('input.txt')
N, M, R = input_file.readline().split()


def sort_key(rang):
    return RANGS.index(rang[0])

answer = 'YES'
RANGS = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
my_cards = sorted(input_file.readline().split(), key=sort_key)
enemy_cards = sorted(input_file.readline().split(), key=sort_key)
my_cards_dict = {}
for card in my_cards:
    rang = card[0]
    color = card[1]
    if color in my_cards_dict.keys():
        my_cards_dict[color].append(rang)
    else:
        my_cards_dict[color] = [rang]
for enemy_card in enemy_cards:
    isCovered = False
    enemy_rang = enemy_card[0]
    enemy_color = enemy_card[1]
    if enemy_color in my_cards_dict.keys():
        for rang in my_cards_dict[enemy_color]:
            if RANGS.index(rang) > RANGS.index(enemy_rang):
                my_cards_dict[enemy_color].remove(rang)
                isCovered = True

    if enemy_color != R and not (isCovered) and R in my_cards_dict.keys() and len(my_cards_dict[R]) > 0:
        my_cards_dict[R].remove(my_cards_dict[R][0])
        isCovered = True

    if not (isCovered):
        answer = "NO"
        break
with open('output.txt', 'w') as output_file:
    print(answer, file=output_file)
print("Время: ", time.perf_counter() - start_time)
print("Память: ", float(tracemalloc.get_tracemalloc_memory()) / (2 ** 20))
tracemalloc.stop()
