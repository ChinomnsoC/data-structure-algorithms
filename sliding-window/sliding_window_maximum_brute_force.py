def sliding_window_max_brute_force(numbers_list, window_size):
    if len(numbers_list) <= window_size:
        return numbers_list
    
    output = []
    number_of_windows = len(numbers_list) - window_size + 1
    # O(1)
    # [a, b, c, 5, 3, 6, 7, 9, 0, 10]
    
    for start_index in range(number_of_windows):
        end_index = start_index + window_size
        current_window = numbers_list[start_index:end_index]
        
        current_max_value = current_window[0]
        for item in current_window:
            if item > current_max_value:
                current_max_value = item
        
        output.append(current_max_value)
    
    return output
        