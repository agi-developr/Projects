# This program calculates binary gap

def solution(n):
    n = bin(n)[2:]
    b = 0
    max_b = 0
    for k in n:
        if int(k) == 0:
            b += 1
        elif int(k) == 1:
            max_b = max(max_b, b)
            b = 0
            
    print(max_b)


try:
    n = input("Type in integer:")
    n = int(n)
    solution(n)
except ValueError:
    print("number is not int")
    pass
