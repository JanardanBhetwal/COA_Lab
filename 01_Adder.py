# Create addition using full adder that takes two inputs in binary and provides output in binary

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
    A=A[::-1]
    B=B[::-1]
    Cin=0
    S=[]
    for i in range(len(A)):
        sum, Cin = full_adder(A[i], B[i], Cin)
        S.append(sum)
    S.append(Cin)
    return S[::-1]


def take_input():
    num1=list(input("Enter 1st binary number: "))
    num2=list(input("Enter 2nd binary number: "))
    A=[]
    for i in range(len(num1)):
        A.append(int(num1[i]))
    B=[]
    for i in range(len(num2)):
        B.append(int(num2[i]))
    print(A)
    print(B)
    return A,B

A,B=take_input()
Sum=binary_addition(A, B)
for i in range(len(Sum)):
    print(Sum[i], end="")