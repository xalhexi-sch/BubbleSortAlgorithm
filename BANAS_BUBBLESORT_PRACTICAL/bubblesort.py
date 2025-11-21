import time

def read_file(path):
    with open(path, "r") as f:
        data = f.read().strip().split()
        return list(map(int, data))

def bubble_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
                swapped = True

        if not swapped:
            break

    return arr, comparisons, swaps

def run_bubble_sort(filename):
    try:
        data = read_file(filename)
    except FileNotFoundError:
        print("File not found:", filename) 
        return

    start = time.time()
    sorted_data, comparisons, swaps = bubble_sort(data)
    end = time.time()

    elapsed_ms = round((end - start) * 1000, 3)

    print(f"ALGORITHM: Bubble Sort")
    print(f"FILE: {filename}")
    print(f"STATUS: {'Success/Sorted' if sorted_data == sorted(data) else 'Failed'}")
    print("PERFORMANCE METRICS:")
    print("--------------------")
    print(f"Time Elapsed: {elapsed_ms} ms")
    print(f"Comparisons: {comparisons}")
    print(f"Swaps/Operations: {swaps}")
    print("")


if __name__ == "__main__":
    files = ["data_small.txt", "data_reverse.txt", "data_large.txt"]

    for filename in files:
        run_bubble_sort(filename)
