"""
Pull lane closure data from data.winnipeg.ca
https://data.winnipeg.ca/browse
"""

from datetime import datetime
from sodapy import Socrata


SOCRATA_API = "data.winnipeg.ca"


class API():
    """ Connect, gather, return lane data  """

    def __init__(self):
        """ Initialize the OpenData API """
        self.api = Socrata(SOCRATA_API, None)
        self.closed_lanes = []

    def get_data(self):
        """
        Returned closed lanes on current date
        """
        lane_data = self.api.get("h367-iifg")

        for i in lane_data:
            c_from, c_to = closed_dates(i)
            if range_check(c_from, c_to):
                self.closed_lanes.append(i)

        return self.closed_lanes

def closed_dates(lane):
    """
    In: One lane dict (2018-04-28T00:00:00)
    Out: formatted c_from, c_to datetime variables
    """
    c_from = datetime.strptime(lane['date_closed_from'], '%Y-%m-%dT%H:%M:%S')
    c_to = datetime.strptime(lane['date_closed_to'], '%Y-%m-%dT%H:%M:%S')
    return c_from, c_to

def range_check(c_from, c_to):
    """
    In: closed from, closed to datetime variables
    Out: binary if today() within closed to/from range.
    """
    if c_from <= datetime.today() <= c_to:
        return True
    else:
        return False
