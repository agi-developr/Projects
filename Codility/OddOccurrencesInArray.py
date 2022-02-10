# OddOccurrencesInArray

A = [2, 3, 7, 7, 2, 9, 3]
def solution(A):
    if len(A) == 1:
        return A[0]
    A.sort()
    for i in range(0, len(A)-1, 2):
        if A[i] != A[i+1]:
            return A[i]
    return A[-1]
    pass

print(solution(A))
