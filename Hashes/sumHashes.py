arr = [0, -1, 2, -3, 1]
target = -2
d = {}


def sum(target, arr):
    for i in range(len(arr)-1):
        if target - arr[i] in arr:
            print(True)
            d[arr[i]] = i
            return d
    return False


# print(sum(target, arr))

# brute force solution
# Time Complexity O(N^2)

arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]


def maxOccurence(arr, element):
    max_dist = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j] and element == arr[i]:
                x = abs(j-i)
                max_dist = max(max_dist, x)

    return max_dist


# print(maxOccurence(arr, 2))


# hash solution
# Time Complexity O(n)

def hashSolution(arr, element):
    max_dist = 0
    d = {}
    print(d)
    for i in range(len(arr)):
        if not arr[i] in d:
            d[arr[i]] = i
        else:
            x = abs(d[arr[i]] - i)
            max_dist = max(max_dist, x)
    return max_dist


# print(hashSolution(arr, 2))


# Most frequent element in an array

# hash solution
# Time Complexity O(n)

arr = [40,50,30,50,30,30]
def maxFrequency(arr):
    d = {}
    maxFreq = -1
    res = -1
    for i in range(len(arr)):
        if not arr[i] in d.keys():

            d[arr[i]] = 1
        else:
            d[arr[i]] +=1
        
    for key, value in d.items():
        print(key, value)
        if value > maxFreq:
            res = key
            maxFreq = value
        
    return res, maxFreq

# print( maxFrequency(arr))


# Find the only repetitive element between 1 to N-1

# hash solution
# Time Complexity O(n)

arr=[1, 3, 2, 3, 4]
def onlyRepetition(arr):
    d={}
    for i in range(len(arr)-1):
        if not arr[i] in d:
            d[arr[i]] = 0
        else:
            d[arr[i]] += 1
    
    for key, value in d.items():
        if value >0:
           return key

    return -1
# print( onlyRepetition(arr))


# How to check if two given sets are disjoint
arr1 = [12, 34, 11, 9, 3]
arr2 = [7, 2, 1, 5]
def isDisjoint(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)

    arr = arr1 - arr2
    if len(arr)==0:
        return True
    
    return arr

print(isDisjoint(arr1,arr2))