## 이 문제가 DP라는 것을 알아차리는 것이 어려움

DIV = 1_000_000_007

def solution(n, money):
    dp = [1] + [0] * n

    for coin in sorted(money):
        for price in range(coin, n+1):
            dp[price] = (dp[price] + dp[price - coin]) % DIV

    return dp[n]