# Create addition using full subtractor that takes two inputs in binary and provides output in binary

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

def ones_complement(A):
    for i in range(len(A)):
        A[i]=not_gate(A[i])
    return A

def binary_subtraction(A, B):
    A=A[::-1]
    B=B[::-1]
    B=ones_complement(B)
    Cin=1
    S=[]
    for i in range(len(A)):
        diff, Cin = full_adder(A[i], B[i], Cin)
        S.append(diff)
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
Sum=binary_subtraction(A, B)
for i in range(len(Sum)):
    print(Sum[i], end="")