def find_index(array):
    if not array:
        raise ValueError('Data is empty')
    if not isinstance(array, list):
        array = list(map(int, array))
    if array[-1] != 0 or array[0] != 1:
        raise ValueError('Data is not correct')
    mid = len(array) // 2
    if array[mid] == 1:
        if array[mid + 1] == 0:
            return mid + 1
        return mid + find_index(array[mid:])
    else:
        if array[mid - 1] == 1:
            return mid
        return find_index(array[:mid])


def is_cross(x1, y1, x2, y2, x3, y3, x4, y4):
    min_1x = min(x1, x2)
    max_1x = max(x1, x2)
    min_1y = min(y1, y2)
    max_1y = max(y1, y2)

    min_2x = min(x3, x4)
    max_2x = max(x3, x4)
    min_2y = min(y3, y4)
    max_2y = max(y3, y4)

    x_1 = max(min_1x, min_2x)
    x_2 = min(max_1x, max_2x)
    y_1 = max(min_1y, min_2y)
    y_2 = min(max_1y, max_2y)

    if x_2 - x_1 < 0 or y_2 - y_1 < 0:
        return False

    else:
        area = abs(y_2 - y_1) * abs(x_2 - x_1)
        return area


if __name__ == '__main__':
    print(is_cross(1, 1, 2, 2, 3, 3, 4, 4))
    print(is_cross(-3, -3, -1, -1, -2, -2, 2, 1))
    print(is_cross(-3, -2, 2, 1, -4, -4, 3, -1))
    print(is_cross(-2, -2, 2, 2, -1, -1, 1, 1))

