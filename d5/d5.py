from enum import Enum

class Index(Enum):
    FROM = 1
    TO = 0
    RANGE = 2

INPUT_FILE = "./d5/input.txt"
with open(INPUT_FILE, 'r') as file:
    rows = file.readlines()

def get_locations(rows) -> list[int]:
    seeds = [int(x) for x in rows[0].split()[1:]]

    maps = []
    temp_map = []
    skip_row = True
    for row in rows[2:]:
        # Save on newlines
        if row == "\n":
            maps.append(temp_map)
            temp_map = []
            skip_row = True
        # Skip name lines
        elif skip_row:
            skip_row = False
            continue
        else:
            # Line format - X Y Z, Y-to-X map
            # X, Y, range
            temp_map.append([int(x) for x in row.split()])

    # Make up for lack of newline at end
    maps.append(temp_map)

    # Find the locations for each seed
    locations = []
    for seed in seeds:
        next_key = seed
        for map in maps:
            print(map)
            for row in map:
                offset = next_key - row[Index.FROM.value]
                if offset >= 0 and offset < row[Index.RANGE.value]:
                    # Add the offset to TO and store as the next key
                    next_key = row[Index.TO.value] + offset
                    break
        locations.append(next_key)

    return locations

def get_locations_v2(rows) -> list[int]:
    seed_data = [int(x) for x in rows[0].split()[1:]]
    seed_groups = []
    for i in range(0, len(seed_data), 2):
        start = seed_data[i]
        rnge = seed_data[i+1]
        seed_groups.append([start, rnge])

    print(seed_groups)

    maps = []
    temp_map = []
    skip_row = True
    for row in rows[2:]:
        # Save on newlines
        if row == "\n":
            maps.append(temp_map)
            temp_map = []
            skip_row = True
        # Skip name lines
        elif skip_row:
            skip_row = False
            continue
        else:
            # Line format - X Y Z, Y-to-X map
            # X, Y, range
            temp_map.append([int(x) for x in row.split()])

    # Make up for lack of newline at end
    maps.append(temp_map)

    # Find the locations for each seed
    locations = []
    for group in seed_groups:
        next_group = group
        subgroups = [next_group]
        print(subgroups)
        for map in maps:
            subgroups_mapped = set()
            for row in map:
                subgroups_grew = False
                for i, subgroup in enumerate(subgroups):
                    if i in subgroups_mapped:
                        continue
                    # Create new subgroup from too low
                    if subgroup[0] < row[Index.FROM.value]:
                        count_below_start = row[Index.FROM.value] - subgroup[0]
                        if count_below_start >= subgroup[1]:
                            continue
                        else:
                            # Make new subgroup
                            new_subgroup = [subgroup[0], count_below_start]
                            subgroup[0], subgroup[1] = [subgroup[0]+count_below_start, subgroup[1]-count_below_start]
                            subgroups.append(new_subgroup)
                            subgroups_grew = True
                    if subgroup[0] + subgroup[1] > row[Index.FROM.value] + row[Index.RANGE.value]:
                        count_above_end = (subgroup[0] + subgroup[1]) - (row[Index.FROM.value] + row[Index.RANGE.value])
                        if count_above_end >= subgroup[1]:
                            continue
                        else:
                            new_subgroup = [row[Index.FROM.value] + row[Index.RANGE.value], count_above_end]
                            subgroup[0], subgroup[1] = [subgroup[0], subgroup[1]-count_above_end]
                            subgroups.append(new_subgroup)
                            subgroups_grew = True

                    # subgroup should be mapped perfectly now
                        
                    # Get a group that matches the map
                    start_offset = subgroup[0] - row[Index.FROM.value]
                    subgroup[0] = row[Index.TO.value] + start_offset
                    subgroups_mapped.add(i)
                if not subgroups_grew and len(subgroups_mapped) == len(subgroups):
                    break
        # After going through all the maps, find the lowest location for this seed group
        locations.append(min(subgroup[0] for subgroup in subgroups))

    return locations

locations = get_locations_v2(rows)
print(locations)
print(min(locations))