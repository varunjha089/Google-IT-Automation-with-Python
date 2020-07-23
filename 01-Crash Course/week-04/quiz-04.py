"""
    This python file is for quiz on week - 04
"""

"""
    Question 01
    
    Not quite. How are you deciding which part of the address is
    the house number and which is the street name? Are you
    removing any trailing blank spaces? Properly formatting the
    return string?
"""

# def format_address(address_string):
#     # Declare variables
#     number = ''
#     name = ''
#
#     # Separate the address string into parts
#     address_list = address_string.split()
#
#     # Traverse through the address parts
#     for lists in address_list:
#         # Determine if the address part is the
#         # house number or part of the street name
#         if lists.isnumeric():
#             number = lists
#
#         # Does anything else need to be done
#         # before returning the result?
#         else:
#             name += lists
#
#     # Return the formatted string
#     return "house number {} on street named {}".format(number.strip(), name.strip())
#
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


"""
    NOT COMPLETED
    Question 2
    InfraError
"""

# def highlight_word(sentence, word):
#     new_sentence = ''
#     sentence_list = sentence.split()
#     # print(sentence_list)
#
#     for lists in sentence_list:
#         if lists.find(word) != -1:
#             new_sentence += lists.upper()
#             new_sentence += " "
#         else:
#             new_sentence += lists
#             new_sentence += " "
#
#     return new_sentence
#
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


"""
    Question 3
    Not quite. Remember that some list functions alter the
    original list instead of returning a new list. Which
    function appends all elements of one list to the end of
    another list, and how are the arguments passed to it?
"""

# def combine_lists(list1, list2):
#     # Generate a new list containing the elements of list2
#     # Followed by the elements of list1 in reverse order
#     list2_copy = list2
#     return list2_copy + list1[::-1]
#
#
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
#
# print(combine_lists(Jamies_list, Drews_list))

# Question 4 ( correct )

# def squares(start, end):
#     return [i**2 for i in range(start, end + 1)]
#
#
# print(squares(2, 3))  # Should be [4, 9]
# print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
# print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


# Question 5 ( correct )

# def car_listing(car_prices):
#     result = ""
#     for i in car_prices:
#         result += "{} costs {} dollars".format(i, car_prices[i]) + "\n"
#     return result
#
#
# print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))

# Question 6 ( correct )

# def combine_guests(guests1, guests2):
#     # Combine both dictionaries into one, with each key listed
#     # only once, and the value from guests1 taking precedence
#     return dict(guests2, **guests1)
#
#
# Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
# Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))


"""
    Question 7
    InfraError
"""


def count_letters(text):
    result = {}
    whitelist = set('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    final_string =''.join(filter(whitelist.__contains__, text))
    # Go through each letter in the text
    for word in final_string.lower().replace(' ', ''):
        # Check if the letter needs to be counted or not
        # print(word)

        if word.isalpha() not in result:
            result[word] = 1
        else:
            update_key = result[word]
            update_key += 1
            result[word] = update_key
        # Add or increment the value in the dictionary
        # ___
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# Question 8 ( correct )

# animal = "Hippopotamus"
#
# print(animal[3:6])
# print(animal[-5])
# print(animal[10:])


# Question 9 ( correct )

# colors = ["red", "white", "blue"]
# colors.insert(2, "yellow")
# print(colors)


# Question 10 ( correct )
#
# host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
# print(host_addresses.keys())
