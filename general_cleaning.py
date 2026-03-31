# Author: Arya Gupta
# Class General Cleaning implements functionality of General Cleaning Condtition
# Returns failed if General cleaning is false, otherwise returns succeded
import bt_library as btl
from ..globals import GENERAL_CLEANING


class GeneralCleaning(btl.Condition):
    """
    Implementation of the condition "general clean?".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:

        bl = blackboard.get_in_environment(GENERAL_CLEANING, False)
        print(bl, 'in GENERAL CLEANING')

        return self.report_failed(blackboard) \
            if blackboard.get_in_environment(GENERAL_CLEANING, False) == False\
            else self.report_succeeded(blackboard)
