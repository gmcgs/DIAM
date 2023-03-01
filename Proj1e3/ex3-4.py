import time

def alineaA(str1, str2):
    print("alínea a):")
    count = 0
    answer = True
    tic = time.perf_counter()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    for i in range(len(str1)):
        for j in range(len(str2)):
            count += 1
            if(str2[j] == str1[i]):
                str2 = str2.replace(str2[j], "X", 1)
    for l in range(len(str2)):
        if(str2[l] != "X"):
            answer = False
    toc = time.perf_counter()
    print(str1)
    print(str2)
    print(count)
    print(f"{toc-tic:.8f}")
    if answer == False: return False
    else: return True


def alineaB(str1, str2):
    print("alínea b):")
    count = 0
    answer = True
    tic = time.perf_counter()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1)
    print(str2)
    for i in range(len(str1)):
        count+=1
        if(str1[i] != str2[i]): answer = False
    print(count)
    toc = time.perf_counter()
    print(f"{toc-tic:.8f}")
    return answer


str1 = "the alias men"
str2 = "alan smithee"

print(alineaA(str1, str2))
print(alineaB(str1, str2))