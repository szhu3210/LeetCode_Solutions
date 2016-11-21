# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        self.nodeLabels={}
        return self.clone(node)

    def clone(self, node):
        label=node.label
        if label in self.nodeLabels:
            return self.nodeLabels[label]
        new=UndirectedGraphNode(label)
        self.nodeLabels[label]=new
        new.neighbors=[self.clone(n) for n in node.neighbors]
        return new
                       