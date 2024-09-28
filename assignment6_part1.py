import math

def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    i = low
    for j in range(low, high):
        if arr[j] < pivot_value:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def median_of_medians(arr, low, high):
    if high - low + 1 <= 5:
        return sorted(arr[low:high + 1])[len(arr[low:high + 1]) // 2]

    medians = []
    for i in range(low, high + 1, 5):
        group = sorted(arr[i:min(i + 5, high + 1)])
        medians.append(group[len(group) // 2])

    return median_of_medians(medians, 0, len(medians) - 1)

def deterministic_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot = median_of_medians(arr, low, high)
    pivot_index = partition(arr, low, high, arr.index(pivot))

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return deterministic_select(arr, low, pivot_index - 1, k)
    else:
        return deterministic_select(arr, pivot_index + 1, high, k)

# Function to select the k-th smallest element (0-indexed)
def kth_smallest_deterministic(arr, k):
    return deterministic_select(arr, 0, len(arr) - 1, k)

import random

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[high], arr[pivot_index] = arr[pivot_index], arr[high]
    return partition(arr, low, high, high)

def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]

    pivot_index = randomized_partition(arr, low, high)

    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k)

# Function to select the k-th smallest element (0-indexed)
def kth_smallest_randomized(arr, k):
    return randomized_select(arr, 0, len(arr) - 1, k)


if __name__ == "__main__":
    arr = [12, 3, 5, 7, 19, 26, 13, 9]
    k = 3  # Looking for the 4th smallest element (0-indexed)

    print(f"The {k + 1}-th smallest element (Deterministic): {kth_smallest_deterministic(arr.copy(), k)}")
    print(f"The {k + 1}-th smallest element (Randomized): {kth_smallest_randomized(arr.copy(), k)}")
