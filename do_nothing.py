# Author: Arya Gupta
# Class Do Nothing implements functionality of Do Nothing Task
# Prings Do nothing and returns succeded

import bt_library as btl
from ..globals import GENERAL_CLEANING
from ..globals import SPOT_CLEANING

class DoNothing(btl.Task):
    """
    Implementation of the Task "Do Nothing" This implementation allows us to a.
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Do Nothing')

        return self.report_succeeded(blackboard)
