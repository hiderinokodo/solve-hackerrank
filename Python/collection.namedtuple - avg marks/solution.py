# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple

n = int(input())
col = input().split()

Student = namedtuple('Student', col)

total = 0
for i in range (n):
    data = input().split()
    s = Student(*data)
    total += int(s.MARKS)
    
print(total/n)
