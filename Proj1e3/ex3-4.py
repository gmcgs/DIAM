import time


def alineaA(str1, str2):
    print("alínea a):")
    count = 0
    answer = True
    tic = time.perf_counter()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str2 = list(str2)
    for i in range(len(str1)):
        for j in range(len(str2)):
            count += 1
            if (str2[j] == str1[i]):
                str2[str2.index(str1[i])] = None
    str2 = "".join(str(x) if x is None else "X" for x in str2)
    toc = time.perf_counter()
    print(str1)
    print(str2)
    print(count)
    print(f"{toc - tic:.8f}")
    for i in range(len(str2)):
        if str2[i] == "X":
            return False
    return True



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
        count += 1
        if (str1[i] != str2[i]): answer = False
    toc = time.perf_counter()
    print(count)
    print(f"{toc - tic:.8f}")
    return answer


countC = 0


def alineaC(str1, str2):
    print("alínea c):")
    global countC
    answer = False
    tic = time.perf_counter()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    combinations = findCombinations(str1)
    for i in range(len(combinations)):
        countC += 1
        if str2 == combinations[i]:
            answer = True
    toc = time.perf_counter()
    print(countC)
    print(f"{toc - tic:.8f}")
    return answer


def findCombinations(str):
    global countC
    countC += 1
    if len(str) == 0:
        return [""]
    if len(str) == 1:
        return [str]
    else:
        output = []
        for i in range(len(str)):
            current_char = str[i]
            other_char = str[:i] + str[i + 1:]
            for x in findCombinations(other_char):
                output.append(current_char + x)
        return output


def alineaD(str1, str2):
    print("alínea d):")
    count = 0
    answer = False
    tic = time.perf_counter()
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = sorted(str1)
    str2 = sorted(str2)
    dictionary1 = {}
    dictionary2 = {}
    for i in str1:
        count += 1
        if i in dictionary1:
            dictionary1[i] += 1
        else:
            dictionary1[i] = 1
    for j in str2:
        count += 1
        if j in dictionary2:
            dictionary2[j] += 1
        else:
            dictionary2[j] = 1
    if dictionary1 == dictionary2: answer = True
    toc = time.perf_counter()
    print(dictionary1)
    print(dictionary2)
    print(count)
    print(f"{toc - tic:.8f}")
    return answer


str1 = "the alias men"
str2 = "alan smithee"

print(alineaA(str1, str2))
print("--------------------------------------------------------------")
print(alineaB(str1, str2))
print("--------------------------------------------------------------")
print(alineaC(str1, str2))
print("--------------------------------------------------------------")
print(alineaD(str1, str2))


print("Conclusão -> com base nos testes executados com diferentes strings, conseguimos concluir que o algoritmo com "
      "menos passos é o da alínea b) enquanto que o algoritmo mais rápido é o da alínea d) (com uma diferença na "
      "ordem dos ~10^-6s)")