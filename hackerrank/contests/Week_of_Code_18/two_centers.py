#!/bin/python3

# https://www.hackerrank.com/contests/w18/challenges/two-centers

# note: this solution is still not valid, it throws an incorrect result on some test cases

n_nodes = int(input())
nodes = [{} for _ in range(n_nodes)]
for edge in range(n_nodes - 1):
    x, y = input().split()
    x, y = int(x) - 1, int(y) - 1
    # set the adges with distance -1
    nodes[x][y] = None
    nodes[y][x] = None

def calculate_max_dist(child, father):
    """Calculate max distance traveling from 'father' to any other edge"""
    # return 1 if we reach a leaf
    if len(nodes[child]) == 1:
        nodes[child][father] = 0
        return 0
    # return dist if it's calcualted
    if nodes[child][father] is not None:
        return nodes[child][father]
    # calcualte distance
    max_dist = -1
    for child_child in nodes[child].keys():
        if child_child != father:
            max_dist = max(max_dist, calculate_max_dist(child_child, child) + 1)
    nodes[child][father] = max_dist
    #global center_node
    #if max_dist > center_node[1]:
    #    center_node[1] = max_dist
    #    center_node[0] = child
    return max_dist

# calculate distances
#center_node = [None, -1]
for node in range(n_nodes):
    for child in nodes[node].keys():
        calculate_max_dist(child, node)

# calculate centers, starting from node 0
center1 = 0
center2 = 0
prev_center1 = -1
prev_center2 = -1
distance_centers = 0
varr = 1
while True:
    dist = -1
    dist2 = -1
    from_cent = False
    decre = False
    # move center1
    next_center1 = [-1, -1, False]  # [node, dist]
    for child in nodes[center1].keys():
        d = (nodes[child][center1] + 1) if nodes[child][center1] is not None else distance_centers
        if d > next_center1[1]:
            next_center1[1] = d
            next_center1[0] = child
            next_center1[2] = True
            if d > dist: 
                dist2 = dist
                dist = d
                from_cent = nodes[child][center1] is None
            elif d > dist2:
                dist2 = d
                
        elif d == next_center1[1]:
            next_center1[2] = False
        #print("- %d" % d) if nodes[child][center1] is not None else print("- %d*" %d)
    #print("-")
    if next_center1[2] and next_center1[0] != prev_center1:
        #print("m1")
        prev_center1 = center1
        prev_center1
        center1 = next_center1[0]
        distance_centers += 1
        # update distances with distance between centers
        nodes[center1][prev_center1] = None
        nodes[prev_center1][center1] = None
        continue

    # move center2
    next_center2 = [-1, -1, False]  # [node, dist]
    for child in nodes[center2].keys():
        d = (nodes[child][center2] + 1) if nodes[child][center2] is not None else distance_centers
        if d > next_center2[1]:
            next_center2[1] = d
            next_center2[0] = child
            next_center2[2] = True
            if d > dist:
                dist2 = dist
                dist = d
                from_cent = nodes[child][center2] is None
            elif d > dist2:
                dist2 = d
        elif d == next_center1[1]:
            next_center2[2] = False
    if next_center2[2] and next_center2[0] != prev_center2:
        #print("m2")
        prev_center2 = center2
        center2 = next_center2[0]
        distance_centers -= 1
        if from_cent: dist = dist2
        # update distances with distance between centers
        nodes[prev_center2][center2] = varr
        varr += 1
        continue

    # if not moving anymore, end
    break

print(dist-1)
