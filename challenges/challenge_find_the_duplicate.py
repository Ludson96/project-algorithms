def binary_search(numbers: int, target: int) -> int | bool:
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == target:
            return mid

        if target < numbers[mid]:
            end = mid - 1
        else:
            start = mid + 1

    return False


def find_duplicate(nums: list[int]) -> int | bool:
    nums.sort()
    if len(nums) < 2 or not nums:
        return False

    for i in range(len(nums)):
        if not isinstance(nums[i], int) or nums[i] < 1:
            return False
        else:
            index = binary_search(nums[i + 1:], nums[i])
            if index is not False:
                return nums[index + i + 1]

    return False
