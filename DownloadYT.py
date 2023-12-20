import pytube

def inicio():

    escolha=int(input("Digite 1 para baixar video ou Digite 2 para baixar o audio "))
    if escolha==1:downloadvidio()
    if escolha==2:downloadaudio()


def downloadvidio(): 


    linkpy=input("Cole o link: ")

    try: #tentar
        vidio = pytube.YouTube(url=linkpy).streams.get_highest_resolution()
        
        vidio.download()

    except:
        print("Tente novamente")

def downloadaudio():

    linkpy=input("Cole o link do audio: ")

    try:
        audio = pytube.YouTube(url=linkpy).streams.get_audio_only()

        audio.download()
    except:
        print("tentar de novo ")
inicio()