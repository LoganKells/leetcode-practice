from typing import List
import pytest

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        i = 0

        # Find all local minima and maxima couples.
        # Buy and sell the coupled minima and maxima and add this to the total profit

        while i < len(prices) - 1:

            # Find next local minima to buy
            while (i < len(prices) - 1) and (prices[i] >= prices[i + 1]):  # negative slope
                i += 1
            minima = prices[i] if i <= len(prices) - 1 else 0

            # Find next local maxima closest to the last minima
            while i < len(prices) - 1 and prices[i] <= prices[i + 1]:  # positive slope
                i += 1
            maxima = prices[i] if i <= len(prices) - 1 else 0
            total_profit += maxima - minima

        return total_profit


test_cases = [([7,1,5,3,6,4], 7), ([7,1,5,3,6,4, 1, 9, 0, 1, 0, 1, 2, 1, 11], 28), ([1], 0), ([9, 1], 0)]


@pytest.mark.parametrize("prices, profit_expected", test_cases)
def test_max_profit(prices, profit_expected):
    solution = Solution()
    max_profit_calculated = solution.maxProfit(prices=prices)

    assert max_profit_calculated == profit_expected