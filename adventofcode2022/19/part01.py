import math
import regex as re
from typing import Optional

data = []
INPUT_PATH: str = 'input'
# INPUT_PATH: str = 'sample'

with open(INPUT_PATH, 'r') as f:
    for line in f.readlines():
        data += [line.strip('\n')]

triangular_number_sequence = [(t - 1) * t // 2 for t in range(24 + 1)]


class Blueprint(object):
    blueprint_id: int
    ore_robot_cost: int
    clay_robot_cost: int
    obsidian_robot_cost: tuple[int, int]
    geode_robot_cost: tuple[int, int]
    cache: dict[tuple[tuple[int, int, int, int], tuple[int, int, int, int], int], tuple[tuple[int, ...], int]]

    def __init__(self, blueprint_id: int, ore_robot_cost: int, clay_robot_cost: int,
                 obsidian_robot_cost: tuple[int, int], geode_robot_cost: tuple[int, int]):
        assert blueprint_id >= 1
        self.blueprint_id = blueprint_id
        self.ore_robot_cost = ore_robot_cost
        self.clay_robot_cost = clay_robot_cost
        self.obsidian_robot_cost = obsidian_robot_cost
        self.geode_robot_cost = geode_robot_cost
        self.cache: dict[tuple[int, int, int, int, int, int, int, int, int], int] = {}

        self.global_max = 0

    def get_optimal_plan(self, ore: int, clay: int, obsidian: int, geode: int, or_robot: int, cl_robot: int,
                         ob_robot: int, ge_robot: int, remaining_minutes: int = 24, depth=0) -> int:
        # stash: ore, clay, obsidian, geode
        # robots: ore, clay, obsidian, geode
        max_value = 0

        if depth <= 20 and (ore, clay, obsidian, geode, or_robot, cl_robot, ob_robot, ge_robot, remaining_minutes) in self.cache:
            # print('cache hit')
            return self.cache[ore, clay, obsidian, geode, or_robot, cl_robot, ob_robot, ge_robot, remaining_minutes]

        if geode + ge_robot * remaining_minutes + triangular_number_sequence[remaining_minutes] <= self.global_max:
            return 0

        if remaining_minutes == 1:
            return geode + ge_robot

        # dfs
        max_value = max(max_value,
                        self.get_optimal_plan(ore + or_robot, clay + cl_robot, obsidian + ob_robot, geode + ge_robot,
                                              or_robot, cl_robot, ob_robot, ge_robot, remaining_minutes - 1, depth + 1))

        if ore >= self.ore_robot_cost:
            max_value = max(max_value, self.get_optimal_plan(ore + or_robot - self.ore_robot_cost, clay + cl_robot,
                                                             obsidian + ob_robot, geode + ge_robot, or_robot + 1,
                                                             cl_robot, ob_robot, ge_robot, remaining_minutes - 1,
                                                             depth + 1))

        if ore >= self.clay_robot_cost:
            max_value = max(max_value, self.get_optimal_plan(ore + or_robot - self.clay_robot_cost, clay + cl_robot,
                                                             obsidian + ob_robot, geode + ge_robot, or_robot,
                                                             cl_robot + 1, ob_robot, ge_robot, remaining_minutes - 1,
                                                             depth + 1))

        if ore >= self.obsidian_robot_cost[0] and clay >= self.obsidian_robot_cost[1]:
            max_value = max(max_value, self.get_optimal_plan(ore + or_robot - self.obsidian_robot_cost[0],
                                                             clay + cl_robot - self.obsidian_robot_cost[1],
                                                             obsidian + ob_robot, geode + ge_robot, or_robot, cl_robot,
                                                             ob_robot + 1, ge_robot, remaining_minutes - 1, depth + 1))
        if ore >= self.geode_robot_cost[0] and obsidian >= self.geode_robot_cost[1]:
            max_value = max(max_value, self.get_optimal_plan(ore + or_robot - self.geode_robot_cost[0], clay + cl_robot,
                                                             obsidian + ob_robot - self.geode_robot_cost[1],
                                                             geode + ge_robot, or_robot, cl_robot, ob_robot,
                                                             ge_robot + 1, remaining_minutes - 1, depth + 1))

        if depth <= 20:
            self.cache[
                ore, clay, obsidian, geode, or_robot, cl_robot, ob_robot, ge_robot, remaining_minutes] = max_value

        # print(potential_values)
        self.global_max = max(max_value, self.global_max)

        return max_value

    def __repr__(self):
        return str(self.__dict__)


blueprints: list[Blueprint] = []

for bp_id, line in enumerate(data):
    ex = re.compile(
        'Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian')
    _, orc, crc, ob_robot_cost_0, ob_robot_cost_1, geode_robot_cost_0, geode_robot_cost_1 = ex.match(
        line).groups()
    bp = Blueprint(bp_id + 1, int(orc), int(crc), (int(ob_robot_cost_0), int(ob_robot_cost_1)),
                   (int(geode_robot_cost_0), int(geode_robot_cost_1)))
    blueprints.append(bp)


# print(blueprints)


def solution():
    quality_level_sum = 0
    total_minutes = 24
    for i in range(len(blueprints)):
        plan = blueprints[i].get_optimal_plan(0, 0, 0, 0, 1, 0, 0, 0, remaining_minutes=24)
        blueprints[i].cache = {}
        quality_level_sum += (i+1)*plan
        print(quality_level_sum)


def main():
    # global data

    solution()


if __name__ == '__main__':
    main()
