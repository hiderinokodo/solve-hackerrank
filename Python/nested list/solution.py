if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    scores = [s[1] for s in records]
    second_lowest = sorted(set(scores))[1]
    students = [s[0] for s in records if s[1] == second_lowest]
    
    for name in sorted(students):
        print(name)