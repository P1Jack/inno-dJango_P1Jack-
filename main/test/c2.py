import time

from tqdm import tqdm

with open("c2.txt", "r") as file:
    file.readline()
    for _ in range(3):
        n = int(file.readline())
        a1 = list(map(int, file.readline().split()))
        a2 = list(map(int, file.readline().split()))
sp = []
print(n, a1)
print(a2)
for i in range(n):
    sp.append((a1[i] - a2[i], a1[i] + a2[i]))
table = {0: [0, ""]}

count = 0
t = time.time()
for num, i in tqdm(enumerate(sp), total=len(sp)):
    num = str(num + 1)
    count += 1
    print(count, len(table), time.time() - t)
    t = time.time()

    # for j in list(table.keys()):
    #     val = table[j][0] + i[1]
    #     key = j + i[0]
    #     if key not in table or val > table[key][0]:
    #         table[key] = [val, table[j][1] + num + " "]

    new_table = {}
    for j in table:
        val = table[j][0] + i[1]
        key = j + i[0]
        if key not in new_table or val > new_table[key][0]:
            new_table[key] = [val, table[j][1] + num + " "]
    for j in new_table:
        if j not in table or new_table[j][0] > table[j][0]:
            table[j] = new_table[j].copy()
print("otvet", table[0][0] / 2)
print(table[0][1])
