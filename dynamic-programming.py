N = 20

dp = [0] * (N + 1)


def fibonacci_with_dp(n: int):
    if n == 1:
        return 1
    if n == 2:
        return 1

    if dp[n] != 0:
        return dp[n]

    dp[n] = fibonacci_with_dp(n - 1) + fibonacci_with_dp(n - 2)
    return dp[n]


print(fibonacci_with_dp(N))
