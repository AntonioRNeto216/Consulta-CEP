import menu
import pegaInfo

menu.mensagem_inicial()

while True:
    while True:
        cep = menu.perguntar_cep()
        dados_cep, status_code = pegaInfo.abre_url(cep)
        if status_code == 200:
            break
        else:
            print()
            print(f" Desculpe, não encontramos o CEP = {cep} na nossa base de dados.")
            escolha = (input(" Gostaria de inserir novamente o CEP? [S] - SIM ou [N] - NÃO: ")).upper()
            if escolha == "N":
                quit()

    opcoes_escolhidas, opcoes_escolhidas_print = menu.escolhe_infos()
    menu.mostra_opcoes_escolhidas(cep, dados_cep, opcoes_escolhidas, opcoes_escolhidas_print)
    per = menu.continua()
    if per == "N":
        break

menu.saida_programa()