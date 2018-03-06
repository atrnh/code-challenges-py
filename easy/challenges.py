def decode_string(word):
    """Return the decoded version of a string.

    Strings are encoded like this:
    - 'Apple' is 'A1p2l1e1'
    - 'cottage' is 'c1o1t2a1g1e1'
    - 'aabbbcca' is 'a2b3c2a1'

    Example:
    >>> decode_string('a2b3c2a1')
    'aabbbcca'
    >>> decode_string('a1p2l1e1')
    'apple'
    >>> decode_string('h1e1l2o1')
    'hello'
    """

    # write your code here...

    pass


def sum_unique(nums):
    """Return the sum of unique integers in a list.

    Example:
    >>> sum_unique([1, 2, 3])
    6
    >>> sum_unique([1, 1, 1, 1, 2, 2, 2])
    3
    """

    # write your code here...

    pass


def get_pig_latin(s):
    """Return the pig latin translation of a sentence.

    If a word starts with a consonant, put the consonant at the end and
    add 'ay' to it. For example, "drink" would be "rinkday"

    If a word starts with a vowel, only put 'ay' at the end of it. For
    example, "apple" would be "appleay"

    Example:
    >>> get_pig_latin("hello there")
    'ellohay heretay'
    >>> get_pig_latin("apples are delicious")
    'applesay areay eliciousday'
    >>> get_pig_latin("breakfast food")
    'reakfastbay oodfay'
    """

    # write your code here...

    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
