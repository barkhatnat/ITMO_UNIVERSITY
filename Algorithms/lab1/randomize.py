import random
RANGS = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

rang = [random.randint(1,9) for i in range(15)]
color = [random.choice(["+", "-", "*"]) for j in range(14)]

print(*rang)
print(*color)
for i in range(14):
    s = str(rang[i]) + str(color[i])
    print(s,end='')
