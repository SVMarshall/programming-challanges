#!python3

# https://www.hackerrank.com/challenges/matrix-rotation-algo/

# Matrix rotation in place.

m, n, r = input().split()
m, n, r = int(m), int(n), int(r)

# get matrix
mx = []
for _ in range(m):
    mx.append(list(input().split()))
    
#iterate ofer each "layer"
for layer in range(min(m, n) // 2):
    layer_len = (m+n-2-layer*4)*2
    layer_r = r % layer_len
    # may be better to rotate backwards if r > layer_len / 2 
    if layer_r < layer_len / 2:
        for _ in range(layer_r):
            lt_corner = mx[layer][layer]
            # shift top side
            for i in range(layer, n - layer - 1):
                mx[layer][i] = mx[layer][i+1]
            # shift right side
            for i in range(layer, m - layer - 1):
                mx[i][n-1-layer] = mx[i+1][n-1-layer]
            # shift bot side
            for i in range(layer, n - layer - 1):
                mx[m-1-layer][n-1-i] = mx[m-1-layer][n-1-i-1]
            # shift left side
            for i in range(layer, m - layer - 1):
                mx[m-1-i][layer] = mx[m-1-i-1][layer]
            i = m - layer - 2
            mx[m-1-i][layer] = lt_corner
    else:
        for _ in range(layer_len - layer_r):
            lt_corner = mx[layer][layer]
            # shift left side
            for i in range(layer, m - layer - 1):
                mx[i][layer] = mx[i+1][layer]
            # shift bot side
            for i in range(layer, n - layer - 1):
                mx[m-1-layer][i] = mx[m-1-layer][i+1]
            # shift right side
            for i in range(layer, m - layer - 1):
                mx[m-1-i][n-1-layer] = mx[m-1-i-1][n-1-layer]
            # shift top side
            for i in range(layer, n - layer - 1):
                mx[layer][n-1-i] = mx[layer][n-1-i-1]
            i = n - layer - 2
            mx[layer][n-1-i] = lt_corner

for i in range(m):
    for j in range(n):
        print(mx[i][j], end=" ")
    print("")