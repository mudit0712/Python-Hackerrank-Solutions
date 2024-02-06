if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    i=len(student_marks[query_name])
    output=0
    for x in student_marks[query_name]:
        output+=x
    output=output/i
    print("{:.2f}".format(output))
