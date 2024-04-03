def bubble_sort_2d(arr):
    n = len(arr)     # Number of rows in 2d arrays
    m = len(arr[0])  # Number of columns in the 2d array: assumes allmrows have equal length
    total_elements = n * m   # Total numbers of elments in the 2d array

    for i in range(total_elements - 1):
        # outer loop: goes through all the elements in 2d array

        for j in range(total_elements - 1 - i):
            # Inner loop: goes through the elements, treeducing the comparison range each time

            # Calculate currnt position in 2d terms
            row1 = j // m
            col1 = j %  m 

            # Calculate next position (right next to current position)
            row2 = (j + 1) // m
            col2 = (j + 1) %  m

            # Compare and possibly swap elements
            if arr[row1][col1] > arr[row2][col2]:
                # If the current element is greater than the next, swap them
                arr[row1][col1], arr[row2][col2] = [row2][col2], [row1][col1]

def search_elements(arr, elements):
    found = False  # Initialize a flag to track if the elements is found
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == elements:
                print(f"Element found at position: row = {i}, column = {j}")
                found = True
                return  # Exit the function after finding the element
    if not found:
        print("Element not found in the given array.")

# Example usage:
arr = [
    [9, 2, 3],
    [4, 5, 6],
    [7, 8, 1]
]

print(arr)
bubble_sort_2d(arr)
print(arr)

# Searching for the element
search = int(input("Enter the element you want to search: "))
search_elements(arr, search)