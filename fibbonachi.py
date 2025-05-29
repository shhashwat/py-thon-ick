def fib(n)->int:
    if n <= 1: return n
    return fib(n-1) + fib(n-2)

def main()->None:
    n: int = int(input("Enter the number: "))
    for i in range(n):
        print(fib(i), end=' ')

if __name__ == "__main__":
    main()