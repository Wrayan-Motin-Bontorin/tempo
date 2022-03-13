from fileinput import close
import requests
import json
import PySimpleGUI as sg


class previsao_do_tempo:
    def __init__(self):
        self.api_key = 'ef337c2024c0a8a6b1420c2a843f5200'
        sg.theme('black')
        layout = [
            [sg.Text('Cidade', size=8), sg.Input(size=25, key='Cidade')],
            [sg.Text('Estado', size=8), sg.Input(size=25, key='Estado')],
            [sg.Button('enviar', key='enviar')],
            [sg.Output(40,100)]
        ]
        self.janela = sg.Window("clima tempo").layout(layout)
        self.janela.set_icon 

    def Iniciar(self):
        while True:
            self.Button, self.values = self.janela.Read()
            self.Cidade = self.values['Cidade']
            self.Estado = self.values['Estado']
            link = (f'https://api.openweathermap.org/data/2.5/weather?q={self.Cidade},{self.Estado}BR&appid={self.api_key}&lang=pt_br')
            req = requests.get(link)
            req_dic = req.json()
            descricao = req_dic['weather'][0]['description']
            temperatura = round(req_dic['main']['temp'] - 273.15)
            humidity = req_dic['main']['humidity']
            print(f'O dia esta {descricao}\nA temperatura e de {temperatura}°C\nA humdade e de {humidity}%\nEm {self.Cidade}\nNo {self.Estado}')


tela = previsao_do_tempo()
tela.Iniciar()
