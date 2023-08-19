def mergeSort(A):
    n = len(A)
    left = []
    right = []

    if n < 2 : 
        return

    mid = n//2

    for i in range(mid) :
        left[i] = A[i]
    
    for i in range(mid,n) :
        right[i] = A[i]

    mergeSort(left)
    mergeSort(right)
    merge(left,right,A)

def merge(L,R,A):
    nLeft = len(L)
    nRight = len(R)
    iLeft = 0
    iRight = 0
    iA = 0

    while(iLeft < nLeft and iRight < nRight):
        if L[iLeft] <= R[iRight]:
            A[iA] = L[iLeft]
            iLeft = iLeft + 1
            iA = iA + 1
        else :
            A[iA] = R[iRight]
            iRight = iRight + 1
            iA = iA + 1

    while(iLeft < nLeft):
        A[iA] = L[iLeft]
        iLeft = iLeft + 1
        iA = iA + 1

    while(iRight < nRight):
        A[iA] = R[iRight]
        iRight = iRight + 1
        iA = iA + 1
        

def main():
    A = [3,4,15,7,28]
    print(mergeSort(A))

if __name__ == '__main__':
    main()
        