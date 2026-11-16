N = int(input())
if N < 1 or N > 1000:
    n = int(input())

for i in (range(N+1)):
    if i != 0:
        print(f'{i} {i**2} {i**3}')