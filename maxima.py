import numpy as np
def find_maxima(x):
    """Find local maxima of x.

    Example:
    >>> x = [1, 2, 3, 2, 4, 3]
    >>> find_maxima(x)
    [2, 4]

    Input arguments:
        x -- 1D list numbers

    Output:
        idx -- list of indices of the local maxima in x
    """

    idx = []
    for i in range(len(x)):
        if i == len(x) - 1:
            if x[i-1] < x[i]:
                idx.append(i)
        elif i == 0:
            if x[0] > x[1]:
                idx.append(i)
        # `i` is a local maximum if the signal decreases before and after it
        elif x[i-1] < x[i] and x[i+1] < x[i]:
            idx.append(i)
    return idx
