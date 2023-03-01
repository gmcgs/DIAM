poema = "Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"

def alineaA():
    lowerCasePoema = poema.lower()
    num_a = lowerCasePoema.count("a")
    num_e = lowerCasePoema.count("e")
    num_i = lowerCasePoema.count("i")
    num_o = lowerCasePoema.count("o")
    num_u = lowerCasePoema.count("u")
    print("nº de vogais: " + str(num_a + num_e + num_i + num_o + num_u))
    print("nº de A's: " + str(num_a))
    print("nº de E's: " + str(num_e))
    print("nº de I's: " + str(num_i))
    print("nº de O's: " + str(num_o))
    print("nº de U's: " + str(num_u))
    ocorrVogais = {"A": num_a, "E": num_e, "I": num_i, "O": num_o, "U": num_u}
    valoresMaisAltos = max(ocorrVogais.values())
    vogalMaisUsada = [k for k, v in ocorrVogais.items() if v == valoresMaisAltos]
    if len(vogalMaisUsada) > 1:
        print("Há vários vencedores! As vogais mais utilizadas foram: " + str(vogalMaisUsada))
    else:
        print("A vogal mais utilizada é: " + str(vogalMaisUsada))



alineaA()
