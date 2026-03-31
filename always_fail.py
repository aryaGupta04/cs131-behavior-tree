# Author: Arya Gupta
# Class Always Fail implements functionality of Always Fails Task
# Retruns Failed

import bt_library as btl

class AlwaysFail(btl.Task):
    """
    Implementation of the Task "always fail".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Always Fail')

        return self.report_failed(blackboard)
