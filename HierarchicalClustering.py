import math


def euclidean_distance(p, q):
    squared_dist = sum((p[i] - q[i])**2 for i in range(len(p)))
    return math.sqrt(max(squared_dist, 0))


def get_data_points(dist_matrix):
    n = len(dist_matrix)
    data_points = []
    for i in range(n):
        point = [0] * n
        for j in range(n):
            point[j] = math.sqrt(dist_matrix[i][i] + dist_matrix[j][j] - 2 * dist_matrix[i][j])
        data_points.append(point)
    return data_points


def hierarchical_clustering(n, dist_matrix):
    # Get the data points corresponding to the distance matrix
    data_points = get_data_points(dist_matrix)

    # Initialize clusters as singletons
    clusters = [[i] for i in range(n)]

    # Loop until there is only one cluster left
    while len(clusters) > 1:
        # Calculate the pairwise distances between clusters
        pairwise_dists = []
        for i in range(len(clusters)):
            row = []
            for j in range(len(clusters)):
                if i == j:
                    row.append(float('inf'))
                else:
                    dist_sum = 0
                    for p in clusters[i]:
                        for q in clusters[j]:
                            dist = euclidean_distance(data_points[p], data_points[q])
                            dist_sum += dist
                    dist = dist_sum / (len(clusters[i]) * len(clusters[j]))
                    row.append(dist)
            pairwise_dists.append(row)

        # Find the indices of the clusters with the minimum distance
        min_dist = float('inf')
        min_i = 0
        min_j = 0
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                if pairwise_dists[i][j] < min_dist:
                    min_dist = pairwise_dists[i][j]
                    min_i = i
                    min_j = j

        # Merge the clusters with the minimum distance
        new_cluster = clusters[min_i] + clusters[min_j]
        clusters.pop(max(min_i, min_j))
        clusters.pop(min(min_i, min_j))
        clusters.append(new_cluster)

        # Print the newly created cluster without commas and brackets
        print(' '.join(str(x+1) for x in new_cluster))


# Test the code on the given input file
FILEPATH = "./HierarchicalClusteringData/input_1.txt"

inFile = open(FILEPATH)

line = inFile.readline().strip("\n\t ")
n = int(line)
d_m = []
while line := inFile.readline():
    d_m.append([])
    for string in line.split(" "):
        d_m[-1].append(float(string))

hierarchical_clustering(n, d_m)
