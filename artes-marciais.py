from random import randint
from time import sleep
lista_torneios = []
lista_lutadores = []


# ###################################################### #
# ################# Classes ############################ #
# ###################################################### #

class Lutador():
    def __init__(self, nome: str, arte: str, peso: float, faixa: str, idade: int, forca: int, id_lutador: int):
        self._nome = nome
        self._arte = arte
        self._peso = peso
        self._faixa = faixa
        self._idade = idade
        self._forca = forca
        self._id_lutador = id_lutador

    def __str__(self):
        return f"Esse é o lutador {self._nome}, tem {self._idade} anos, é faixa {self._faixa} em {self._arte } e seu número de registro é {self._id_lutador}"

    @property
    def nome(self):
        return self._nome

    @property
    def arte(self):
        return self._arte

    @property
    def peso(self):
        return self._peso

    @property
    def faixa(self):
        return self._faixa

    @property
    def idade(self):
        return self._idade

    @property
    def forca(self):
        return self._forca

    @property
    def id_lutador(self):
        return self._id_lutador


class Torneio():
    def __init__(self, nome_torneio: str, arte: str, lista_pesos: list, lista_faixas: list, id_torneio):
        self._nome_torneio = nome_torneio
        self._arte = arte
        self._lista_pesos = lista_pesos
        self._lista_faixas = lista_faixas
        self._id_torneio = id_torneio
        self._incritos_categorias = {}
        self._lista_incritos_torneio = []
        self._ranking_torneio = {}
        self._lista_lutas = {}
        for faixa in lista_faixas:
            self._incritos_categorias[faixa] = {}
            self._ranking_torneio[faixa] = {}
            self._lista_lutas[faixa] = {}
            for indice_faixa_de_peso in range(len(lista_pesos)):
                self._incritos_categorias[faixa][indice_faixa_de_peso] = []
                self._ranking_torneio[faixa][indice_faixa_de_peso] = {}
                self._lista_lutas[faixa][indice_faixa_de_peso] = []



    def __str__(self):
        return f"Esse é o Torneio {self._nome_torneio} da modalidade {self._arte} e seu número de registro é {self._id_torneio}"

    @property
    def nome_torneio(self):
        return self._nome_torneio

    @property
    def arte(self):
        return self._arte

    @property
    def lista_pesos(self):
        return self._lista_pesos

    @property
    def lista_faixas(self):
        return self._lista_faixas

    @property
    def id_torneio(self):
        return self._id_torneio

    @property
    def lista_incritos_torneio(self):
        return self._lista_incritos_torneio

    @property
    def incritos_categorias(self):
        return self._incritos_categorias

    @property
    def ranking_torneio(self):
        return self._ranking_torneio

    @property
    def lista_lutas(self):
        return self._lista_lutas

    def inscrever_lutador(self, lutador: Lutador, faixa: str, faixa_de_peso: list):
        self._lista_incritos_torneio.append(lutador)
        indice = self._lista_pesos.index(faixa_de_peso)
        self._incritos_categorias[faixa][indice].append(lutador)
        self._ranking_torneio[faixa][indice][lutador] = [0, 0]


    def atualizar_ranking(self, vencedor: Lutador, perdedor: Lutador, faixa: str, indice_peso: int):
        self.ranking_torneio[faixa][indice_peso][vencedor][0] += 1
        self.ranking_torneio[faixa][indice_peso][perdedor][1] += 1

    def lutar(self, lutador1, lutador2):
        poder1 = lutador1.forca * randint(1, 5) / lutador1.idade
        poder2 = lutador2.forca * randint(1, 5) / lutador2.idade
        if poder1 > poder2:
            return lutador1, lutador2
        else:
            return lutador2, lutador1





# ###################################################### #
# ################# Torneio ############################ #
# ###################################################### #

