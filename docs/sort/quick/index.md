# Quick Sort Two Way Solution



## Solution 1: Take the Last Number as Pivot

### Logic Design
--- 

!!! abstract "Design"

    ``` python
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
    4 3 2 5 1 {8} 7 [6]     first_high += 1, no more i, loop end

    finally swap pivot with first_high
    4 3 2 5 1 {6} 7 [8] 

    part result:
    4 3 2 5 1 <6< 7 [8] 
    ```


### Implementation 
---

!!! Example "Take the Last Number as Pivot"

    ```python linenums="1"
    def part(a, low, high):
        p_value = a[high]
        first_high = low

        for i in range(low, high):
            if a[i] < p_value:
                a[i], a[first_high] = a[first_high], a[i]
                first_high += 1

        a[first_high], a[high] = a[high], a[first_high]
        return first_high

    def quick_sort(a, l, r):
        if l < r:
            p = part(a, l, r)

            quick_sort(a, l, p - 1)
            quick_sort(a, p + 1, r)


    a = [4, 3, 8, 2, 7, 5, 1, 6]
    print('before', a)
    quick_sort(a, 0, len(a) - 1)
    print('after', a)

    ```


### Trace Study
---

!!! Example "Last Number as Pivot"

    ```python tab="Output" linenums = "1"
    before [4, 3, 8, 2, 7, 5, 1, 6]
    =====================================================
    Before Round 0:  { 4 } 3 8 2 7 5 1 6
    =====================================================
     i = 0, first_high = 0
     a[0] = 4 < 6, swaping [a[i]:4 <-> a[first_high]:4]

     updating index...

     i = 0, first_high = 1
     a[i] = 4, a[first_high] = 3
    =====================================================
    After Round 0:  4 { } 3 8 2 7 5 1 6
    =====================================================
    =====================================================
    Before Round 1:  4 { 3 } 8 2 7 5 1 6
    =====================================================
     i = 1, first_high = 1
     a[1] = 3 < 6, swaping [a[i]:3 <-> a[first_high]:3]

     updating index...

     i = 1, first_high = 2
     a[i] = 3, a[first_high] = 8
    =====================================================
    After Round 1:  4 3 { } 8 2 7 5 1 6
    =====================================================
    =====================================================
    Before Round 2:  4 3 { 8 } 2 7 5 1 6
    =====================================================
     i = 2, first_high = 2

     updating index...

     i = 2, first_high = 2
     a[i] = 8, a[first_high] = 8
    =====================================================
    After Round 2:  4 3 { 8 } 2 7 5 1 6
    =====================================================
    =====================================================
    Before Round 3:  4 3 { 8 2 } 7 5 1 6
    =====================================================
     i = 3, first_high = 2
     a[3] = 2 < 6, swaping [a[i]:2 <-> a[first_high]:8]

     updating index...

     i = 3, first_high = 3
     a[i] = 8, a[first_high] = 8
    =====================================================
    After Round 3:  4 3 2 { 8 } 7 5 1 6
    =====================================================
    =====================================================
    Before Round 4:  4 3 2 { 8 7 } 5 1 6
    =====================================================
     i = 4, first_high = 3

     updating index...

     i = 4, first_high = 3
     a[i] = 7, a[first_high] = 8
    =====================================================
    After Round 4:  4 3 2 { 8 7 } 5 1 6
    =====================================================
    =====================================================
    Before Round 5:  4 3 2 { 8 7 5 } 1 6
    =====================================================
     i = 5, first_high = 3
     a[5] = 5 < 6, swaping [a[i]:5 <-> a[first_high]:8]

     updating index...

     i = 5, first_high = 4
     a[i] = 8, a[first_high] = 7
    =====================================================
    After Round 5:  4 3 2 5 { 7 8 } 1 6
    =====================================================
    =====================================================
    Before Round 6:  4 3 2 5 { 7 8 1 } 6
    =====================================================
     i = 6, first_high = 4
     a[6] = 1 < 6, swaping [a[i]:1 <-> a[first_high]:7]

     updating index...

     i = 6, first_high = 5
     a[i] = 7, a[first_high] = 8
    =====================================================
    After Round 6:  4 3 2 5 1 { 8 7 } 6
    =====================================================
    after [1, 2, 3, 4, 5, 6, 7, 8]
    [Finished in 0.1s]
    ```


    ```python tab="full trace source" linenums="1"

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
    ```


## Solution 2: Take the First Number as Pivot

### Logic Design
---

!!! abstract "Design"

    ``` python
    a = [5] 3 4 7 1 2 6 7 9 8

    {l} =>        <=  (r)
    # if l < r: no cross
    [5] 3 4 {7} 1 (2) 6 7 9 8

    # swap
    [5] 3 4 {2} 1 (7) 6 7 9 8

    # and proceed 
    #      {l}=> <={r}
    [5] 3 4 (2) 1 {7} 6 7 9 8

    # l > r, crossed
    [5] 3 4 2 (1) {7} 6 7 9 8

    # swap r with pivotal
    [1] 3 4 2 (1) {7} 6 7 9 8
    ```

### Implementation
---

!!! Example "First Number as Pivot - Implementation"

    ```python linenums="1"
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

    ```



### Trace Study
---

!!! Example "First Number as Pivot - Trace Table"

    ```python tab="Output" linenums = "1"

    before [5, 3, 4, 7, 1, 2, 6, 7, 9, 8]

    === not cross, swapping {l} and (r) ===
     5 3 4 { 7 } 1 ( 2 ) 6 7 9 8

    === swapped and continue loop ===
     5 3 4 { 2 } 1 ( 7 ) 6 7 9 8

    === crossed, get pivot (r) ===
     5 3 4 2 ( 1 ) { 7 } 6 7 9 8

    === crossed, get pivot (r) ===
     ( 1 ) { 3 } 4 2 5 7 6 7 9 8

    === not cross, swapping {l} and (r) ===
     1 3 { 4 } ( 2 ) 5 7 6 7 9 8

    === swapped and continue loop ===
     1 3 { 2 } ( 4 ) 5 7 6 7 9 8

    === crossed, get pivot (r) ===
     1 3 ( 2 ) { 4 } 5 7 6 7 9 8

    === crossed, get pivot (r) ===
     1 2 3 4 5 7 ( 6 ) 7 { 9 } 8

    === crossed, get pivot (r) ===
     1 2 3 4 5 6 7 ( 7 ) { 9 } 8

    === crossed, get pivot (r) ===
     1 2 3 4 5 6 7 7 9 ( { ) 8 }
    after [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
    [Finished in 0.1s]
    ```

    ```python tab="full trace source"
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


    ```
