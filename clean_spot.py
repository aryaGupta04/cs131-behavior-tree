# Author: Arya Gupta
# Class Clean Spot implements functionality of Clean Spot Task
# Prints clean spot and always returns running

import bt_library as btl
from ..globals import SPOT_CLEANING

class CleanSpot(btl.Task):
    """
    Implementation of the Task "clean spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning Spot in progress...')

        return self.report_running(blackboard)