def menu_do_torneio():
    while True:
        imprime_menu_do_torneio()
        acao_torneio = input("O que deseja? ")
        if acao_torneio not in ['1', '2', '3', '4', '5','6','7', '8']:
            print("Digite valores validos\n")
            sleep(2)
            continue
        elif acao_torneio == '1':
            criar_torneio()
        elif acao_torneio == '2':
            inscrever_lutador()
        elif acao_torneio == '3':
            ver_detalhes_torneio()
        elif acao_torneio == '4':
            ver_torneios()
        elif acao_torneio == '5':
            ver_ranking()
        elif acao_torneio == '6':
            ver_lutadores_no_torneio()
        elif acao_torneio == '7':
            realizar_luta()
        elif acao_torneio == '8':
            sleep(1)
            print()
            break


def imprime_menu_do_torneio():
    print('---------------------------------------')
    print('1- Criar Torneio')
    print('2- Inscrever Lutador')
    print('3- Ver detalhe de torneio')
    print('4- Ver Torneios existentes')
    print('5- Ver Ranking de Torneio')
    print('6- Ver Lutadores incritos em Torneio')
    print('7- Realizar Luta')
    print('8- Retornar ao Menu Principal')
    print('----------------------------------------')

# Criar Torneio #

def criar_torneio():
    nome_torneio = input("Nome do Torneio: ")
    arte_do_torneio = input("Modalidade do torneio: ")
    faixas = []
    while True:
        try:
            quantidade_de_faixas = int(input("Quantas faixas poderão disputar o torneio? "))
            break
        except ValueError:
            continue
    for e in range(quantidade_de_faixas):
        faixa = input("Digite a faixa: ")
        faixas.append(faixa)
    absoluto = input("Haverá categoria absoluto? ")
    if absoluto.lower() == 's' or absoluto.lower() == 'sim':
        faixas.append("absoluto")
    pesos = []
    while True:
        try:
            quantidade_de_categorias = int(input("Quantas categorias irão disputar o torneio? "))
            break
        except ValueError:
            continue
    for e in range(quantidade_de_categorias):
        while True:
            while True:
                try:
                    inicial = int(input("Digite o peso inicial da categoria: "))
                    break
                except ValueError:
                    print("Digite um valor apropriado")
                    sleep(1)
                    continue

            while True:
                try:
                    final = int(input("Digite o peso final da categoria: "))
                    break
                except ValueError:
                    print("Digite um valor apropriado")
                    sleep(1)
                    continue
            if final > inicial:
                break
            else:
                print("O peso final deve ser maior que o inicial")
                sleep(1)

        peso = [inicial, final]
        pesos.append(peso)
        print("Categoria adicionada")
    livre = input("Haverá categoria sem peso? ")
    if livre.lower() == 's' or livre.lower() == 'sim':
        pesos.append([0, 500])
    id_torneio = len(lista_torneios) + 1
    torneio = Torneio(nome_torneio=nome_torneio, arte=arte_do_torneio, lista_pesos=pesos, lista_faixas=faixas, id_torneio=id_torneio)
    lista_torneios.append(torneio)

    print("Torneio Adicionado com sucesso")



# Inscrever Lutador #

