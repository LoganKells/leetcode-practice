import pytest

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # Base case
    if len(S) < 2:
        return S

    if "AB" in S:
        split_s = S.split("AB")
        s_new = "".join(split_s)
        return solution(S=s_new)
    elif "BA" in S:
        split_s = S.split("BA")
        s_new = "".join(split_s)
        return solution(S=s_new)
    elif "DC" in S:
        split_s = S.split("DC")
        s_new = "".join(split_s)
        return solution(S=s_new)
    elif "CD" in S:
        split_s = S.split("CD")
        s_new = "".join(split_s)
        return solution(S=s_new)
    else:
        # Recursive solution
        idx_mid = len(S) // 2

        # Dive and recurse
        s_left, s_right = S[:idx_mid], S[idx_mid:]
        return solution(S=s_left) + solution(S=s_right)


test_cases = [('CABABD', "")]


@pytest.mark.parametrize("s, expected", test_cases)
def test_split(s, expected):
    s_split = solution(S=s)
    assert s_split == expected