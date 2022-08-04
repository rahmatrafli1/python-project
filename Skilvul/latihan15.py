def seq_search(nums, x):
    for i in range(len(nums)):
        if x == nums[i]:
            return i

    return -1


S = [10, 20, 30, 40, 50]
x = 30
pos = seq_search(S, x)

print(pos)
