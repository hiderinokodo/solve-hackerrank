def merge_the_tools(string, k):
    n = len(string)
    temp = []
    
    for i in range(0,n,k):
        temp.append(string[i:i+k])
    
    res = ["".join(dict.fromkeys(w)) for w in temp]
    
    for items in res:
        print(items)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)