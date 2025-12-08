def connect_n_junciton_boxes(junciton_boxes, n):
    possible_connections = calc_all_connections(junction_boxes)
    
    parent = []
    size = []

    for i in range(len(junciton_boxes)):
        parent.append(i)
        size.append(1)
    
    connection_count = 0
    for dist, u, v in possible_connections:
        union(u, v, parent, size)  #change "if union(u, v, parent, size):" for kruskals, eg no cycles (AoC accepts cycles)
        connection_count += 1
        
        if connection_count == n:
            break
    
    circut_size = []
    for i in range(len(parent)):
        if parent[i] == i:
            circut_size.append(size[i])
    
    circut_size.sort(reverse=True)
    a, b, c = circut_size[:3]

    return a * b * c

        

def union(a, b, parent, size):
    root_a = find(a, parent)
    root_b = find(b, parent)

    if root_a == root_b:
        return False
    
    parent[root_b] = root_a
    size[root_a] += size[root_b]
    return True 
    

def find(x, parent):
    while parent[x] != x:
        x = parent[x]
    return x


def calc_all_connections(junction_boxes):
    possible_connections = []
    for i in range(len(junction_boxes)):
        x1, y1, z1 = junction_boxes[i]
        for j in range(i + 1, len(junction_boxes)):
            x2, y2, z2 = junction_boxes[j]

            dx, dy, dz = x2 - x1, y2 - y1, z2 - z1

            dist2 = dx * dx + dy * dy + dz * dz
            possible_connections.append((dist2, i, j))
    possible_connections.sort(key=lambda t: t[0])
    return possible_connections


    

with open('input.txt', 'r') as file:
    junction_boxes = []
    for line in file:
        x, y, z = map(int, line.strip().split(','))
        junction_boxes.append((x, y, z))
    
    print(connect_n_junciton_boxes(junction_boxes, 1000))
    



