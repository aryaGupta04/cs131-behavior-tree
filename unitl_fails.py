
# Author: Arya Gupta
# Class Until Fails implements functionality of Until Fails decorator
# Returns succeded if inputed function returns failed, otherwise returns running 

from bt_library.blackboard import Blackboard
from bt_library.common import ResultEnum
from bt_library.decorator import Decorator
from bt_library.tree_node import TreeNode


class UntilFails(Decorator):
    """
    Specific implementation of the until fails decorator.
    """

    def __init__(self, child: TreeNode):
        """
        Default constructor.

        :param time: Duration of the timer [counts]
        :param child: Child associated to the decorator
        """
        super().__init__(child)

    def run(self, blackboard: Blackboard) -> ResultEnum:
        """
        Execute the behavior of the node.

        :param blackboard: Blackboard with the current state of the problem
        :return: The result of the execution
        """
    
        result_child = self.child.run(blackboard)

        # If the child failed, terminate immediately the timer
        return self.report_succeeded(blackboard) \
            if result_child == ResultEnum.FAILED\
            else self.report_running(blackboard)
