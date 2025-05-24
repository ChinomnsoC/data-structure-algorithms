def insert_interval(existing_intervals, new_interval):

    # Iterate through all intervals.
    # If current interval ends before new_interval starts → append it to output.
        # Else if current interval starts after new_interval ends → append new_interval (if not yet added), 
        # then append current interval.
        # Else → they overlap: merge current interval into new_interval.
    # After loop, if new_interval wasn't added yet, add it.

    output_list = []
    inserted = False
    for interval in existing_intervals:
        if interval[1] <= new_interval[0]:
            output_list.append(interval)
            print("smaller than new interval", output_list, "new interval", new_interval)
        elif interval[0] > new_interval[1]:
            if not inserted:
                output_list.append(new_interval)
                inserted = True
            output_list.append(interval)
        else:
            print("we are here")
            new_interval[0] = min(new_interval[0], interval[0])
            new_interval[1] = max(new_interval[1], interval[1])
            print("after merge", output_list, "interval", interval)
            print(interval, "something", output_list)

    if not inserted:
        output_list.append(new_interval)
        print(output_list)
        



    return output_list


existing = [[1,2],[3,4],[5,8],[9,15]] 
new_interval = [16,17]

insert_interval(existing, new_interval)
