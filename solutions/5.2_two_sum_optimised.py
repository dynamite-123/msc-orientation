def solve(numbers: list[int], target: int) -> list:
    # write your logic here and return the indices of the two numbers
    # format: [index1, index2] where index1 < index2
    res = [-1, -1]
    cache = {}
    for i in range(len(numbers)):
        req = target - numbers[i]
        if req in cache:
            res[0] = cache[req]
            res[1] = i
            return res
        else:
            cache[numbers[i]] = i
    return res


n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
result = solve(numbers, target)
print(result[0], result[1])
