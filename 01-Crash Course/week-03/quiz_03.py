# Question 01

# number = 1
# while number <= 7:
#     print(number, end=" ")
#     number += 1

# question 7
# def decade_counter():
#     while year < 50:
#         year += 10
#     return year
#
# >>> failure to initialize a variable

#  Question 2
#
# def show_letters(word):
#     for letter in word:
#         print(letter)
#
#
# show_letters("Hello")
# Should print one line per letter


# Question 3

# def digits(n):
#     count = 0
#     if n == 0:
#         count = 1
#     while n > 0:
#         n = n // 10
#         count += 1
#
#     return count
#
#
# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1

# Question 4

# def multiplication_table(start, stop):
#     for x in range(start, 10):
#         for y in range(1, 50):
#             print(str(x * y) + " | ", end=" ")
#         print(" | ")
#
#
# multiplication_table(1, 3)
# Should print the multiplication table shown above

# Question 5
#
# def counter(start, stop):
#     x = start
#     if x > stop:
#         return_string = "Counting down: "
#         while x >= stop:
#             return_string += str(x)
#             if isinstance(int(return_string[-1]), int):
#                 if int(return_string[-1]) != stop:
#                     return_string += ","
#             x -= 1
#     else:
#         return_string = "Counting up: "
#         while x <= stop:
#             return_string += str(x)
#             if isinstance(int(return_string[-1]), int):
#                 if int(return_string[-1]) != int(str(stop)[-1]):
#                     return_string += ","
#             x += 1
#     return return_string
#
#
# print(counter(1, 10))  # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1))  # Should be "Counting down: 2,1"
# print(counter(5, 5))  # Should be "Counting up: 5"
# print(counter(10, 1))  # Should be "Counting down: 2,1"

# Question 6
#
def even_numbers(maximum):
    return_string = ""
    if maximum != 0 and maximum != 1:
        for x in range(maximum + 1):
            if x != 0:
                if x % 2 == 0:
                    return_string += str(x) + " "
    return return_string.strip()


print(even_numbers(6))  # Should be 2 4 6
print(even_numbers(10))  # Should be 2 4 6 8 10
print(even_numbers(1))  # No numbers displayed
print(even_numbers(3))  # Should be 2
print(even_numbers(0))  # No numbers displayed

# Question 8

# for x in range(1, 10, 3):
#     print(x)

# Question 9
#
# for x in range(10):
#     for y in range(x):
#         print(y)

# Question 10
#
# def votes(params):
#     for vote in params:
#         print("Possible option:" + vote)
#
#
# votes(['yes', 'no', 'maybe'])