def inscrever_lutador():
    if len(lista_lutadores) == 0:
        print("Ainda não existem lutadores")
        return
    if len(lista_torneios) == 0:
        print("Ainda não existem torneios")
        return
    while True:
        try:
            id_lutador = int(input("Digite o número de registro do lutador(caso não saiba, digite 0): "))
            if id_lutador == 0:
                ver_lutadores_existentes()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    while True:
        try:
            id_torneio = int(input("Digite o número de registro do torneio(caso não saiba, digite 0): "))
            if id_torneio == 0:
                ver_torneios()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    if id_torneio > len(lista_torneios):
        print("Torneio inexistente")
        sleep(1)
        return
    if id_lutador > len(lista_lutadores):
        print("Lutador inexistente")
        sleep(1)
        return

    lutador = lista_lutadores[id_lutador-1]
    torneio = lista_torneios[id_torneio-1]

    if lutador in torneio.lista_incritos_torneio:
        print("O lutador já está inscrito no torneio")
        sleep(1)
        return

    if lutador.arte.lower() != torneio.arte.lower():
        print("O lutador não está apto a participar desse torneio devido a sua modalidade")
        return

    if lutador.faixa.lower() in torneio.lista_faixas:
        if 'absoluto' in torneio.lista_faixas:
            print(f"1- Lutar na categoria Faixa: {lutador.faixa}")
            print(f"2 - Lutar na categoria absoluto")
            while True:
                resposta = input("O lutador irá lutar em que categoria? ")
                if resposta == "1":
                    categoria = lutador.faixa.lower()
                    break
                elif resposta == "2":
                    categoria = "absoluto"
                    break
        else:
            print(f"1- Lutas na categoria {lutador.faixa}")
            while True:
                resposta = input("O lutador irá lutar em que categoria? ")
                if resposta == "1":
                    categoria = lutador.faixa.lower()
                    break
    else:
        if "absoluto" in torneio.lista_faixas:
            print("1 - Luta na categoria absoluto")
            while True:
                cat = input("Deseja lutar em que categoria? ")
                if cat == '1':
                    categoria = "absoluto"
                    break

        else:
            print("O lutador não está apto para participar do torneio, devido a sua faixa")
            return
    pesos_disponiveis = []
    for faixa_pesos in torneio.lista_pesos:
        if faixa_pesos[0] <= lutador.peso < faixa_pesos[1]:
            pesos_disponiveis.append(faixa_pesos)

    if len(pesos_disponiveis) >= 1:
        for e in range(len(pesos_disponiveis)):
            if pesos_disponiveis[e] == [0, 500]:
                print(f"{e+1} - Sem peso")
            else:
                print(f"{e+1} - Entre {pesos_disponiveis[e][0]}kg e {pesos_disponiveis[e][1]}kg")
        while True:
            try:
                resposta = int(input("Deseja lutar em que faixa de peso? "))
                if resposta <= len(pesos_disponiveis):
                    peso = pesos_disponiveis[resposta - 1]
                    break
            except ValueError:
                print('Digite um valor válido')
                sleep(1)
    else:
        print("O lutador não está apto para participar do torneio devido ao seu peso")
        return
    torneio.inscrever_lutador(lutador=lutador, faixa=categoria, faixa_de_peso=peso)

# Ver Torneios #
def ver_torneios():
    if len(lista_torneios) == 0:
        print("Ainda não existem torneios")
        sleep(1)
        return
    print()
    print('Id - Torneio')
    for torneio in lista_torneios:
        print(f"{torneio.id_torneio} - {torneio.nome_torneio}")

# Ver detalhes de torneio #
def ver_detalhes_torneio():
    while True:
        try:
            id_torneio = int(input("Digite o número de registro do torneio(caso não saiba, digite 0): "))
            if id_torneio == 0:
                ver_torneios()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    if id_torneio > len(lista_torneios):
        print("Torneio inexistente")
        sleep(1)
        return
    torneio = lista_torneios[id_torneio - 1]
    print(torneio)



# Ver Ranking #
def ver_ranking():
    if len(lista_torneios) == 0:
        print("Ainda não existem torneios")
        sleep(1)
        return

    while True:
        try:
            id_torneio = int(input("Digite o número de registro do torneio(caso não saiba, digite 0): "))
            if id_torneio == 0:
                ver_torneios()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    if id_torneio > len(lista_torneios):
        print("Torneio inexistente")
        sleep(1)
        return
    torneio = lista_torneios[id_torneio-1]
    for indice in range(len(torneio.lista_faixas)):
        print(f"{indice + 1} - faixa: {torneio.lista_faixas[indice]}")
    while True:
        try:
            indice_faixa = int(input("Digite o número correspondente a faixa que você deseja: ")) - 1
            if indice_faixa in range(len(torneio.lista_faixas)):
                faixa = torneio.lista_faixas[indice_faixa]
                break
            print("Digite um valor válido")

        except ValueError:
            print("Digite um valor válido")
            sleep(1)

    for indice in range(len(torneio.lista_pesos)):
        if torneio.lista_pesos[indice] == [0, 500]:
            print(f"{indice + 1} - Categoria sem peso")
        else:
            print(f"{indice + 1} - Categoria entre {torneio.lista_pesos[indice][0]}kg e {torneio.lista_pesos[indice][1]}kg")
    while True:
        try:
            indice_peso = int(input("Digite o número correspondente ao peso que você deseja: ")) - 1
            if indice_peso in range(len(torneio.lista_pesos)):
                break
            print("Digite um valor válido")

            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    print()
    print('Id - Nome - Vitorias - Derrotas')
    for indice in range(len(torneio.ranking_torneio[faixa][indice_peso])):
        lutador = torneio.incritos_categorias[faixa][indice_peso][indice]
        print(f"{(lutador.id_lutador)} - {lutador.nome} - {torneio.ranking_torneio[faixa][indice_peso][lutador][0]} - {torneio.ranking_torneio[faixa][indice_peso][lutador][1]}")





