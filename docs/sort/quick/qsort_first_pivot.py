def part(a, low, high):
    p_value = a[low]

    l = low + 1
    r = high

    while True:
        while l < high:
            if a[l] > p_value:
                break
            l = l + 1

        while r > low:
            if a[r] < p_value:
                break
            r = r - 1

        if l < r:
            # no cross, swap
            a[l], a[r] = a[r], a[l]
        else:
            # cross!
            break

    a[low], a[r] = a[r], a[low]
    return r


def quick_sort(a, l, r):
    if l < r:
        p = part(a, l, r)
        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, r)


a = [5, 3, 4, 7, 1, 2, 6, 7, 9, 8]
print('before', a)
quick_sort(a, 0, len(a) - 1)
print('after', a)


