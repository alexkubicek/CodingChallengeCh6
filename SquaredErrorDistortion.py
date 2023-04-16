import math


def get_distance(point, center):
    distance = float(0)
    for j in range(len(center)):
        distance += (point[j] - center[j]) ** 2
    return math.sqrt(distance)


def get_distance_to_closest_center(data_point, centers):
    distances = []
    for center in centers:
        distances.append(get_distance(data_point, center))
    return min(distances)


def distortion(data, centers):
    summation = float(0)
    for point in data:
        summation += (get_distance_to_closest_center(point, centers)) ** 2
    return summation / len(data)


FILEPATH = "./SquaredErrorDistortionData/dataset_873254_3.txt"

inFile = open(FILEPATH)
line = inFile.readline()
line = inFile.readline()
given_centers = []
given_data = []
while '-' not in line:
    cur_center = []
    line = line.split(" ")
    for d in line:
        if len(d) > 0:
            cur_center.append(float(d.strip("\n\t ")))
    given_centers.append(cur_center)
    line = inFile.readline()
while line := inFile.readline():
    cur_data = []
    line = line.split(" ")
    for d in line:
        if len(d) > 0:
            cur_data.append(float(d.strip("\n\t ")))
    given_data.append(cur_data)

print(distortion(given_data, given_centers))
