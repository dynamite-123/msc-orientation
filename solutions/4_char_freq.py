def solve(text: str) -> None:
    # write your logic here and print character frequencies
    # format: "character: count" for each character in alphabetical order
    freq = {}

    N = len(text)
    for i in range(N):
        if text[i] in freq:
            freq[text[i]] += 1
        else:
            freq[text[i]] = 1

    for c in freq:
        print(f"{c}: {freq[c]}")


text = input()
solve(text)
