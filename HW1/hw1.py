# Name: Yeesa kee
# Section: AE
# This program solves 8 problems given to us in Homework 1
# Including count_divisible_digits, is_relatively_prime, travel, swip_swap
# compress, longest_line_length, longest_word, and mode_digit


def funky_sum(a, b, mix):
    """
    Returns a mixture between a and b.

    If mix is 0, returns a. If mix is 1, returns b. Otherwise returns a linear
    interpolation between them. If mix is outside the range of 0 and 1, it is
    capped at those numbers.
    """
    if mix < 0:
        return a
    elif mix > 1:
        return b
    else:
        return (1 - mix) * a + mix * b


def count_divisible_digits(n, m):
    """
    Returns the number of digits in n that is divisible by m.
    Returns 0 if m is 0.

    Any digit in n that is 0 is divisble by any number
    """
    total = 0
    n = abs(n)
    if(m == 0):
        return 0
    while(n > 0):
        # get the last digit of the number to compare
        digit = n % 10
        # update the number by removing the last digit of the number
        n = n // 10
        # test if the number is 0 or divisible by m
        if(digit % m == 0 or digit == 0):
            total += 1
    return total


def is_relatively_prime(n, m):
    """
    Returns True if n and m are relatively prime to each other, False otherwise

    Two numbers are relatively prime if they share no common factors besides 1.
    n and m should be at least 1.
    """
    for i in range(2, 10):
        if(n % i == 0 and m % i == 0):
            return False
    return True


def travel(direction, x, y):
    """
    Returns a string in the format "(x_new, x_new)" representing the new
    coordinates as a result of the directions stated in direction.

    Takes a string direction that stores the directions moved from the given
    starting points: x as the x-coordinate and y as the y-coordinate.
    In the string (case ignored)
    N = +1 to y-coordinate
    S = -1 to y-coordinate
    E = +1 to x-coordinate
    W = -1 to x-coordinate
    all other characters are ignored.
    """
    direction = direction.lower()
    for i in range(len(direction)):
        if(direction[i] == "n"):
            y += 1
        elif(direction[i] == "s"):
            y -= 1
        elif(direction[i] == "e"):
            x += 1
        elif(direction[i] == "w"):
            x -= 1
    return "(" + str(x) + ", " + str(y) + ")"


def swip_swap(source, c1, c2):
    """
    Returns a string of source that has any c1 and c2 characters swapped.
    (a c1 character will be replaced by c2 and vise versa)

    c1 and c2 are single characters.
    """
    result = ""
    for i in range(len(source)):
        if(source[i] == c1):
            result += c2
        elif(source[i] == c2):
            result += c1
        else:
            result += source[i]
    return result


def compress(word):
    """
    Returns a string that represents the string word formated such that
    each character is followed by its count, and any adjacent duplicate
    characters are removed.

    The string should only contain letters.
    """
    # store the number of the same characters in a row
    count = 0
    # store the character we're comparing
    curr = ""
    # store the resulting string
    result = ""

    if(word == ""):
        return ""

    for i in range(len(word)):
        if(count == 0):
            curr = word[i]
            count += 1
        elif(curr == word[i]):
            count += 1
        else:
            # add the character and the number of times that character appears
            # in a row
            result += curr + str(count)
            count = 1
            curr = word[i]
    # add the last character and number of times the character appear in a row
    result += curr + str(count)
    return result


def longest_line_length(file_name):
    """
    Returns the length of the longest line in the given file.
    Returns None if the file is empty.

    The length of the line is the total characters present in the line
    Assumes that the given file name exist.
    """
    length = 0
    with open(file_name) as file:
        lines = file.readlines()
        # return none if lines is empty
        if(len(lines) == 0):
            return None
        for line in lines:
            if(len(line) > length):
                length = len(line)
    return length


def longest_word(file_name):
    """
    Returns the longest word in the given file and which line it appears on in
    the format of "line #: word".
    Returns None if the file is empty or contains no words.

    If there are ties for the longest word it will return the one that
    appears first in the file.
    Assumes that the given file name exist.
    """
    # keep track of the line number on right now
    line_number = 1
    # store the line of the longest word
    line_keep_track = 1
    # store the longest word
    longest = ""
    with open(file_name) as file:
        # stores all the lines in file
        lines = file.readlines()
        # returns None if the lines is empty (= file is empty)
        if(len(lines) == 0):
            return None
        # loop through each line in lines
        for line in lines:
            # store each word in line into a list
            words = line.split()
            # loop through each word in words
            for word in words:
                if(len(word) > len(longest)):
                    longest = word
                    line_number = line_keep_track
            line_keep_track += 1
    return str(line_number) + ": " + longest


def mode_digit(n):
    """
    Returns the number that most frequently appears in n.
    The returned digit will always be non-negative.

    If there is a tie then the digit with the greatest value is returned.
    The given number can be positive or negative.
    """
    # stores the number of times each number appears
    # index represent the number and value represents the count
    numbers = [0] * 10
    # stores the the number that appeared the most
    max_num = 0
    # keeps count of the number of times the most frequent number appears
    max_num_count = 0
    n = abs(n)
    if(n == 0):
        numbers[0] = 1
    while(n > 0):
        num = n % 10
        n = n // 10
        numbers[num] += 1
    for i in range(10):
        # if the the number of times the number i appears is greater than
        # or equal max_num_counts
        if(numbers[i] >= max_num_count):
            max_num = i
            max_num_count = numbers[i]
    return max_num
