A = [2, 7, 11, 15]
target = 9

def two_sum(A, target):
    compmap = {}
    for i in range(len(A)):
        if A[i] in compmap:
            return [compmap[A[i]] , A[i]]
        else:
            compmap[target - A[i]] = A[i]


print(two_sum(A, target))

nums = [2, 7, 11, 15]
target = 9


def two_sum_index(A, target):
    compmap = {}
    for i in range(len(nums)):
        if nums[i] in compmap:
            return [compmap[nums[i]], i]
        else:
            compmap[target - nums[i]] = i

print(two_sum_index(A, target))
