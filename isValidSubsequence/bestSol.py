# space O(1) time O(n)
def isValidSubsequence(array, sequence):
    sequence_index = 0
    for i in array:
        if sequence_index == len(sequence):
            break
        if i == sequence[sequence_index]:
            sequence_index += 1
    return sequence_index == len(sequence)