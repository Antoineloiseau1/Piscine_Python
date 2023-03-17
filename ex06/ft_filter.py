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
