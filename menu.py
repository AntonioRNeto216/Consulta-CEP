
class Menu:
    def __init__(self):
        self._dicionarioAPI = {1: "address_type", 2: "address_name", 3: "address", 4: "district", 5: "state", 6: "city", 7: "lat",
               8: "lng", 9: "ddd", 10: "city_ibge"}
        self._dicionarioPrint = {1: "Tipo De Endereço", 2: "Nome Do Endereço", 3: "Endereço", 4: "Distrito", 5: "Estado", 6: "Cidade",
                              7: "Latitude", 8: "Longitude", 9: "DDD", 10: "Cidade Do IBGE"}
        self._decoracao = "#" * 75
        self._decoracao2 = " " * 30

    @property
    def decoracao(self):
        return self._decoracao

    @property
    def decoracao2(self):
        return self._decoracao2

    def retorna_ConteudoDicAPI(self, escolha):
        return self._dicionarioAPI[escolha]

    def retorna_ConteudoDicPrint(self, escolha):
        return self._dicionarioPrint[escolha]

    def mensagem_inicial(self):
        print(f"\n {self.decoracao} ")
        print(f"{self.decoracao2}BEM VINDO")
        print(f" {self.decoracao} ")

    def perguntar_cep(self) -> str:
        while True:
            cep = input("\n Digite um CEP para retornarmos informações sobre o mesmo: ")
            if len(cep) != 8:
                print("\n O CEP digitado não apresenta o padrão, ou seja, não contém 8 digitos. Tente novamente")
            else:
                break
        return cep

    def escolhe_infos(self) -> list:
        escolhas = []
        print("\n Agora que sabemos o CEP desejado, quais informações deseja do mesmo?")
        print(" Opções: 1 - Tipo De Endereço       2 - Nome Do Endereço       3 - Endereço")
        print("         4 - Distrito               5 - Estado                 6 - Cidade")
        print("         7 - Latitude               8 - Longitude              9 - DDD")
        print("         10 - Cidade Do IBGE")
        while True:
            print("\n Qual opção você deseja saber? Obs: Digite o número da opção desejada.")
            escolha = int(input(" Opção: "))
            if 1 <= escolha <= 10:
                opcao = self.retorna_ConteudoDicAPI(escolha)
                mensagem_print = self.retorna_ConteudoDicPrint(escolha)
                escolhas.append((mensagem_print, opcao))
                escolha2 = (input("\n Deseja escolher mais opções? [S] - SIM ou [N] - NÃO: ")).upper()
                if escolha2 == "N":
                    break
            else:
                print("\n Essa opção não existe. Confira o número digitado e tente novamente.")
        return escolhas

    def mostra_opcoes_escolhidas(self, cep: str, dados_cep: dict, opcoes_escolhidas: list):
        print(f"\n Os dados escolhidos do CEP = {cep} são: \n")
        for mensagem, codigoAPI in opcoes_escolhidas:
            if codigoAPI in dados_cep:
                print(f"  - {mensagem}: {dados_cep[codigoAPI]}")
            else:
                print(f" Não foi possível obter a opção {mensagem}. Desculpe pelo imprevisto :c")

    def continua(self) -> str:
        escolha = (input("\n Deseja obter informações de outro CEP? [S] - SIM ou [N] - NÃO: ")).upper()
        return escolha

    def saida_programa(self):
        print(f" {self.decoracao} ")
        print(f"{self.decoracao2}OBRIGADO PRO USAR O PROGRAMA !!!")
        print(f" {self.decoracao} ")