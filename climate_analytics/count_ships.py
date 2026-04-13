def hasShips(bottomLeft, topRight) -> bool:
    # Black box — given to you, do not implement
    # Returns True if at least one ship exists in the rectangle
    pass


def countShips(bottomLeft, topRight) -> int:
    # bottomLeft = (x1, y1)
    # topRight = (x2, y2)
    x1, y1 = bottomLeft
    x2, y2 = topRight
    
    if x1 > x2 or y1 > y2:
        return 0

    if not hasShips(bottomLeft, topRight):
        return 0

    if x1 == x2 and y1 == y2:
        return 1

    midX = (x1 + x2) // 2
    midY = (y1 + y2) // 2

    return (
        countShips(bottomLeft, (midX, midY))
        + countShips((midX + 1, y1), (x2, midY))
        + countShips((x1, midY+1), (midX, y2))
        + countShips((midX + 1, midY+ 1), (x2, y2))
    )

# Complexity:

# Time: O(S log N) where S = number of ships, N = grid size — branches with no ships are pruned immediately
# Space: O(log N) recursion depth

# ```

# Example:
# ```
# Ships are at: (1,1), (3,3), (4,2)

# countShips((0,0), (4,4)) → 3
# countShips((0,0), (2,2)) → 1  # only (1,1) in this area
# countShips((3,0), (4,4)) → 2  # (3,3) and (4,2)
# ```
