def some_alg(elements):
    res = 0
    for element in elements:
        res += element
    for element in elements:
        res *= element
    return res