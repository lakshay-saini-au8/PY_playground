#question https://www.hackerrank.com/challenges/finding-the-percentage/problem?isFullScreen=true
#solution
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name ,*lines = input().split()
        marks = list(map(float,lines))
        student_marks[name] = marks
    query = input()
    query_items = student_marks.get(query)
    result = sum(query_items)/len(query_items)
    print(f'{result:.2f}')
        
    
    
    
    
    
    
    
    
    
    
