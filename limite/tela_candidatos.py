from limite.abstract_tela import Tela


class TelaCandidatos(Tela):

    def mostra_tela_candidatos(self):
        print('-' * 20)
        print('Candidatos')
        print('-' * 20)
        print('1 - Ver Lista de Candidatos')
        print('2 - Adicionar Candidatos')
        print('3 - Remover Candidatos')
        print('4 - Definir Máximo de Candidatos')
        print('0 - Voltar ao Menu Principal')
        opcao = self.pega_opcao('Escolha uma opção: ', [1, 2, 3, 4, 0])
        return opcao

    def mostra_candidato(self, dados_candidato):
        print(f"Nome: {dados_candidato['nome']}")
        print(f"Cpf: {dados_candidato['cpf']}")
        print(f"Categoria: {dados_candidato['categoria']}")
        print(f"Número: {dados_candidato['numero']}")
        print(f"Chapa: {dados_candidato['chapa']}")
        print(f"Cargo: {dados_candidato['cargo']}")

    def pega_opcao(self, mensagem: str = "", opcoes_validas: [] = None):
        while True:
            valor_lido = input(mensagem)
            try:
                opcao = int(valor_lido)
                if opcoes_validas and opcao not in opcoes_validas:
                    raise ValueError
                return opcao
            except ValueError:
                print("Opção indisponível, tente uma opção válida.")
                if opcoes_validas:
                    print('Opções válidas: ', opcoes_validas)
