# Name: Yeesa Kee
# Section: AE
# This program solves 7 problems given in Homework 2 using pandas,
# includes showing specified data in the problems with the given DataFrame.
# This programs assumes that the given DataFrame is non-empty (contains
# at least one row of Pokemon data), the parameters that are passed in
# are of the expected types described for that problem and are NOT None.
# Problems include species_count, max_level, filter_range, mean_attack_for_type
# count_types, highest_stage_per_type, and mean_attack_per_type.


def species_count(data):
    """
    Returns the number of unique Pokemon species
    (determined by the name column) found in the given DataFrame.

    This program assumes that the data is well formatted in the sense
    that this program would not need to transform any values in the
    name column.
    """
    return len(data.groupby('name'))


def max_level(data):
    """
    Returns a tuple of length 2, where the first element is the name of the
    Pokemon with the highest level in the given DataFrame and the second
    element is the level of that Pokemon.
    If a tie appears the Pokemon that appears earlier will be returned.
    """
    index = data['level'].idxmax()
    return data.loc[index]['name'], data['level'].max()


def filter_range(data, low_level, high_level):
    """
    Returns a list of Pokemon names that have a level between
    low_level(inclusive) and high_level(exclusive).

    The list returned will be in the same order that they appear in the
    given DataFrame.
    """
    # stores a Series of true or false depending on if the row has a level
    # column value of greater or equal to low_level
    low = data['level'] >= low_level
    # stores a series of true or false depending on if the row has a level
    # column value of less than high_level
    high = data['level'] < high_level
    return list(data[low & high]['name'])


def mean_attack_for_type(data, poke_type):
    """
    Returns the average attack stat for all the Pokemon in the DataFrame
    with type poke_type.
    Returns None if there are no Pokemon of type poke_type in the
    given DataFrame
    """
    # stores a Series with column type and the mean of column atk
    result = data.groupby('type')['atk'].mean()
    dic = dict(result)
    # if dic does not contain a key of poke_type
    if poke_type not in dic:
        return None
    return result[poke_type]


def count_types(data):
    """
    Returns a dictionary containing keys that represent Pokemon types and
    values that represent the number of times that type of Pokemon appears
    in the DataFrame.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    return dict(data.groupby('type')['id'].count())


def highest_stage_per_type(data):
    """
    Returns a dictionary containing keys that represent Pokemon types and
    values that represent the highest value of the stage column for that
    Pokemon type in the given DataFrame.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    return dict(data.groupby('type')['stage'].max())


def mean_attack_per_type(data):
    """
    Returns a dictionary containing keys that represent Pokemon types and
    values that represent the average atk column values for that Pokemon type.

    The order of the keys in the dictionary might not be in the order of how
    they appear in the given dataset.
    """
    return dict(data.groupby('type')['atk'].mean())
