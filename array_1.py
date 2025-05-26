x :list[int] = list(map(int, input("Enter numbers separated by spaces: ").split()))

y: int = int(input("Enter a number to add to the array: "))

print("Do you want to add a number to the array? (yes/no)")

def add_to_array(arr: list[int], value: int) -> list[int]:
    print("Adding value to the array...")
    arr.append(value)
    return arr

if input().strip().lower() == 'yes':
    x = add_to_array(x, y)
    print(f"Updated array: {x}")
else:
    pass

def sort_array(arr: list[int]) -> list[int]:
    print("Sorting the array...")
    return sorted(arr)

def reverse_array(arr: list[int]) -> list[int]:
    print("Reversing the array...")
    return arr[::-1]

def find_max(arr: list[int]) -> int:
    print("Finding the maximum value in the array...")
    return max(arr)

def find_min(arr: list[int]) -> int:
    print("Finding the minimum value in the array...")
    return min(arr)

print("Select operation:")
print("1. Sort")
print("2. Reverse")
print("3. Max")
print("4. Min")

choice: int = input("Enter choice (1/2/3/4): ") 

if choice == 1:
    print(f"Sorted array: {sort_array(x)}")
elif choice == 2:
    print(f"Reversed array: {reverse_array(x)}")
elif choice == 3:
    print(f"Maximum value: {find_max(x)}")
elif choice == 4:
    print(f"Minimum value: {find_min(x)}")
else:
    print("Invalid input. Please enter a valid choice (1/2/3/4).")