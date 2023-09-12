from typing import List
import pytest

# see - https://leetcode.com/problems/k-th-symbol-in-grammar/

# Fast, recursive
class SolutionFastRecursive:
    def kthGrammar(self, n: int, k: int) -> int:
        # handle if n is just one row
        if n == 1:
            return 0

        # values are repeated from previous row for the first half of the current row.
        # The second half of the current row is the "compliment" of the first half.
        # row 1: 0
        # row 2: 01
        # row 3: 0110
        # row 4: 01101001

        # Each row has 2^n-1 total values.
        # e.g. row 4 has 2^3 = 8 total values
        idx_half = 2 ** (n - 2)

        if k <= idx_half:
            # If k is in the first half, then only calculate the previous row
            return self.kthGrammar(n=n-1, k=k)
        else:
            # if k is in the second half, then calculate the "compliment" of the previous row
            value_at_idk_compliment_to_k = self.kthGrammar(n=n-1, k=k-idx_half)
            return 1 if value_at_idk_compliment_to_k == 0 else 0  # return the compliment of previous row

test_cases_a = [(3, 1, 0), (1, 1, 0), (30, 434991989, 0)]
@pytest.mark.parametrize("n, k, expected", test_cases_a)
def test_kth_grammar_fast_recursive(n, k, expected):
    solution = SolutionFastRecursive()
    value_at_idx_k = solution.kthGrammar(n, k)

    assert value_at_idx_k == expected

# Slow, iterative
class SolutionSlowIterative:
    def kthGrammar(self, n: int, k: int) -> tuple:
        if n == 1 and k == 1:
            return [0], 0

        prev_row = [0]
        row = []
        for i in range(n - 1):
            row = []
            for j, num in enumerate(prev_row):
                if num == 0:
                    row.append(0)
                    row.append(1)
                else:
                    row.append(1)
                    row.append(0)
            prev_row = row
        return row, row[k]

test_cases_b = [(1, 1, ([0], 0)), (3, 1, ([0, 1, 1, 0], 1))]
@pytest.mark.parametrize("n, k, expected", test_cases_b)
def test_kth_grammar_slow_iterative(n, k, expected):
    solution = SolutionSlowIterative()
    last_row = solution.kthGrammar(n, k)

    assert last_row == expected
