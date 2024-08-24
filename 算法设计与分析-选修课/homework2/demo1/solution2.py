if __name__ == '__main__':
    print("hello world")


def solution2(n, r):
    dp = [[999] * (n - 1) for i in range(n)]  # 999只是代表一个很大的数字
    for i in range(n):
        dp[i][i] = 0  # 给出发地和终止地一致的地方赋值为0
    for r in range(0, n):
        for i in range(n - r - 1):
            j = i + r - 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][k] + dp[k][j] + r[i][j])
    return dp[0][n - 1]
