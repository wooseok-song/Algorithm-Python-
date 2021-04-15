import heapq

array = [3, 4, 5, 5, 3, 1, 2, 3, 1, 4]


# ctrl alt l reformat

def bubblesort(a):
    n = len(a)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]


def insertionsort(a):
    n = len(a)
    for i in range(1, n):
        x = a[i]
        j = i - 1
        while j > 0 and a[j] > x:
            a[j + 1] = a[j]
            j -= 1

        a[j + 1] = x


def


print(array)
