# Code borrowed from the internet for testing/learning purposes.
    #BUGS IN THE CODE
def partition(alist, first, last):
    pivot = alist[first]
    lMarker = first + 1
    rMarker = last
    done = False
    while not done:
        while lMarker <= rMarker and alist[lMarker] <= pivot:    #Moves the marker until it finds something out of place relative to the pivot.
            lMarker += 1

        while alist[rMarker] >= pivot and rMarker >= lMarker:    #Same as above.
            rMarker = rMarker - 1

        if rMarker < lMarker:   #Pretty much marks the sort relative to that pivot point as done.
            done = True
        else:                   #Flips the two values to be ordered.
            print("ALIST")
            print(alist)
            print("LMARKER")
            print(lMarker)
            temp = alist[lMarker]
            alist[lMarker] = alist[rMarker]
            alist[rMarker] = temp

    temp = alist[lMarker]
    alist[lMarker] = alist[rMarker]
    alist[rMarker] = temp

    return rMarker

def quickSortHelper(alist, first, last):
    if first < last:
        splitPoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitPoint - 1)
        quickSortHelper(alist, splitPoint + 1, last)

def quicksort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
    return alist

