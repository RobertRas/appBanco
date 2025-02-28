#variáveis globais
saldo=0
#lista responsável por guardar os registros de depósito e saque
extrato = []


qtdd_saques_dia=0


def deposito():
    
    global saldo 
    valor_deposito=0
    
    while valor_deposito == 0:
        
        valor_deposito = float(input("Qual valor deseja depositar? "))
        if valor_deposito <= 0:
            print ("Valor informado é menor que zero reais")
            continue
        else:
            
            saldo += valor_deposito
            
            extrato.append(f"{valor_deposito:.2f}")
            
            resposta = input("Deseja realizar mais depósitos? s/n ")
            
            
            if resposta == "s":
                print("irá realizar depósito")
                valor_deposito=0
                continue
            elif resposta == "n": 
                print("não irá realizar depósito")
                break
            
    menu()
            
        
    
def saque ():
    global qtdd_saques_dia
    global saldo
    global extrato
    
    while qtdd_saques_dia < 3:
        valor_retirado=float(input("Qual o valor que deseja sacar? "))
        
        if valor_retirado <= 500:
                    #verifica se o valor a ser retirado é menor que o saldo
                    if valor_retirado <= saldo:
                        saldo-=valor_retirado
                        qtdd_saques_dia+=1 #iteração
                        
                        """inserir a lista para guardar o histórico
                        de saques"""
                        extrato.append(f"- {valor_retirado:.2f}")
                        #condição que impede de aprecer a mensagem 4 vezes
                        if qtdd_saques_dia < 3:
                            resposta=input("deseja realizar mais um saque? s/n ")
                        
                        if resposta == "n":
                            menu()
                            
                        
                        elif resposta == "s":
                            continue
                        else:
                            print("Resposta inválida. Operação finalizada.")
                            break   
                    else:
                        print("o valor é maior que o saldo")
        else :
            print("valor máximo do saque é de R$500,00")
    
    print ("operação finalizada")
    
    menu()
    
def extrato_conta():
    global extrato
    
    for item in extrato:
        print(item)
        
        
    print("-----------------")
    print(f"saldo: {saldo}")
    
    menu()



    
def menu():
    opcoes = ["saque: 1","depósito: 2", "extrato: 3","finalizar operação: 4"]
    for item in opcoes:
        print(item)
    
    
    print("-------------------------")    
    while True:
        
        opcao_escolhida = int(input("digite a opção desejada: "))
            
        if opcao_escolhida == 1:
            saque()
        elif opcao_escolhida == 2:
            deposito()
        elif opcao_escolhida == 3:
            extrato_conta()
            
        elif opcao_escolhida == 4:
            Print("operação finalizada!")
            break
        else:
            print("operação inválida, por favor, selecione novamente a opção desejada")
            
            
menu()