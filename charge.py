# Author: Arya Gupta
# Class Charge implements functionality of Charge Task
# Changes blackboard to show that the robot is charging then updates the 
# robots battery level, then switched the charging variable back to false once 
# done and returns succeded

import bt_library as btl
from ..globals import CHARGING
from ..globals import BATTERY_LEVEL


class Charge(btl.Task):
    """
    Implementation of the Task "Charge".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Charging')

        blackboard.set_in_environment(CHARGING, True)
        blackboard.set_in_environment(BATTERY_LEVEL, 100)
        blackboard.set_in_environment(CHARGING, True)


        return self.report_succeeded(blackboard)
