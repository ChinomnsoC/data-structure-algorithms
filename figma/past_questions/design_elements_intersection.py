#  # **Design Elements Intersection**

# As a Figma engineer, you need to implement a function that calculates the intersection area between two design elements (represented as rectangles) on the canvas.

# **Problem Statement:** Write a function that takes the coordinates of two rectangles, where each rectangle is defined by its bottom-left (x1, y1) and top-right (x2, y2) coordinates.

# **Input:**

# - Rectangle 1: (x1_left, y1_bottom, x1_right, y1_top)
# - Rectangle 2: (x2_left, y2_bottom, x2_right, y2_top)
# - All coordinates are in pixels
# - The coordinate system has (0,0) at the bottom-left of the canvas, with:
#     - x increasing rightward
#     - y increasing upward

# **Output:**

# - If the rectangles intersect: Return the intersection rectangle's coordinates in the same format: (left, bottom, right, top)
# - If the rectangles don't intersect: Return null

# **Example:**

# ```jsx
# // Example input
# const rect1 = [10, 10, 110, 110];  // bottom-left: (10,10), top-right: (110,110)
# const rect2 = [50, 50, 150, 150];  // bottom-left: (50,50), top-right: (150,150)

# // Expected output
# // [50, 50, 110, 110]  // intersection rectangle coordinates
# ```

# Intersecting rectangles
# Deal with X coordinates, then deal with Y
# Deal with X bottom, find max, then deal with X right, find min
# Same with y

# **3. Checking for actual overlap**

# If the calculated `intersection_left_x` is less than `intersection_right_x` AND `intersection_bottom_y` is less than 
# `intersection_top_y`, then the rectangles overlap, and the resulting intersection rectangle has a positive area.
# - If `intersection_left_x >= intersection_right_x` or `intersection_bottom_y >= intersection_top_y`, it means there's 
# no actual overlap, or the overlap has zero area (e.g., they only touch at an edge or corner).
# In essence, you are checking if the projections of the two rectangles onto both the x and y axes overlap. 
# If both projections overlap, the rectangles themselves overlap.
# This method assumes that larger Y values are "higher" on the y-axis, and X values increase to the right. 
# If your coordinate system is different, you might need to adjust the interpretations of "top" and "bottom" accordingly.


        
def calculate_intersection(rectangle_a, rectangle_b):
    
    def validate_input(rect):
        
        # check length
        if len(rect) != 4:
            return False, "Rectangle must have exactly 4 coordinates"
        
        left, bottom, right, top = rect
        
         
        # check the items in list are integers or coordinates
        
        if not all(isinstance(coord, (int, float)) for coord in rect):
            return False, "All coordinates must be numbers" 
    
        # check that left is always smaller than right 
        if left >= right:
            return False, f"Invalid coordinate for {left}"
        
    
        # check that bottom is smaller than top
        if bottom >= top:
            return False, f"Invalid coordinate for {bottom}"
        
        return True, "Valid"
    
    valid_rect_a, error_a = validate_input(rectangle_a)
    if not valid_rect_a:
        raise ValueError(f"Rectangle A invalid: {error_a}")
    
    valid_rect_b, error_b = validate_input(rectangle_b)
    if not valid_rect_b:
        raise ValueError(f"Rectangle A invalid: {error_b}")
    
    
    x1_left, y1_bottom, x1_right, y1_top = rectangle_a
    x2_left, y2_bottom, x2_right, y2_top = rectangle_b
    
    
    
    intersection_left_x = max(x1_left, x2_left) # 50
    intersection_right_x = min(x1_right, x2_right) # 110
    intersection_bottom_y = max(y1_bottom, y2_bottom) #50
    intersection_top_y = min(y1_top, y2_top) # 110
    
    if intersection_left_x < intersection_right_x and intersection_bottom_y < intersection_top_y:
        print("rectangles overlap")
        intersecting_area_coordinates = [intersection_left_x, intersection_bottom_y, intersection_right_x, intersection_top_y]

    else:
        print("rectangles do not overlap")
        intersecting_area_coordinates = None
        
    return intersecting_area_coordinates

        
rect1 = [0, 0, 10, 10]
rect2 = [10, 0, 20, 10]


answer = calculate_intersection(rect1, rect2)
print(answer)