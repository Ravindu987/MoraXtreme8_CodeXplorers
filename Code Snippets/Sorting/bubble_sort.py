def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


if __name__ == "__main__":
    test = [43, 11, 9, 58, 6, 24, 89, 103, 1, 44, 32, 75, 124, 2, 66, 91]

    print(bubble_sort(test))
