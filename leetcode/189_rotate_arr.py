# que https://leetcode.com/problems/rotate-array/submissions/
# solution
def rotate(nums, k):
    for _ in range(k):
        el = nums.pop()
        nums.insert(0, el)

    return nums


print(rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
print(rotate(nums=[-1, -100, 3, 99], k=2))
