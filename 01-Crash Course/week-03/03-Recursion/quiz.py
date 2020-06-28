def is_power_of(number, base):
    # Base case: when number is smaller than base.
    if number < base:
        # If number is equal to 1, it's a power (base**0).
        return number == 1

    # Recursive case: keep dividing number by base.
    return is_power_of(number // base, base)


print(is_power_of(8, 2))  # Should be True
print(is_power_of(64, 4))  # Should be True
print(is_power_of(70, 10))  # Should be False
print(is_power_of(128, 2))


# def count_users(group):
#     count = 0
#     for member in get_members(group):
#         count += 1
#
#         if is_group(member):
#             count += count_users(member)
#             count -= 1
#     return count
#
# print(count_users("sales"))  # Should be 3
# print(count_users("engineering"))  # Should be 8
# print(count_users("everyone"))  # Should be 18
