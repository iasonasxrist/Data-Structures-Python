# Subset of array
# Naive solution
# O(n*m)
def isSubset(arr1, arr2):
    n = len(arr1)
    m = len(arr2)

    for i in range(m):
        for j in range(n):
            if arr2[i] == arr1[j]:
                break
        if (j == n):
            return 0
    return 1



# Hashe Table
# O(m+n)
def hash_is_a_subset(arr1, arr2):
    n = len(arr1)
    m = len(arr2)
    hashset = set()

    for i in range(n):
        hashset.add(arr1[i])

    for j in range(m):
        if arr2[j] in hashset:
            continue
        else:
            return False

    return True


def union_Intersection_Hashing(arr1, arr2):
    hashmap = set()
    union =[]
    intersection = set()
    for i in range(len(arr1)):
        hashmap.add(arr1[i])
        union.append(arr1[i])

    for j in range(len(arr2)):
        union.append(arr2[j])
        if arr2[j] in hashmap:
            intersection.add(arr2[j])
    
    return union,intersection


if __name__ == "__main__":

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 7, 1]

    if isSubset(arr1, arr2):
        print("array2 is subset of array1")
    else:
        print("array2 is not a subset of array1")

    if hash_is_a_subset(arr1, arr2):
        print("array2 is subset of array1")
    else:
        print("array2 is not a subset of array1")

    union,intersection = union_Intersection_Hashing(arr1, arr2)
    print(union,intersection)


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashS = dict()
        hashT = dict()

        for i in s:
            hashS[i] = hashS.get(i,0)+1

        for i in t:
            hashT[i] = hashT.get(i,0)+1
                

        for i in hashT:
            if hashT[i] > hashS[i] or i not in hashS:
                return i
            
# Test cases
sol = Solution()
print(sol.findTheDifference("abcd", "abcde"))  # Output: 'e'
