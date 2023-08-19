from insertion_sort import insertion_sort_asc, insertion_sort_desc

def main():
    A = [5, 2, 10, 27, 33]

    print("Array sebelum pengurutan:", A)

    sorted_asc = insertion_sort_asc(A.copy())
    sorted_desc = insertion_sort_desc(A.copy())

    print("Array setelah pengurutan ascending:", sorted_asc)
    print("Array setelah pengurutan descending:", sorted_desc)

if __name__ == "__main__":
    main()
