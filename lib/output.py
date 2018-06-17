"""
Central control for data publishing, storage, reporting
"""

from .api_data import closed_dates

import math

def console_out(lane_data):
    """ 
    In: List of tuples from lane data
    Out: Prints lane data to console
    """

    for i in lane_data:

        c_from, c_to = closed_dates(i)

        print(i['primary_street'], c_header(i))
        print("From:", c_from.date(), " To:", c_to.date())
        print("Between:", i['boundaries'])
        print("Effect:")

        for i in c_effect(i['traffic_effect']):
            print(i)

        print("-"*60)

def c_header(i):
    """ Clean, standard size header """
    num_dash = 59 - len(i['primary_street'])
    return "-"*num_dash

def c_effect(i):
    """ Splits traffic effect shorter line length, watching for spaces """
    e = len(i)
    j = 1
    rot = int(math.ceil(e / 50.0))
    e_list = []

    low = 0
    high = 50

    while j <= rot:
        while not c_space(i,high):
            if high > len(i):
                break
            high += 1
        if j == 1:
            e_list.append(i[low:high])
        else:
            e_list.append(i[low+1:high])
        low = high
        high += 50
        j += 1
    return e_list

def c_space(i, h):
    """ Finds the next space so it doesn't cut words """
    j = h + 1
    if i[h:j] == " ":
        return True
    else:
        return False

