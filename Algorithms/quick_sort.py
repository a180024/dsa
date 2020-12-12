def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[j], array[i] = array[i], array[j]

    array[high], array[i + 1] = array[i + 1], array[high]
    return i + 1


def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)


if __name__ == "__main__":
    data = [8, 7, 2, 1, 0, 9, 6]
    size = len(data)
    quickSort(data, 0, size - 1)
    print("Sorted Array in Ascending Order:")
    print(data)
