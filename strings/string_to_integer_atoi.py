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


@pytest.mark.parametrize("test_input, expected", [("-13+8", -13), (" ", 0), ("3.14159", 3), ("00000-42a1234", 0), ("1", 1), ("", 0), ("-+12", 0),
                                                  ("   -42", -42), ("42", 42),
                                                  ("4193 with words", 4193),
                                                  ("-91283472332", -2147483648), ("words and 987", 0),
                                                  ])
def test_my_atoi(test_input, expected):
    sol = Solution()
    value = sol.myAtoi(s=test_input)
    assert value == expected
