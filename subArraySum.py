def subArraySum(arr, n, sum): 
    """
    Description: Function returns sub array indexes for sum
    parameters: 
        arr: list if numbers
        n: Numver of elements in a list
        sum: Sum that needs to match with the sub-array
    """
    count = 1
    while (count < n):
        actual = 0
        for j in arr:
            actual = actual + j
            if actual == sum:
                return count, arr.index(j)+count
            elif actual > sum:
                arr.pop(0)
                count += 1
                break
    return []
    
# sample input  -> subArraySum([1,2,3,7,5], 5, 12)
# sample output -> (2,4)
