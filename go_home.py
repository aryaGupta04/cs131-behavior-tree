# Author: Arya Gupta
# Class Go Hoe implements functionality of Go Home Task
# Retrieves the specified home path
# returns succeded

import bt_library as btl
from ..globals import HOME_PATH


class GoHome(btl.Task):
    """
    Implementation of the Task "Go Home".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Going home')

        blackboard.get_in_environment(HOME_PATH, '')

        return self.report_succeeded(blackboard)
