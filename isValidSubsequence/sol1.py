def isValidSubsequence(array, sequence):
    # Write your code here.
    array_index, sequence_index = 0, 0

    while array_index < len(array) and sequence_index < len(sequence):
        if(array[array_index] == sequence[sequence_index]):
            sequence_index += 1
        array_index += 1
    return sequence_index == len(sequence)
