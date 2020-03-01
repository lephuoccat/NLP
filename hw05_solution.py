def levenshtein_dp(a, b):
    m = len(a)
    n = len(b)
    dp_array = [[0 for i in range(n+1)] for j in range(m+1)]

    print(n)
    for i in range(n+1):
        dp_array[0][i] = i
        print(dp_array[0][i])

    for i in range(m+1):
        dp_array[i][0] = i

    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp_array[i][j] = min(
                dp_array[i-1][j] + 1, dp_array[i][j-1] + 1, dp_array[i-1][j-1] + cost)

    return dp_array[m][n]
