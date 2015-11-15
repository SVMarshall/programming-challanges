#!python3

# https://www.hackerrank.com/challenges/even-tree/

class Vertex: 
    def __init__(self):
        self.edges = []

n, m = input().split()
n, m = int(n), int(m)

forest = [Vertex() for _ in range(n)]

for _ in range(m):
    a, b = input().split()
    a, b = int(a)-1, int(b)-1
    forest[b].edges.append(forest[a])

def even_tree(node, tab=0):
    """returns (even?, cuts)"""
    cuts = 0
    odds = 0
    for edge in node.edges:
        edge_even, edge_cuts = even_tree(edge, tab+2)
        cuts += edge_cuts 
        if edge_even:
            cuts += 1
        else:
            odds += 1
    odds += 1
    return (odds % 2 == 0, cuts)

is_even, cuts = even_tree(forest[0])
print(cuts)