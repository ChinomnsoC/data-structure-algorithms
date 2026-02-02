from collections import deque

def sliding_window_max(nums_list, window_size):
    if not nums_list or window_size == 0:
        return []
    
    if len(nums_list) <= window_size:
        return [max(nums_list)]
    
    indices_deque = deque()
    result = []
    
    # number_of_windows = len(nums_list) - window_size + 1
    # sliding_window_max([1,3,-1,-3,5,3,6,7], 3))
    
    for current_index in range(len(nums_list)):
        window_start_index = current_index - window_size + 1
        
        while indices_deque and indices_deque[0] < window_start_index:
            indices_deque.popleft()
            
        
        while indices_deque and nums_list[current_index] > nums_list[indices_deque[-1]]:
            indices_deque.pop()
            
        
        indices_deque.append(current_index)
        
        # have we processed enough indices to cover for our first window?
        if current_index >= window_size - 1:
            result.append(nums_list[indices_deque[0]])
        
    return result
        
        
        