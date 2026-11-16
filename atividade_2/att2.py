n = int(input())
for i in range(13):
    if i != 0:
        if (n + i) % 2 == 1:
            print(n+i)