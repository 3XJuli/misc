import math
data = []
INPUT_PATH: str = 'input'
y: int = 2000000

# INPUT_PATH: str = 'sample'
# y: int = 10


def read_data():
    global data
    with open(INPUT_PATH, 'r') as f:
        for line in f.readlines():
            data += [line.strip('\n')]
read_data()

def parse():
    global data
    sensors = [tuple()] * len(data)
    beacons = [tuple()] * len(data)
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

    return sensors, beacons

def manhatten_dist(x: tuple[int, int], y: tuple[int, int]) -> int:
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

def main():
    sensors, beacons = parse()
    taken = dict()
    seen_points = dict()
    for ix, sensor in enumerate(sensors):
        beacon = beacons[ix]
        if beacon[1] == y:
            taken[beacon[0]] = 1
        if sensor[1] == y:
            taken[sensor[0]] = 1

        d = manhatten_dist(sensor, beacon)

        if sensor[1] >= y >= sensor[1] - d:
            d_y = sensor[1] - y
            remaining_dist = d - d_y + 1
            for i in range(remaining_dist):
                seen_points[sensor[0] - i] = 1
                seen_points[sensor[0] + i] = 1


        elif sensor[1] < y <= sensor[1] + d:
            d_y = y - sensor[1]
            remaining_dist = d - d_y + 1
            for i in range(remaining_dist):
                seen_points[sensor[0] - i] = 1
                seen_points[sensor[0] + i] = 1

    minus = len(set(seen_points.keys()).intersection(taken))
    print(len(seen_points.keys()) - minus)



if __name__ == '__main__':
    main()
