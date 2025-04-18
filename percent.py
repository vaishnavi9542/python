def percentage(n,student_marks):
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    avg=student_marks[query_name]
    avg_marks=sum(avg)/len(avg)
    print(format(avg_marks,".2f"))
    
    
