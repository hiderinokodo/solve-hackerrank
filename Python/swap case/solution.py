def swap_case(s):
    char_list = list(s)
    char_convert = []
    
    for c in char_list:
        if c.isupper():
            char_convert.append(c.lower())
        elif c.islower():
            char_convert.append(c.upper())
        else:
            char_convert.append(c)
    
    return ''.join(char_convert)
# I try this before realize that Python has a built-in function: s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)