# Task
'''
1. Given a list of numbers, write a list comprehension that
produces a list of only the positive numbers in that
list.
Eg:- input = [-2, -1, 0, 1, 2]
Output = [1,2]

'''


def positiveNum(list):
    return [num for num in list if num > 0]


print(positiveNum([-2, -1, 0, 1, 2]))

'''
2. Given a list of numbers, write a list comprehension that
produces a list of strings of each number that is
divisible by 5.
Eg:- Input = [25, 91, 22, -7, -20]
Output = [‘25’, ‘-20’]
'''


def div_by_5(numlist):
    return [str(num) for num in numlist if (abs(num) % 5) == 0]


print(div_by_5([25, 91, 22, -7, -20]))

'''
3. Given a string representing a word, write a list
comprehension that produces a list of all the vowels in
that word.
Eg:- Input = “mathematics”
Output = [‘a’, ‘e’, ‘a’, ‘i’]

'''


def get_vowel(string):
    vowel = ["a", "e", "i", "o", "u"]
    return [ch for ch in string if ch.lower() in vowel]


print(get_vowel("mAthematics"))