# Ver lutadores #
def ver_lutadores_no_torneio():
    if len(lista_torneios) == 0:
        print("Ainda não existem torneios")
        sleep(1)
        return

    while True:
        try:
            id_torneio = int(input("Digite o número de registro do torneio(caso não saiba, digite 0): "))
            if id_torneio == 0:
                ver_torneios()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    if id_torneio > len(lista_torneios):
        print("Torneio inexistente")
        sleep(1)
        return
    torneio = lista_torneios[id_torneio - 1]
    print()
    print('Id - Nome')
    for lutador in torneio.lista_incritos_torneio:
        print(f"{lutador.id_lutador} - {lutador.nome}")


# TODO
# Lutar #
def realizar_luta():
    if len(lista_torneios) == 0:
        print("Ainda não existem torneios")
        sleep(1)
        return

    while True:
        try:
            id_torneio = int(input("Digite o número de registro do torneio(caso não saiba, digite 0): "))
            if id_torneio == 0:
                ver_torneios()
                continue
            break
        except ValueError:
            print("Digite um valor válido")
            sleep(1)
    if id_torneio > len(lista_torneios):
        print("Torneio inexistente")
        sleep(1)
        return
    torneio = lista_torneios[id_torneio-1]

    for indice in range(len(torneio.lista_faixas)):
        print(f"{indice + 1} - {torneio.lista_faixas[indice]} ")
    while True:
        try:
            indice_faixa = int(input("A luta deve acontecer entre pessoas de que faixa? ")) - 1
            if 0 <= indice_faixa < len(torneio.lista_faixas):
                faixa = torneio.lista_faixas[indice_faixa]
                break
        except ValueError:
            print("Digite valores válidos")
            sleep(1)
    for indice in range(len(torneio.lista_pesos)):
        if torneio.lista_pesos[indice] == [0,500]:
            print(f"{indice + 1} - Sem peso")
        else:
            print(f"{indice + 1} - Entre {torneio.lista_pesos[indice][0]}kg e {torneio.lista_pesos[indice][1]}kg")
    while True:
        try:
            indice_peso = int(input("A luta deve acontecer entre pessoas de que categoria? ")) - 1
            if 0 <= indice_faixa < len(torneio.lista_faixas):
                break
        except ValueError:
            print("Digite valores válidos")
            sleep(1)
    if len(torneio.incritos_categorias[faixa][indice_peso]) < 2:
        print("Não há lutadores suficientes")
        return

    print("Esses são os lutadores diponíveis:")
    for indice in range(len(torneio.incritos_categorias[faixa][indice_peso])):
        print(f"{indice + 1} - {torneio.incritos_categorias[faixa][indice_peso][indice].nome}")
    while True:
        try:
            indice1 = int(input("Digite o número correspondente ao primeiro lutador: ")) - 1
            if indice1 < len(torneio.incritos_categorias[faixa][indice_peso]):
                lutador1 = torneio.incritos_categorias[faixa][indice_peso][indice1]
                break
        except ValueError:
            print("Digite valores válidos")

    while True:
        try:
            indice2 = int(input("Digite o número correspondente ao segundo lutador: ")) - 1
            if indice2 < len(torneio.incritos_categorias[faixa][indice_peso]):
                lutador2 = torneio.incritos_categorias[faixa][indice_peso][indice2]
                break
        except ValueError:
            print("Digite valores válidos")

    print(f"Luta entre {lutador1.nome} e {lutador2.nome}")
    sleep(1)
    vencedor, perdedor = torneio.lutar(lutador1, lutador2)
    print(f"Vencedor: {vencedor.nome}")






