def merge_sort(arr, step=0):
    if len(arr) > 1:
        mid = len(arr) // 2  # Finding the middle of the array
        left_half = arr[:mid]  # Dividing the array into two halves
        right_half = arr[mid:]

        print(f"Step {step}: Left half to be sorted: {left_half}")
        print(f"Step {step}: Right half to be sorted: {right_half}")

        # Sorting the first half
        merge_sort(left_half, step + 1)

        # Sorting the second half
        merge_sort(right_half, step + 1)

        i = j = k = 0

        # Merging the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        
        print(f"Step {step}: Merged array: {arr}")


# Input from the user
n = int(input("Enter the number of elements: "))
arr = []

for i in range(n):
    element = int(input(f"Enter element {i + 1}: "))
    arr.append(element)

print(f"Initial array: {arr}")
merge_sort(arr)

print(f"Sorted array: {arr}")
