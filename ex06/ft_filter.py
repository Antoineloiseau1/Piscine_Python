# print(filter.__doc__)
def ft_filter(function, iterable):
    """ft_filter(function or None, iterable) --> ft_filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    if function is None:
        var = [item for item in iterable if item]
    else:
        var = [item for item in iterable if function(item)]
    for item in var:
        yield item

# if __name__ == "__main__":
# 	letters = ['a', 'b', 'd', 'e', 'i', "", 0]

# 	# a function that returns True if letter is vowel
# 	def filter_vowels(letter):
# 		vowels = ['a', 'e', 'i', 'o', 'u']
# 		return True if letter in vowels else False

# 	# filtered_vowels = filter(None, letters)
# 	filtered_vowels = ft_filter(None, letters)

# 	# converting to tuple
# 	vowels = tuple(filtered_vowels)
# 	print(vowels)
