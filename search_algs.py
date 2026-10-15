def linear_search(array: list[int], target: int) -> int:
    i = 0
    while i < len(array):
        if array[i] == target:
            return i
        i += 1
    return -1

def binary_search(array: list[int], value: int) -> int:
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return -1

if __name__ == "__main__":
    nums = [7, 4, 6, 9, 10, 2, 5, 3, 8]
    index = -1

    print(nums)

    print("Linear Search")
    index = linear_search(nums, 7)   # first item
    print(index)
    index = linear_search(nums, 8)   # last item
    print(index)
    index = linear_search(nums, 11)  # not found
    print(index)

    # need to sort first for binary search
    nums.sort()
    print(nums)

    print("Binary Search")
    index = binary_search(nums, 7)   # first item (in sorted list)
    print(index)
    index = binary_search(nums, 8)   # last item (in sorted list)
    print(index)
    index = binary_search(nums, 11)  # not found
    print(index)

