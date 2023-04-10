from assets import *

class SystemClients:
    def __init__(self):
        
        sg.theme('DarkGrey6')
        layout = [
            [sg.Text('Nome:',size=(12,1)), sg.InputText(key='Nome', size=(35, 1))],
            [sg.Text('Telefone:',size=(12,1)), sg.InputText(key='Numero', size=(35, 1))],
            [sg.Text('Data da Visita:',size=(12,1)), sg.Input(key='Data', size=(18, 1)), sg.CalendarButton("Selecione a Data", close_when_date_chosen=True,  target='Data', no_titlebar=True)],
            [sg.Text('Endereço:',size=(12,1)), sg.Input(key='Endereço', size=(35, 1))],
            [sg.Text('Complemento:',size=(12,1)), sg.Input(key='Complemento', size=(35, 1))],
            [sg.Text('Descrição do Serviço:',size=(16,1)), sg.InputText(key='Serviço', size=(31,3))],
            [sg.Output(size=(49, 9))],
            [sg.Button('Registrar'), sg.Button('Fechar')]
        ]
        
       
        self.janela = sg.Window('Registro de Chamados', layout, icon=r'img/icon1.ico')
        
    
    def Iniciar(self):
     while True:
      evento, valores = self.janela.read()
      if evento == sg.WINDOW_CLOSED:
        break
      if evento == 'Registrar':
        cadastrodone = self.cadastro1(valores)
        print(cadastrodone)
      if evento == 'Fechar':
        break


    def cadastro1(self, valores):
       name2 = (valores['Nome']) 
       nmr2 = (valores['Numero'])
       dat2 = (valores['Data'])
       end2 = (valores['Endereço'])
       mot2 = (valores['Complemento'])
       serv2 = (valores['Serviço'])
       short_end1 = (f' Nome: ' + name2 + '\n Número de Telefone: ' + nmr2 + '\n Data de Visita: ' + dat2 + '\n Endereço: ' + end2 + '\n Complemento:' + mot2 + '\n Serviço:  ' +  serv2)
       print(' Solicitação de visita: \n ')
       dados = [(valores)]
       df = pd.DataFrame(dados)
       df.to_excel('TelaCadTeste.xlsx', index = False)
       return short_end1
    
     
gen = SystemClients()
gen.Iniciar()