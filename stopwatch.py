# Python3 program to find maximum
# in arr[] of size n 
  
# python function to find maximum
# in arr[] of size n
def largest(arr,n):
  
    # Initialize maximum element
    max = arr[0]
  
    # Traverse array elements from second
    # and compare every element with 
    # current max
    for i in range(1, n):
        if arr[i] > max:
            max = arr[i]
    return max

def smallest(arr,n):
  
    # Initialize minimum element
    min = arr[0]
  
    # Traverse array elements from second
    # and compare every element with 
    # current min
    for i in range(1, n):
        if arr[i] < min:
            min = arr[i]
    return min
  
# Driver Code
print("These are the time from stop-watch in seconds")
arr = [10, 324, 45, 90, 980, 40]
n = len(arr)
Ans1 = largest(arr,n)
Ans2 = smallest(arr,n)
print ("Largest in given array is",Ans1)
print ("Smallest in given array is",Ans2)