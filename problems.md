# Python Basics – Practice Problems

This file contains 5 beginner-friendly Python problems designed to practice:
- Loops  
- Conditionals  
- Lists  
- Dictionaries  
- Strings  
- Primary data types  

---

## 1. Even or Odd
Write a program that takes an integer as input and prints `"Even"` if the number is even, and `"Odd"` if the number is odd.

### Boiler Plate
``` python
def solve(x: int) -> None:
    # write your logic here and print 'Even' or 'Odd'

num = int(input())
solve(num)
```
#### Sample Input
```
7
```

#### Sample Output
```
Odd
```

#### Sample Input
```
10
```

#### Sample Output
```
Even
```

---

## 2. Maximum in a List
Write a program that takes a list of integers and finds the maximum value in the list.

### Boiler Plate
``` python
def solve(numbers: list[int]) -> int:
    # write your logic here and return the maximum number

n = int(input())
numbers = list(map(int, input().split()))
print(solve(numbers))
```

#### Sample Input
```
5
3 8 1 9 2
```

#### Sample Output
```
9
```

#### Sample Input
```
4
-5 -2 -8 -1
```

#### Sample Output
```
-1
```

---

## 3. Reverse Input
Write a program that takes a string as input and prints the string in reverse order.

### Boiler Plate
``` python
def solve(text: str) -> str:
    # write your logic here and return the reversed string

text = input()
print(solve(text))
```

#### Sample Input
```
hello
```

#### Sample Output
```
olleh
```

#### Sample Input
```
Python
```

#### Sample Output
```
nohtyP
```

---

## 4. Character Frequency Counter
Write a program that takes a string as input and counts the frequency of each character, then prints the character and its count.

### Boiler Plate
``` python
def solve(text: str) -> None:
    # write your logic here and print character frequencies
    # format: "character: count" for each character in alphabetical order

text = input()
solve(text)
```

#### Sample Input
```
hello
```

#### Sample Output
```
e: 1
h: 1
l: 2
o: 1
```

#### Sample Input
```
programming
```

#### Sample Output
```
a: 1
g: 2
i: 1
m: 2
n: 1
o: 1
p: 1
r: 2
```

---

## 5. Two Sum Problem
Write a program that takes an array of integers and a target sum, then finds two numbers in the array that add up to the target. Print the indices of these two numbers (0-indexed).

### Boiler Plate
``` python
def solve(numbers: list[int], target: int) -> list:
    # write your logic here and return the indices of the two numbers
    # format: [index1, index2] where index1 < index2

n = int(input())
numbers = list(map(int, input().split()))
target = int(input())
result = solve(numbers, target)
print(result[0], result[1])
```

#### Sample Input
```
4
2 7 11 15
9
```

#### Sample Output
```
0 1
```

#### Sample Input
```
3
3 2 4
6
```

#### Sample Output
```
1 2
```
