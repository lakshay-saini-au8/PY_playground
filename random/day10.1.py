
'''
1. Write a Python function that takes two lists and returns True if they have at
least one common member.
2. Write a Python program to print a specified list after removing the 0th, 4th
and 5th elements.
3. Write a Python program to find the second smallest number in a list.
4. Write a Python program to find common items from two list

'''

# task 1


def checkCommon(listA, listB):
    for num in listA:
        for num1 in listB:
            if num1 == num:
                return True

    return False


print(checkCommon([1, 2, 3, 4], ["a", "C", "b", "s", 4]))

#  task 2


def removeElement(listnum, *index):
    numwe = []
    for i in index:
        numwe.append(listnum[i])
    for num in numwe:
        listnum.remove(num)
    print(listnum)


removeElement([1, 2, "a", 4, "b", 6, "c", 8], 1, 2, 3, 4)

# task 3


def second_last(num_list):

    maxNum = min(num_list)
    minNum = min(num_list)
    if len(num_list) > 1:
        for num in num_list:
            if(num > maxNum):
                minNum = maxNum
                maxNum = num
            else:
                if(num > minNum):
                    minNum = num
        if minNum == maxNum:
            print(f"we have common {minNum}")
        else:
            print(f"{maxNum} {minNum}")

    else:
        print("we have only one element")


second_last([1, 2, 3, 4, 5, 20, 4, -1, -2])
second_last([-1, -1, -1, -1, -1])

# task 4


def intersection(set1, set2):
    setinter = list(set(set1) & set(set2))
    if(len(setinter) == 0):
        print("We don't have equal element")
    else:
        print(f"we have some equal elements {setinter}")


intersection([1, 2], [2, 4, 5, 7, 8, 6])
