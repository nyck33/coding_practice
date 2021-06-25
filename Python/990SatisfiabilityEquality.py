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
    def equationsPossible(self, equations: list[str]) -> bool:
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
        e_graph = {}
        ne_graph = {}

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
                otherSide = equalEdges

            # wz so z is dst
            if z in thisSide:
                no_indirect = self.check_u(thisSide, otherSide, z, w)
                if not no_indirect:
                    return False
            if w in thisSide:  #w is the zw destination
                no_indirect = self.check_u(thisSide, otherSide, w, z)
                if not no_indirect:
                    return False
            #neither vertex in thisSide so for case a!=b, a==b if both vertices in other side -> False
            elif z in otherSide and w in otherSide:
                return False
            else: #only
                thisSide[z]

    def check_u(self, thisSide, otherSide, dst, start):
        '''

        :param thisSide:
        :param otherSide:
        :param vert: either w or z from equation, get list of edges from it and for each dst vertex, check otherSide, if
        there, get list of edges, check dst vertices to see if z or w is there, if so return False
        :return:
        '''
        edgesFromVert = thisSide[dst]
        for j in range(len(edgesFromVert)):
            # check if any dst's from this z on the
            u = edgesFromVert[j]
            if u in otherSide:  # check if wz zu's u in other side
                otherSideDsts = otherSide[u]
                if start in otherSideDsts:  # there is an indirect w->z->u->w that crosses from == to !=
                    return False
        return True

if __name__=="__main__":
    sol = Solution()

    equations= ["a==b","b!=a"]
    print(sol.equationsPossible(equations))

    equations= ["b==a","a==b"]
    print(sol.equationsPossible(equations))

    equations= ["a==b","b==c","a==c"]
    print(sol.equationsPossible(equations))

    equations= ["a==b","b!=c","c==a"]
    print(sol.equationsPossible(equations))

    equations= ["c==c","b==d","x!=z"]
    print(sol.equationsPossible(equations))

