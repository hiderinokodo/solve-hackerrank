def minion_game(string):
    # your code goes here
    vowels = ['A', 'I', 'U', 'E', 'O']
    s_count = 0
    k_count = 0
    string = string.upper()
    
    for i in range(len(string)):
        if string[i] in vowels:
            k_count += len(string) - i
        else:
            s_count += len(string) - i
    
    if s_count > k_count:
        print("Stuart", str(s_count))
    elif k_count > s_count:
        print("Kevin", str(k_count))
    else:
        print("Draw")
        

if __name__ == '__main__':
    s = input()
    minion_game(s)