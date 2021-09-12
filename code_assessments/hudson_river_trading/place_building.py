import pytest


def solution(K, A):
    # Get the (row, col) indexes of each house
    idx_houses = []
    i = 0
    for row in A:
        for j, col in enumerate(row):
            if col == 1:
                idx_houses.append([i + 1, j + 1])
        i += 1

    # Evaluate each index i,j to determine if it is valid (within k distance)
    idx_valid = {}  # Must be unique spots, use a map
    idx = 0
    i = 0
    for row in A:
        for j, col in enumerate(row):
            valid_point = True
            point = [i + 1, j + 1]
            for idx_house in idx_houses:
                if (abs(idx_house[0] - point[0]) + abs(idx_house[1] - point[1])) > K:
                    valid_point = False
                    break
            if valid_point and point not in idx_houses:
                # create unique key
                idx_str = str(point[0]) + str(point[1])
                idx_valid[idx_str] = point
        i += 1

    return len(idx_valid.keys())


test_cases = [(4, [[0, 0, 0, 1], [0, 1, 0, 0], [0, 0, 1, 0], [1, 0, 0, 0], [0, 0, 0, 0]], 8),
    (1, [[0, 1], [0, 0]], 2),
    (2, [[0, 0, 0, 0], [0, 0, 1, 0], [1, 0, 0, 1]], 2)]


@pytest.mark.parametrize("K, A, expected", test_cases)
def test_pick_spots(K, A, expected):
    valid_spot_count = solution(K=K, A=A)
    assert valid_spot_count == expected