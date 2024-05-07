pilha = list()
exp = str(input("Digite uma expressão matemática: "))
for c in exp:
    if c == "(":
        pilha.append("(")
    elif c == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")
            break
if len(pilha) > 0:
    print("A sua expressão está errada.")
else :
    print("Sua expressão está correta.")

    