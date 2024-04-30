def teams_allocation(n, idx, white_idx, black_idx, dp, elements):
    if idx == n:
        return 0

    if dp[idx][white_idx][black_idx] != 0:
        return dp[idx][white_idx][black_idx]

    secondary = 0
    tertiary = 0

    if white_idx == n or elements[idx] > elements[white_idx]:
        secondary = 1 + teams_allocation(n, idx + 1, idx, black_idx, dp, elements)

    if black_idx == n or elements[idx] < elements[black_idx]:
        tertiary = 1 + teams_allocation(n, idx + 1, white_idx, idx, dp, elements)

    dp[idx][white_idx][black_idx] = max(teams_allocation(n, idx + 1, white_idx, black_idx, dp, elements), secondary,
                                        tertiary)

    return dp[idx][white_idx][black_idx]


n = int(input())

dp = [[[0] * (n + 1) for _ in range(n + 1)] for _ in range(n + 1)]
elements = [int(x) for x in input().split()]

print(n - teams_allocation(n, 0, n, n, dp, elements))
