#Dijkstra's Algorithm with D-ary Heap

INF = 1000000

class  heap_node: 
    def __init__(self, name, distance):
        self.name = name #jayi ke hastim
        self.distance = distance #fasele ash ta start

def size(heap):
    return len(heap)

def heap_parent(i, d):
    return (i-1) // d

def heap_child(d, index, pos):
    return index * d + (pos + 1)

def get_node(heap, i):
    return heap[i]

def get_min_node(heap):
    if size(heap) == 0:
        return None
    return heap[0]

def delet_min_node(heap):
    if(size(heap) == 0):
        return None

    final[heap[0].name] = heap[0].distance
    node_loc[heap[0].name] , node_loc[heap[-1].name] = -1 , 0
    heap[0] , heap[-1] = heap[-1] , heap[0]
    del heap[-1]
    down_min_heapify(d, heap, 0)

def up_min_heapify(d, heap, i):
    if(i < 0):
        return

    min = i
    for j in range(d):
        c = heap_child(d, i, j)
        if c < size(heap) and get_node(heap, c).distance < get_node(heap, min).distance:
            min = c

    if min != i:
        swap(heap, min, i)
        up_min_heapify(d, heap, node_loc[min]) 

def down_min_heapify(d, heap, i):
    if(i > size(heap)):
        return

    min = i
    for j in range(d):
        c = heap_child(d, i, j)
        if c < size(heap) and get_node(heap, c).distance < get_node(heap, min).distance:
            min = c

    if min != i:
        swap(heap, min, i)
        up_min_heapify(d, heap, min) 

def swap(heap, i, j):
    node_loc[heap[i].name], node_loc[heap[j].name] = j, i
    heap[i], heap[j] = heap[j], heap[i]


num_node, num_connection_node, start = list(map(int, input().strip().split())) 
finish = [0] * num_node 
connections = []
node_loc = [0] * num_node
heap = []
final = [INF] * num_node 

d = num_connection_node // num_node

heap.append(heap_node(start, 0)) 
node_loc[start] = 0

for i in range(0, start):
    heap.append(heap_node(i, INF))  
    node_loc[i] = i

for i in range(start + 1, num_node):
    heap.append(heap_node(i, INF))
    node_loc[i] = i

for i in range(num_connection_node): 
    connections += [list(map(int, input().strip().split()))]

for i in range(len(connections)): 
    finish[connections[i][0]] += 1

while len(connections) and size(heap): 

    now = get_min_node(heap).name

    for i in range(len(connections)):                             
        if connections[i][0] == now:
            from_node = now
            to = connections[i][1]
            dis = connections[i][2]

            if final[to] != INF:
                finish[now] -= 1

                if finish[now] <= 0: 
                    delet_min_node(heap)

            elif heap[node_loc[to]].distance != INF: 
                if heap[node_loc[to]].distance > heap[node_loc[from_node]].distance + dis:
                    heap[node_loc[to]].distance = heap[node_loc[from_node]].distance + dis
                    up_min_heapify(d, heap, heap_parent(node_loc[to], d))
                    finish[now] -= 1
                    if finish[now] <= 0:
                        delet_min_node(heap)
                    del connections[i]
                    break
                else:
                    del connections[i]

            elif heap[node_loc[to]].distance == INF: 
                heap[node_loc[to]].distance = heap[node_loc[from_node]].distance + dis
                finish[now] -= 1
                if finish[now] <= 0:
                    delet_min_node(heap)
                del connections[i]
                break


for i in range(len(final)):
    print(i, "       ", final[i])