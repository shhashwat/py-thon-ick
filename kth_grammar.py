def kthGrammar(n: int, k: int) -> int:
        if n == 1: return 0
        m: int = 2**(n - 2)
        if k <= m: return kthGrammar(n-1,k)
        else: return 1 - kthGrammar(n-1,k-m)

def main()->None:
    n: int = int(input("Enter the number of rows: "))
    k: int = int(input("Enter the kth element: "))
    
    print(kthGrammar(n,k))

if __name__ == "__main__":
      main()