# Author: Arya Gupta
# Class Dusty Spot implements functionality of Dusty Spot Condition
# Returns successed if there Dusty Spot is true, otherwise returns failed
import bt_library as btl
from ..globals import DUSTY_SPOT_SENSOR


class DustySpot(btl.Condition):
    """
    Implementation of the condition "Dusty Spot".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        bl = blackboard.get_in_environment(DUSTY_SPOT_SENSOR, False)
        print(bl, 'in DUSTY SPOT')

        return self.report_succeeded(blackboard) \
            if blackboard.get_in_environment(DUSTY_SPOT_SENSOR, True) \
            else self.report_failed(blackboard)