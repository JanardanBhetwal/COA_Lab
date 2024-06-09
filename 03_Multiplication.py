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
    A=A[::-1]
    B=B[::-1]
    Cin=0
    S=[]
    for i in range(len(A)):
        sum, Cin = full_adder(A[i], B[i], Cin)
        S.append(sum)
    return S[::-1]

def shift_left(A):
    bit=len(A)
    for i in range(1,bit):
        A[i-1]=A[i]

    A[bit-1]=0
    return A


def multiplication(A,B):
    bit=len(A)
    M=[]
    for i in range(bit):
        M.append(0)
        M.append(0)
        A.insert(0,0)
        B.insert(0,0)
    for i in range(bit):
        if B[bit]==1:
            M=binary_addition(M,A)
        if i<bit-1:
            M=shift_left(M)
            B=shift_left(B)
    
    return M

def take_input():
    num1=list(input("Enter multiplicand in binary number: "))
    num2=list(input("Enter multiplier in binary number: "))
    A=[]
    for i in range(len(num1)):
        A.append(int(num1[i]))
    B=[]
    for i in range(len(num2)):
        B.append(int(num2[i]))
    if len(A)>len(B):
        for i in range(len(A)-len(B)):
            B.insert(0,0)
    elif len(A)<len(B):
        for i in range(len(B)-len(A)):
            A.insert(0,0)
    return A,B

multiplicand,multiplier=take_input()
print(multiplication(multiplicand,multiplier))
# print(shift_left(multiplicand))