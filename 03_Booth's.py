# Use Booth's algorithm to multiply two binary numbers

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


def ASR(A,B,q_1):
    bit=len(A)
    q_1=B[bit-1]
    for i in range(len(B)-1,0,-1):
        B[i]=B[i-1]

    B[0]=A[bit-1]
    for i in range(len(A)-1,0,-1):
        A[i]=A[i-1]

    return A,B,q_1


    


def BoothMultiplication(multiplicand,multiplier):
    Accumulator=[]
    bit=len(multiplicand)
    q0=multiplier[bit-1]
    for i in range(bit):
        Accumulator.append(0)
    q_1=0
    print(Accumulator)
    for i in range(bit):
        print("Here i=",i,"q0=", q0,"q_1=",q_1)
        if (q0==0 and q_1==1):
            print("Addition")
            Accumulator=binary_addition(Accumulator,multiplicand)
        elif (q0==1 and q0==0):
            print("Subtraction")
            Accumulator=binary_subtraction(Accumulator,multiplicand)

        Accumulator,multiplier,q_1=ASR(Accumulator,multiplier,q_1)
        print("Final result ",Accumulator,multiplier)

    return Accumulator,multiplier
    
    
    



def take_input():
    num1=list(input("Enter multiplicand in binary number: "))
    num2=list(input("Enter multiplier in binary number: "))
    A=[]
    for i in range(len(num1)):
        A.append(int(num1[i]))
    B=[]
    for i in range(len(num2)):
        B.append(int(num2[i]))
    return A,B

multiplicand,multiplier=take_input()
a,q=BoothMultiplication(multiplicand,multiplier)
print(a,q)
# a,q,q_1=ASR(multiplicand,multiplier,0)
# print(a,q,q_1)
# multiplicand = binary_addition(multiplicand,multiplier)
# print(multiplicand)

# print(multiplicand,multiplier)