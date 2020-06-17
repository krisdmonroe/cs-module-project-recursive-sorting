# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []
    # Your code here
    a = 0
    b = 0

    while a < len(arrA) and b < len(arrB):
        # compare the elements that a and b point at 
        if arrA[a] < arrB[b]:
            merged_arr.append(arrA[a])
            a += 1
        else:
            merged_arr.append(arrB[b])
            b += 1

    # at this point, we've finished traversing one of the lists completely
    # we need to add all of the elements from the other list to the combined list 
    while a < len(arrA):
        merged_arr.append(arrA[a])
        a += 1 
    while b < len(arrB):
        merged_arr.append(arrB[b])
        b += 1

    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    # if len(arr) >1: 
    #     mid = len(arr)//2 #Finding the mid of the array 
    #     L = arr[:mid] # Dividing the array elements  
    #     R = arr[mid:] # into 2 halves 
  
    #     merge_sort(L) # Sorting the first half 
    #     merge_sort(R) # Sorting the second half 
  
    #     i = j = k = 0
          
    #     # Copy data to temp arrays L[] and R[] 
    #     while i < len(L) and j < len(R): 
    #         if L[i] < R[j]: 
    #             arr[k] = L[i] 
    #             i+=1
    #         else: 
    #             arr[k] = R[j] 
    #             j+=1
    #         k+=1
          
    #     # Checking if any element was left 
    #     while i < len(L): 
    #         arr[k] = L[i] 
    #         i+=1
    #         k+=1
          
    #     while j < len(R): 
    #         arr[k] = R[j] 
    #         j+=1
    #         k+=1
    if len(arr) > 1:
    # break the array down recursively
    # base case: when the lists get down to lengths of 1 
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)
    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here
    start2 = mid + 1 
  
    # If the direct merge is already sorted 
    if (arr[mid] <= arr[start2]): 
        return 
      
    # Two pointers to maintain start 
    # of both arrays to merge 
    while (start <= mid and start2 <= end): 
  
        # If element 1 is in right place 
        if (arr[start] <= arr[start2]): 
            start += 1
        else: 
            value = arr[start2]
            index = start2 
  
            # Shift all the elements between element 1 
            # element 2, right by 1. 
            while (index != start): 
                arr[index] = arr[index - 1]
                index -= 1
              
            arr[start] = value
  
            # Update all the pointers 
            start += 1
            mid += 1
            start2 += 1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    if (l < r): 
  
        # Same as (l + r) / 2, but avoids overflow 
        # for large l and r 
        m = l + (r - l) // 2 
  
        # Sort first and second halves 
        merge_sort_in_place(arr, l, m) 
        merge_sort_in_place(arr, m + 1, r) 
  
        merge_in_place(arr, l, m, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
