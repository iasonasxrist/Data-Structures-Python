
# Maximum sum of a subarray of size k
# O(n * k) Brute-Force

# Returns maximum sum in a
# subarray of size k.


def maxSum(arr, n, k):
    max_sum = -1
    for left in range(n - k +1):
        maxi = 0
        for right in range(k):
            maxi = maxi + arr[left + right] 
        # print(left, right)
        max_sum = max(maxi, max_sum)
        
    return max_sum


# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print("Find maximum (or minimum) sum of a subarray of size k \n",maxSum(arr, n, k))

print("Better Approach\n")
# Better Approach 

# O(n)

def SlidingWindowMaxSum(arr, n, k):

    max_sum = 0

    for left in range(n-k+1):
        suma = sum(arr[left: left + k])
        max_sum = max(suma, max_sum)
    
    return max_sum

print(SlidingWindowMaxSum(arr, len(arr),4) )


# Given an array of positive integers, 
# find the subarrays that add up to a given number

# Brute Force Aprroach
# O(n^2)

def lenOfLongSubarr(arr,n, value):
    count = 0
    for i in range(n):
        sami = 0

        for j in range(i+1,n):
            sami += arr[j]
            if sami == value:
                count+=1

    return count

arr = [1,7,4,3,1,2,1,5,1]
print("Longest Subarray given a number\n",lenOfLongSubarr(arr,n,7))


def Optimised(arr, n, value):
    count = 0
    left = 0
    suma = 0

    for right in range(n):
        # print(arr[left],arr[right])
        # increase the window
        suma += arr[right]
        while suma > value:
            # decrease it conditionally
            suma -= arr[left]
            left+=1
        if suma == value:
            count+=1  
      
    return count

print("Better Approach \n",Optimised(arr,n,7))

# Given an array of integers (NEGATIVE, POSITIVE, 0) 
# find the subarrays that add up to a given number

# Kadane's Algorithm

# TODO READ IT

# def KadanesApproach(arr,target):
#     count= 0
#     prefix_sum = {0:1}
#     suma = 0

#     for num in arr:

#         suma += num
#         print("suma:\n", suma)
#         count += prefix_sum.get(suma-target,0)
#         print("count: \n", count)
#         prefix_sum[suma] = prefix_sum.get(suma,0)+1 
#         print("prefix:\n", prefix_sum[suma])


#     return count
# print(KadanesApproach(arr, 7))


# Time Complexity: O(N)

def findSubarrayWithGivenSum(arr, target):
    
    left = 0
    suma=0

    for right in range(len(arr)):

        suma += arr[right]

        while suma > target:

            suma -= arr[left]
            left+=1
        if suma == target:
             print("Sum found between indexes % d and % d \n" % (left-1, right))
             return
        
    print("No subarray found")
    return


arr = [1, 4, 20, 3, 10, 5]
print("Find Subarray with given sum \n",findSubarrayWithGivenSum(arr,33))


# Sliding Window Maximum 

# Brute - Force
# O(n*k)

def SlidingWindowMaximumBruteForce(arr, k):

    for left in range(len(arr) - k + 1): 
        subset = []
        for right in range(left,left+k):

            subset.append(arr[right])
        maximum = max(subset)
        # print(f"Maximum of subset {subset} is {maximum}")
    return

arr=[1, 2, 3, 1, 4, 5, 2, 3, 6]
print("Sliding Window Maximum (Maximum of all subarrays of size K)\n",SlidingWindowMaximumBruteForce(arr,3))

print("Better Approach \n")

# Best solution
# O(n)
def SlidingWindowMaximum(arr,k):

  
    for left in range(len(arr) - k + 1): 
            subset = arr[left: left+k]
            max_value = max(subset)
            print(f"Maximum of subset {subset} is {max_value}")
        
    return

print(SlidingWindowMaximum(arr,3))




# Length of the longest substring without repeating characters

x = "AABCDEFGABEF"
def LongestSubstring(x):
    setOfString = []
    left = 0
    max_length = 0
    for right in range(len(x)):
        while x[right] in setOfString:
            print(left)
            if x[right] in setOfString:
                setOfString.remove(x[left])
                left+=1
           
    
        setOfString.append(x[right])
        max_length = max(max_length, right-left+1)
         
    return max_length
            

# Test cases
test_cases = ["ABCDEFGABEF", "ABCBDEFGH", "AAAAA", "ABCD", ""]
for x in test_cases:
    print(f"Length of the longest substring without repeating characters in '{x}': {LongestSubstring(x)}")


# 5. Longest Palindromic Substring

s="lookkooa"


def longestPalindrome(x):
    res=""
    count=0

    for i in range(len(x)):

        # odd
        left, right = i, i
        while left >= 0 and right<len(x) and x[left] == x[right]:
                if (right -left + 1) > count:
                    res = x[left:right+1]
                    count = right - left + 1

                left -= 1
                right +=1
        # even 
        left, right = i, i + 1 
        while left >= 0 and right<len(x) and x[left] == x[right]:
                if (right -left + 1) > count:
                    res = x[left:right+1]
                    count = right - left + 1

                left -= 1
                right += 1
        


    return res
print(f"Longest Palindrome", {longestPalindrome(s)})

# 28. Find the Index of the First Occurrence in a String

def strStr( haystack: str, needle: str) -> int:
    k = len(needle)

    for right in range(len(haystack)- k + 1):
        if haystack[right:right+k] == needle:
            return right
    
    return -1

haystack = "sadbutsad"
needle = "sad"
print(f"FindIndexOfOccurence", {strStr(haystack,needle)})