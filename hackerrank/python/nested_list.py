
#solution 1
if __name__ == '__main__':
    students = []
    numbers= []
    for i in range(int(input())):
        name = input()
        marks = float(input())
        students.append([name,marks])

    def sorting(item):
        return item[1]
    sort_arr = sorted(students,key = sorting)
    for name,number in sort_arr:
        numbers.append(number)
    unique_num =list(set(numbers)) 
    unique_num.sort()
    sec_lar = unique_num[1]
    names = []
    for item in sort_arr:
        if(item[1] == sec_lar):
            names.append(item[0])
        elif (item[1]> sec_lar):
            break
    names.sort()
    for item in names:
        print(item)
    
# solution 2
if __name__ == '__main__':
    students = [[input(),float(input())] for i in range(int(input()))]
    def sorting(item):
        return item[1]
    sort_arr = sorted(students,key = sorting)
    sec_lar =sorted(set([number for name,number in sort_arr]))[1]

    names = sorted([name for name,number in sort_arr if(number == sec_lar)])

    for item in names:
        print(item)
     
        
