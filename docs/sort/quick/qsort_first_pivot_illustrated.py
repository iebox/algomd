def show_progress(a, l, r, crossed):
    offside = 2
    if crossed:
        # no r is on the left, need to go over l
        offside = 0

    progress = a[:]
    progress.insert(l, '{')
    progress.insert(l + 2, '}')

    progress.insert(r + offside, '(')
    progress.insert(r + offside + 2, ')')

    str_a = map(lambda x: str(x), progress)
    info = ' '.join(list(str_a))
    return info


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
            print('\n=== not cross, swapping {l} and (r) ===\n', show_progress(a, l, r, False))
            a[l], a[r] = a[r], a[l]
            print('\n=== swapped and continue loop ===\n', show_progress(a, l, r, False))
        else:
            # cross!
            print('\n=== crossed, get pivot (r) ===\n', show_progress(a, l, r, True))
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


