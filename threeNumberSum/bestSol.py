def threeNumberSum(array, targetSum):
    array.sort()
    result = []
    for index in range(len(array) - 2):
        left = index + 1
        right = len(array) - 1
        while left < right:
            currentSum = array[index] + array[left] + array[right]
            if currentSum == targetSum:
                result.append([array[i], array[left], array[right]])
                # to not miss other possible pairs, move left and right pointers at once
                left += 1
                right = - 1
            elif currentSum > targetSum:
                right -= 1
            elif currentSum < targetSum:
                left += 1
    return result
