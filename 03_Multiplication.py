# Perform simple binary multiplication of two numbers
def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def xor_gate(a, b):
    return a ^ b

def not_gate(a):
    return not a

def full_adder(a, b, c):
    sum = xor_gate(xor_gate(a, b), c)
    carry = or_gate(and_gate(a, b), and_gate(c, xor_gate(a, b)))
    return sum, carry

def binary_addition(A, B):
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    Cin = 0
    S = []
    for i in range(max_len-1, -1, -1):
        sum, Cin = full_adder(A[i], B[i], Cin)
        S.insert(0, sum)
    if Cin == 1:
        S.insert(0, 1)
    return S

def shift_left(A):
    return A[1:] + [0]

def multiplication(A, B):
    bit = len(A)
    A = [0] * bit + A
    B = [0] * bit + B
    M = [0] * (2 * bit)
    B=B[::-1]
    for i in range(bit):
        if B[i] == 1:
            M = binary_addition(M, A)
        if i<bit-1:
            A = shift_left(A)
    return M

def take_input():
    num1 = input("Enter multiplicand in binary number: ")
    num2 = input("Enter multiplier in binary number: ")
    A = [int(x) for x in num1]
    B = [int(x) for x in num2]
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    return A, B

multiplicand,multiplier=take_input()
print(multiplicand,multiplier)
result=multiplication(multiplicand,multiplier)
print("Product:", ''.join(map(str, result)))