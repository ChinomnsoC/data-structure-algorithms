def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    if len(intervals) == 1:
        return intervals
        
    output_list = [intervals[0]]
    print("output_list initial",output_list)
   
    for interval in intervals[1:]:
        # If the input interval overlaps with the last interval in the output list, 
        # merge these two intervals and replace the last interval of the output 
        # list with this merged interval.
        # For each pair, check if the start time of the next interval is less than 
        # or equal to the end time of the current interval. If it is, the intervals overlap.
        something = interval
        print(something)
        print(intervals[1:])
        if interval[0] <= output_list[-1][1]:
            print(f"there is an overlap between input interval {interval} and last interval of the output list {output_list}")
            print("interval[0] and output_list[-1][1]", interval[0], output_list[-1][1])
            print("interval[1], output_list[-1][1]", interval[1], output_list[-1][1])
            merged = merger(interval, output_list[-1])
            print("merged:", merged)
            output_list[-1] = merged
            print("output_list after merge:", output_list)         
        else:
            print("no overlap")
            output_list.append(interval)
            print("output_list no overlap", output_list)

    return output_list

def merger(input_list, last_interval_in_output_list):
    merged_intervals = [min(input_list + last_interval_in_output_list), max(input_list + last_interval_in_output_list)]
    return merged_intervals
    

# working_list = [[1, 5], [2, 6], [3, 7]] #Expected merge: [[1, 7]]
# working_list = [[1, 4], [5, 6], [6, 8]] # Expected merge: [[1, 4], [5, 8]]
# working_list = [[1, 2], [3, 4], [5, 6]] # Expected merge: [[1, 2], [3, 4], [5, 6]]
# working_list = [[1, 10], [2, 3], [4, 5], [6, 9]] # Expected merge: [[1, 10]]
# working_list = [[5, 7], [1, 3], [2, 6]] # Needs sorting first → Merge result: [[1, 7]]
# working_list = [[0,6333],[6462,7449],[7123,8776],[9958,9989],[9975,9990]] # Expected merge: [[0,6333],[6462,8776],[9958,9990]]
# merge_intervals(working_list)