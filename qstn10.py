def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list
 

def nextPermutation(arr):
    n = len(arr)
    i = len(arr)-2
    j = 0
     
    
    while i>=0:
      if arr[i]<arr[i+1]:
        break
      i=i-1
 
    if (i < 0):
        arr.reverse()
 
    
    else:
       
        for j in range(n-1, i, -1):
            if (arr[j] > arr[i]):
                break
 
       
        swapPositions(arr, i, j)
         
        
        strt, end = i+1, len(arr)
 
       
        arr[strt:end] = arr[strt:end][::-1]
if __name__ == "__main__":
    arr = [1, 2, 3, 6, 5, 4]
     
   
    nextPermutation(arr)
     
   
    for i in arr:
        print(i, end=" ")
