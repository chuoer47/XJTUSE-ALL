if __name__ == '__main__':
    print("hello world")


def solution(n, dp):
    for i in range(n - 2, 0):
        for j in range(0, i):
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1]) + dp[i][j]
    return dp[0][0]
