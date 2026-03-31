# Author: Arya Gupta
# Class Done General implements functionality of Done General Task
# Changes blackboard to show General Cleaning is done/true
#Retruns succeeded

import bt_library as btl
from ..globals import GENERAL_CLEANING

class DoneGeneral(btl.Task):
    """
    Implementation of the Task "Done General".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Done general Cleaning')
        blackboard.set_in_environment(GENERAL_CLEANING, False)

        return self.report_succeeded(blackboard)
