def solve(numbers: list[int], target: int) -> list:
    # write your logic here and return the indices of the two numbers
    # format: [index1, index2] where index1 < index2
    N = len(numbers)
    res = [-1, -1]
    for i in range(N - 1):
        for j in range(i + 1, N):
            if numbers[i] + numbers[j] == target:
                res[0] = i
                res[1] = j
                return res
    return res


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
result = solve(numbers, target)
print(result[0], result[1])
