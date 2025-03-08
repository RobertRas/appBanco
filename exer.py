import datetime
qttd_transacoes = 0
#esta variável é a responsável por guardar a data
"""foi colocada uma data aleatória para que o código pudesse iniciar
do contrário, ela poderia ser vazia e na definição da função verificadorData
poderíamos atribuir o valor da variável data_corrente_formatada a ela"""
data_registrada = datetime.datetime(2025,3,6)
data_registrada_formatada=data_registrada.strftime("%d-%m-%Y")


#essa variável é a responsável por atualizar a data
data_corrente = datetime.datetime.now()
data_corrente_hora =  data_corrente.strftime("%d-%m-%Y %H:%M:%S")
data_corrente_formatada = data_corrente.strftime("%d-%m-%Y")

#variáveis globais
saldo=0
#lista responsável por guardar os registros de depósito e saque
extrato = []

verifica_dia=""



def verificadorDia():
    global data_registrada_formatada,data_corrente_formatada,qttd_transacoes
    
    if data_registrada_formatada == data_corrente_formatada:
        #print("verificou que a data são iguais")
        if qttd_transacoes < 10:
            #print("analisou que a qtdd de transações é menor que 10")
            #print("transação permitida")
            return True
        else:
            #print("verificou que qtdd de transações é maior que 10")
            #print("você alcançou a quantidade de transações diárias")
            return False
    else:
        #print("verificou que as datas não são iguais")
        data_registrada_formatada = data_corrente_formatada
        #print("atualizou o valor de qtdd de transações para 0")
        qttd_transacoes=0
        return True


def deposito():
    
    global saldo, verifica_dia, qttd_transacoes
    valor_deposito=0
    

    
    if verifica_dia:
        
        
        if qttd_transacoes < 10:
            while valor_deposito == 0:
                
                valor_deposito = float(input("Qual valor deseja depositar? "))
                if valor_deposito <= 0:
                    print ("Valor informado é menor que zero reais")
                    continue
                else:
                    
                    saldo += valor_deposito
                    qttd_transacoes += 1
                    extrato.append(f"{data_corrente_hora}: {valor_deposito:.2f}")
                    #print(f"valor da qtdd_transações é {qttd_transacoes}")
                    
                    resposta = input("Deseja realizar mais depósitos? s/n ")
                    
                    
                    if resposta == "s" and qttd_transacoes < 10:
                        #print("irá realizar depósito")
                        valor_deposito=0
                        continue
                    elif resposta == "n": 
                        #print("não irá realizar depósito")
                        break
                    else:
                        print("-----------------")
                        print("Limite de transações diárias atingido.")
                        print("-----------------")
    else:
        print("-----------------")
        print("Limite de transações diárias atingido.") 
        print("-----------------")       
    menu()
            
        
    
def saque():
    global qttd_transacoes, verifica_dia
    global saldo
    global extrato


    if verifica_dia:
        
        
        resposta = ""
        while qttd_transacoes < 10:
            
                valor_retirado = float(input("Qual o valor que deseja sacar? "))
                
                if valor_retirado > 500:
                    print("O valor máximo para saque é de R$500,00.")
                    continue
                
                if valor_retirado > saldo:
                    print("Saldo insuficiente para realizar o saque.")
                    continue
                
                # Realiza o saque
                saldo -= valor_retirado
                qttd_transacoes += 1
                extrato.append(f"{data_corrente_hora}: - {valor_retirado:.2f}")
                print(f"valor da qtdd_transações é {qttd_transacoes}")
                print(f"Saque de R$ {valor_retirado:.2f} realizado com sucesso!")
                print(f"Saldo atual: R$ {saldo:.2f}")
                
                if qttd_transacoes < 10:
                    resposta = input("Deseja realizar mais um saque? (s/n): ").strip().lower()
                    
                    if resposta == "n":
                        break
                    elif resposta != "s":
                        print("-----------------")
                        print("Resposta inválida. Operação finalizada.")
                        print("-----------------")
                        break
            
        else:
            print("-----------------")
            print("Você atingiu o limite de saques diários.")
            print("-----------------")

    else:
        print("-----------------")
        print("Limite de transações diárias atingido.")
        print("-----------------")
    
    
    #verificadorDia()
    menu()  # Retorna ao menu principal

    
def extrato_conta():
    global extrato
    
    for item in extrato:
        print(item)
        
        
    print("-----------------")
    print(f"saldo: {saldo:.2f}")
    print("-----------------")
    
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
            print("operação finalizada!")
            break
        else:
            print("operação inválida, por favor, selecione novamente a opção desejada")
            
            

verifica_dia = verificadorDia()

menu()

