# ___A better solution____

def insert_interval(existing_intervals, new_interval):
  i = 0
  n = len(existing_intervals)
  output_list = []
  # existing_interval is less than new interval, append the existing_interval to the output_list
  # increase i counter
  while i < n and existing_intervals[i][0] < new_interval[0]:
    output_list.append(existing_intervals[i])
    i +=1
  # Here we check that the new_interval doesn't overlap, and if it doesn't, 
  # we append it to the output_list
  if not output_list or output_list[-1][1] < new_interval[0]:
    output_list.append(new_interval)
  # if there is an overlap, we merge
  else:
    output_list[-1] = [min(new_interval + output_list[-1]), max(new_interval + output_list[-1])]
  # once we've successfully added the new_interval to the output_list, we handle the rest of the existing_intervals
  while i < n:
    # we check that the next interval in existing_intervals doesn't overlap with the last item in output_list
    if existing_intervals[i][0] <= output_list[-1][1]:
      # if there's an overlap, we merge with the last item in output_list
      output_list[-1][1] = max(existing_intervals[i][1], output_list[-1][1])
    else:
      # if there's no overlap, append the current interval
      output_list.append(existing_intervals[i])
    # increase counter so that we move forward in life
    i += 1

  return output_list

# Initial Solution
def insert_interval_second_solution(existing_intervals, new_interval):

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
