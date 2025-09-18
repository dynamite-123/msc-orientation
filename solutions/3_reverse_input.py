def solve(text: str) -> str:
    # write your logic here and return the reversed string
    res = ""
    N = len(text)
    for i in range(N - 1, -1, -1):
        res += text[i]
    return res


text = input()
print(solve(text))
