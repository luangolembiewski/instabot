from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from webdriver_manager.chrome import ChromeDriverManager
from PySimpleGUI import PySimpleGUI as sg

class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def login(self):
        driver = self.driver
        driver.maximize_window()
        driver.get("http://www.instagram.com")
        time.sleep(5)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username) 
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password) 
        campo_senha.send_keys(Keys.RETURN)

    @staticmethod
    def digite_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comenta_foto(self,url):
        time.sleep(20)
        driver = self.driver
        driver.get(url)
        time.sleep(5)
        x=0
        y=0
        #comentarios = ["Ja ganhei","Eu quero"]
        comentarios = ["ok","ok"]
        #comentarios = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        while (qComentarios > x):
            try: 
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(1,3))
                self.digite_pessoa(random.choice(comentarios),campo_comentario)
                time.sleep(random.randint(120,150))
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                
                x = x+1
                print("COMENTARIOS:", x, '/',qComentarios)
                time.sleep(5)
            except Exception as e:
                y = y+1
                print("Erro:",y)
                time.sleep(5)

sg.theme('Reddit')
layout = [
    [sg.Text('Url da publicação'),sg.Input(key='url')],
    [sg.Text('Quant. Comentarios'),sg.Input(key='qComentarios')],
    [sg.Text('Usuário'),sg.Input(key='usuario')],
    [sg.Text('Senha'),sg.Input(key='senha', password_char='*')],
    [sg.Button('Entrar')]
]

janela = sg.Window('Tela de login', layout)
eventos, valores = janela.read()
usuario = valores['usuario']
senha = valores['senha']
url = valores['url']

qComentarios = valores['qComentarios']
qComentarios = (int(qComentarios))

janela.close()
time.sleep(2)

print("INICIANDO...")
luanBot = InstagramBot(usuario,senha)
luanBot.login()
luanBot.comenta_foto(url)
print ("FIM DO PROGRAMA")