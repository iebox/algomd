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

def show_title(header, i, info):
    print('=====================================================')
    print(f'{header} {i}:  {info}')
    print('=====================================================')


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

    # show progress during the 1st patition calling only
    log = True 

    for i in range(low, high):
        if high - low != len(a) - 1:
            log = False

        if log:
            show_title('Before Round', i, show_progress(a, first_high, i))
            print(f' i = {i}, first_high = {first_high}')

        if a[i] < p_value:
            if log:
                print(f' a[{i}] = {a[i]} < {p_value}, swaping [a[i]:{a[i]} <-> a[first_high]:{a[first_high]}]')
                # print(' a[{0}] = {1} {2}'.format(i, a[i], a))

            a[i], a[first_high] = a[first_high], a[i]
            first_high += 1

        if log:
            print('\n updating index...\n')
            print(f' i = {i}, first_high = {first_high}')
            print(f' a[i] = {a[i]}, a[first_high] = {a[first_high]}')
            show_title('After Round', i, show_progress(a, first_high, i))


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


