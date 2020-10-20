# Isabella Gomez A15305555
# ECE143 HW3

# Instructions:
# Implement a sliding window for an arbitrary input list. The function
# should take the window width and the window increment as inputs and
# should produce a sequence of overlapping lists from the input list.
# For example, given x=list(range(15)), the following is the output
# given a window width of 5 and window increment of 2. In the event
# that the input parameters do not yield a complete set of even
# sublists, just truncate the ragged tail.

def slide_window(x,width,increment):
    '''
    This function returns a list of lists formatted to a given width. It
    goes through the given list and increments the items printed on the
    lines by the given increment number.

    :param x: arbitrary list
    :param width: width wanted of the list output
    :param increment: how the list increments per line
    :return: a list of lists
    '''

    # check x is a list of ints
    if len(x) > 0:
        for element in range(len(x)):
            assert type(x[element]) == int
    # if x is empty, return empty list
    elif len(x) == 0:
        return list(x)

    # check width and increments are positive ints greater than 0
    assert type(width) == int and type(increment) == int
    assert width > 0 and increment > 0

    # algorithm
    list_of_lists = []
    entry = [] # entries in the list of lists

    while True:
        # adds elements to entry for the size of the width
        for i in range(width):
            # if list is size of width, we are at end of list
            if len(x) <= width:
                list_of_lists.append(x)
                print(list_of_lists)
                return list_of_lists
            entry.append(x[i])

        # append to the final list a new entry
        list_of_lists.append(entry)
        entry = [] # empty the list

        # delete unnecessary elements from copyx
        for i in range(increment):
            x.pop(0)
