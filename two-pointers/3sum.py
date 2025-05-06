def three_sum(nums):
    target = 0
    length_of_nums = len(nums)
    triplets = []
    result = [[]]

    for i in range(length_of_nums - 2):
        print("i value =", i)
        our_set = set()

        for j in range(length_of_nums - 1):
            print("j value =", j)
            second_triplet = target - nums[i] - nums[j]
            print("second triplet", second_triplet)
            if second_triplet in our_set:
                trip = [nums[i], second_triplet, nums[j]]
                if trip not in triplets:
                    triplets.append(trip)
                print("triplet", trip)
                print("grouped triplets", triplets)

            our_set.add(nums[j])
            print("our set", our_set)

    return triplets


# --------------------------
# Example usage
# --------------------------

our_list = [-4, -2, -2, -2, 0, 2, 2, 2, 4]

output_of_3sum = three_sum(our_list)

# Final output
print("\nFinal linked list:", output_of_3sum)
