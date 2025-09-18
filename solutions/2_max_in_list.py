def solve(numbers: list[int]) -> int:
    # write your logic here and return the maximum number
    N = len(numbers)
    mx = float("-inf")  # assign minimum value of an integer
    for i in range(0, N):
        if numbers[i] > mx:
            mx = numbers[i]
    return mx


n = int(input())
numbers = list(map(int, input().split()))
print(solve(numbers))
