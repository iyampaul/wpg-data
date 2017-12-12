#!/usr/bin/python3

"""
Pull data from data.winnipeg.ca
https://data.winnipeg.ca/browse
"""

from datetime import datetime
from sodapy import Socrata

def __init__():

    wpg_api = Socrata("data.winnipeg.ca", None)

    lane_list, validated_lanes = date_scope(pull_closures(wpg_api))

    output_lanes(lane_list, validated_lanes)

def pull_closures(wpg_api):
    """ Pull all publishes lane closures """
    return wpg_api.get("h367-iifg")

def date_scope(lanes):
    """
    In: Full lane output from API
    Out: lanes closed on current date and original list
    """
    validated_lanes = []

    for lane in lanes:
        # validate the lane
        closed_from, closed_to = range_format(lane)
        if date_range_check(closed_from, closed_to):
            validated_lanes.append(lane['lane_closure_id'])

    return lanes, validated_lanes

def range_format(lane):
    """
    In: One lane dict (2018-04-28T00:00:00)
    Out: formatted closed_from, closed_to strings (YYMMDD)
    """
    closed_from = datetime.strptime(lane['date_closed_from'], '%Y-%m-%dT%H:%M:%S')
    closed_to = datetime.strptime(lane['date_closed_to'], '%Y-%m-%dT%H:%M:%S')
    return closed_from, closed_to

def date_range_check(closed_from, closed_to):
    """
    In: closed_from and closed_to of the lane
    Out: binary if current date in range
    """
    if closed_from <= datetime.today() <= closed_to:
        return True
    else:
        return False

def output_lanes(lane_list, validated_lanes):
    """ Prints validated lanes """
    for v_lane in validated_lanes:
        for lane in lane_list:
            if lane['lane_closure_id'] == v_lane:
                print(lane['primary_street'] + " between " + lane['boundaries'])
                print(lane['traffic_effect'])
                print("-"*20)

if __name__ == '__main__':
    __init__()