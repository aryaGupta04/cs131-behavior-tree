# Author: Arya Gupta
# Class Spot Cleaning implements functionality of Spot Cleaning Condition
# Returns succeded if Spot cleaning is true, otherwise returns failed
import bt_library as btl
from ..globals import SPOT_CLEANING


class SpotCleaning(btl.Condition):
    """
    Implementation of the condition "spot cleaning?".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        bl = blackboard.get_in_environment(SPOT_CLEANING, False)
        print(bl, 'in SPOT CLEANING')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(SPOT_CLEANING, False) \
            else self.report_failed(blackboard)
