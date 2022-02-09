# Cyclic Array rotation
A = list([2, 3, 4, 5, 6])
K = int(3)


def solution(A, K):
    N = len(A)
    # B = A.copy()
    B = [None] * N
    for i in range(0,N):
        B[(i+K)%N] = A[i]
    print(B)
solution(A, K)
