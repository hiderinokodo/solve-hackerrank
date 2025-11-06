# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
my_arr = list(map(int, input().split()))
set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

hap = 0

for i in my_arr:
    if i in set_a:
        hap += 1
    elif i in set_b:
        hap -= 1
        
print(hap)