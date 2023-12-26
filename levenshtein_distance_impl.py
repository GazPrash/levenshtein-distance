# source, destination --> Lower the score --> better
def levenshtein_func(s1, s2):
    cache = [([None] * (len(s2) + 1)) for _ in range(len(s1) + 1)]
    return levenshtein_impl(s1, s2, len(s1), len(s2), cache)


# wrapper for levenshtein_func
def levenshtein_impl(str1: str, str2: str, n1, n2, cache) -> int:
    if cache[n1][n2] is not None:
        return cache[n1][n2]
    if n1 == 0:
        cache[n1][n2] = n2
        return cache[n1][n2]
    if n2 == 0:
        cache[n1][n2] = n1
        return cache[n1][n2]
    if str1 == str2:
        cache[n1][n2] = 0
        return cache[n1][n2]
    if str1[0] == str2[0]:
        cache[n1][n2] = levenshtein_impl(str1, str2, n1 - 1, n2 - 1, cache)
        return cache[n1][n2]
    cache[n1][n2] = 1 + min(
        levenshtein_impl(str1, str2, n1 - 1, n2, cache),
        levenshtein_impl(str1, str2, n1, n2 - 1, cache),
        levenshtein_impl(str1, str2, n1 - 1, n2 - 1, cache),
    )
    return cache[n1][n2]


def main():
    s1 = "stage"
    s2 = "fasdkhhasdhjashdhadsaklsdja"
    s3 = "stash"
    s4 = "cache"
    other_s = [s2, s3, s4]
    for s in other_s:
        print(s1, s)
        print(levenshtein_func(s1, s))


if __name__ == "__main__":
    main()
