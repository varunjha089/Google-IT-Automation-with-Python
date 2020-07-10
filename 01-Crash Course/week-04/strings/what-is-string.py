def double_word(word):
    double_word_string = word * 2
    double_word_string_length = int(len(double_word_string))
    # noinspection PyTypeChecker
    final = double_word_string + str(double_word_string_length)
    return final


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return 0
