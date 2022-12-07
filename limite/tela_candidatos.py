import PySimpleGUI as psg


class TelaCandidatos():
    def __init__(self):
        self.__window = None

    def tela_opcoes(self, lista_candidatos: list):
        psg.ChangeLookAndFeel('Reddit')
        headings = ['NOME', 'CPF', 'CATEGORIA', 'NÚMERO', 'CHAPA', 'CARGO']
        layout = [[psg.Table(values=lista_candidatos,
                             headings=headings,
                             key='LISTA',
                             vertical_scroll_only=True,
                             auto_size_columns=False,
                             col_widths=(19,19,19,19,19,19),
                             num_rows=38,
                             enable_events=True)],
                  [psg.Button('ADICIONAR'),
                   psg.Button('ALTERAR'),
                   psg.Button('REMOVER'),
                   psg.Button('VOLTAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CANDIDATOS', size=(1080,720)).Layout(layout)

    def tela_adiciona_candidato(self, cpf_eleitores:list, chapas: list, cargos: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('- O CANDIDATO DEVE POSSUIR UM ELEITOR CADASTRADO COM SEU CPF')],
                  [psg.Text('CPF: '), psg.Combo(cpf_eleitores, key='1')],
                  [psg.Text('NÚMERO: '), psg.InputText(key='2')],
                  [psg.Text('CHAPA: '), psg.Combo(chapas, key='3')],
                  [psg.Text('CARGO: '), psg.Combo(cargos, key='4')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ADICIONAR CANDIDATO', size=(1080,720)).Layout(layout)

    def tela_remove_candidato(self, candidato: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR A REMOÇÃO DO ELEITOR:')],
                  [psg.Text(f'NOME: {candidato[0]}')],
                  [psg.Text(f'CPF: {candidato[1]}')],
                  [psg.Text(f'CATEGORIA: {candidato[2]}')],
                  [psg.Text(f'NÚMERO: {candidato[3]}')],
                  [psg.Text(f'CHAPA: {candidato[4]}')],
                  [psg.Text(f'CARGO: {candidato[5]}')],
                  [psg.Submit('CONFIRMAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - REMOVER CANDIDATO', size=(1080,720)).Layout(layout)

    def tela_altera_candidato(self, candidato: str, chapas: list, cargos: list):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIRMAR ALTERAÇÃO DO CANDIDATO:')],
                  [psg.Text(f'NOME: {candidato[0]}')],
                  [psg.Text(f'CPF: {candidato[1]}')],
                  [psg.Text(f'CATEGORIA: {candidato[2]}')],
                  [psg.Text('NÚMERO: '), psg.InputText(candidato[3], key='1')],
                  [psg.Text('CHAPA: '), psg.Combo(chapas, candidato[4], key='2')],
                  [psg.Text('CARGO: '), psg.Combo(cargos, candidato[5], key='3')],
                  [psg.Submit('SALVAR'), psg.Cancel('CANCELAR')]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - ALTERAR CANDIDATO', size=(1080,720)).Layout(layout)

    def abre(self):
        event, values = self.__window.Read()
        return event, values

    def fecha(self):
        self.__window.Close()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)
