from entidade.categoria import Categoria
from limite.tela_categoria import TelaCategoria
import PySimpleGUI as psg


class ControladorCategoria():
    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_categoria = TelaCategoria()

    def mostra_tela_inicial(self):
        if self.__ctrl_sistema.ctrl_urna.urna.turno == 3:
            self.__tela_categoria.mostra_mensagem('AVISO', 'ELEIÇÕES ENCERRADAS')
            return self.__ctrl_sistema.abre_menu_inicial()
        self.__tela_categoria.tela_categorias([x.name for x in self.__ctrl_sistema.ctrl_urna.urna.categorias])
        while True:
            event, values = self.__tela_categoria.abre()
            if event in ('SAIR', psg.WIN_CLOSED):
                self.__tela_categoria.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
