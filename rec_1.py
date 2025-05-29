def rec(n: int)->None:
    if n == 0: return
    print(n, end=' ')
    rec(n-1)
    print(n, end=' ')

def main()->None:
    n: int = int(input())
    rec(n)

if __name__ == "__main__":
    main()