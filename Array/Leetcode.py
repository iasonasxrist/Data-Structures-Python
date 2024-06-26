# 88. Merge Sorted Array

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
def merge( nums1, m, nums2, n):
 
    p1 = m - 1 
    p2 = n - 1
    al = m + n - 1
    
    while p1>=0 and p2>=0:
        
        # edge case 1 :
        # nums1[i] > nums2[j]
    
    
        if nums1[p1] > nums2[p2]:
            nums1[al] = nums1[p1]
            al -= 1
            p1 -= 1
        
        # edge case 2 :
        # nums1[i] < nums2[j]
    
        else:
            nums1[al] = nums2[p2]
            al -= 1
            p2 -= 1
    
        # edge case 3:
        # nums2 has sufficient data which  nums1[i] < nums2[j]
    while p2 >= 0:
        
        nums[al] = nums[p2]
        p2-=1
        al-=1
    return nums1
    
print(merge( nums1, m, nums2, n))

# 27. Remove Element

def removeElement(nums, val):
    k=0
    for i in range(len(nums)):
        if nums[i]!=val:
            nums[k] = nums[i]
            k += 1
    return k

nums = [3,2,2,3]
print(removeElement(nums, 2))


nums=[1,1,2,2,3,3,3,4,5,5,6]

# 80. Remove Duplicates from SortedArrayII
def removeDuplicatesFromArray(nums):
    l=0
    for r in range(0,len(nums)):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1
        print(l,r,nums)
    return l
    
print(removeDuplicatesFromArray(nums))
    
    
# 1929. Concatenation of Array
   
def getConcatenation(nums):
    n = len(nums)
    new = [0] * (2*n)

    for i in range(len(nums)):

        new[i] = nums[i]
        new[n+i] = nums[i]
        print(new)
        
    return new 
nums = [1,2,3]
new = getConcatenation(nums)
print(new)

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0 , len(nums)-1

        while left <= right:
            mid = left + (right - left) //2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid]:
                left+=1
                continue
            if  nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]: 
                    left = mid+1
                else:
                   right = mid-1
            else:
                if nums[left] <= target <= nums[mid]:

                    right= mid - 1
                else:
                    left = mid + 1
        return False

solution = Solution()
ok = solution.search([1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1], 13)
print("ok",ok) 


# Box interview question
def getSecondLargestNumber(arr):

    first ,second = -1 , -1 
     
    if len(arr)< 2 :
            return None
    for i in range(len(arr)):
        
        if arr[i]> first:
            second = first
            first = arr[i]
        elif arr[i]>second and arr[i]<first:
            second = arr[i]

    if second == -1:
        return None
    return second
# Test cases
test_cases = [
    ([1, 2, 3, 4, 5], 4),      # Second largest is 4
    ([7, 3, 9, 1, 4], 7),       # Second largest is 7
    ([1, 1, 1, 1], None),       # All elements are the same, no second largest
    ([5], None),                # Only one element, no second largest
    ([], None)                  # Empty array, no second largest
]

# Run test cases
for arr, expected_result in test_cases:
    result = getSecondLargestNumber(arr)
    print(f"Array: {arr}, Second Largest: {result}, Expected: {expected_result}")


# 229. Majority Element II
#  find all elements that appear more than ⌊ n/3 ⌋ times.



def MajorityElement(arr):
    hashmap = dict()

    if len(arr) < 2 :
        return arr
    for i in range(len(arr)):
        
        if arr[i] in hashmap:
            hashmap[arr[i]] +=1
        else:
            hashmap[arr[i]] = 1
    
    li = []

    for key, value in hashmap.items():
        if value > len(arr)//3 :
            li.append(key)
    
    return li

# Test cases
test_cases = [
    ([3, 2, 3], [3]),                  # 3 is the majority element
    ([1, 1, 1, 3, 3, 2, 2, 2], [1, 2]), # 1 and 2 are majority elements
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), # No majority element
    ([1], [1]),                         # Single element array
    ([], [])                            # Empty array
]

# Run test cases
for arr, expected_result in test_cases:
    result = MajorityElement(arr)
    print(f"Array: {arr}, Majority Elements: {result}, Expected: {expected_result}")




def findPeakElement(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = left + (right - left) // 2

        if nums[mid] < nums[mid + 1]:
            # Peak must be on the right side of mid
            left = mid + 1
        else:
            # Peak must be on the left side of or at mid
            right = mid

    # At the end of the loop, left and right will converge to the peak element
    return left


# Test cases
test_cases = [
    ([1, 2, 3, 1], 2),      # Peak element is 3
    ([1, 2, 1, 3, 5, 6, 4], 5), # Peak element is 6
    ([1, 2, 3, 4], 3),      # Peak element is 4
    ([4, 3, 2, 1], 0)       # Peak element is 4
]

# Run test cases
for nums, expected_result in test_cases:
    result = findPeakElement(nums)
    print(f"Array: {nums}, Peak Element Index: {result}, Expected Index: {expected_result}")
