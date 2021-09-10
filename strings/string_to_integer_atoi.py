import pytest

# 8. String to Integer (atoi)
# see: https://leetcode.com/problems/string-to-integer-atoi/


# 32 bit signed integer limits
MAX_INT = 2 ** 31 - 1
MIN_INT = -1 * 2 ** 31


class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "":
            return 0
        else:
            # Strip the leading white space and trailing white spaces
            s = s.strip()

            # If the first char is not an integer, then return 0, unless it is "+" or "-".
            if len(s) == 1 and 47 < ord(s[0]) < 58:
                value = int(s)
                return value
            # If the first two chars do not contain an integer then return 0.
            elif len(s) > 1 and (47 < ord(s[0]) < 58 or (ord(s[0]) in (ord("-"), ord("+"))) and 47 < ord(s[1]) < 58):
                # Strip trailing chars that are not integers
                s = s.strip(" +abcdefghijklmnopqrstuvwxyz")

                # Handle positive, negative
                if s[0] == "-":
                    mult = -1
                    s = s[1:]
                elif s[0] == "+":
                    mult = 1
                    s = s[1:]
                else:
                    mult = 1

                # Handle floating points, or first instance of non-numeric char
                nums = [' ', '-', '.', '+', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
                        'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a',
                        'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z']
                idx = next((i for i, ch in enumerate(s) if ch in nums), None)
                if idx is not None:
                    s = s[:idx]

                # Convert to integer
                value = int(s) * mult

                # If the converted integer is above 32 bit signed integer limits, then clip to the limits
                if value > MAX_INT:
                    return MAX_INT
                elif value < MIN_INT:
                    return MIN_INT
                else:
                    return value
            else:
                return 0


class Solution2:
    def myAtoi(self, s: str) -> int:
        # ignore leading whitespace
        first_c = s[0] if s != "" else None
        while first_c == " ":
            s = s[1:]
            first_c = s[0] if s != "" else None

        # Handle if s is now none
        if s == "":
            return 0

        # Check sign
        sign = -1 if s[0] == "-" else 1

        # Strip the sign
        if s[0] in ("-", "+", "0"):
            s = s[1:]

        # Evaluate the length of the return int, which is the len until the first non integer char
        length = 0
        i = 0
        # Handle if s is now none
        if s == "":
            return 0
        c = s[length]
        while 48 <= ord(c) <= 57:
            length += 1
            c = s[length] if length < len(s) else "q"

        # Calculate the number as a float: 1.3 -> 13 later
        num = 0
        level = length - 1
        for i in range(length):
            c = s[i] if i < length else "q"
            if 48 <= ord(c) <= 57:
                new_val = int(c)
                num += new_val * 10 ** level
                level -= 1
            else:
                break

        # Convert from float to int: 1.3 -> 13
        num_int = int(sign * num * (10 ** (-1 * level - 1)))
        if num_int > MAX_INT:
            return MAX_INT
        elif num_int < MIN_INT:
            return MIN_INT
        else:
            return num_int


test_case = [("   -42", -42)]
test_cases = [("+", 0),
    (" -1010023630o4", -1010023630),
                ("", 0),
              ("   -42", -42),
              ("-13+8", -13),
              (" ", 0),
              ("3.14159", 3),
              ("00000-42a1234", 0),
              ("1", 1),
              ("", 0),
              ("-+12", 0),
              ("42", 42),
              ("4193 with words", 4193),
              ("-91283472332", -2147483648),
              ("words and 987", 0),
              ("000000000000000000000000000011", 11)
              ]


@pytest.mark.parametrize("test_input, expected", test_cases)
def test_my_atoi(test_input, expected):
    sol = Solution()
    value = sol.myAtoi(s=test_input)
    assert value == expected


@pytest.mark.parametrize("test_input, expected", test_cases)
def test_my_atoi(test_input, expected):
    sol = Solution2()
    value = sol.myAtoi(s=test_input)
    assert value == expected
