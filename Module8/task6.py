# Быстрая сортировка
def partition(lst):
    pivot = lst[-1]
    less = []
    equal = []
    greater = []
    for x in lst:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return less, equal, greater

def quicksort(lst, start, end):
    if end - start <= 0:
        return lst
    less, equal, greater = partition(lst[start:end + 1])
    pivot_index = start + len(less)
    quicksort(lst, start, pivot_index - 1)
    quicksort(lst, pivot_index + len(equal), end)
    lst[start:end + 1] = less + equal + greater
    return lst

nums = [5, 8, 9, 4, 2, 9, 1, 8]
sorted_nums = quicksort(nums, 0, len(nums) - 1)
print(sorted_nums)