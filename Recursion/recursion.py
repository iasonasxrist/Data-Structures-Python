# Run DEBUG and Watch the Stack Memory
def printall(n):
    print1(n)
    print(n)

def print1(n):
    print2(n)
    print(n)

def print2(n):

    print(n)

# printall(3)


def fibonacci(n):
    if n < 2:
        return n

    
    return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4))
    


# Binary Search using Recursion
# Time Complexity O(logn)

def binarySearch(left, right, arr, target):

    if (left>right):
        return -1

    if (left==right) :
        return left
    
    if (left < right):

        mid = left +  (right-left)//2
        print(arr[mid])

        if (target == arr[mid]):
            return arr[mid]
        
        elif target > mid:
            return binarySearch(mid+1, right, arr, target)
        else :
            return binarySearch(left, mid-1, arr, target)
    return False

arr=[1,2,4,5,6,7,16, 20, 50]
print(binarySearch(0, len(arr)-1, arr, 5))



# O(N)
def factorial(n):
    if n==1:
        return n
    return n * factorial(n-1)

print(factorial(3))

# Simple Implementation

sum = 0
def reverseNum(n):
    global sum
    if n == 0 :
        return;

    remainder =  n%10
    sum = sum * 10 + remainder
    reverseNum(n//10)

print(reverseNum(1234))
print(sum)


#More Challenging Implementation
import math
def reverse2(n):

    digits = math.log10(n) 
    return helper(n, digits);

def helper(n, digits):
    
    if (n%10 == n ):
        return 1
    remainder = n%10
    return remainder * math.pow(10, digits-1)  + helper(n//10 , digits-1)

print(reverse2(1234))
print(sum)


# Count number of zeros

def countZeros(n,counter):

    if n == 0:
        return counter

    rem = n%10 
    if rem ==0:
        return countZeros(n//10, counter +1)
   
    return countZeros(n//10, counter)

print(countZeros(30121034302420,0))

# Sorted Array
arr=[1,2,6,4,3,-1,3]
def sorted(arr, index):

    if (index==len(arr)-1):
        return True
    
    return arr[index] < arr[index+1] and sorted(arr, index +1)

print(sorted(arr, 0))

# Linear Search

def search(arr, index, target):

    if (arr[index]==target):
        return index
    
    return search(arr, index+1, target)

print(search(arr, 0, 3))


# 
li = []
def findAllIndex(arr, index, target):

    if (index == len(arr)):
        return 

    if (arr[index]==target):
        li.append(index)
    
    return findAllIndex(arr, index+1, target)

print(findAllIndex(arr, 0, 3))
print(li)



# 33. Search in Rotated Sorted Array
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binarySearch(left, right, nums, target):
            while left <= right:
                mid = left + (right - left) // 2
                
                # Base Case
                if target == nums[mid]:
                    return mid

                # Right Side
                if nums[mid] < nums[right]:
                    if nums[mid] < target <= nums[right]:
                        return binarySearch(mid + 1, right, nums, target)
                    else:
                        return binarySearch(left, mid-1, nums, target)
                
                # Left Side
                else:
                    if nums[left] <= target < nums[mid]:
                        return binarySearch(left, mid-1, nums, target)
                    else:
                        return binarySearch(mid+1, right, nums, target)

        return binarySearch(0, len(nums)-1, nums, target)


sol = Solution()
nums = [3, 1]
target = 1
result = sol.search(nums, target)
print(result)