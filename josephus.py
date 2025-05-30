def findTheWinner(n: int, k: int) -> int:
        def josephus(n: int)->int:
            if n == 1: return 0
            return (josephus(n-1) + k)%n
        return josephus(n) + 1

def main()->None:
      n: int = int(input())
      k: int = int(input())

      print(findTheWinner(n,k))

if __name__ == "__main__":
      main()