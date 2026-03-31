# Author: Arya Gupta
# Class Done Spot implements functionality of Done Spot Task
# Changes blackboard to show that the robot is done cleaning the spot by setting
# Spot cleaning variable to false
# returns succeded if spot cleaning is false, otherwise returns failed

import bt_library as btl
from ..globals import SPOT_CLEANING


class DoneSpot(btl.Condition):
    """
    Implementation of the condition "spot cleaning?".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        blackboard.set_in_environment(SPOT_CLEANING, False)

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, False) == False \
            else self.report_failed(blackboard)
