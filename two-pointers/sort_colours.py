def sort_colors(colors):
    n = len(colors)
    
    left, right = 0, n-1
    
    
    while left < right:
        if colors[left] == colors[left + 1]:
            continue
        # colors[left] - colors[left + 1]
        if (colors[left] > colors[left + 1]) and colors[left] - colors[left + 1] == 1:
            print(f"colors[left]: {colors[left]} is bigger than colors[left + 1]: {colors[left + 1]} ")
            position_of_left_plus_1 = left + 1
            colors.insert(0, colors.pop(position_of_left_plus_1))
            left += 1
            right -= 1
        
        elif (colors[left] > colors[left + 1]) and colors[left] - colors[left + 1] == 2:
            print(f"colors[left]: {colors[left]} is bigger than colors[left + 1]: {colors[left + 1]} ")
            colors.insert(n-1, colors.pop(left))
            print(colors)
            
            
  
        left += 1
        right -= 1
        print("new colors:", colors)
            
        # check for duplicates
        # check that i and i + 1 are the same, otherwise, the difference between the value at i and i+1 should be 1, and colors[i] < colors[i + 1]
        # if it is 2, then colors[i + 1] should move to the end of the list.
        # if the difference is one, but colors[i] > colors[i + 1] and colors[i + 1] is 0, then colors[i + 1] should move to the beginning of the list
    return colors


colours_list = [0,1,0]

output_of_3sum = sort_colors(colours_list)

# Final output
print("\nSorted colors list:", output_of_3sum)