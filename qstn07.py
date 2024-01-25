def printRepeating(arr):
    repeating_set = set()
 
    # Iterate through each element in the array
    for i in range(len(arr)):
        repeating = False
 
        # Iterate through the remaining elements to find repeating elements
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                # If it's the first time the element is repeating, add it to the set
                if not repeating:
                    repeating_set.add(arr[i])
                repeating = True
                break  # Break the inner loop once a repeating element is found
 
    # Print the repeating elements
    for item in repeating_set:
        print(item, end=" ")
 
 
# Driver code
if __name__ == "__main__":
    arr = [4, 3, 2, 7, 8, 2, 1, 4]
    printRepeating(arr)