# o(nlog(n) time) , o(1) space
def twoNumberSum(array, targetSum):
    # Write your code here.
   array.sort()
   left = 0
   right = len(array) - 1
   while(left < right):
       currentSum = array[left] + array[right]
       if currentSum == targetSum:
           return [array[left], array[right]]
       elif currentSum < targetSum:
        #    move to right if sum is lesser than expected
            left += 1
       elif currentSum > targetSum:
            right -= 1
    return []
