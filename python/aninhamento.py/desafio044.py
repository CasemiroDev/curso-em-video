print("----- Bem vindo a maquininha Itaú Press! -----")
valo = float(input("Digite o valor de seu produto: "))
pay = str(input("Digite o método de pagamento: (à vista / cheque / cartão) "))

if pay == "À vista" or pay == "à vista" or pay == "cheque" or pay == "Cheque" :
    neoval = valo * 0.90
    print("Seu desconto foi de 10% ee o novo preço foi de {:.2f} reais".format(neoval))
elif pay == "cartão" or pay == "Cartão" or pay == "cartao" or pay == "Cartao" :
    parcel = int(input("Digite quantas parcelas serão feitas no cartão: "))
    if parcel == 1 :
        neoval = valo * 0.95
        print("Seu desconto foi de 5% e o novo preço é {:.2f} reais".format(neoval))
    elif parcel == 2 :
        print("Você não teve desconto e o valor não altera sendo",valo,"reais.")
    elif parcel >= 3 :
        neoval = valo * 1.20
        print("O novo valor teve 20% de juros sendo agora {:.2f} reais.".format(neoval))
    else :
        print("Tente digitar o valor apenas com números ou digite um valor válido.")
else :
    print("Tente digitar a forma de pagamento da forma correta.")


trye = str(input("Confirmar pagamento? (S/N) "))

if trye == "S" or trye == "s" :
    ys = str(input("Pagamento concluído, deseja a notinha? (S/N) "))
    if ys == "S" or ys == "s" :
        print("--------- pagamento efetuado ----------")
        print("Compra x ------------ valor: R$ {:.2f}".format(neoval))
    elif ys == "N" or ys == "n" :
        print("Pagamento cancelado, bom dia!")
    else :
        print("Digite S ou N")
elif trye == "N" or trye == "n" :
    print("Pagamento Cancelado")
else :
    print("Digite S ou N")
