class Node:
    def __init__(self, name):
        self.name = name
        self.adjaencylist = []
        self.visited = False


class BreadthFirstSearch:
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True
        while queue:
            actualNode = queue.pop(0)
            print(actualNode.name)

            for i in actualNode.adjaencylist:
                if not i.visited:
                    i.visited = True
                    queue.append(i)


class DepthFirstSearch:
    def dfs(self, node):
        node.visited = True
        print(node.name)
        for n in node.adjaencylist:
            if not n.visited:
                self.dfs(n)


node1 = Node('A')
node2 = Node('B')
node3 = Node('C')
node4 = Node('D')
node5 = Node('E')
node1.adjaencylist.append(node2)
node1.adjaencylist.append(node3)
node2.adjaencylist.append(node4)
node4.adjaencylist.append(node5)

bfs = BreadthFirstSearch()
bfs.bfs(node1)

dfs = DepthFirstSearch()
dfs.dfs(node1)