# ###################################################### #
# ################# Lutador ############################ #
# ###################################################### #



def menu_do_lutador():
    while True:
        imprime_menu_do_lutador()
        acao_lutador = input("O que deseja? ")
        if acao_lutador not in ['1', '2', '3', '4']:
            print("Digite valores validos\n")
            sleep(2)
            continue
        elif acao_lutador == '1':
            cadastrar_lutador()
        elif acao_lutador == '2':
            ver_lutadores_existentes()
        elif acao_lutador == '3':
            ver_detalhes_lutador()
        elif acao_lutador == '4':
            sleep(1)
            print()
            break


def imprime_menu_do_lutador():
    print('-----------------------------')
    print('1- Cadastrar Lutador')
    print('2- Ver Lutadores')
    print("3- Ver detalhes de Lutador")
    print('4- Retornar ao Menu Principal')
    print('-----------------------------')


# Cadastrar Lutador #
def cadastrar_lutador():
    nome = input('Digite o nome do lutador: ')
    arte = input('Digite a especialidade do lutador: ')
    while True:
        try:
            peso = float(input('Digite o peso do lutador: '))
            break
        except ValueError:
            print('Digite um valor valido')
            sleep(1)
            continue
    faixa = input('Digite a faixa do lutador: ')
    while True:
        try:
            idade = int(input('Digite a idade do lutador: '))
            break
        except ValueError:
            print('Digite um valor valido')
            sleep(1)
            continue
    while True:
        while True:
            try:
                forca = int(input('Digite a força do lutador: '))
                break
            except ValueError:
                print('Digite um valor valido')
                sleep(1)
                continue
        if forca in range(1, 101):
            break
        else:
            print("A força deve ser um valor entre 1 e 100")
            sleep(1)
    id_lutador = len(lista_lutadores) + 1
    lutador = Lutador(nome=nome, arte=arte, peso=peso, faixa=faixa, idade=idade, forca=forca, id_lutador=id_lutador)
    lista_lutadores.append(lutador)
    print("Lutador cadastrado com sucesso")

# Ver Lutadores Existentes #

def ver_lutadores_existentes():
    if len(lista_lutadores) == 0:
        print("Ainda não existem lutadores")
        sleep(1)
        return
    print()
    print("Id - Nome")
    for lutador in lista_lutadores:
        print(f"{lutador.id_lutador} - {lutador.nome}")
    print()

# Ver Detalhe  de Lutador#

def ver_detalhes_lutador():
    if len(lista_lutadores) == 0:
        print("Ainda não existem lutadores")
        sleep(1)
        return
    while True:
        try:
            id = int(input('Digite o Número de Registro do lutador (caso não saiba, digite 0): '))
            if id == 0:
                ver_lutadores_existentes()
                continue
            break
        except ValueError:
            print('Digite um valor valido')
            sleep(1)
            continue
    for lutador in lista_lutadores:
        if lutador.id_lutador == id:
            print(lutador)
            break





# ######################################################## #
# ################# Aleatorio ############################ #
# ######################################################## #

def torneio_aleatorio():
    pass


# ################################################### #
# ################# Main ############################ #
# ################################################### #


def main():
    while True:
        imprime_menu_principal()
        acao_principal = input("O que deseja? ")
        if acao_principal not in ['1', '2', '3', '4']:
            print("Digite valores validos\n")
            sleep(2)
            continue
        elif acao_principal == '1':
            sleep(1)
            print()
            menu_do_torneio()
        elif acao_principal == '2':
            sleep(1)
            print()
            menu_do_lutador()
        elif acao_principal == '3':
            sleep(1)
            print()
            torneio_aleatorio()
        elif acao_principal == '4':
            break

def imprime_menu_principal():
    print("#############################")
    print("1- Menu de Torneio")
    print("2- Menu de Lutador")
    print("3- Criar Torneio Aleatório")
    print("4- Sair")
    print("#############################")








if __name__ == "__main__":
    main()