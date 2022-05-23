import speech_recognition as sr
import wikipedia
import pyttsx3
import time
from tkinter import messagebox
import winsound
from tkinter import *
from tkcalendar import *
import datetime as dt
import pywhatkit
import sounddevice as sd
from scipy.io.wavfile import write
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

while True:
    audio = sr.Recognizer()
    maquina = pyttsx3.init()
    maquina.say('Olá, meu nome é BÉTA, Qual função deseja acessar, Pesquisa, Pomodóro, Datas, Gravador de voz, '
                'toque, livro')
    maquina.runAndWait()


    def executa_comando():

        try:
            with sr.Microphone() as source:
                print('Ouvindo...')
                voz = audio.listen(source)
                comando = audio.recognize_google(voz, language='pt-BR')
                comando = comando.lower()

                if 'beta' in comando:
                    comando = comando.replace('beta', '')
                    maquina.say(comando)
                    maquina.runAndWait()
        except:
            print('Microfone não está conectado')
        return comando


    def comando_voz_usuario():
        comando = executa_comando()
        if 'pesquisa' in comando:
            procurar = comando.replace('pesquisa', '')
            wikipedia.set_lang('pt')
            resultado = wikipedia.summary(procurar, 2)
            maquina.say(resultado)
            maquina.runAndWait()
        elif 'datas' in comando:
            root = Tk()
            root.title("Calendário")
            root.geometry("500x350")
            root.config(bg="gray")

            t_now = dt.datetime.now()  # Coleta data e hora atual
            data = t_now.date()  # Coleta somente data atual
            ano = int(data.strftime("%Y"))  # Coleta ano atual
            mes = int(data.strftime("%m"))  # Coleta mes atual
            dia = int(data.strftime("%d"))  # Coleta dia atual

            cal = Calendar(root, select="day", year=ano, month=mes, day=dia)
            cal.pack(pady=20, fill="both", expand="yes")

            root.mainloop()
        elif 'pomodoro' in comando:

            t_now = dt.datetime.now()  # data e hora atual;

            t_pom = 25 * 60  # tempo de duração do fluxo pomodoro 25m;

            t_delta = dt.timedelta(0, t_pom)  # diferença de tempo;

            t_fut = t_now + t_delta  # hora que o pomodoro termina e começa a pausa;

            delta_sec = 5 * 60  # definição de intervalo;

            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)  # hora que a pausa termina;

            pomodoro = pyttsx3.init()

            pomodoro.say("Pomodóro iniciado " "\n\nAgora é " + t_now.strftime(

                "%H:%M") + " hrs. \n\nTemporizador definido por 25 minutos")

            pomodoro.runAndWait()

            total_pomodoros = 0

            breaks = 0

            # Looping simples dividido em três seções: Hora pomodoro, intervalo e fim do código;

            while True:

                if dt.datetime.now() < t_fut:

                    print('Pomodóro')

                elif t_fut <= dt.datetime.now():

                    if total_pomodoros in range(3, 100, 5):

                        for i in range(1):
                            winsound.Beep((i + 400), 500)  # Primeiro número é referente ao volume do bip.

                        print('Hora do intervalo! Você tem 25 minutos de descanso.')

                        breaks += 1

                        audio = sr.Recognizer()

                        pomodoro = pyttsx3.init()

                        pomodoro.say('Hora do intervalo!')

                        pomodoro.runAndWait()

                        time.sleep(
                            5)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 25 min ficou 21 min

                        print("Foi")

                    if breaks == 0:

                        for i in range(2):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.

                        print('Hora do intervalo!')

                        breaks += 1

                        audio = sr.Recognizer()

                        pomodoro = pyttsx3.init()

                        pomodoro.say('Hora do intervalo! Você tem 5 minutos de descanso.')

                        pomodoro.runAndWait()

                        time.sleep(
                            5)  # Por conta do delay da fala subtrair do tempo de pausa um tempo,então o que era pra ser 5 min ficou o tempo determinado como 1260 dividido por 5, pra ficar um descanso proporcional.

                    else:

                        print('Fim')

                        breaks = 0

                        for i in range(1):
                            winsound.Beep((i + 400), 700)  # Primeiro número é referente ao volume do bip.

                            audio = sr.Recognizer()

                            pomodoro = pyttsx3.init()

                            pomodoro.say('O intervalo acabou, deseja iniciar um novo pomodóro?')

                            pomodoro.runAndWait()

                        usr_ans = messagebox.askyesno("Fim da primeira sequência do pomodóro",

                                                      "Deseja iniciar outra sequência de pomodóro?")

                        total_pomodoros += 1

                        print(total_pomodoros)

                        if usr_ans == True:

                            t_now = dt.datetime.now()

                            t_fut = t_now + dt.timedelta(0, t_pom)

                            t_fin = t_now + dt.timedelta(0, t_pom + delta_sec)


                        elif usr_ans == False:

                            msg = messagebox.showinfo("Fim do pomodóro",

                                                      "\nVocê completou " + str(total_pomodoros) + " pomodóro(s) hoje!")

                            break

                    print("sleeping")

                    time.sleep(1)

                    t_now = dt.datetime.now()

                    timenow = t_now.strftime("%H:%M")
        elif 'toque' in comando:
            musica = comando.replace('toque', '')
            resultado = pywhatkit.playonyt(musica)
            maquina.say('Iniciando musica')
            maquina.runAndWait()
        elif 'gravador de voz' in comando:
            freq = 44100
            seconds = 10

            gravacao = sd.rec(int(seconds * freq), samplerate=freq, channels=2)
            print("Começando: Fale agora!!")
            sd.wait()
            print("Fim da gravação!")
            write('output.wav', freq, gravacao)
            os.startfile("output.wav")
        elif 'livro' in comando:
            maquina.say('Estou pesquisando o livro que pediu')
            maquina.runAndWait()
            consulta = comando.replace('livro', '')
            try:
                from googlesearch import search
            except ImportError:
                print("Resultado não encontrado")
            X = []
            for j in search(consulta, tld="co.in", num=10, stop=10,
                            pause=2):  # Retorna um compilado dos 10 primeiros links que aparecem na pesquisa google
                X.append(j)  # Converte o compilado de links em lista para manipular sua posição no pdf
            print(X)

            def mm2p(milimetros):
                return milimetros / 0.352777  # converte pontos em milimetros

            cnv = canvas.Canvas('SUA_PESQUISA.pdf', pagesize=A4)  # Define o nome do arquivo pdf e o tamanho da página

            eixo = 250

            for i in range(0, 10):
                cnv.drawString(mm2p(20), mm2p(eixo), X[i])
                eixo -= 5  # colocado menos para os links aparecerem na ordem correta
            cnv.save()  # salva o pdf na pasta downloads do PC

            maquina.say('Foram pesquisados 10 links que estão salvos em pdf em sua pasta downloads')
            maquina.runAndWait()
        elif 'clima' in comando:
            audio = sr.Recognizer()
            maquina = pyttsx3.init()
            with sr.Microphone() as source:
                maquina.say("Informe a cidade da qual deseja descobrir a temperatura. ")
                maquina.runAndWait()
                print('ouvindo...')
                voz = audio.listen(source)
                cidade = audio.recognize_google(voz, language='pt-BR')
                print(cidade)


                API_KEY = "00a7922cfcccb7df823f10e7014e2e42"
                link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

                requisicao = requests.get(link)
                requisicao_dic = requisicao.json()  # Faz a requisição
                descricao = requisicao_dic['weather'][0]['description']  # Puxa a descrição de como esta o clima
                temperatura = requisicao_dic['main']['temp'] - 273.15  # Puxa a temperatura atual e faz a conversão
                maquina = pyttsx3.init()
                maquina.say(f'Em {cidade} o céu está {descricao} e está {temperatura:.0f}ºC hoje')
                maquina.runAndWait()


    comando_voz_usuario()
