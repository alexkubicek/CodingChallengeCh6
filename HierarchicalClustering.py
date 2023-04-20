import math


def get_distance(one, two):
    global OGMATRIX
    distance = 0
    sub_one = sub_two = 0
    for point in one:
        if point == 0:
            sub_one += 1
            continue
        for second_point in two:
            if second_point == 0:
                sub_two += 1
                continue
            distance += OGMATRIX[point][second_point]
    distance /= (len(one) - sub_one) * (len(two) - sub_two)
    return distance


def join_clusters(two_clusters):
    global matrix
    new_cluster = []
    for c in two_clusters:
        for cl in c:
            if cl != 0:
                new_cluster.append(cl)
    new_cluster = tuple(new_cluster)
    del matrix[two_clusters[0]]
    del matrix[two_clusters[1]]
    new_distances = {}
    for key in matrix.keys():
        new_distances[key] = get_distance(key, new_cluster)
        matrix[key][new_cluster] = new_distances[key]
        del matrix[key][two_clusters[0]]
        del matrix[key][two_clusters[1]]
    new_distances[new_cluster] = float(0)
    matrix[new_cluster] = new_distances
    return new_cluster


def get_closest(cur_clusters):
    min_dist = math.inf
    closest_clusters = ()
    for cluster in cur_clusters:
        for second_cluster in cur_clusters:
            cur_distance = matrix[cluster][second_cluster]
            if cur_distance == 0:
                continue
            if cur_distance < min_dist:
                min_dist = cur_distance
                closest_clusters = (cluster, second_cluster)
    return closest_clusters


def hierarchical_clustering():
    global n, matrix
    clusters = []
    for my_int in range(n):
        clusters.append((my_int + 1, 0))
    while len(clusters) > 1:
        closest = get_closest(clusters)
        for clus in closest:
            for point in clus:
                if point != 0:
                    print(point, end=" ")
        print()
        newest = join_clusters(closest)
        for my_int in range(2):
            clusters.remove(closest[my_int])
        clusters.append(newest)


FILEPATH = "./HierarchicalClusteringData/dataset_873261_7.txt"

inFile = open(FILEPATH)

n = int(inFile.readline().strip("\n\t "))

matrix = {}
OGMATRIX = {}
i = 1
while line := inFile.readline():
    OGMATRIX[i] = {}
    matrix[(i, 0)] = {}
    j = 1
    line = line.strip("\n\t ").split(" ")
    for num in line:
        OGMATRIX[i][j] = float(num)
        matrix[(i, 0)][(j, 0)] = (float(num))
        j += 1
    i += 1

print(matrix.keys())
print(OGMATRIX.keys())
inFile.close()

hierarchical_clustering()
