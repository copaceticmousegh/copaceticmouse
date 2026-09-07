"""
# calculate discrete derivative from list of same length arrays of t and x
"""


def diff(t, x):
    if len(t) == len(x):
        v = []
        for i in range(len(t)-1):
            v.append((x[i+1]-x[i])/(t[i+1]-t[i]))
        return v
    else:
        return 'Arrays are not the same length'
    

