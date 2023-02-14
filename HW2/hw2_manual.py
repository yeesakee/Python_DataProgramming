# Name: Yeesa Kee
# Section: AE
# This program solves 7 problems given in Homework 2 without using pandas, and
# includes methods showing specified data in the problems with the given list.
# All the methods in this file will assume that the given dataset will contain
# at least one row of Pokemon data, users will pass parameters of the
# expected types and that those parameters are NOT None.
# Problems include species_count, max_level, filter_range, mean_attack_for_type
# count_types, highest_stage_per_type, and mean_attack_per_type.


def species_count(data):
    """
    Returns the number of unique Pokemon species in the given dataset.

    It is assumed that the data is well formatted and the methods would
    not need to transform any values in the name column.
    """
    result = set()
    for dic in data:
        result.add(dic['name'])
    return len(result)


def max_level(data):
    """
    Returns a tuple with the first element containing the name of the Pokemon
    with the highest level and the second element containing the level of
    the Pokemon.
    If a tie appears the Pokemon that appears earlier will be returned
    """
    name = ""
    level = 0
    for dic in data:
        if dic['level'] > level:
            level = dic['level']
            name = dic['name']
    return name, level


def filter_range(data, low_level, high_level):
    """
    Returns a list of Pokemon names having a level between
    low_level(inclusive) and high_level(exvlusive).

    The returned list will be in the same order that they appear in
    the provided dataset.
    """
    result = list()
    for dic in data:
        if dic['level'] >= low_level and dic['level'] < high_level:
            result.append(dic['name'])
    return result


def mean_attack_for_type(data, poke_type):
    """
    Returns the average attack stat for all the Pokemon of type poke_type
    in the given dataset.
    Returns None if there are no Pokemon of the given type.
    """
    # stores the total attack stat for all the Pokemon of type poke_type
    result = 0
    # stores the number of times the Pokemon of type poke_type appears in
    # the dataset
    count = 0
    for dic in data:
        if dic['type'] == poke_type:
            result += dic['atk']
            count += 1
    if count == 0:
        return None
    return result / count


def count_types(data):
    """
    Returns a dictionary with keys that are of Pokemon types and contains
    values that represent the number of times that Pokemon type appears
    in the given dataset.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    # stores keys that represent Pokemon types and values representing
    # the number of times that Pokemon type appears in the given dataset
    result = dict()
    for line in data:
        poke_type = line['type']
        # if result contains a key of poke_type
        if poke_type in result:
            result[poke_type] += 1
        else:
            result[poke_type] = 1
    return result


def highest_stage_per_type(data):
    """
    Returns a dictionary that contains keys representing the Pokemon types
    and values that represents the highest value of the stage column for that
    Pokemon type.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    # stores keys that represent Pokemon types and values that represent
    # the highest value of the stage column of that Pokemon type
    result = dict()
    for dic in data:
        poke_type = dic['type']
        poke_stage = dic['stage']
        # if result does not contain a key of poke_type
        if poke_type not in result:
            result[poke_type] = poke_stage
        elif result[poke_type] < poke_stage:
            result[poke_type] = poke_stage
    return result


def mean_attack_per_type(data):
    """
    Returns a dictionary that contains keys that represent Pokemon types and
    values that represent the average attack for that Pokemon type.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    # stores keys that represent Pokemon types and values that represent
    # the average attack for that Pokemon type
    result = dict()
    # stores keys that represent Pokemon types and values that represent
    # how many times that Pokemon type appears in the dataset
    result_count = dict()
    for dic in data:
        poke_type = dic['type']
        poke_attack = dic['atk']
        # if result does not contain a key of poke_type
        if poke_type not in result:
            result[poke_type] = poke_attack
            result_count[poke_type] = 1
        else:
            result[poke_type] += poke_attack
            result_count[poke_type] += 1
    for key in result.keys():
        # divide each key value of result by the key value of
        # result_count to get the average attack for each Pokemon type
        result[key] /= result_count[key]
    return result
