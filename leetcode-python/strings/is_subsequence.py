import pytest

# 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Two pointers solution -> Walk through.
        c1, c2 = 0, 0

        while c1 < len(s) and c2 < len(t):
            # If values at both pointers match, then advance both
            if s[c1] == t[c2]:
                c1 += 1
                c2 += 1
            # Otherwise only advance the pointer for the string, t.
            else:
                c2 += 1

        # If the pointer c1 made it to the end of the substring via matches, then the substring exists in t.
        if c1 == len(s):
            return True
        else:
            return False


test_cases = [("aaaaaa", "bbaaaa", False),
              ("acb", "ahbgdc", False),
              ("bb", "ahbgdc", False),
              ("abc", "ahbgdc", True),
              ("rjufvjafbxnbgriwgokdgqdqewn", "mjmqqjrmzkvhxlyruonekhhofpzzslupzojfuoztvzmmqvmlhgqxehojfowtrinbatjujaxekbcydldglkbxsqbbnrkhfdnpfbuaktupfftiljwpgglkjqunvithzlzpgikixqeuimmtbiskemplcvljqgvlzvnqxgedxqnznddkiujwhdefziydtquoudzxstpjjitmiimbjfgfjikkjycwgnpdxpeppsturjwkgnifinccvqzwlbmgpdaodzptyrjjkbqmgdrftfbwgimsmjpknuqtijrsnwvtytqqvookinzmkkkrkgwafohflvuedssukjgipgmypakhlckvizmqvycvbxhlljzejcaijqnfgobuhuiahtmxfzoplmmjfxtggwwxliplntkfuxjcnzcqsaagahbbneugiocexcfpszzomumfqpaiydssmihdoewahoswhlnpctjmkyufsvjlrflfiktndubnymenlmpyrhjxfdcq", False)]


@pytest.mark.parametrize("s, t, expected", test_cases)
def test_is_subsequence(s, t, expected):
    sol = Solution()
    is_subsequence = sol.isSubsequence(s=s, t=t)
    assert is_subsequence == expected
