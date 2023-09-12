import pytest
from typing import List

# 48. Rotate Image
# See - https://leetcode.com/problems/rotate-image/

class Solution091721:
    def rotate_custom(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        a = m // 2
        for i in range(m // 2 + m % 2):
            for j in range(m // 2):
                value_final = matrix[m - 1 - j][i]

                # Swap in pairs
                matrix[m - 1 - j][i] = matrix[m - 1 - i][m - 1 - j]  # Pair A
                matrix[m - 1 - i][m - 1 - j] = matrix[j][m - 1 - i]  # Pair B
                matrix[j][m - 1 - i] = matrix[i][j]  # Pair C
                matrix[i][j] = value_final  # Pair D
        return matrix


test_cases = [([[1,2,3],[4,5,6],[7,8,9]], [[7,4,1],[8,5,2],[9,6,3]])]


@pytest.mark.parametrize("m, expected", test_cases)
def test_matrix_rotate(m, expected):
    sol = Solution091721()
    m_rotated = sol.rotate_custom(matrix=m)
    assert m == expected
