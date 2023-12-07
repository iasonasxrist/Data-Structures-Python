
import heapq



def replacement_selection(buffer_size, numbers):

    buffers = create_initial_buffers(buffer_size, numbers)
    sorted_output = merge_buffers(buffers)
    return sorted_output
    
def create_initial_buffers(buffer_size, numbers):

    buffers = []

    for i in range(0,len(numbers),buffer_size):
        
        buffer = numbers[i:i+buffer_size]
        buffer.sort()
        buffers.append({'data': buffer,'index': 0})

    return buffers


def merge_buffers(buffers):

    priority_queue = []
    output = []
    for buffer in buffers:
        if buffer['index'] < len(buffer['data']):
            heapq.heappush(priority_queue, (buffer['data'][buffer['index']], buffer))
            print(priority_queue)


    while priority_queue:
        min_num, next_buff = heapq.heappop(priority_queue)
        output.append(min_num)
            
        next_buff['index'] +=1
        if next_buff['index'] < len(next_buff['data']):
            heapq.heappush(priority_queue, (next_buff['data'][next_buff['index']], next_buff))

    return output




if __name__ == "__main__":

    input_numbers = [15, 3, 7, 25, 2, 18, 12, 9, 31, 5] #e.g Pages of Database must be loaded
    buffer_size = 4  # Number of elements that fit into memory
    sorted_output = replacement_selection(buffer_size, input_numbers) 
    print("External Merge Sort Solution", sorted_output)
