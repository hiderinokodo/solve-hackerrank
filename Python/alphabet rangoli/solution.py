def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 123)]
    total_width = 4 * size - 3
    
    for i in range(size - 1):
        left_part = alphabet[size-1:size-i-1:-1]
        right_part = alphabet[size-i-1:size]
        line = "-".join(left_part + right_part)
        padding = (total_width - len(line)) // 2
        print("-" * padding + line + "-" * padding)
        
    left_part = alphabet[size-1::-1]
    right_part = alphabet[1:size]
    middle_line = "-".join(left_part + right_part)
    print(middle_line)
    
    for i in range(size - 2, -1, -1):
        left_part = alphabet[size-1:size-i-1:-1]
        right_part = alphabet[size-i-1:size]
        line = "-".join(left_part + right_part)
        padding = (total_width - len(line)) // 2
        print("-" * padding + line + "-" * padding)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)