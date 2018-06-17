#!/usr/bin/python3

"""
Reports on lane closures in Winnipeg
"""

from lib.api_data import API
from lib.output import console_out


def __init__():
    """ Make script go now! """
    lane_request = API()

    console_out(lane_request.get_data())


if __name__ == '__main__':
    __init__()
