import datetime
from datetime import datetime
import Adafruit_DHT as dht
import RPi.GPIO as gpio
import time
import requests
from random import randint
import time
gpio.setmode(gpio.BCM)

menu = True
e = False
h = False
dataAtual = datetime.now()
dataAtual = dataAtual.strftime('%d/%m/%Y')
print(dataAtual)
while menu == True:
    print("\n   /===/ Temperatura Spreadsheet & Envio de dados a nuvem /===/")
    print(" 1) Digite 1 para setar o horario de start.")
    print(" 2) Digite 2 para setar o delay entre o envio de dados.")
    print(" 3) Digite 3 para iniciar o programa.")
    entrada = int(input(""))
    if entrada == 1:
        print("\nInsira o horario desejado:")
        print("Formato: hora:minutos")
        horario = str(input(""))
        print("\nHorario: '"+horario+"' setado com sucesso!")
        h = True
    elif entrada == 2:
        print("\nInsira o delay entre o envio de dados:")
        print("Formato: segundos")
        delay = int(input(""))
        print("\nDelay: '"+str(delay)+"' segundos, setado com sucesso!")
        e = True
    elif entrada == 3:

            if h == True & e == True:
                    horaatual2 = datetime.now()
                    horaatual2 = horaatual2.strftime('%H:%M')
                    while horaatual2 < horario:
                        horaatual2 = datetime.now()
                        horaatual2 = horaatual2.strftime('%H:%M')
                        print("Aguardando tempo setado.")
                        time.sleep(5)
                    while horaatual2 >= horario:
                        try:
                            while True:
                                    humidade, temperatura = dht.read_retry(dht.DHT11, 4)
                                    horaatual = datetime.now()
                                    horaatual = horaatual.strftime('%H:%M')
                                    dataAtual = datetime.now()
                                    dataAtual = dataAtual.strftime('%d/%m/%Y')
                                    time.sleep(delay)
                                    r = requests.get(
                                            "https://script.google.com/macros/s/AKfycbwgJbIVzosgQz3Kk7JIfLfl7JLgBIrTdj1h_beQoAOjIS-Ojak/exec?temperatura=" + str(temperatura) + "C&" + "horario=" + str(horaatual)+"&"+"humidade="+str(humidade))
                                    print("\n" + r.text)
                                    print("Pressione ctrl + C  para encerrar o envio.")
                        except KeyboardInterrupt:
                            break

    else:
            print("\nEntre com os dados de start e delay!")

