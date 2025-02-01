"""
Explanation of the Code:

1.Initialization:
a.left points to the beginning of the array.
b.right points to the end of the array.

2.Binary Search Loop:
a.Calculate the middle index, mid.
b.Compare arr[mid] with arr[right]:
--If arr[mid] > arr[right], move left to mid + 1 (pivot is in the right half).
--Otherwise, move right to mid (pivot is in the left half).

3.Final Result:
The left index points to the smallest element, which gives the rotation count 𝑘.

4.Time Complexity
Binary Search:(log𝑛)
Space Complexity:O(1)

"""













def find_rotation_k(arr):
    """
    Finds the number of rotations (k) in a rotated sorted array.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # If mid element is greater than the rightmost element, pivot is on the right side
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            # Pivot is on the left side (including mid)
            right = mid

    # `left` is now the index of the smallest element, which is also the rotation count (k)
    return left


# Test example
A = [15, 18, 2, 3, 6, 12]
k = find_rotation_k(A)
print(f"The array was rotated {k} times.")
