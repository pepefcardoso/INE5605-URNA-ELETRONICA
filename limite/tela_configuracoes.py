import PySimpleGUI as psg


class TelaConfiguracoes():
    def __init__(self):
        self.__window = None

    def tela_configuracoes(self, max_eleitores: str, max_candidatos: str):
        psg.ChangeLookAndFeel('Reddit')
        layout = [[psg.Text('CONFIGURAÇÕES')],
                  [psg.Text('Nº MÁXIMO DE ELEITORES: '), psg.InputText(max_eleitores, key='ELEITORES')],
                  [psg.Text('Nº MÁXIMO DE CANDIDATOS: '), psg.InputText(max_candidatos, key='CANDIDATOS')],
                  [psg.Submit('ALTERAR'), psg.Cancel('VOLTAR')]]
        layout = [[psg.Sizer(0, 200), psg.Column([[psg.Sizer(500, 0)]] + layout, element_justification='c', pad=(0, 0))]]
        self.__window = psg.Window('URNA ELETRÔNICA UFSC - CONFIGURAÇÕES', layout, margins=(0, 0))

    def abre(self):
        button, values = self.__window.Read()
        return button, values

    def fecha(self):
        self.__window.Close()

    def atualiza_dados(self, max_eleitores: str, max_candidatos: str):
        self.__window['ELEITORES'].Update(max_eleitores)
        self.__window['CANDIDATOS'].Update(max_candidatos)
        self.__window.Refresh()

    def mostra_mensagem(self, titulo: str, mensagem: str):
        psg.Popup(titulo, mensagem)
