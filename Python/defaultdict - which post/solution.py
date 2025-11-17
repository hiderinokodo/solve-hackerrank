# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

n, m = map(int, input().split())
a = defaultdict(list)

for i in range(1, n+1):
    a[input()].append(str(i))
    
for j in range(m):
    b = input()
    if a[b]:
        ans = " ".join(a[b])
        print(ans)
    else:
        print(-1)
    
