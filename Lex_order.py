def lex_insert(L, a, b):
    index = 0
    while index < len(L) and L[index] < (a, b):
        index += 1
    L.insert(index, (a, b))
    return L


def lex_insertion_sort(pairs):
    L = []
    for (a, b) in pairs:
        lex_insert(L, a, b)
    return L


if __name__ == "__main__":
    L = []
    lex_insert(L, 3, 1)
    lex_insert(L, 1, 10)
    lex_insert(L, 8, 11)
    lex_insert(L, 2, 5)
    lex_insert(L, 8, 9)

    print(L)
    # Expected order (ascending):
    # (1, 10), (2, 5), (3, 1), (8, 9), (8, 11)