import sample.utils as utils


class HellTriangle:

    def __init__(self, multilist):
        self.ht = utils.multiarrays_from_multilist(multilist)
        self.calculated_maximum = {}

    def height(self):
        return len(self.ht)

    def maximum_total(self):
        return self._maximum_total_from_node(0, 0)

    def _maximum_total_from_node(self, depth, index):

        if self.ht.size == 0:
            return 0

        if (depth, index) in self.calculated_maximum:
            return self.calculated_maximum[(depth, index)]

        node_value = self.ht[depth][index]
        if depth+1 == self.height():
            self.calculated_maximum[(depth, index)] = node_value
            return self.calculated_maximum[(depth, index)]

        left_child_value = self.ht[depth+1][index]
        right_child_value = self.ht[depth+1][index+1]

        if left_child_value > right_child_value:
            self.calculated_maximum[(depth, index)] = (
                node_value + self._maximum_total_from_node(depth+1, index)
            )
        elif left_child_value < right_child_value:
            self.calculated_maximum[(depth, index)] = (
                node_value + self._maximum_total_from_node(depth+1, index+1)
            )
        else:
            self.calculated_maximum[(depth, index)] = node_value + max([
                self._maximum_total_from_node(depth+1, index),
                self._maximum_total_from_node(depth+1, index+1)
            ])

        return self.calculated_maximum[(depth, index)]
