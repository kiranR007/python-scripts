def find_kth_largest(nums, k):
    nums.sort(reverse=True)
    return nums[k-1]

print(find_kth_largest([3, 2, 1, 5, 6, 4,9,9], 2))