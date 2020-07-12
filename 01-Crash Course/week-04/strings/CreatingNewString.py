word = "supercalifragilisticexpialidocious"

"""
    So using for loop it is iterating over length of word, and Using if statement if character at index "i" is equals
    to 'x' or not. This "i for i in range(len(word) - 1) if word[i] == 'x'" returns a "generator object" and 
    needed to be converted into "list" or "tuples", and as more than one value is possible to be in the list, so 
    using indexing method to access the string at index "0".
"""

print((list(i for i in range(len(word) - 1) if word[i] == 'x'))[0])