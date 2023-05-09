from collections import defaultdict

num_vertices = 0
num_edges = 0
colors_list = []
not_isolated = set()
isolated = []
loosely_connected = []

class Stack:
  def __init__(self):
    self.storage = []
  def isEmpty(self):
    return len(self.storage) == 0
  def push(self, node):
    self.storage.append(node)
  def pop(self):
    return self.storage.pop()

class Graph:

    def __init__(self):
        # self.V = vertices
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v, color2):
        self.graph[u].append([v, color2])

    def DFS(self):

        # Mark current node as visited
        visited = [False] * num_vertices
        stack = Stack()
        # print("The keys", self.graph.keys())
        # print(list(self.nodes)[1])
        stack.push(isolated[0])
        visited[isolated[0]] = True

        while (not stack.isEmpty()):
            node = stack.pop()
            nbrs = g.graph[node]
            # print("CURRENT NODE", node)

            #we check if this node is in the middle of two loosely connected nodes
            if len(nbrs) > 1:
                find_loose_points(nbrs)

            for n in nbrs:
                if not visited[n[0]]:
                    stack.push(n[0])
                    visited[n[0]] = True


def create_graph():
    global num_vertices
    global num_edges
    global colors_list

    num_vertices, num_edges, num_colors = input().split(" ")
    num_vertices = int(num_vertices)
    num_edges = int(num_edges)
    num_colors = int(num_colors)
    # print(num_vertices, num_edges, num_colors)

    templine = input().strip()
    colors_list = templine.split(" ")
    colors_list = [int(i) for i in colors_list]
    # print(colors_list)
    for temp in range(num_edges):
        temp = input().strip()
        v1, v2 = temp.split(" ")
        v1 = int(v1)
        v2 = int(v2)
        # print(v1,v2)
        g.addEdge(v1, v2, colors_list[v2])
        g.addEdge(v2, v1, colors_list[v1])


def find_isolated_nodes(g):
    global colors_list
    global num_vertices
    global isolated

    full_set = set()

    for k, v in g.graph.items():
        full_set.add(k)
        # print("Next key", k)
        for neib in v:
            if neib[1] == colors_list[k]:
                # print(k, "- is NOT isolated!")
                not_isolated.add(k)

    isolated = list(full_set.difference(not_isolated))
    isol_matrix = [0*num_vertices]*num_vertices
    for i in isolated:
        isol_matrix[i] = 1
    return isol_matrix


def find_loose_points(neibors):
    global loosely_connected

    for i in range(0, len(neibors)):
        for j in range(1, len(neibors)):
            if i < j:
                # we check if they are both isolated nodes
                # we delete the ones that are same
                if neibors[i][0] != neibors[j][0]:
                    #  we check if the neibor is an isolated node
                    if isol_matrix[neibors[i][0]] == 1 and isol_matrix[neibors[j][0]] == 1:
                    #  we can also use binary search but it is longer
                    # if search_for_k(isolated, neibors[i][0]) and search_for_k(isolated, neibors[j][0]):

                        if neibors[j][0] not in g.graph[neibors[i][0]]:
                            loosely_connected.append((neibors[i][0], neibors[j][0]))



def clean_loose():
    global loosely_connected
    global num_loose

    final = {tuple(sorted(item)) for item in loosely_connected}
    num_loose = len(final)
    # print(final)
    # print(len(final))
    print(num_loose)


# Binary search function
def search_for_k(isolated,k,low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(isolated)-1

    if high < low:
        return False

    midpoint = (low+high) // 2

    if isolated[midpoint] == k:
        return True
    elif k < isolated[midpoint]:
        return search_for_k(isolated,k, low, midpoint-1)
    else:
        return search_for_k(isolated,k, midpoint+1, high)



g = Graph()
create_graph()
# print(g.graph)
isol_matrix = find_isolated_nodes(g)
g.DFS()
# print(len(loosely_connected))
# print(loosely_connected)
clean_loose()
