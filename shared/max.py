
# O(n)
def max(items):
    max_item = items[0]
    for item in items:
        if item > max_item:
            max_item = item
    return max_item
