def sort_colors(colors):
    n = len(colors)
    low, mid, high = 0, 0, n-1
    
    # starting list = [2,1,1,0,0]
    # colors[low] = 2
    # colors[mid] = 2
    # colors[high] = 0
    while mid <= high:
        if colors[mid] == 0:
            # 0, 0 = 0, 0
            colors[low], colors[mid] = colors[mid], colors[low]
            low += 1
            mid += 1
            # now colors[low] = 1 and colors[mid] = 1
            # second_iteration_results = [0, 1, 1, 0, 2]
            # fifth_iteration_results = [0, 0, 1, 1, 2]
            # for the 5th iteration, colors[low] = 1 on position  and colors[mid] = 2 on position 4
        elif colors[mid] == 1:
            mid += 1
            # now colors[low] = 1 on position 1 and colors[mid] = 1 on position 2
            # third_iteration_results = [0, 1, 1, 0, 2]
            # for the 4th iteration, colors[low] = 1 on position 1 and colors[mid] = 0 on position 3
        else:
            # 2, 0 = 0, 2
            # first_iteration_results = [0, 1, 1, 0, 2]
            colors[mid], colors[high] = colors[high], colors[mid]
            high -= 1 # n-2 = position 3
            # colors[low] = 0
            # colors[mid] = 0
            # colors[high] = 0
            
        
    return colors


colours_list = [0, 1, 0]

output_of_3sum = sort_colors(colours_list)

# Final output
print("\nSorted colors list:", output_of_3sum)

