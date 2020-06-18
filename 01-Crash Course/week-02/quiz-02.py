"""
    question 01
"""


def color_translator(color):
    if color == "red":
        hex_color = "#ff0000"
    elif color == "green":
        hex_color = "#00ff00"
    elif color == "blue":
        hex_color = "#0000ff"
    else:
        hex_color = "unknown"
    return hex_color


print(color_translator("blue"))  # Should be #0000ff
print(color_translator("yellow"))  # Should be unknown
print(color_translator("red"))  # Should be #ff0000
print(color_translator("black"))  # Should be unknown
print(color_translator("green"))  # Should be #00ff00
print(color_translator(""))  # Should be unknown

"""
    question 02
"""

# print("big" > "small")

"""
    question 04
"""


def exam_grade(score):
    if score > 95:
        grade = "Top Score"
    elif score >= 60:
        grade = "Pass"
    else:
        grade = "Fail"
    return grade


print(exam_grade(65))  # Should be Pass
print(exam_grade(55))  # Should be Fail
print(exam_grade(60))  # Should be Pass
print(exam_grade(95))  # Should be Pass
print(exam_grade(100))  # Should be Top Score
print(exam_grade(0))  # Should be Fail

"""
    question 05
"""

print(11%5)

"""
    question 06
"""


def format_name(first_name, last_name):
    # code goes here
    name = ''
    if first_name and last_name:
        name = first_name + ", " + last_name
    elif first_name:
        name = first_name
    elif last_name:
        name = last_name
    else:
        name = name
    string = "Name: " + name
    return string


print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string


"""
    question 07
"""


def longest_word(word1, word2, word3):
    if len(word1) >= len(word2) and len(word1) >= len(word3):
        word = word1
    elif len(word2) >= len(word1) and len(word2) >= len(word3):
        word = word2
    else:
        word = word3
    return (word)


print(longest_word("chair", "couch", "table"))
print(longest_word("bed", "bath", "beyond"))
print(longest_word("laptop", "notebook", "desktop"))

"""
    question 08
"""


def sum(x, y):
    return x + y


# print(sum(sum(1, 2), sum(3, 4)))

"""
    question 09
"""

# print((10 >= 5*2) and (10 <= 5*2))

"""
    question 10
"""


def fractional_part(numerator, denominator):
    # Operate with numerator and denominator to
    # keep just the fractional part of the quotient

    fraction = 0
    if numerator != 0 and denominator != 0:
        fraction = numerator % denominator

    return fraction


print(fractional_part(5, 5))  # Should be 0
print(fractional_part(5, 4))  # Should be 0.25
print(fractional_part(5, 3))  # Should be 0.66...
print(fractional_part(5, 2))  # Should be 0.5
print(fractional_part(5, 0))  # Should be 0
print(fractional_part(0, 5))  # Should be 0
