def gradingStudents(grades):
    # Write your code here
    res = []
    for i in grades:

        if i < 38:
            res.append(i)
        else:
            div = i % 5
            if div == 0 or (5-div) >= 3:
                res.append(i)
            else:
                res.append(i+5-div)
    return res
