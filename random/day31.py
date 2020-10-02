'''
Question:1
Write a program to sort a stack using extra stack.
Input: [23,12,90,5,7]
Output: [5,7,12,23,90]
'''


def sort_stack(arr):
    stack_1 = []
    stack_2 = []
    n = len(arr)
    if len(stack_1) == 0:
        stack_1.append(arr[0])
    for i in range(1, n):
        s1_top = stack_1[-1]
        if s1_top > arr[i]:
            stack_1.append(arr[i])

        else:
            b = len(stack_1)
            while b > 0:

                if stack_1[-1] < arr[i]:
                    stack_2.append(stack_1.pop())
                    b -= 1
                else:
                    break

            stack_1.append(arr[i])
            while len(stack_2) > 0:
                stack_1.append(stack_2.pop())

    print(stack_1)


sort_stack([23, 12, 90, 5, 7])



