'''
a = [4 3 8 2 7 5 1 6]
4 3 8 2 7 5 1 [6]
choice first_high and i

{first_high} =>
(i) =>
({4}) 3 8 2 7 5 1 [6]
4 3 {8} (2) 7 5 1 [6]   2 < [6]
4 3 (2) {8} 7 5 1 [6]
4 3 2 {8} 7 (5) 1 [6]   5 < [6] swap with first_high 
4 3 2 {5} 7 (8) 1 [6]   5 < [6] swap with first_high 
4 3 2 5 {7} 8 (1) [6]   first_high += 1, i += 1
4 3 2 5 {7} 8 (1) [6]   1 < [6] swap with first_high
4 3 2 5 1 {8} 7 [6]   first_high += 1, no more i, loop end

finally swap pivot with first_high
4 3 2 5 1 {6} 7 [8] 

part result:
4 3 2 5 1 <6< 7 [8] 

'''

def show_progress(a, first_high, i):
    progress = a[:]
    progress.insert(first_high, '{')
    progress.insert(i + 2, '}')

    str_a = map(lambda x: str(x), progress)
    info = ' '.join(list(str_a))
    return info

def part(a, low, high):
    p_value = a[high]

    first_high = low
    for i in range(low, high):
        if a[i] < p_value:
            a[i], a[first_high] = a[first_high], a[i]
            first_high += 1

        if high - low == len(a) - 1:
            print('\n======== progress i = {0} ========\n a[{0}] = {1} [{2}]'.format(i, a[i], show_progress(a, first_high, i)))


    a[first_high], a[high] = a[high], a[first_high]
    return first_high


def quick_sort(a, l, r):
    if l < r:
        p = part(a, l, r)
        # print('part', a)

        quick_sort(a, l, p - 1)
        quick_sort(a, p + 1, r)


a = [4, 3, 8, 2, 7, 5, 1, 6]
print('before', a)
quick_sort(a, 0, len(a) - 1)
print('after', a)


