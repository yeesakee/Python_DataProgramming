# Name: Yeesa Kee
# Section: AE
# This program simulates tests to make sure that the methods in hw1.py
# outputs the correct/expected values.

import math

import hw1


def main():
    test_funky_sum()
    test_count_divisible_digits()
    test_is_relatively_prime()
    test_travel()
    test_swip_swap()
    test_compress()
    test_longest_line_length()
    test_longest_word()
    test_mode_digit()


def assert_equals(expected, received):
    """
    Checks received against expected, throws an AssertionError
    if they don't match. If expected or recieved are floats,
    will do an approximate check.
    """
    # You don't need to understand how this function works
    # just look at its documentation!
    if type(expected) == 'float' or type(received) == 'float':
        match = math.isclose(expected, received)
    else:
        match = expected == received

    assert match, f'Failed: Expected {expected}, but received {received}'


def test_funky_sum():
    """
    Tests the function funky_sum
    """
    print('Testing funky_sum')

    # Notice that we have to start the function calls with "hw1." since
    # they live in another file

    # Cases from the made up "spec" for this problem
    assert_equals(1, hw1.funky_sum(1, 2, 0))
    assert_equals(2, hw1.funky_sum(1, 2, 1))
    assert_equals(1.5, hw1.funky_sum(1, 2, 0.5))
    assert_equals(1.33, hw1.funky_sum(1, 2, 0.33))

    # edge cases to test the 0 check
    assert_equals(1, hw1.funky_sum(1, 2, -1))
    assert_equals(1, hw1.funky_sum(1, 2, -0.1))
    assert_equals(1.01, hw1.funky_sum(1, 2, 0.01))

    # edge cases to test the 1 check
    assert_equals(2, hw1.funky_sum(1, 2, 2))
    assert_equals(2, hw1.funky_sum(1, 2, 2.1))
    assert_equals(1.99, hw1.funky_sum(1, 2, 0.99))


def test_count_divisible_digits():
    """
    Tests the function test_count_divisible_digits
    """
    assert_equals(2, hw1.count_divisible_digits(5032, 2))
    assert_equals(4, hw1.count_divisible_digits(33203, 3))
    assert_equals(0, hw1.count_divisible_digits(3120, 0))
    assert_equals(1, hw1.count_divisible_digits(301, 2))
    assert_equals(1, hw1.count_divisible_digits(-204, 5))
    assert_equals(4, hw1.count_divisible_digits(650899, 3))
    assert_equals(0, hw1.count_divisible_digits(24, 5))
    assert_equals(0, hw1.count_divisible_digits(1, 0))
    print('Testing test_count_divisible_digits complete')


def test_is_relatively_prime():
    """
    Tests the function test_is_relatively_prime
    """
    assert_equals(True, hw1.is_relatively_prime(12, 13))
    assert_equals(False, hw1.is_relatively_prime(4, 24))
    assert_equals(True, hw1.is_relatively_prime(5, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 9))
    assert_equals(True, hw1.is_relatively_prime(8, 1))
    assert_equals(False, hw1.is_relatively_prime(2, 14))
    assert_equals(True, hw1.is_relatively_prime(1, 3))

    print("Testing test_is_relatively_prime complete")


def test_travel():
    """
    Tests the function test_travel
    """
    assert_equals("(-1, 4)", hw1.travel("NW!ewnW", 1, 2))
    assert_equals("(0, 5)", hw1.travel(")NEfwwsnewwa", 2, 4))
    assert_equals("(0, 0)", hw1.travel("aNNWEWessew!", 0, 0))

    print("Testing test_travel complete")


def test_swip_swap():
    """
    Tests the function test_swip_swap
    """
    assert_equals("offbar", hw1.swip_swap("foobar", "f", "o"))
    assert_equals("foocar", hw1.swip_swap("foobar", "b", "c"))
    assert_equals("foobar", hw1.swip_swap("foobar", "z", "c"))
    assert_equals("etseing", hw1.swip_swap("testing", "t", "e"))
    assert_equals("ababeec", hw1.swip_swap("acaceeb", "b", "c"))

    print("Testing test_swip_swap complete")


def test_compress():
    """
    Tests the function test_compress
    """
    assert_equals(
        "c1o17l1k1a1n1g1a1r1o2",
        hw1.compress("cooooooooooooooooolkangaroo"))
    assert_equals("a3", hw1.compress("aaa"))
    assert_equals("", hw1.compress(""))
    assert_equals("d2o3a1", hw1.compress("ddoooa"))
    assert_equals("a4e1c4d1e1a1", hw1.compress("aaaaeccccdea"))

    print("Testing test_compress complete")


def test_longest_line_length():
    """
    Tests the funtion test_longest_line_length
    """
    assert_equals(13, hw1.longest_line_length("/home/poem.txt"))
    assert_equals(25, hw1.longest_line_length("/home/problem6_1.txt"))
    assert_equals(6, hw1.longest_line_length("/home/problem6_2.txt"))
    assert_equals(None, hw1.longest_line_length("/home/problem6_3.txt"))

    print("Testing test_longest_line_length complete")


def test_longest_word():
    """
    Tests the funtion test_longest_word
    """
    assert_equals("3: shells", hw1.longest_word("/home/poem.txt"))
    assert_equals("2: problem", hw1.longest_word("/home/problem6_1.txt"))
    assert_equals("1: tests", hw1.longest_word("/home/problem6_2.txt"))
    assert_equals(None, hw1.longest_word("/home/problem6_3.txt"))

    print("Testing test_longest_word complete")


def test_mode_digit():
    """
    Tests the function test_mode_digit
    """
    assert_equals(1, hw1.mode_digit(12121))
    assert_equals(0, hw1.mode_digit(0))
    assert_equals(2, hw1.mode_digit(-122))
    assert_equals(2, hw1.mode_digit(1211232231))
    assert_equals(9, hw1.mode_digit(9))
    assert_equals(3, hw1.mode_digit(-3133298311))

    print("Testing test_mode_digit complete")


if __name__ == '__main__':
    main()
