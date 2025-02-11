from typing import List, Tuple
import random

class GraphBuilder:
    def build(self) -> List[Tuple[int, int, int]]:
        pass

class RndWeightedGB(GraphBuilder):
    def __init__(self, num_nodes: int, num_edges: int, weight_range: range, directed: bool = False):
        self.num_nodes = num_nodes
        self.num_edges = num_edges or num_nodes
        self.directed = directed or False
        self.weight_range = weight_range or range(10, self.num_nodes*10)
    
    def _pick_a_node(self):
        return random.randint(1, self.num_nodes)

    def _pick_a_weight(self):
        return random.randint(self.weight_range.start, self.weight_range.stop-1)

    def build(self) -> List[Tuple[int, int, int]]:
        edges = []
        for i in range(self.num_edges):
            n1, n2 = self._pick_a_node(), self._pick_a_node()
            wt = self._pick_a_weight()
            edges.append((n1, n2, wt))
        return edges

from enum import Enum
class GraphShape(Enum):
    DUMBELL = 1
    BRIDGE = 2 # Königsberg bridge
    CIRCLE = 3
    CITY = 4
    LOLLYPOP = 5

class ShapeWeightedGB(GraphBuilder):
    def __init__(self, num_nodes: int, shape: GraphShape, weight_range: range):
        super().__init__()
        self.num_nodes = num_nodes
        self.shape  = shape
        self.weight_range = weight_range or range(10, self.num_nodes*10)
        self._validate_num_nodes()
    
    def _validate_num_nodes(self):
        if self.shape == GraphShape.CIRCLE:
            if self.num_nodes < 3:
                raise ValueError("CIRCLE needs min 3 nodes")
        elif self.shape == GraphShape.DUMBELL:
            if self.num_nodes < 6:
                raise ValueError("DUMBELL needs min 6 nodes")
        elif self.shape == GraphShape.LOLLYPOP:
            if self.num_nodes < 4:
                raise ValueError("LOLLYPOP needs min 4 nodes")
            
    def _pick_a_weight(self):
        return random.randint(self.weight_range.start, self.weight_range.stop-1)
    
    def build_circle(self, nodes: List[int]):
        edges = []
        for i in range(1, len(nodes)):
            edges.append([nodes[i-1], nodes[i], self._pick_a_weight()])
        edges.append([nodes[0], nodes[-1], self._pick_a_weight()])
        return edges

    def build_line(self, nodes: List[int]):
        edges = []
        for i in range(1, len(nodes)):
            edges.append([nodes[i-1], nodes[i], self._pick_a_weight()])
        return edges

    def build(self):
        nodes = random.shuffle([i for i in range(1, self.num_nodes+1)])
        if self.shape == GraphShape.CIRCLE:
            return self.build_circle(nodes)
        
        elif self.shape == GraphShape.DUMBELL:
            half_nodes = nodes[:self.num_nodes//2]
            left_edges = self.build_circle(half_nodes)
            right_edges = self.build_circle(nodes[self.num_nodes//2:])

            left_anchor = random.randint(0, len(half_nodes)-1)
            right_anchor = random.randint(len(half_nodes), self.num_nodes-1)

            bridge_edge = [nodes[left_anchor], nodes[right_anchor], self._pick_a_weight()]
            edges = left_edges + right_edges + [bridge_edge]
            return edges
        
        elif self.shape == GraphShape.LOLLYPOP:
            circle_end = int(self.num_nodes * 3 / 4)
            circle_nodes = nodes[:circle_end]
            stick_nodes = nodes[circle_end-1:]

            circle_edges = self.build_circle(circle_nodes)
            stick_edges = self.build_line(stick_nodes)
            return circle_edges + stick_edges

        raise ValueError(f'unsupported {self.shape}')
