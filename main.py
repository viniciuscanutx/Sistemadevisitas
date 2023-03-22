import PySimpleGUI as sg
import os
import pyshorteners
import clipboard 

class SystemClients:
    def __init__(self):
        sg.theme('Reddit')
        layout = [
            [sg.Text('Nome:',size=(12,1)), sg.Input(key='name1', size=(35, 1))],
            [sg.Text('Numero:',size=(12,1)), sg.Input(key='nmr1', size=(15, 1))],
            [sg.Text('Data Visita:',size=(12,1)), sg.Input(key='dat1', size=(15, 1))],
            [sg.Text('Endereço:',size=(12,1)), sg.Input(key='end1', size=(35, 1))],
            [sg.Text('Motivo:',size=(12,1)), sg.Input(key='mot1', size=(35, 1))],
            [sg.Output(size=(52, 7))],
            [sg.Button('Cadastrar'), sg.Button('Exportar'), sg.Button('Fechar')]
        ]
        
        self.janela = sg.Window('System', layout)
        
    def Iniciar(self):
     while True:
      evento, valores = self.janela.read()
      if evento == sg.WINDOW_CLOSED:
                break
      if evento == 'Fechar':
                break


    def cadastro1(self, valores):
       name2 = (valores['name1']) 
       nmr2 = (valores['nmr1'])
       dat2 = (valores['dat1'])
       end2 = (valores['end1'])
       mot2 = (valores['mot1'])
       short_end1 = (f'Nome:' + name2 + '\n Número de Telefone: ' + nmr2 + '\n Data de Visita: ' + dat2 + '\n Endereço: ' + end2 + '\n Motivo:  ' +  mot2)
       print('\n Solicitação de visita:')
       return short_end1
       

gen = SystemClients()
gen.Iniciar()