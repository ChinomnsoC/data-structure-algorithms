# Minimize Flight Costs - 1 week before March 13th
# Bloomberg wants to invite N candidates to in-person interviews from different locations and Bloomberg will be paying for the flight tickets. 
# Bloomberg has to split the candidates equally across 2 locations, NY and SFO. You've been given a 2-D array of size N (N=number of candidates) and each candidate has 2 costs associated with him/her: cost of flight tickets to NY and second one is for SFO.

# [
# [CostToNY1, CostToSF1],
# [CostToNY2, CostToSF2],
# ...
# [CostToNYN, CostToSFN]
# ]
# where N = even number.
# Find total minimum cost to fly candidates for Bloomberg given the constraints.

# e.g. [[1,5], [8,2], [4,5] [4, 0]]
# For 2 candidates above, candidate0 can go to NY and candidate1 can go to SFO, which result in a total cost of 3

# Time: O(n log n) — dominated by the sort.
# Space: O(1) — sorting in place.
def maximize_flight_costs(invites_list):
    n = len(invites_list)
    
    # -4, -1, 4, 6
    
    running_sum = 0
    
    # if diff is neg, go to NY, if diff is positive, go to SF
    
    invites_list.sort(key=lambda x: x[0] - x[1])
    
    for i in range(n):
        
        candidate = invites_list[i]
        print(candidate)
        if i < n // 2:
            running_sum += candidate[0]
        else:
            running_sum += candidate[1]
    
        
    return running_sum

print(maximize_flight_costs([[1,5], [8,2], [4,5], [4, 0]]))