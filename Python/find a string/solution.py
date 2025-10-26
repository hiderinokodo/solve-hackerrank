def count_substring(string, sub_string):
    temp = []
    count = 0
    for i in range (len(string)):
        temp.append(string[i])
        if len(temp) == len(sub_string):
            string_temp = ''.join(temp)
            if string_temp == sub_string:
                count += 1
            temp.pop(0)
            
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)