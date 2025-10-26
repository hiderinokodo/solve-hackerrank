# Enter your code here. Read input from STDIN. Print output to STDOUT
# n is height and m is width

def door_mat(n, m):
    if n%2 != 0 and m == 3*n:
        for h in range(1, n, 2):
            pattern = '.|.'*h
            dash = (m-len(pattern))//2
            print('-'*dash + pattern + '-'*dash)
        
        welcome = 'WELCOME'
        dash = (m-len(welcome))//2
        print(('-'*dash + welcome + '-'*dash))
        
        for h in range(n-2, 0, -2):
            pattern = '.|.'*h
            dash = (m-len(pattern))//2
            print('-'*dash + pattern + '-'*dash)

if __name__ == '__main__':
    n, m = map(int, input().split())
    door_mat(n, m)