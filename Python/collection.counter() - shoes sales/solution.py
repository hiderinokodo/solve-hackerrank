# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

x = int(input())
shoe = list(map(int, input().split()))
n = int(input())

money = 0
shoe_count = Counter(shoe)

for i in range(n):
    s, xi = map(int, input().split())
    if shoe_count[s] > 0:
        shoe_count[s] -= 1
        money += xi

print(money)
