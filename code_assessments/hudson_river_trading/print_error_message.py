import pytest


class Solution:
    def print_error(self, s: str, y: int, z: int):
        """
        :param s: input text
        :param y: index of the error in s
        :param z: maximum number of characters to return on each side of the error
        :return: error message
        """
        s_split = s.split("\n")
        for i, sub_string in enumerate(s_split):
            s_split[i] = sub_string + "\n"

        b4_error = s[y - 1]
        error_point = s[y]

        sub_string_lengths = {}
        # determine which sub-string the error is in
        for i, sub_string in enumerate(s_split):
            sub_string_lengths[i] = len(sub_string)

        # Determine which substring the error is inside of
        running_length = 0
        idx_sub_strings_w_error = 0
        idx_error_from_start = 0
        for idx_sub_string, length in sub_string_lengths.items():
            running_length += length
            if y <= running_length:  # Error is in this sub_string
                idx_sub_strings_w_error += idx_sub_string
                idx_error_from_end = running_length - y
                idx_error_from_start = len(s_split[idx_sub_string]) - idx_error_from_end
                break

        # Create the final return
        line_w_error = s_split[idx_sub_strings_w_error]
        line_above = s_split[idx_sub_strings_w_error - 1] if idx_sub_strings_w_error > 0 else ""
        line_below = s_split[idx_sub_strings_w_error + 1] if len(s_split) > idx_sub_strings_w_error + 1 else ""

        # return results
        error_message_lines = (line_above, line_w_error, line_below)
        idx_error = len(line_above) + idx_error_from_start
        error_message = "".join(error_message_lines)

        # Clip the left and right side with z
        left_side = error_message[:idx_error]
        left_side_rev = left_side[::-1]
        end_left = min(len(left_side), z)
        left_side_rev = left_side_rev[:end_left]
        left_side = left_side_rev[::-1]

        right_side = error_message[idx_error + 1:]
        right_side_rev = right_side[::-1]
        end_right = min(len(right_side), z)
        right_side_rev = right_side_rev[:end_right]
        right_side = right_side_rev[::-1]

        # Create the line with the ^ carrot just after the error
        spaces = []
        for i in range(len(left_side)):
            spaces.append(" ")
        spaces.append("^\n")
        line_w_carrot = "".join(spaces)


        # Return clipped error message
        error_message_lines = (left_side, s[y], "\n", line_w_carrot, right_side)
        error_message_final = "".join(error_message_lines)

        return error_message_final

# "int main() {\n"
# "    return 0\n"
# "            ^\n"
# "}\n"


test_cases = [("123",
               1, 0,
               "2\n" + "^\n"),
              ("// comment\n" + "int main() {\n" + "    return 0\n" + "}\n",
               36, 126,
               "int main() {\n" + "    return 0\n" + "            ^\n" + "}\n")
              ]


@pytest.mark.parametrize("s, y, z, expected", test_cases)
def test_print_error(s, y, z, expected):
    sol = Solution()
    error_message = sol.print_error(s=s, y=y, z=z)
    assert error_message == expected
