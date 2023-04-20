import math


data = []
centers = []
clusters = {}


def get_distance(point, center):
    distance = float(0)
    for j in range(len(center)):
        distance += (point[j] - center[j]) ** 2
    return math.sqrt(distance)


def get_closest_center(data_point):
    global centers
    distances = []
    for center in centers:
        distances.append(get_distance(data_point, center))
    min_dist = min(distances)
    for j in range(len(distances)):
        if distances[j] == min_dist:
            return centers[j]
    return None


def center_of_gravity(points):
    center = []
    for j in points[0]:
        center.append(float(0))
    for cur in points:
        for j in range(len(cur)):
            center[j] += cur[j]
    for cur_c in range(len(center)):
        center[cur_c] /= len(points)
    return center


def centers_to_clusters():
    global data
    for point in data:
        closest_center = get_closest_center(point)
        if tuple(closest_center) not in clusters.keys():
            clusters[tuple(closest_center)] = []
        clusters[tuple(closest_center)].append(point)


def clusters_to_centers():
    global centers, clusters
    new_clusters = dict()
    centers_to_remove = []
    for c in centers:
        if tuple(c) not in clusters:
            centers_to_remove.append(c)
            continue
        new_center = center_of_gravity(clusters[tuple(c)])
        new_clusters[tuple(new_center)] = []
    for c in centers_to_remove:
        centers.remove(c)
    clusters = new_clusters


def lloyd_algorithm(k):
    MAX_ITERATION = 1000
    global centers, data, clusters
    for j in range(k):
        centers.append(data[j])
    for c in centers:
        clusters[tuple(c)] = []
    prev_centers = []
    iteration_count = 0
    while prev_centers != centers:
        if iteration_count > MAX_ITERATION:
            break
        prev_centers = centers
        centers_to_clusters()
        new_centers = []
        for c in centers:
            new_center = center_of_gravity(clusters[tuple(c)])
            new_centers.append(new_center)
        centers = new_centers
        iteration_count += 1


FILEPATH = "./LloydAlgorithmData/dataset_873255_3.txt"

inFile = open(FILEPATH)
num_centers = int(inFile.readline().split(" ")[0].strip("\n\t "))
while line := inFile.readline():
    line = line.split(" ")
    if len(line) > 0:
        cur_point = []
        for string in line:
            cur_point.append(float(string.strip("\n\t ")))
        data.append(cur_point)

lloyd_algorithm(num_centers)

for c in centers:
    for d in c:
        print(d, end=" ")
    print()
