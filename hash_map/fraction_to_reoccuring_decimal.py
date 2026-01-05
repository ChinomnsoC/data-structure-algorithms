def fraction_to_decimal(numerator, denominator):
    if numerator == 0:
        return "0"

    result = ""

    if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0):
        result += "-"

    numerator = abs(numerator)
    denominator = abs(denominator)

    integer_part_of_result = numerator // denominator
    result += str(integer_part_of_result)

    remainder = numerator % denominator

    print("integer_part_of_result", integer_part_of_result)
    print("remainder", remainder)
    print(numerator / denominator)

    if remainder == 0:
        print("here")
        return result
    else:
        result += "."

    remainder_hash_map = {}

    while remainder != 0:
        if remainder in remainder_hash_map:
            index = remainder_hash_map[remainder]
            result = result[:index] + "(" + result[index:] + ")"
            return result

        remainder_hash_map[remainder] = len(result)

        remainder *= 10
        digit = remainder // denominator
        result += str(digit)
        remainder = remainder % denominator

    return result


print(fraction_to_decimal(99999, 39196))
