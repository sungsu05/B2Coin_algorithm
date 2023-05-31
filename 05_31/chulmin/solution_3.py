N = int(input())
for i in range(1, 2 * N):
    if i > N:
        i = 2 * N - i

    print(" " * (N - i) + "*" * (2 * i - 1))
