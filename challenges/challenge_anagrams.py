def partition(array, low, high):
    pivot = array[high]
    j = low - 1
    for i in range(low, high):
        if array[i] <= pivot:
            j = j + 1
            (array[j], array[i]) = (array[i], array[j])
    (array[j + 1], array[high]) = (array[high], array[j + 1])
    return j + 1


def quick_sort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quick_sort(array, low, pi - 1)
        quick_sort(array, pi + 1, high)
    return array


def is_anagram(first_string, second_string):
    first_word = list(first_string.lower())
    second_word = list(second_string.lower())

    first_sorted = quick_sort(first_word, 0, len(first_word) - 1)
    second_sorted = quick_sort(second_word, 0, len(second_word) - 1)

    if first_string == "" or second_string == "":
        return ("".join(first_sorted), "".join(second_sorted), False)
    return (
        "".join(first_sorted),
        "".join(second_sorted), first_sorted == second_sorted)

# inspirado em https://www.geeksforgeeks.org/python-program-for-quicksort/
# #:~:text=The%20key%20process%20in%20quickSort,greater%20than%20x)%20after%20x.
