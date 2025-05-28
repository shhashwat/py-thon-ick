# def monotonic_array(array)->bool:
#     n: int = len(array)
    
#     if n == 0:
#         return True
    
#     count: int = 0
#     duds: int = 0
    
#     for i in range(n - 1):
#         if array[i] > array[i+1]:
#             count += 1
#         elif array[i] == array[i+1]:
#             duds +=1
#         else:
#             count -= 1
    
#     count: int = abs(count) + duds
    
#     if count != n - 1:
#         return False
#     else:
#           return True

# !BETTER APPROACH
def monotonic_array(arr)->bool:    
    if len(arr) == 0:
        return True
    
    inc = dec = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            dec = False
        elif arr[i] < arr[i - 1]:
            inc = False
    
    return inc or dec


def main()->None:
    arr: list[int] = list(map(int, input("Enter your array here: ").split()))
    
    monotonic: bool = monotonic_array(arr)

    if monotonic:
        print('It is monotonic')
    else:
        print('It is not monotonic')

if __name__ == "__main__":
    main()