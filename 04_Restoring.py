# Perform division for unsigned binary numbers using restoring method
def and_gate(a, b):
    return a and b

def or_gate(a, b):
    return a or b

def xor_gate(a, b):
    return a ^ b

def not_gate(a):
    return not a

def shift_left(A):
    return A[1:] + [0]

def full_adder(a, b, c):
    sum = xor_gate(xor_gate(a, b), c)
    carry = or_gate(and_gate(a, b), and_gate(c, xor_gate(a, b)))
    return sum, carry

def twos_complement(A):
    A = [not_gate(bit) for bit in A]
    A = binary_addition(A, [0] * (len(A) - 1) + [1])
    return A

def binary_addition(A, B):
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    Cin = 0
    S = []
    for i in range(max_len-1, -1, -1):
        sum, Cin = full_adder(A[i], B[i], Cin)
        S.insert(0, sum)
    return S

def restoring_division(Q,M):
    A=[0]*len(Q)
    Minus_M=twos_complement(M)
    for i in range(len(Q)):
        A=shift_left(A)
        A[-1]=Q[0]
        Q=shift_left(Q)
        A=binary_addition(A,Minus_M)
        if A[0]==1:
            A=binary_addition(A,M)
            Q[-1]=0
        else:
            Q[-1]=1
    return Q,A
    

def take_input():
    num1 = input("Enter dividend in binary number: ")
    num2 = input("Enter divisor in binary number: ")
    A = [int(x) for x in num1]
    B = [int(x) for x in num2]
    max_len = max(len(A), len(B))
    A = [0] * (max_len - len(A)) + A
    B = [0] * (max_len - len(B)) + B
    return A, B

dividend,divisor=take_input()
print(dividend,divisor)
quotient,remainder=restoring_division(dividend,divisor)
print(quotient,remainder)

