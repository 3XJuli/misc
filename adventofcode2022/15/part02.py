import math
# import numpy as np
data = []
INPUT_PATH: str = 'input'
y: int = 2000000
minn: int = 0
maxx: int = 4000000


# INPUT_PATH: str = 'sample1'
# y: int = 10
# minn: int = 0
# maxx: int = 20


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]
read_data()

sensors = [tuple()] * len(data)
beacons = [tuple()] * len(data)
distances = [0] * len(data)
n = 0

def parse():
    global data
    global sensors
    global beacons
    global distances
    global n

    for ix, line in enumerate(data):
        sensor, beacon = line.split(':')
        sensor_x, sensor_y = sensor[10:].split(', ')
        sensor_x = int(sensor_x[2:])
        sensor_y = int(sensor_y[2:])
        beacon_x, beacon_y = beacon[22:].split(', ')
        beacon_x = int(beacon_x[2:])
        beacon_y = int(beacon_y[2:])

        sensors[ix] = (sensor_x, sensor_y)
        beacons[ix] = (beacon_x, beacon_y)
        distances[ix] = manhatten_dist(sensors[ix], beacons[ix])
    n = len(sensors)

def manhatten_dist(x: tuple[int, int], y: tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def check_point(x: tuple[int, int]) -> bool:
    global data
    global sensors
    global beacons
    global distances
    global n


    if minn <= x[0] and minn <= x[1] and maxx >= x[0] and maxx >= x[1]:
        for i in range(n):
            d = manhatten_dist(x, sensors[i])
            if d <= distances[i] or (manhatten_dist(x, beacons[i]) == 0):
                return False

        print(x[0] * 4_000_000 + x[1])
        print('TRUE')
        return True
    return False

def main():
    global data
    global sensors
    global beacons
    global distances
    parse()
    for j in range(len(sensors)):
        print(j)
        sensor = sensors[j]
        d = distances[j] + 1
        for i in range(d):
            if check_point((sensor[0] + i, sensor[1] - d + i)):
                return
            if check_point((sensor[0] - i, sensor[1] - d + i)):
                return
            if check_point((sensor[0] - i, sensor[1] + d - i)):
                return
            if check_point((sensor[0] + i, sensor[1] + d - i)):
                return






if __name__ == '__main__':
    main()
