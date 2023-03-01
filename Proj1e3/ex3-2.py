poema = "Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"

def alineaA():
    num_a = poema.count("a")
    num_A = poema.count("A")
    num_e = poema.count("e")
    num_E = poema.count("E")
    num_i = poema.count("i")
    num_I = poema.count("I")
    num_o = poema.count("o")
    num_O = poema.count("O")
    num_u = poema.count("u")
    num_U = poema.count("U")
    print("nº de vogais: " + str(num_a + num_A + num_e + num_E + num_i + num_I + num_o + num_O + num_u + num_U))
    print("nº de A's: " + str(num_a + num_A))
    print("nº de E's: " + str(num_e + num_E))
    print("nº de I's: " + str(num_i + num_I))
    print("nº de O's: " + str(num_o + num_O))
    print("nº de U's: " + str(num_u + num_U))

alineaA()
