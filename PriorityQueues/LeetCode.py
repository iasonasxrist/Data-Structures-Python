from collections import defaultdict
from queue import PriorityQueue
from heapq import *

# 215. Kth Largest Element in an Array


def findKthLargest(nums, k) -> int:

    nums = list(map(lambda x: -x, nums))
    heapify(nums)
    print(nums)
    for i in range(k-1):
        heappop(nums)
    return -heappop(nums)


print(findKthLargest([1, 4, 7, 9, 2, 3], 2))

# 1338. Reduce Array Size to The Half


def minSetSize(arr) -> int:

    freq_map = defaultdict(int)
    for element in arr:
        freq_map[element] = freq_map[element] + 1

    queue = PriorityQueue()
    for value in freq_map.values():
        neg_value = -value
        queue.put(neg_value)

    count = 0
    sumx = 0
    half_size = len(arr)/2

    while (sumx < half_size):

        real_value = queue.get()
        freq = -real_value
        sumx += freq
        count += 1

    return count


arr = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
print(minSetSize(arr))

nums = [3, 3, 3, 3, 5, 5, 5, 2, 2, 7]
# 347. Top K Frequent Elements


def topKFrequent(nums, k: int):

    my_map = defaultdict(int)

    for element in nums:
        my_map[element] = my_map[element] + 1

    queue = []
    for key, v in my_map.items():
        heappush(queue, (v, key))
        if k < len(queue):
            print(queue)
            heappop(queue)

    print(queue)

    result = []
    while (queue):
        v, key = heappop(queue)
        result.append(key)
    return result


print(topKFrequent(nums, 2))
