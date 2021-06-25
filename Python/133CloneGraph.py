class Solution(object):
    def cloneGraph1(self, node): #DFS iteratively
        '''
        node is a Node obj
        class Node {
            public int val;
            public List<Node> neighbors;
        }
        :param node: 
        :return: 
        '''
        if not node:
            return node
        #dict of {node_obj: cloned Node}
        m = {node: Node(node.val)}
        # push original node obj on stack
        stack = [node]
        while stack:
            #pop the original node
            n = stack.pop()
            # iterate the original node's neighbors
            for neigh in n.neighbors:
                # neigh is unvisited/not cloned
                if neigh not in m:
                    stack.append(neigh)
                    #marking as visited with new clone as value
                    m[neigh] = Node(neigh.val)
                #append the clone neighbor to cloned u's neighbors
                m[n].neighbors.append(m[neigh])
        #return cloned node
        return m[node]


class Solution(object):
    def cloneGraph1(self, node):  # DFS iteratively
        '''
        I have no idea what graph looks like,
        start at given node, look at neighbors
        '''
        # track graph with dict {node_obj: new Node obj}
        graph = {}
        stack = [node]
        while stack:
            u = stack.pop()
            # mark visited and clone
            graph[u] = Node(u.val)
            # iterate original's neighbors
            neighbors = u.neighbors
            for v in neighbors:
                # v is not cloned or visited yet
                if v not in graph:
                    stack.append(v)
                # append neighbor to clone Node's neighbors list
                graph[u].neighbors.append(Node(v.val))

        return graph[node]


if __name__=="__main__":
