# 빠른 모듈러 거듭제곱법 : https://ko.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation
# finding a^b^c^... mod m : https://stackoverflow.com/questions/4223313/finding-abc-mod-m
import sys

a, b, c, p = map(int, sys.stdin.readline().split())

def binary(n):

    binary_list = list()
    while n != 1:
        binary_list.append(n%2)
        n //= 2

    binary_list.append(1)

    return binary_list

c_binary = binary(c)
b_sqrt_mod = [b % (p-1)]

for i in range(1, len(c_binary)):
    b_sqrt_mod.append((b_sqrt_mod[i-1]**2)%(p-1))

b_sqrt_c_mod = 1

for i in range(len(c_binary)):
    if c_binary[i] == 1:
        b_sqrt_c_mod *= b_sqrt_mod[i]
b_sqrt_c_mod %= p-1

# repeat
x_binary = binary(b_sqrt_c_mod)
a_sqrt_mod = [a % p]

for i in range(1, len(x_binary)):
    a_sqrt_mod.append((a_sqrt_mod[i-1]**2)%p)

answer = 1

for i in range(len(x_binary)):
    if x_binary[i] == 1:
        answer *= a_sqrt_mod[i]

answer %= p
print(answer)