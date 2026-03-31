# Author: Arya Gupta
# Class Clean Floor implements functionality of Clean Floor Task
# Defines a low probability of returning Failed onlt returns succeeede
# 10% of the time to indicate that the floors are clean

import bt_library as btl
import random


class CleanFloor(btl.Task):
    """
    Implementation of the Task "clean floor".
    """
    def run(self, blackboard: btl.Blackboard) -> btl.ResultEnum:
        self.print_message('Cleaning Floor in progress...')
        probability = random.random()

        if probability < 0.1:
            self.print_message("CLEAN_FLOOR: No more dirt detected. Stopping.")
            return self.report_failed(blackboard)
        else :

            self.print_message("CLEAN FLOOR IN PROGRESS")
            return self.report_running(blackboard)
