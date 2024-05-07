palavras = (
    "banana","abacate","uva","manga"
)
c = 0
for c in range(0,len(palavras)):
    if "a" or "e" or "i" or "o" or "u" in palavras:
        if "a" in palavras[c]:
            print(f"Na palavra {palavras[c]} temos a vogal a")
        if "e" in palavras[c]:
            print(f"Na palavra {palavras[c]} temos a vogal e")
        if "i" in palavras[c]:
            print(f"Na palavra {palavras[c]} temos a vogal i")
        if "o" in palavras[c]:
            print(f"Na palavra {palavras[c]} temos a vogal o")
        if "u" in palavras[c]:
            print(f"Na palavra {palavras[c]} temos a vogal u")
