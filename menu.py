
def mensagem_inicial():
    decoracao = "#" * 30
    decoracao2 = " " * 12
    print()
    print(f" {decoracao} ")
    print(f"{decoracao2}BEM VINDO")
    print(f" {decoracao} ")

def perguntar_cep():
    while True:
        print()
        cep = input(" Digite um CEP para retornarmos informações sobre o mesmo: ")
        if len(cep) < 8 or len(cep) > 8:
            print()
            print(" O CEP digitado não apresenta o padrão, ou seja, não contém 8 digitos. Tente novamente")
        else:
            break

    return cep

def dic(escolha):
    dic = {"Tipo De Endereço": "address_type", "Nome Do Endereço": "address_name", "Endereço": "address", "Distrito": "district", "Estado": "state", "Cidade": "city", "Latitude": "lat", "Longitude": "lng", "DDD": "ddd", "Cidade Do IBGE": "city_ibge"}
    if escolha in dic:
        return True, dic[escolha]
    else:
        return False, " "

def escolhe_infos():
    escolhas = []
    print()
    print(" Agora que sabemos o CEP desejado, quais informações deseja do mesmo?")
    print(" Opções: Tipo De Endereço       Nome Do Endereço       Endereço")
    print("         Distrito               Estado                 Cidade")
    print("         Latitude               Longitude              DDD")
    print("         Cidade Do IBGE")
    while True:
        print()
        print(" Qual opção você deseja saber? Obs: escreva exatamente como está acima.")
        escolha = input(" Opção: ")
        bool, opcao = dic(escolha)
        if bool:
            escolhas.append(opcao)
            print()
            escolha2 = (input(" Deseja escolher mais opções? [S] - SIM ou [N] - NÃO: ")).upper()
            if escolha2 == "N":
                break
        else:
            print()
            print(" Essa opção não existe. Confira se digitou corretemente e tente denovo.")

    return escolhas