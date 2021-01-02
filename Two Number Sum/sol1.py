# o(n) time
def twoNumberSum(array, targetSum):
    # Write your code here.
	# traverse through the array
	for i in array:
		#declare co i
		coI = targetSum - i
# 		if coI is in the array and is not equal to i , return array else continue
		if coI in array and coI != i:
			return [coI, i]
		else:
			continue
	return []
