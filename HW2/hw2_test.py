import pandas as pd

# Name: Yeesa Kee
# Section: AE
# This program simulates tests to check that the methods in hw2_manual.py and
# hw2_pandas.py outputs the correct/expected values.

# Don't worry about this import syntax, we will talk about it later
# You can call the method using
#    assert_equals(expected, received)
#    parse(file)
from cse163_utils import assert_equals, parse

import hw2_manual
import hw2_pandas

parsed_pokemon_test = parse("/home/pokemon_test.csv")
parsed_pokemon_my_test = parse("/home/pokemon_empty_test.csv")
parsed_pokemon_box = parse("/home/pokemon_box.csv")
pandas_pokemon_test = pd.read_csv("/home/pokemon_test.csv")
pandas_pokemon_my_test = pd.read_csv("/home/pokemon_empty_test.csv")


def main():
    test_species_count()
    test_max_level()
    test_filter_range()
    test_mean_attack_for_type()
    test_count_type()
    test_highest_stage_per_type()
    test_mean_attack_per_type()


def test_species_count():
    """
    Tests the function species_count in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(3, hw2_manual.species_count(parsed_pokemon_test))
    assert_equals(1, hw2_manual.species_count(parsed_pokemon_my_test))
    print("Testing test_manual_species_count complete")

    assert_equals(3, hw2_pandas.species_count(pandas_pokemon_test))
    assert_equals(1, hw2_pandas.species_count(pandas_pokemon_my_test))
    print("Testing test_pandas_species_count complete")


def test_max_level():
    """
    Tests the function max_level in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(('Lapras', 72), hw2_manual.max_level(parsed_pokemon_test))
    assert_equals(('Persian', 40),
                  hw2_manual.max_level(parsed_pokemon_my_test))
    print("Testing test_manual_max_level complete")

    assert_equals(('Lapras', 72), hw2_pandas.max_level(pandas_pokemon_test))
    assert_equals(('Persian', 40),
                  hw2_pandas.max_level(pandas_pokemon_my_test))
    print("Testing test_pandas_max_level complete")


def test_filter_range():
    """
    Tests the function filter_range in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_manual.filter_range(parsed_pokemon_test, 30, 70))
    assert_equals([], hw2_manual.filter_range(parsed_pokemon_my_test, 0, 30))
    print("Testing test_manual_filter_range complete")

    assert_equals(['Arcanine', 'Arcanine', 'Starmie'],
                  hw2_pandas.filter_range(pandas_pokemon_test, 30, 70))
    assert_equals([], hw2_pandas.filter_range(pandas_pokemon_my_test, 0, 30))
    print("Testing test_pandas_filter_range complete")


def test_mean_attack_for_type():
    """
    Tests the function mean_attack_for_type in hw2_manual.py and hw2_pandas.py
    """
    assert_equals(47.5, hw2_manual.mean_attack_for_type(parsed_pokemon_test,
                  'fire'))
    assert_equals(None, hw2_manual.mean_attack_for_type(parsed_pokemon_my_test,
                  'fire'))
    print("Testing test_manual_mean_attack_for_type complete")

    assert_equals(47.5, hw2_pandas.mean_attack_for_type(pandas_pokemon_test,
                  'fire'))
    assert_equals(None, hw2_pandas.mean_attack_for_type(pandas_pokemon_my_test,
                  'fire'))
    print("Testing test_pandas_mean_attack_for_type complete")


def test_count_type():
    """
    Tests the function count_type in hw2_manual.py and hw2_pandas.py
    """
    assert_equals({'water': 2, 'fire': 2},
                  hw2_manual.count_types(parsed_pokemon_test))
    assert_equals({'normal': 1},
                  hw2_manual.count_types(parsed_pokemon_my_test))
    print("Testing test_manual_count_type complete")

    assert_equals({'water': 2, 'fire': 2},
                  hw2_pandas.count_types(pandas_pokemon_test))
    assert_equals({'normal': 1},
                  hw2_pandas.count_types(pandas_pokemon_my_test))
    print("Testing test_pandas_count_type complete")


def test_highest_stage_per_type():
    """
    Tests the function highest_stage_per_type in
    hw2_manual.py and hw2_pandas.py
    """
    assert_equals({'water': 2, 'fire': 2},
                  hw2_manual.highest_stage_per_type(parsed_pokemon_test))
    assert_equals({'normal': 2},
                  hw2_manual.highest_stage_per_type(parsed_pokemon_my_test))
    print("Testing test_manual_highest_stage_per_type complete")

    assert_equals({'water': 2, 'fire': 2},
                  hw2_pandas.highest_stage_per_type(pandas_pokemon_test))
    assert_equals({'normal': 2},
                  hw2_pandas.highest_stage_per_type(pandas_pokemon_my_test))
    print("Testing test_pandas_highest_stage_per_type complete")


def test_mean_attack_per_type():
    """
    Tests the function mean_attack_per_type in hw2_manual.py and hw2_pandas.py
    """
    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_manual.mean_attack_per_type(parsed_pokemon_test))
    assert_equals({'normal': 104},
                  hw2_manual.mean_attack_per_type(parsed_pokemon_my_test))
    print("Testing test_manual_mean_attack_per_type complete")

    assert_equals({'water': 140.5, 'fire': 47.5},
                  hw2_pandas.mean_attack_per_type(pandas_pokemon_test))
    assert_equals({'normal': 104},
                  hw2_pandas.mean_attack_per_type(pandas_pokemon_my_test))
    print("Testing test_pandas_mean_attack_per_type complete")


if __name__ == '__main__':
    main()
