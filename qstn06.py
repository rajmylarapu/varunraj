def count_all_subarrys(arr,  n):
    # count all subarrays
    res = 0
    for i in range(n):
        summ = 0
        for j in range(i, n):
 
            # Calculate required sum
            summ += arr[j]
 
            # Check if sum is equal to
            # required sum
            if summ == k:
                res += 1
    return res
 
 
# main function
if __name__ == "__main__":
    arr = [1,1,1]
    n = len(arr)
    k = 2
    print(count_all_subarrys(arr, n))