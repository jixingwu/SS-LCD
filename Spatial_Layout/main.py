import numpy as np

tau = 0.2  # threshold for matching
K = 2  # number of neighbors
# read txt file, format is node1 node2 distance, and reture np.array
def read_txt(filename):
    with open(filename) as f:
        data = f.readlines()
    data = [x.strip() for x in data]
    data = [x.split() for x in data]
    data = np.array(data)
    data = data.astype(np.float)
    return data


def cal_neighbors(data, i):
    edges_i = data[data[:, 0] == i][:, 2]
    nei_i = edges_i / np.linalg.norm(np.sort(edges_i), ord=1)
    if nei_i.shape[0] < K:
        return nei_i
    else:
        return nei_i[:K]

# matching the graphs
def matching(data1, data2):
    detections = []
    objects = []
    graph1 = np.unique(data1[:, 0:2])
    graph2 = np.unique(data2[:, 0:2])
    for i in range(len(graph1)):
        ini = graph1[i]
        nei_i = cal_neighbors(data1, ini)
        if np.size(nei_i) == 0:
            continue
        for j in range(len(graph2)):
            inj = graph2[j]
            nei_j = cal_neighbors(data2, inj)
            if np.size(nei_j) == 0:
                continue
            d_f = np.linalg.norm(nei_i - nei_j, ord=1)
            if d_f < tau:
                detections.append(ini)
                objects.append(inj)
    return detections, objects


# read txt file
data1 = read_txt('graph1.txt')  # detections graph
data2 = read_txt('graph2.txt')  # objects graph
detections, objects = matching(data1, data2)
assert len(detections) == len(objects)
# print detections and objects
for i in range(len(detections)):
    print("detection {} in local map matches with object {} in global map".format(np.int(detections[i]), np.int(objects[i])))

