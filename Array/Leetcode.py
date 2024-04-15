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



