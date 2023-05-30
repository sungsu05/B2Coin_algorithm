import sys
N = int(sys.stdin.readline().rstrip())
count = 0
gomgom_set = set()
for i in range(N):
    a = sys.stdin.readline().rstrip()
    if a == 'ENTER':
        count += len(gomgom_set)
        gomgom_set = set()
    else:
        gomgom_set.add(a)
count += len(gomgom_set)
print(count)
