import math

data = []
INPUT_PATH: str = "input"
# INPUT_PATH: str = "debug_input"
with open(INPUT_PATH, "r") as f:
    for line in f.readlines():
        data += [line.strip("\n")]


def solution():
    original_seeds = list(map(int, data[0].split(": ")[1].split()))
    seed_ranges = [x for x in zip(original_seeds[::2], original_seeds[1::2])]
    ranges = []
    current_ranges = []
    for line in data[2:]:
        if not len(line):
            ranges.append(current_ranges)
            current_ranges = []

        elif not line[0].isdigit():
            continue
        else:
            range_tuple = list(map(int, line.split()))
            current_ranges.append(range_tuple)
    ranges.append(current_ranges)

    for j, map_range in enumerate(ranges):
        new_seeds = []
        for seed_st, seed_length in seed_ranges:
            seed_end = seed_st + seed_length
            mapped_ranges = []
            new_seed = []

            # check each range whether we intersect with the interval
            for dst_st, src_st, src_length in map_range:
                src_end = src_st + src_length
                # [o_l, s_l ,o_u]
                if src_st <= seed_st <= src_end:
                    # [o_l, s_l, s_u, o_u]
                    if seed_end <= src_end:
                        mapped_ranges.append((seed_st, seed_length))
                        new_seed.append((dst_st + (seed_st - src_st), seed_length))
                    # [o_l, s_l, o_u, s_u]
                    else:
                        mapped_ranges.append((seed_st, src_end - seed_st))
                        new_seed.append(
                            (dst_st + (seed_st - src_st), src_end - seed_st)
                        )
                # [s_l, o_l, s_u, o_u]
                elif src_st <= seed_end <= src_end:
                    mapped_ranges.append((src_st, seed_end - src_st))
                    new_seed.append((dst_st, seed_end - src_st))
                # [s_l, o_l, o_u, s_u]
                elif seed_st < src_st and src_end < seed_end:
                    mapped_ranges.append((src_st, src_length))
                    new_seed.append((dst_st, src_length))

            sorted_mapped = sorted(mapped_ranges, key=lambda x: x[0])

            if len(sorted_mapped) == 0:
                new_seed.append((seed_st, seed_length))

            # since we have now mapped part of the seed, we need to also make sure that we split correctly (i. e.
            # make sure that we don't loose part of the seed by means of 1:1 mappings)
            for i, (st, length) in enumerate(sorted_mapped):
                if i == 0 and st > seed_st:
                    new_seed.append((seed_st, st - seed_st))

                if i == (len(sorted_mapped) - 1):
                    if (st + length) < seed_end:
                        new_seed.append((st + length, seed_end - (st + length)))
                    continue

                if st + length < sorted_mapped[i + 1][0]:
                    new_seed.append(
                        (st + length + 1, sorted_mapped[i + 1][0] - (st + length))
                    )
            assert sum([seed[1] for seed in new_seed]) == seed_length
            new_seeds.extend(new_seed)
        seed_ranges = new_seeds

    print(min([seed[0] for seed in seed_ranges]))


def main():
    # global data

    solution()


if __name__ == "__main__":
    main()
