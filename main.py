#!/usr/local/bin/python3

"""
Reports on lane closures in Winnipeg
"""

from lib.api_data import API

def __init__():
    """ Make script go now! """
    lane_request = API()

    lane_request.get_data()


if __name__ == '__main__':
    __init__()
