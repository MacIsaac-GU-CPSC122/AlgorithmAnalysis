def swap(arr: list, i:int, j:int) -> None:
    """ Takes and array and swaps the 
        values at index i and j
    """
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selection_sort(values: list[int]) -> None:
    counts = {
            "data_comparisons": 0,
            "loop_comparisons": 0,
            "data_assignments": 0,
            "loop_assignments": 0,
            "other": 0 
            }

    
    i = 0
    counts["loop_assignments"] += 1
    while i < len(values) - 1:
        counts["loop_comparisons"] += 1
        # min_index stores the location of the smallest value found so far.
        min_index = i
        counts["data_assignments"] += 1

        j = i + 1
        counts["loop_assignments"] += 1
        while j < len(values):
            counts["loop_comparisons"] += 1

            
            if values[j] < values[min_index]:
                # Update min_index.
                min_index = j
                pass
            j += 1
        
        # keep tracks of the last while loop comparison
        # which causes us to exit the while loop
        counts["loop_comparisons"] += 1
 
        # if current i is the minimum value, do nothing
        # if not, swap items i and min_index
        # count the operations it takes to do these
        swap(values, i, min_index)

        print(f"{i}: {values} ")
        i += 1
        
    # keep track of the last while loop comparison
    # which causes us to exit the while loop
    counts["loop_comparisons"] += 1

    return counts



def main():
    l = [1,8,5,2,4,9,0]
    counts = selection_sort(l)
    print(l)
    print(counts)

if __name__=="__main__":
    main()