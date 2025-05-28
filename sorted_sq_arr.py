def sorted_sq_arr(arr)->list[int]:
    n = len(arr)
    i: int = 0
    j: int = n - 1

    res: list[int] = [0]*n

    for k in reversed(range(n)):
        if arr[i]**2 > arr[j]**2:
            res[k] = arr[i]**2
            i += 1
        else:
            res[k] = arr[j]**2
            j -= 1
    
    return res

def main()->None:
    arr: list[int] = list(map(int, input("Enter the array: ").split()))
    print(f'Sorted and Squared array: {sorted_sq_arr(arr)}')

if __name__ == "__main__":
    main()