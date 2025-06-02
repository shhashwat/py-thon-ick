# def findTheWinner(n: int, k: int) -> int:
#         def josephus(n: int)->int:
#             if n == 1: return 0
#             return (josephus(n-1) + k)%n
#         return josephus(n) + 1

def findTheWinner(n: int, k:int)->int:
      s: int = 0
      for i in range(2, n+1):
            s = (s+k)%i
      return s + 1

def main()->None:
      n: int = int(input("Enter the size of the circle: "))
      k: int = int(input("Enter the counting number: "))

      print(f"The safe position is: {findTheWinner(n,k)}")

if __name__ == "__main__":
      main()