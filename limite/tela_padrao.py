class TelaPadrao():

    def abre_tela_inicial(self, nome_menu: str = '', opcoes_menu: list = [], msg_saida: str = ''):
        print(f'\n----- {nome_menu} -----\n')
        i = 1
        for opcao in opcoes_menu:
            print(f'{i} - {opcao}')
            i += 1
        print(f'0 - {msg_saida}\n')

    def pega_opcao(self, mensagem: str = "", opcoes_validas: list = []):
        while True:
            valor_lido = input(mensagem)
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")

    def mostra_entidade(self, dados_entidade: dict = {}):
        for key in dados_entidade:
            print(f'{key}: {dados_entidade[key]}')

    def mostra_mensagem(self, mensagem: str):
            print(mensagem)