"""Given a list, sort it using insertion sort.

For example::

    >>> from random import shuffle
    >>> alist = range(1, 11)

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    >>> shuffle(alist)
    >>> insertion_sort(alist)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""


def insertion_sort(alist):
    """Given a list, sort it using insertion sort."""

    # INSERTION SORT:
        # start w/ 2nd item in lst
        # compare item to items in left, shifting it as long as item < comparison
        # when comparison > item, stop shift, and move on to next item
        # this algorithm sorts IN PLACE + best for almost-sorted lst + small lst

    # start at 2nd item (since 1st item has no left comparison)
    for idx in range(1, len(alist)):
        value = alist[idx]

        # compare value to each item to left of it
        i = idx - 1

        while i >= 0:
            # shift values
            if value < alist[i]:
                alist[i+1] = alist[i]
                alist[i] = value

                # move to left
                i -= 1
            else:
                break

    return alist


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE SORTING!\n"
