def binary_search(a_list, n):
    """
    Perform binary search on a sorted list.

    Parameters:
    a_list (list): A sorted list of elements
    n (int): The number to search for

    Returns:
    bool: True if found, False otherwise
    """
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid = (first + last) // 2

        if a_list[mid] == n:
            return True
        elif n < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1

    return False


#  Example usage
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11, 13]

    target = int(input("Enter number to search: "))

    if binary_search(numbers, target):
        print("Number found!")
    else:
        print("Number not found.")
