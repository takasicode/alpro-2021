def merge(left,right):
    result = []
    i,j = 0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j] :
            result.append(left[i])
            i += 1
        else :
            result.append(right[j])
            j += 1
    while (i<len(left)):
        result.append(left[i])
        i += 1
    while (j<len(right)):
        result.append(right[j])
        j += 1
    return result

def mergeSort(L):
    if len(L) <2 :
        return L[:]
    else:
        middle = len(L)//2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        return merge(left,right)

def main():
    A = [3,4,15,7,28]
    print(mergeSort(A))

main()