def count_in_list(lst: list, needle: str) -> int:
    """
    Count N times needle appears in lst
    """
    return len([i for i in lst if i == needle])
