def twoSum(self, arr, target):
    # Your code here
    n = len(arr)
    l = 0
    r = n - 1
    while l < r:
        sum = arr[l] + arr[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l = l + 1
        else:
            r = r - 1

    return []

    # Time Complexity: O(n)
    # Space Complexity: O(1)


# for un sorted array
def twoSum(self, arr, target):
    # Your code here
    sorted_arr = sorted(arr)
    n = len(sorted_arr)
    l = 0
    r = n - 1
    while l < r:
        sum = sorted_arr[l] + sorted_arr[r]
        if sum == target:
            return [l + 1, r + 1]
        elif sum < target:
            l = l + 1
        else:
            r = r - 1

    return []

