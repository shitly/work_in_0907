# from django.test import TestCase

# Create your tests here.

def BinnaySerach(ls, m):
    low_index = 0
    high_index = len(ls) - 1

    while (low_index <= high_index):
        mid_index = int(low_index + 0.5 * (high_index - low_index))
        midval = ls[mid_index]

        if midval < m:
            low_index = mid_index + 1
        elif midval > m:
            high_index = mid_index - 1
        else:
           return ls[mid_index]

    return ls[high_index]

ls = [2,3,4,55,66,77]
print(BinnaySerach(ls, 3))
