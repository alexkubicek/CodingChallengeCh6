# FarthestFirstTraversal(Data, k)
#    Centers ← the set consisting of a single randomly chosen point from Data
#    while |Centers| < k
#        DataPoint ← the point in Data maximizing d(DataPoint, Centers)
#        add DataPoint to Centers
#    return Centers
import math


def get_distance(point, center):
    distance = float(0)
    for j in range(len(center)):
        distance += (point[j] - center[j]) ** 2
    return math.sqrt(distance)


def maximize_d(data, centers):
    max_distance = 0
    max_point = []
    for point in data:
        distances = []
        for center in centers:
            distances.append(get_distance(point, center))
        distance = min(distances)
        if distance > max_distance:
            max_distance = distance
            max_point = point
    return max_point


def farthest_first_traversal(data, k):
    centers = [data[0]]
    while len(centers) < k:
        data_point = maximize_d(data, centers)
        centers.append(data_point)
    return centers


FILEPATH = "./FarthestFirstTraversalData/dataset_873253_2.txt"

inFile = open(FILEPATH)
line = inFile.readline().split(" ")
k = int(line[0].strip("\n\t "))
m = int(line[1].strip("\n\t "))

input_data = []
while line := inFile.readline():
    line = line.split(" ")
    cur_point = []
    for i in range(m):
        str_form = line[i].strip("\n\t ")
        if len(str_form) > 0:
            cur_point.append(float(str_form))
    input_data.append(cur_point)

my_centers = farthest_first_traversal(input_data, k)
for c in my_centers:
    for d in c:
        print(d, end=" ")
    print()
