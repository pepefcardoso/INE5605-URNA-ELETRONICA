from limite.tela_candidatos import TelaCandidatos
from entidade.candidato import Candidato
from entidade.cargo import Cargo
from entidade.chapa import Chapa
import PySimpleGUI as psg


class ControladorCandidatos:

    def __init__(self, ctrl_sistema):
        self.__ctrl_sistema = ctrl_sistema
        self.__tela_candidatos = TelaCandidatos()

    def mostra_tela_inicial(self):
        if self.__ctrl_sistema.ctrl_urna.urna.turno == 3:
            self.__tela_candidatos.mostra_mensagem('AVISO', 'ELEIÇÕES ENCERRADAS')
            return self.__ctrl_sistema.abre_menu_inicial()
        lista = self.__ctrl_sistema.ctrl_urna.lista_candidatos()
        self.__tela_candidatos.tela_opcoes(lista)
        opcoes = {'REMOVER': self.remove_candidato,
                  'ALTERAR': self.altera_candidato}
        while True:
            event, values = self.__tela_candidatos.abre()
            if event in ('VOLTAR', psg.WIN_CLOSED):
                self.__tela_candidatos.fecha()
                return self.__ctrl_sistema.abre_menu_inicial()
            if event == 'ADICIONAR':
                self.__tela_candidatos.fecha()
                return self.adiciona_candidato()
            if event in ('REMOVER', 'ALTERAR'):
                if values['LISTA'] == []:
                    self.__tela_candidatos.mostra_mensagem('ERRO', "NENHUM CANDIDATO FOI SELECIONADO")
                else:
                    self.__tela_candidatos.fecha()
                    return opcoes[event](lista[values['LISTA'][0]])

    def adiciona_candidato(self):
        chapas = [i[1] for i in self.__ctrl_sistema.ctrl_urna.lista_chapas()]
        cargos = [c.name for c in Cargo]
        cpf_eleitores = self.__ctrl_sistema.ctrl_urna.lista_cpf_eleitores()
        if chapas == []:
            self.__tela_candidatos.mostra_mensagem('ERRO', 'SEM CHAPAS CADASTRADAS!')
            self.__tela_candidatos.fecha()
            return self.mostra_tela_inicial()
        if cpf_eleitores == []:
            self.__tela_candidatos.mostra_mensagem('ERRO', 'SEM ELEITORES CADASTRADOS!')
            self.__tela_candidatos.fecha()
            return self.mostra_tela_inicial()
        self.__tela_candidatos.tela_adiciona_candidato(cpf_eleitores,chapas, cargos)
        while True:
            event, values = self.__tela_candidatos.abre()
            if event in ('CANCELAR', psg.WIN_CLOSED):
                self.__tela_candidatos.fecha()
                return self.mostra_tela_inicial()
            if event == 'SALVAR':
                cpf = values['1'].strip()
                numero = values['2'].strip()
                chapa = values['3'].strip()
                cargo = values['4'].strip()
                try:
                    if self.__ctrl_sistema.ctrl_urna.adiciona_candidato(cpf, numero, chapa, cargo):
                        self.__tela_candidatos.mostra_mensagem('SUCESSO', 'CANDIDATO ADICIONADO!')
                        self.__tela_candidatos.fecha()
                        return self.mostra_tela_inicial()
                except Exception as e:
                    self.__tela_candidatos.mostra_mensagem('ERRO', e)

    def remove_candidato(self, candidato: list):
        if candidato is not None and candidato != []:
            self.__tela_candidatos.tela_remove_candidato(candidato)
            while True:
                event, values = self.__tela_candidatos.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_candidatos.fecha()
                    return self.mostra_tela_inicial()
                if event == 'CONFIRMAR':
                    try:
                        if self.__ctrl_sistema.ctrl_urna.remove_candidato(candidato[1]):
                            self.__tela_candidatos.mostra_mensagem('SUCESSO', 'CANDIDATO REMOVIDO!')
                            self.__tela_candidatos.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_candidatos.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()

    def altera_candidato(self, candidato: list):
        chapas = [i[1] for i in self.__ctrl_sistema.ctrl_urna.lista_chapas()]
        cargos = [c.name for c in Cargo]
        if candidato is not None and candidato != []:
            self.__tela_candidatos.tela_altera_candidato(candidato, chapas, cargos)
            while True:
                event, values = self.__tela_candidatos.abre()
                if event in ('CANCELAR', psg.WIN_CLOSED):
                    self.__tela_candidatos.fecha()
                    return self.mostra_tela_inicial()
                if event == 'SALVAR':
                    numero = values['1'].strip()
                    chapa = values['2'].strip()
                    cargo = values['3'].strip()
                    try:
                        if self.__ctrl_sistema.ctrl_urna.altera_candidato(candidato[1], numero, chapa, cargo):
                            self.__tela_candidatos.mostra_mensagem('SUCESSO', 'CANDIDATO ALTERADO!')
                            self.__tela_candidatos.fecha()
                            return self.mostra_tela_inicial()
                    except Exception as e:
                        self.__tela_candidatos.mostra_mensagem('ERRO', e)
        return self.mostra_tela_inicial()
