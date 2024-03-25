with open('compressed.txt', 'r') as f:
    for line in f.readlines():
        print(len(line.split()))
        print(line)
