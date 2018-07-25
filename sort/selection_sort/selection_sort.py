"""
selection sort
"""

def selection_sort(data):
    """data is a list
    """
    if not data:
        return data
    i = 0
    while i < len(data) - 1:
        j = i + 1
        while j < len(data) - 1:
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
            j += 1
        i += 1
    return data


if __name__ == "__main__":

    data = [5, 7, 2, 4, 1, 8]
    print(selection_sort(data))
