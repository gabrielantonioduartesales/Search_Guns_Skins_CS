import customtkinter 
import requests
import pandas as pd
import urllib.request
from PIL import Image, ImageTk
import pygame
pygame.init()
nome_descricao=[]
requiscao = requests.get('https://bymykel.github.io/CSGO-API/api/pt-BR/skins.json',verify=False)
dados = requiscao.json()
df = pd.DataFrame(dados).drop(['id', 'weapon', 'pattern', 'min_float', 'max_float', 'rarity'], axis=1)

skins = df.to_dict(orient='index')

customtkinter.set_appearance_mode("dark")


app = customtkinter.CTk()
app.geometry("900x600")
app.title("Consulta Skins")
app.resizable(False,False)
#OBS: Aqui no código "music.load" antes de execultar o código deve verificar se a música está na mesma página.
pygame.mixer.music.load("music_cs.mp3")
pygame.mixer.music.play()
#OBS: Aqui no código "Image.open" antes de execultar o código deve verificar se a imagem está na mesma página.
tela_fundo = Image.open('imagem_cs.jpg')
tela_fundo=tela_fundo.resize((1200,800), Image.ANTIALIAS)
tela_fundo_x=ImageTk.PhotoImage(tela_fundo)
canvas = customtkinter.CTkCanvas(app, width=1200, height=800)
canvas.pack()
canvas.create_image(0, 0, anchor='nw', image=tela_fundo_x)

def Consultar_skins():
    arma = Arma_gui.get()
    if arma:
        global skins_dic,nome_arma,nome_desc
        skins_dic = {}
        for skin, dados in skins.items():
            if arma.lower() in dados['name'].lower():
                skins_dic [dados['name']] = [dados['image'],dados['description']]
        Skins_escolha.configure(values = list(skins_dic.keys()))

def Mostrar_skin(SKIN):
    global skins_dic
    for chave,valor in skins_dic.items():
        if chave==SKIN:
            urllib.request.urlretrieve(valor[0],"skin.png")
            imagem_skin = customtkinter.CTkImage(light_image=Image.open("skin.png"), dark_image=Image.open("skin.png"),size=(400,200))
            label.configure(image= imagem_skin)
            label02.configure(text=chave,font=('Futura Extra Bold',20),wraplength=425)
            label03.configure(text=valor[1],font=('Futura Extra Bold',20),wraplength=425)



Skins_escolha = customtkinter.CTkOptionMenu(master=app,values=[""],command=Mostrar_skin,width=300,height=60)
Skins_escolha.place(relx=0.3, rely=0.35, anchor=customtkinter.N)



texto = customtkinter.CTkLabel(app, text="Busca de skins CS GO",text_color= 'white', font = ('Futura Extra Bold',50))
texto.place(relx=0.5, rely=0.01, anchor=customtkinter.N)

Arma_gui = customtkinter.CTkEntry(app,width=300,height=60,font = ('Futura Extra Bold',40),fg_color= 'gray',placeholder_text='Insira a arma desejada')
Arma_gui.place(relx=0.3, rely=0.2, anchor=customtkinter.N)

botao_Busca= customtkinter.CTkButton(app,width=300,height=45,text="Buscar",font=('Futura Extra Bold',20),command=Consultar_skins,fg_color='Green')
botao_Busca.place(relx = 0.3, rely = 0.5, anchor = customtkinter.N)

label = customtkinter.CTkLabel(app,text='')
label.place(relx=0.5,rely=0.2)

label02 = customtkinter.CTkLabel(app,text='')
label02.place(relx=0.5,rely=0.15)

label03 = customtkinter.CTkLabel(app,text='')
label03.place(relx=0.5,rely=0.55)

app.mainloop()
pygame.mixer.music.stop()