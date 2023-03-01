import time

def bubbleSortA(array):
    print("alínea a):")
    tic = time.time()
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if(array[j] > array[j+1]):
                x = array[j]
                array[j] = array[j+1]
                array[j+1] = x
    toc = time.time()
    print(array)
    print(f"Tempo: {toc-tic:.6f} segundos")
    print("--------------------------------------------------------------")

def bubbleSortB(array):
    print("alínea b):")
    tic = time.time()
    n = len(array)
    for i in range(n-1):
        for j in range(n-i-1):
            if(array[j] > array[j+1]):
                array[j], array[j+1] = array[j+1], array[j]
    toc = time.time()
    print(array)
    print(f"Tempo: {toc - tic:.6f} segundos")
    print("--------------------------------------------------------------")

array = [93, 150, 58, 91, 112, 187, 109, 83, 171, 125, 9, 141, 140, 196, 50, 33, 5, 99, 34, 61, 157, 22, 43, 54, 119, 153, 178, 41, 69, 32, 1, 137, 183, 169, 49, 82, 131, 191, 11, 35, 10, 167, 114, 116, 44, 45, 168, 146, 111, 189, 186, 158, 95, 46, 86, 55, 75, 142, 96, 194, 180, 19, 200, 87, 110, 105, 51, 16, 40, 85, 68, 53, 26, 103, 66, 135, 192, 151, 161, 198, 164, 115, 89, 138, 120, 132, 163, 188, 15, 104, 118, 197, 64, 67, 128, 7, 129, 42, 175, 122]
bubbleSortA(array)
bubbleSortB(array)
