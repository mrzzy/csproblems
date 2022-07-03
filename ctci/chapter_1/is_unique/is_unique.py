#
# Cracking the Coding Interview
# Chapter 1
# 1. Is Unique
#


def is_member(c: str, search_str: str) -> bool:
    """Performs binary search to determine if character c is in search str.

    Args:
        c: The character to search for
        search_str: The sorted search string to binary search for the character c.
    Returns:
        True if c is in search_str, False otherwise
    """
    if len(search_str) <= 0:
        return False

    # check if mid is c, use int division with //
    mid = len(search_str) // 2
    if search_str[mid] == c:
        return True
    # otherwise recusively search half of search_str
    elif search_str[mid] > c:
        return is_member(c, search_str[:mid])
    else:
        return is_member(c, search_str[mid + 1 :])


def is_unique(check_str: str) -> bool:
    """Determines if the given string is unique

    Args:
        check_str: string to check if it is unique.
    Returns:
        True if the string is unique False otherwise
    """
    if len(check_str) in [0, 1]:
        return True

    # sort the check_str so that we can do binary search on it
    check_str = "".join(sorted([c for c in check_str]))

    for i in range(len(check_str) - 1):
        # check next character f
        c, search_str = check_str[i], check_str[i + 1 :]
        # check if c is in search str
        if is_member(c, search_str):
            return False
    # no character matches any other in check_str
    # hence check_str is unique
    return True
