
from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout = [ 
    [sg.Text('Usuario'), sg.Input(key='usuario')],
    [sg.Text('senha'), sg.Input(key= 'senha', password_char='*')],
    [sg.Checkbox('salvar o login')],
    [sg.Button('entrar')]

]
#janela
janela = sg.Window('Tela de login', layout)

#ler os eventos 
while True:
 eventos, valores = janela.read()
 if eventos  == sg.WINDOW_CLOSED:
     break
if eventos == 'Entrar':
    if valores['usuario'] == 'jhonatan' and valores['senha'] == ('123456'):
        print('bem vindo')