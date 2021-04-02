'''
Example 1:

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Example 2:

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Example 3:

Input: ["a==b","b==c","a==c"]
Output: true

Example 4:

Input: ["a==b","b!=c","c==a"]
Output: false

Example 5:

Input: ["c==c","b==d","x!=z"]
Output: true

'''
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        '''
        Make 2 adjacency lists for edges and non-edges
        Then when you get an equation as edge wz, check for wz or zw in Edges, if there, it's okay.             Else
        add the edge wz as in an undirected graph
        iff check wv's of vertex w in notEdges, go back to Edges[v] to check vu's and if
        any u==w or u==z, return False
        Look up dst v on current side, then look at all dst v's on other side.  if start v is on the
        other side, False
        edges = {u:[v,w,x,z], v:[u,w], w:[u,v], z:[u]}
        '''
        equalEdges = {}
        notEqualEdges = {}

        for i in range(len(equations)):
            equation = equations[i]
            w = equation[0]
            z = equation[3]
            operand = equation[1:3]
            thisSide = None
            otherSide = None
            if operand is "==":
                thisSide = equalEdges
                otherSide = notEqualEdges
            else:
                thisSide = notEqualEdges
                otherside = equalEdges

            # check the dst in equalEdges
            if z in equalEdges:
                edgesFromZ = equalEdges[z]
                for j in range(len(edgesFromZ)):
                    # check if any dst's from this z on the other side contain the current w
                    curr_dst = edgesFromZ[j]
                    if curr_dst in notEqualEdges:
                        notEqualDsts = notEqualEdges[curr_dst]
                        if w in notEqualDsts:
                            return False
                    else:
                        continue
            # z is not a dst but w==z is the same as z==w
            elif w in equalEdges:
                edgesFromW = equalEdges[w]
                for k in range(len(edgesFromW)):
                    # check if any dst's from this z on the other side contain the current w
                    curr_dst = edgesFromW[k]
                    if curr_dst in notEqualEdges:
                        notEqualDsts = notEqualEdges[curr_dst]
                        if z in notEqualDsts:
                            return False
            elif operand is "!=":
                pass
