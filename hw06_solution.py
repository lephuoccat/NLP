
def suggest(word, dictionary):
    if word in dictionary:
        return word
    else:
        distances = {}
        for item in dictionary:
            distances[item] = levenshtein_dp(word, item)
        minimum = min(distances.values())
        print(minimum)
        return_list = []
        for item in dictionary:
            if distances[item] == minimum:
                return_list.append(item)
        return return_list


def levenshtein_dp(a, b):
    m = len(a)
    n = len(b)
    dp_array = [[0 for i in range(n+1)] for j in range(m+1)]

    for i in range(m+1):
        dp_array[i][0] = i

    for j in range(n+1):
        dp_array[0][j] = j

    for i in range(1, m+1):
        for j in range(1, n+1):
            cost = 0 if a[i-1] == b[j-1] else 1
            dp_array[i][j] = min(
                dp_array[i-1][j] + 1, dp_array[i][j-1] + 1, dp_array[i-1][j-1] + cost)

    return dp_array[m][n]
