# 22-09-2026

## TASK - Python 

```python
'''Write a program which can compute the factorial of a given numbers.Theresults should be printed in a comma-separated sequence on a singleline.Suppose the following input is supplied to the program:8
Then, the output should be:40320'''

n = int(input())

fact = 1;

for i in range(1,n+1):
  fact = fact*i;
print(fact)


-----


'''Write a Python program which accepts a sequence of comma separated 4 digit
binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated
sequence.
Example:
0100,0011,1010,1001
0100,0011-1010/1001_1111
Then the output should be:
1010'''

import re

a = re.split(r'[_/, -]+', input())

res = []

for n in a:
    n = n.strip()
    if int(n, 2) % 5 == 0:
        res.append(n)

print(",".join(res))

---

'''Write a Python program that accepts a sentence and calculate the number of
letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3'''

s = input()

let = 0;
dig = 0;

for n in s:
  if n.isalpha():
    let+=1
  elif n.isdigit():
    dig+=1

print("LETTERS",let)
print("DIGITS",dig)
```
