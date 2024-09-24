#Criando Layout
import PySimpleGUI as sg

def criar_novatarefa():
    sg.theme('reddit')
    linha = [
        [sg.Checkbox(''),sg.Input('')]
    ]
    layout = [
        [sg.Frame('Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True)
#Criar Janela
janela = criar_novatarefa()
#Criar as regras da janela
while True:
    event, values = janela.read()
    if event == sg.WIN_CLOSED   :
        break
    elif event == 'Nova Tarefa':
        janela.extend_layout(janela['container'], [[sg.Checkbox(''),sg.Input('')]])
    elif event == 'Resetar':
        janela.close()
        janela = criar_novatarefa()