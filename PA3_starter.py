def swap(arr, i, j) -> None:
    """ Takes and array and swaps the 
        values at index i and j
    """
    pass

def selection_sort(values) -> None:
    counts = {
            "data_comparisons": 0,
            "loop_comparisons": 0,
            "data_assignments": 0,
            "loop_assignments": 0,
            "other": 0 
            }
    i = 0

    while i < len(values) - 1:
        # min_index stores the location of the smallest value found so far.
        min_index = i

        j = i + 1

        while j < len(values):
            if values[j] < values[min_index]:
                # TODO: Update min_index.
                pass
            j += 1

        # TODO:
        # if current i is the minimum value, do nothing
        # if not, swap items i and min_index
        # count the operations it takes to do these
        
        i += 1
    
    return counts



def main():
    l = [1,8,5,2,4,9,0]
    counts = selection_sort(l)
    print(l)
    print(counts)

if __name__=="__main__":
    main()