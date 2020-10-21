from menu import Menu
import pegaInfo

# Inicia Menu
menu = Menu()

# Mensagem Inicial
menu.mensagem_inicial()

while True:

    # Pegando CEP e abrindo API para o cep escolhido
    cep = menu.perguntar_cep()
    dados_cep, status_code = pegaInfo.abre_url(cep)

    if status_code == 200:
        opcoes_escolhidas = menu.escolhe_infos()
        menu.mostra_opcoes_escolhidas(cep, dados_cep, opcoes_escolhidas)
        continua = menu.continua()
        if continua == "N":
            break
    else:
        print(f"\n Desculpe, não encontramos o CEP = {cep} na nossa base de dados.")
        escolha = (input(" Gostaria de inserir novamente o CEP? [S] - SIM ou [N] - NÃO: ")).upper()
        if escolha == "N":
            break

menu.saida_programa()