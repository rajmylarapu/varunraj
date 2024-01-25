def find_triplets(list1, n):  
      
    triplets = []  
    flag = False  
    for i in range(0, n-2):  
          
        s = set()  
        for j in range(i + 1, n):  
            x = -(list1[i] + list1[j])  
            if x in s:  
                  
                triplets.append([x, list1[i], list1[j]])  
                flag = True  
            else:  
                s.add(list1[j])  
        
                
    # If no triplet with 0 sum   
    # flag in list1ay  
    if (flag == False):  
        print(" not exist ")  
          
    return triplets  
list1 = [-20, 0, 20, 40, -20, -40, 80]  
n = len(list1)  
print(find_triplets(list1, n))    