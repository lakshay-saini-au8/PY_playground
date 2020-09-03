'''
1. Write a Python program to check if two given sets have no elements in
common.
2. Write a Python program which returns a new set with all items from both
sets by removing duplicates.
3. Write a program which uses all of the api’s of dictionaries and sets
discussed in class.
'''
#  Task 1


def intersection(set1, set2):
    setinter = set1 & set2
    if(len(setinter) == 0):
        print("We don't have equal element")
    else:
        print(f"we have some equal elements {setinter}")


intersection({1, 2}, {4, 5, 7, 8, 6})

# Task2


def unionset(set1, set2):
    setinter = set1 | set2
    if(len(setinter) == 0):
        print("We don't have any element")
    else:
        print(f" union of set is  {setinter}")


unionset({1, 2}, {4, 5, 7, 8, 6})


# task 3
def properites():
    sets = set()
    dicts = {}
    sets.add(1)
    dicts["hello"] = "lakshay"
    print(sets)
    print(dicts)


properites()
