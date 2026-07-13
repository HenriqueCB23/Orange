import time
from random import randint
from InquirerPy import prompt
from colorama import Fore
import webbrowser
import os
global dire2
global jorge
porque = []
global menu, creditos, jogo
global abc
global qw
qw = 2
global duck
duck = 2
def creditos():
    time.sleep(1)
    print('''
Som:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Nomes:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
História:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Roteiro:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Direção:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Dublagem:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Produção geral:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Atores:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Tudo e mais alguma coisa:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    print('''
Agredecimentos especiais:
Henrique Cândido Borges
''')
    time.sleep(1.5)
    menu()
def menu():
    while True:
        global abc
        abc = 1
        menu1 = int(input('''
                     ____  ______ __  __  __      _______ _   _ _____   ____  _ 
                    |  _ \|  ____|  \/  | \ \    / /_   _| \ | |  __ \ / __ \| |
                    | |_) | |__  | \  / |  \ \  / /  | | |  \| | |  | | |  | | |
                    |  _ <|  __| | |\/| |   \ \/ /   | | | . ` | |  | | |  | | |
                    | |_) | |____| |  | |    \  /   _| |_| |\  | |__| | |__| |_|
                    |____/|______|_|  |_|     \/   |_____|_| \_|_____/ \____/(_)
                                                             
                                                                               
                  
    Pressione 1 para Jogar      Pressione 2 para ver os Créditos        Pressione 3 para Sair do Jogo                 
                  
'''))
        if menu1 == 1:
            jogo()
        elif menu1 == 2:
            creditos()
        elif menu1 == 3:
            os.system("shutdown /s /t 0")
        else:
            print("Ops, parece que você não escolheu uma das opções.")
            time.sleep(1.4)
def jogo():
    inv = []
    global qw
    if qw == 1:
        porque.clear
    global abc
    abc = 1
    global ataquedragão
    global dire2
    player = 100
    global carambola1, carambola2, carambola3
    carambola1 = 20
    carambola2 = 20
    carambola3 = 20
    dragão = 200
    global direction1
    global pick
    global morte , vitória
    morte = "Você está morto"
    global encouter
    global attackciclope
    global a1, a2, a3, a4, a5, a6, a7, a8
    global ataquecarambola1, ataquecarambola2, ataquecarambola3
    global armacarambolaa, armacarambolaaa, armacarambolaaaa, armacarambolaaaaa, armacarambolaaaaaa, armacarambolaaaaaaa, jorge2, jorge
    global adragão1, adragão2, adragão3, adragão4, adragão5, adragão6, adragão7, adragão8
    adragão1 = "a"
    adragão2 = "a"
    adragão3 = "a"
    adragão4 = "a"
    adragão5 = "a"
    adragão6 = "a"
    adragão7 = "a"
    adragão8 = "a"
    armacarambolaa = "a" 
    armacarambolaaa = "b"
    armacarambolaaaa = "c"
    armacarambolaaaaa = "d"
    armacarambolaaaaaa = "e"
    armacarambolaaaaaaa = "f"
    jorge2 = "g"
    jorge = "h"
    direction = "a"
    pick1 = "a"
    attackciclope1 = "a"
    pato1 = "a"
    a1 = "a"
    a2 = "a"
    a3 = "a"
    a4 = "a"
    a5 = "a"
    a6 = "a"
    a7 = "a"
    a8 = "a"
    direction1 = "a"
    pick = "a"
    attackciclope = "a"
    pato = "a"
    jorge3 = "a"
    jorge4 = "a"
    jorge5 = "a"
    jorge6 = "a"
    jorge7 = "a"
    jorge8 = "a"
    jorge9 = "a"
    jorge10 = "a"
    adragão9 = "a"
    adragão10 = "a"
    adragão11 = "a"
    adragão12 = "a"
    adragão13 = "a"
    adragão14 = "a"
    adragão15 = "a"
    adragão16 = "a"
    a9 = "a"
    a10 = "a"
    a11 = "a"
    a12 = "a"
    a13 = "a"
    a14 = "a"
    a15 = "a"
    a16 = "a"
    o = 2
    global duck
    if "Força_Aumentada" in porque:
        abc = 2
    vitória = ('''
  __      _______ _____ _______ ____  _______     ___ 
  \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |
   \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |
    \ \/ /   | || |       | | | |  | |  _  / \   / | |
     \  /   _| || |____   | | | |__| | | \ \  | |  |_|
      \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)
                                                     
                                                     
          
          Você acabou com todas as carambolas!
          
''')
    vitória2 = ('''
  __      _______ _____ _______ ____  _______     ___ 
  \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |
   \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |
    \ \/ /   | || |       | | | |  | |  _  / \   / | |
     \  /   _| || |____   | | | |__| | | \ \  | |  |_|
      \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)
                                                     
                                                     
          
      Com um ataque certeiro você derrota o dragão...
COMO TU MATOU UM DRAGÃO SENDO QUE TU É UM HUMANO NORMAL CARA!?
          
''')
    vitória23 = ('''
  __      _______ _____ _______ ____  _______     ___ 
  \ \    / /_   _/ ____|__   __/ __ \|  __ \ \   / / |
   \ \  / /  | || |       | | | |  | | |__) \ \_/ /| |
    \ \/ /   | || |       | | | |  | |  _  / \   / | |
     \  /   _| || |____   | | | |__| | | \ \  | |  |_|
      \/   |_____\_____|  |_|  \____/|_|  \_\ |_|  (_)
                                                     
                                                     
          
                        ...
          
''')
    arvoro = input('''
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣸⠀⠀⠀⠀⠀⠀⠀⠀⡄⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢶⢠⠀⢀⡸⡄⠒⢺⠀⣸⣀⡀⣦⠽⠑⠁⠀⠀⠀⠀⠀⠀⠀⣆⣀⠗⠂⠀⠀⡆⢠⠃⡠⠜⠒⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⢤⠞⢳⠊⠓⠣⢸⡸⣲⠇⣘⣦⠚⢗⣻⠉⠻⡴⠂⢀⣀⠀⠀⣠⠂⠀⡇⠀⠀⠀⠀⡚⡲⢃⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠐⠺⠤⢼⡀⡞⢶⠦⣤⡖⠯⠭⡽⠟⡲⠀⠀⣆⠴⠊⢀⠀⠈⠅⡜⠒⠁⠀⠀⠉⢱⠀⠀⠀⠈⣑⡼⠁⢀⢠⢠⠄⢠⠆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠢⢄⢳⣁⣀⠆⠃⣇⡇⠜⠍⢳⡄⢰⢃⡈⡩⣲⠾⡃⢀⠀⠘⠤⢁⣠⠃⢠⢼⣇⣰⢃⣼⠀⠀⠀⣩⡾⠦⣆⠷⣅⠜⠉⠁⠀⠀⠀⠀
⠀⠀⠀⢦⠀⠈⠒⡥⣽⢁⠌⢹⢶⡤⡧⣾⠀⠀⠙⣾⣤⠖⠿⡿⣄⡗⢴⢣⡌⢲⣩⠚⠸⣌⣍⠹⣸⣚⡙⢷⣤⠞⠡⢄⣀⡳⣎⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢄⣣⡈⠦⡜⣸⡹⣰⠃⡀⢱⣛⣰⣑⢽⣧⠀⢰⣿⡇⠰⠋⠑⡜⡗⡞⠋⠂⠘⢦⠳⣠⠿⠦⣼⢩⣤⢊⡾⠋⠀⠀⠀⠋⠀⢨⠏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢁⠇⠀⡏⠀⠈⢾⡄⠙⣤⠃⣟⠀⠋⣿⣅⡾⢻⢀⡀⡆⣰⣥⣟⢱⣞⣀⠀⣨⠧⣯⡀⠀⢸⣈⣷⡟⠀⢀⢦⠀⠀⠀⢠⠏⠀⠀⡀⣷⠀⠀⠀⠀
⠤⢲⠚⢒⢻⠙⢶⣴⢺⠉⠒⡧⠔⠛⠲⢤⣸⣿⠁⣼⡶⠿⠿⣽⣓⣸⢿⣓⡶⣚⢧⡷⣿⢫⣦⣸⣿⠏⢹⡴⠋⠸⡄⠀⠀⡞⠀⢰⣰⢣⠊⠀⣰⡠⠀
⠀⠈⡄⠀⢭⡇⡀⠉⠻⣇⠀⡇⠀⠀⠀⣀⡝⢿⡆⣿⢁⢀⡴⠋⣏⣏⡼⠋⡷⣇⡝⣇⣿⡜⠋⣿⣿⡆⣼⡝⡄⣠⢹⠀⣸⠁⠀⠀⠀⠛⣄⣸⡖⠊⠀
⠐⠴⣅⡆⠘⡎⢢⠀⠀⢹⣎⣷⠀⠀⣀⡕⠻⢚⣿⣿⡉⠉⠳⣄⣰⠟⠑⢶⠁⠹⢴⠁⡇⣠⣴⠿⣏⣾⡇⢹⡃⡗⢸⣷⢃⣠⠔⠋⠀⢠⠃⠀⠑⠹⠀
⠀⢤⢎⣈⡲⠵⣈⠉⠓⣾⠙⣾⣇⠀⠀⠛⣆⡇⢻⣿⡇⠀⣠⡾⠛⢶⡆⠈⣇⣰⠏⢰⣿⢏⡏⢠⣏⣼⠞⠉⠉⠱⣿⢿⡭⣄⠀⠀⢠⠏⠀⠀⠀⠀⠀
⠐⠚⠒⠂⠼⣄⠀⠉⠢⣼⡀⠈⢻⣆⠠⡄⠳⡇⢸⣿⣧⣾⡟⠀⠀⢸⡇⠀⣸⠋⠀⣼⡏⢾⠛⣿⢹⡏⠀⠀⢀⡼⠃⢘⠂⢨⠀⢀⡞⠀⢀⠄⢀⠆⡀
⠀⠀⠀⠀⠀⠈⠳⣄⠀⠈⠳⣄⠀⣿⣆⠸⡠⠜⣆⣿⣿⠏⠀⠀⠀⢸⡇⢰⠇⠀⢀⣿⠁⣿⢰⡇⣼⠁⠀⢠⡞⠁⠀⠸⣚⣮⠵⠟⠓⠦⣸⠀⡤⠼⠓
⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⣈⠳⣜⢿⣯⠀⠀⢈⣿⡿⠦⣤⣀⠀⢸⣷⡏⠀⠀⣸⣿⡾⠋⣿⢁⡟⠀⣰⣯⣤⠶⠞⣋⠽⢓⣒⡡⠤⠒⠛⠳⢧⡀⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠙⠳⣿⣷⡀⢸⣿⡇⠀⠀⠉⠛⢾⣿⠀⠀⠀⣿⡟⠁⣸⣿⣾⣿⣿⠟⢉⣠⣴⠞⠋⠉⠉⠉⠂⠀⠀⠀⠀⠈⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣾⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⢸⡟⢀⣼⡿⠋⣼⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⣿⣷⡿⠋⠀⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣄⠀⠀⠀⠀⢿⡇⣸⣿⠟⠀⠀⢀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⣸⣷⣿⡇⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡏⢿⣿⣦⣀⣾⣿⢯⣿⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣮⣿⣿⣿⡿⠁⣸⡟⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡟⠀⢠⣿⠃⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣠⣾⣿⣤⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠿⠛⠻⣿⣿⠿⠿⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠡⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
   ____  _____            _   _  _____ ______ 
  / __ \|  __ \     /\   | \ | |/ ____|  ____|
 | |  | | |__) |   /  \  |  \| | |  __| |__   
 | |  | |  _  /   / /\ \ | . ` | | |_ |  __|  
 | |__| | | \ \  / ____ \| |\  | |__| | |____ 
  \____/|_|  \_\/_/    \_\_| \_|\_____|______|
                                              



    Pressione qualquer botão para continuar         
    ''')
    if "Força_Aumentada" in porque:
        input("Você acorda em uma floresta lembrando tudo que aconteceu na sua vida passada?\n")
        input("É sério que o jeito que você vai ganhar de mim é 'mudando o rumo da história'?\n")
        input("Não é como se você conseguise me responder mesmo\n")
    else:
        input("Você acorda em uma floresta sem lembranças de quem é e nem de onde está\n")
    if "Força_Aumentada" in porque:
        dire = [
    {
        "type" : "list",
        "name" : "direção",
        "message" : "O que você gostaria de fazer?",
        "choices" : ["ir ao Norte"]
    }
    ]
        direção = prompt(dire)
        direction = direção['direção']
    else:   
        dire1 = [
    {
        "type" : "list",
        "name" : "1direção",
        "message" : "O que você gostaria de fazer?",
        "choices" : ["ir ao Norte", "ir ao Sul", "desistir"]
    }
    ]
        direção1 = prompt(dire1)
        direction1 = direção1['1direção']
    if direction1 == "ir ao Norte" or direction == "ir ao Norte":
        input("Enquanto andava para o norte você encontra um tipo estranho de pedra brilhando no fundo de um lago\n")
        if "Força_Aumentada" in porque:
            pega = [

            {
            "type" : "list",
            "name" : "pegar",
            "message" : "O que você gostaria de fazer?",
            "choices" : ["tentar pegar o objeto"]
            }
            ]
            pegue = prompt(pega)
            pick1 = pegue['pegar']
        else:
            pega1 = [

    {
        "type" : "list",
        "name" : "pegar1",
        "message" : "O que você gostaria de fazer?",
        "choices" : ["tentar pegar o objeto", "Voltar e seguir para o sul"]
    }
    ]
            pegue1 = prompt(pega1)
            pick = pegue1['pegar1']
        if pick == "tentar pegar o objeto" or pick1 == "tentar pegar o objeto":
            if "Força_Aumentada" in porque:
                input("Diferente do que aconteceu ou aconteria das ultimas vezes quando você olha para a pedra ela começa a brilhar\n")
                input("Você bate a pedra no chão e dentro dela tem uma laranja?\n")
                input("...\n")
                input("Quem escreveu a bosta desse roteiro?\n")
                input("Você ingere a laranja e se sente ficando muito mais forte. 'suspiro'\n")
                player = 1000
            else:
                input("Você tenta com todas as forças pegar o objeto, mas é como se algo o estivesse o segurando. Você não consegue o pegar\n")
        elif pick == "Voltar e seguir para o sul":
            print()
    elif direction1 == "ir ao Sul" or direction == "ir ao Sul":
        print()
    elif direction1 == "desistir" or direction == "desistir":
        player = 0
    if player <= 0:
            input(Fore.RED+morte)
            time.sleep(0.000001)
            i = ""
            print(Fore.WHITE+i)
            inv.clear
            jogo()       
    input("Enquanto anda sem rumo você vê uma cidade na distância e decide seguir para lá\n")
    input("Enquanto caminha até essa cidade você se depara com um ciclope em seu caminho\n")
    enc1 = [
    {
        "type" : "list",
        "name" : "enco1",
        "message" : "O que você gostaria de fazer?",
        "choices" : ["tentar lutar contra a besta", "Fugir sem olhar para trás", "Pedir para passar"]
    }
    ]
    encon1 = prompt(enc1)
    encouter = encon1['enco1']
    if encouter == "tentar lutar contra a besta":
        if "Força_Aumentada" in porque:
            ataqueciclope1 = [
        {
            "type" : "list",
            "name" : "ataqueciclope1",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Suas proprias mãos"]
        }
        ]
            ataqueciclo1 = prompt(ataqueciclope1)
            attackciclope1 = ataqueciclo1['ataqueciclope1']
        else:
            ataqueciclope = [
        {
            "type" : "list",
            "name" : "ataqueciclope",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Suas proprias mãos", "Jogar galhos e pedras"]
        }
        ]
            ataqueciclo = prompt(ataqueciclope)
            attackciclope = ataqueciclo['ataqueciclope']                                      
        if attackciclope == "Suas proprias mãos":
            print()
            encontrociclope1 = randint(20 , 21)
            if encontrociclope1 > 1:
                input('''
Você tenta socar o gigantesco monstro mas ele não parece sentir nada. O monstro parece ficar irritado,
                 e com toda a sua furia o esmaga quebrando todos os seus ossos
''')
                player = 0
        if attackciclope == "Jogar galhos e pedras":
            print()
            encontrociclope2 = randint(20, 21)
            if encontrociclope2 > 1:
                input('''
Você tenta jogar galhos e pedras mas não parece surtir efeito. O monstro parece ficar irritado,
              e com toda a sua furia o esmaga quebrando todos os seus ossos
''')
                player = 0
        if attackciclope1 == "Suas proprias mãos":
            input("Com um unico soco você faz o ciclope cair no chão sem vida.\n")
            input("Quem poderia imaginar...\n")
    elif encouter == "Fugir sem olhar para trás":
        input("Você corre como sua vida dependesse disso e o montro parece pensar que você não vale o tempo dele\n")
    elif encouter == "Pedir para passar":
        input('''
                    Você pergunta para ele se poderia passar por ali. Ele fica surpreso disso,
  normalmente os aventureiros que passam por ali tentam o atacar ou fojem de medo,e então ele diz que é claro que pode passar.
mas antes de ir ele fala que se você quiser sua ajuda no futuro é só usar isso que ele será invocado mas isso só funciona uma vez
        ''')
        inv.append("Runa do ciclope")
        input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
    if player <= 0:
            input(Fore.RED+morte)
            time.sleep(0.000001)
            i = ""
            print(Fore.WHITE+i)
            inv.clear
            jogo()
    if "Força_Aumentada" in porque:
        input("Chegando na cidade você não estranha nada porque você já viveu isso\n")
    else:
        input('''
         Chegando na cidade você estranha o fato que os guardas te deixam entrar sem problema algum, mas isso não é problema seu,
melhor assim afinal você não precisará de nenhum documento. Afinal qual o problema de deixar alguém que você nunca viu entrar na sua cidade
''')       
    input("Você pensa em certos lugares que seriam de ajuda para sua aventura\n")
    while True:
        direção2 = [
        {
            "type" : "list",
            "name" : "direção2",
            "message" : "Para onde você gostaria de ir?",
            "choices" : ["Ir para o ferreiro", "Ir para a distante torre do mago", "Entrar em um beco nada suspeito", "Continuar a aventura"]
        }
        ]
        direction2 = prompt(direção2)
        dire2 = direction2['direção2']
        if dire2 == "Continuar a aventura":
            break 
        elif dire2 == "Entrar em um beco nada suspeito" and "Runa da Força" in inv:
            input("Você já foi lá")
        elif dire2 == "Entrar em um beco nada suspeito" and "Força_Aumentada" in porque:
            input("Você entra no beco sem nem se preocupar com nada pois já sabe que nada vai o ferir\n")
            input("...\n")
            input("Eu acabei de ver a faca do goblin quebrar no meio quando ele tentou te apunhalar...\n")
            input("Nessa altura porque você pensou em pegar algo pra te deixar mais forte ainda?\n")
            input("Tá... Você conversa com a senhora e pega a runa\n")
            inv.append("Runa da Força")
            input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
        elif dire2 == "Entrar em um beco nada suspeito" and "Espada" in inv:
            input("Você entra no beco e um goblin vem para cima de você mas com um rápido movimento você consegue o acertar com sua espada o fazendo ir embora\n")
            input("Você também percebe uma senhora que te chama\n")
            input("'Venha aqui jovem tenho algo para lhe mostrar'\n")
            input("'Eu normalmente cobraria por isso mas sinto algo especial em você e acho que deve ficar com isso'\n")
            input("'É uma runa que vai fazer o seu próximo ataque infligir mais dano que o normal'\n")
            inv.append("Runa da Força")
            input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
        elif dire2 == "Entrar em um beco nada suspeito":
            input("Quando entra no beco um goblin te apunhala pelas costas e você sangra até morrer\n")
            input(Fore.RED+morte)
            time.sleep(0.000001)
            i = ""
            print(Fore.WHITE+i)
            inv.clear
            jogo()
        elif dire2 == "Ir para o ferreiro" and "Espada" in inv:
            input("Você já foi lá")
        elif dire2 == "Ir para o ferreiro":
            input("Você segue em direção ao ferreiro e chegando lá ele diz\n")
            input('''
'Ah estavamos esperando um aventureiro como você.' 'Venha aqui tenho uma coisa que vai ajudar na sua aventura'
            ''')
            inv.append("Espada")
            input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
        elif dire2 == "Ir para a distante torre do mago" and "Livro de Feitiços" in inv:
            input("Você já foi lá")
        elif dire2 == "Ir para a distante torre do mago":
            if "Força_Aumentada" in porque and duck == 1:
                input("Você chega na torre e novamente encontra pato\n")
                input("Ele olha pra você e diz 'QUACK'\n")
            else:
                input("Você segue em direção da torre do mago mas chegando lá você não encontra uma pessoa, e sim um PATO\n")
                input("Ele olha pra você e diz 'QUACK'\n")
                duck = 1
            quack = [
            {
            "type" : "list",
            "name" : "quack",
            "message" : "O que gostaria de responder",
            "choices" : ["Dizer 'Ola tudo bem?'", "Dizer 'QUACK'"]
            }
            ]
            quackk = prompt(quack)
            pato = quackk['quack']     
            if pato == "Dizer 'QUACK'":
                input("Que isso cara, só porque eu sou um pato tu acha que eu não sei falar?\n")
                input("O pato conjura uma bola de fogo maior que você e a lança na sua direção\n")
                if "Força_Aumentada" in porque:
                    input("Já que agora você é o 'Todo poderoso' o ataque não parece surtir efeito\n")
                    input("O pato te olha com uma cara de surpreso enquanto você pega o livro de suas...\n")
                    input("Mãos?\n")
                    inv.append("Livro de Feitiços")
                    input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
                else:
                    player = 0
                if player <= 0:
                    input(Fore.RED+morte)
                    time.sleep(0.000001)
                    i = ""
                    print(Fore.WHITE+i)
                    inv.clear
                    jogo()
            else:
                input("Eae, tudo certo? eu vi tu vindo pra ca e por algum motivo motivo eu acho que tu deveria ficar com isso\n")
                inv.append("Livro de Feitiços")
                input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
    if "Força_Aumentada" in porque:
        input("Saindo da cidade você vê no horizonte um castelo gigantesco e já sabe que seu objetivo está lá dentro\n")
    else:
        input("Saindo da cidade você vê no horizonte um castelo gigantesco e pensa que é bem provavel que o seu objetivo está lá dentro\n")
    if "Força_Aumentada" in porque:
        input("Você chegou nas carambolas...\n")
        input("To começando a me preucupar\n")
    else:
        input("Enquanto vai até esse objetivo você se depara com um grupo de 3 carambolas na sua frente (Pequenas criaturas com formato de estrela e canhões na testa)\n")
    while True:
        ataquecarambola1 = randint(1, 20)
        ataquecarambola2 = randint(1, 20)
        ataquecarambola3 = randint(1, 20)
        if "Força_Aumentada" in porque and "Runa da Força" in porque:
            espadada1 = randint(100, 400)
            bola1 = randint(20, 800)
            soco1 = randint(60, 200)
            porque.remove("Runa da Força")
        elif "Força_Aumentada" in porque:
            espadada1 = randint(50, 200)
            bola1 = randint(10, 400)
            soco1 = randint(30, 100)
        elif "Runa da Força" in porque:
            espadada1 = randint(20, 40)
            bola1 = randint(2, 60)
            soco1 = randint(2, 20)
            porque.remove("Runa da Força")
        else:
            espadada1 = randint(10, 20)
            bola1 = randint(1, 30)
            soco1 = randint(1, 10)
        if carambola1 > 0:
            print(f'''
Você {player}

Carambola {carambola1}
Carambola {carambola2}
Carambola {carambola3}              
            ''')
        elif carambola1 <= 0 and carambola2 > 0:
            print(f'''
Você {player}

Carambola {carambola2}
Carambola {carambola3}
''') 
        elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
            print(f'''
Você {player}

Carambola {carambola3}
''')
        if "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv and "Runa da Força" in inv:
            armando1 = [
            {
            "type" : "list",
            "name" : "armando1",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a Runa da Força"]
            }
            ]
            armacarambola9 = prompt(armando1)
            jorge3 = armacarambola9['armando1']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            armacarambola = [
            {
            "type" : "list",
            "name" : "armacarambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope"]
            }
            ]
            armacarambola1 = prompt(armacarambola)
            armacarambolaa = armacarambola1['armacarambola']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa da Força" in inv:
            armando2 = [
            {
            "type" : "list",
            "name" : "armando2",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa da Força"]
            }
            ]
            armacarambola10 = prompt(armando2)
            jorge4 = armacarambola10['armando2']
        elif "Espada" in inv and "Runa do ciclope" in inv and "Runa da Força" in inv:
            armando3 = [
            {
            "type" : "list",
            "name" : "armando3",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa do ciclope", "Usar a Runa da Força"]
            }
            ]
            armacarambola11 = prompt(armando3)
            jorge5 = armacarambola11['armando3']
        elif "Livro de Feitiços" in inv and "Runa do ciclope" in inv and "Runa da Força" in inv:
            armando4 = [
            {
            "type" : "list",
            "name" : "armando4",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a Runa da Força"]
            }
            ]
            armacarambola12 = prompt(armando4)
            jorge6 = armacarambola12['armando4']
        elif "Espada" in inv and "Livro de Feitiços" in inv:
            armcarambola = [
            {
            "type" : "list",
            "name" : "armcarambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo"]
            }
            ]
            armacarambola2 = prompt(armcarambola)
            armacarambolaaa = armacarambola2['armcarambola']
        elif "Espada" in inv and "Runa do ciclope" in inv:
            aracarambola = [
            {
            "type" : "list",
            "name" : "aracarambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa do ciclope"]
            }
            ]
            armacarambola3 = prompt(aracarambola)
            armacarambolaaaa = armacarambola3['aracarambola']
        elif "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            rmacarambola = [
            {
            "type" : "list",
            "name" : "rmacarambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa do ciclope"]
            }
            ]
            armacarambola4 = prompt(rmacarambola)
            armacarambolaaaaa = armacarambola4['rmacarambola']
        elif "Espada" in inv and "Runa da Força" in inv:
            armando5 = [
            {
            "type" : "list",
            "name" : "armando5",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa da Força"]
            }
            ]
            armacarambola13 = prompt(armando5)
            jorge7 = armacarambola13['armando5']
        elif "Livro de Feitiços" in inv and "Runa da Força" in inv:
            armando6 = [
            {
            "type" : "list",
            "name" : "armando6",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa da Força"]
            }
            ]
            armacarambola14 = prompt(armando6)
            jorge8 = armacarambola14['armando6']
        elif "Runa do ciclope" in inv and "Runa da Força" in inv:
            armando7 = [
            {
            "type" : "list",
            "name" : "armando7",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Soca-lás","Usar a Runa do ciclope", "Usar a Runa da Força"]
            }
            ]
            armacarambola15 = prompt(armando7)
            jorge9 = armacarambola15['armando7']
        elif "Runa da Força" in inv:
            armando8 = [
            {
            "type" : "list",
            "name" : "armando8",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Soca-lás", "Usar a Runa da Força"]
            }
            ]
            armacarambola16 = prompt(armando8)
            jorge10 = armacarambola16['armando8']
        elif "Espada" in inv:
            armaarambola = [
            {
            "type" : "list",
            "name" : "armaarambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada"]
            }
            ]
            armacarambola5 = prompt(armaarambola)
            armacarambolaaaaaa = armacarambola5['armaarambola']
        elif "Livro de Feitiços" in inv:
            armacrambola = [
            {
            "type" : "list",
            "name" : "armacrambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo"]
            }
            ]
            armacarambola6 = prompt(armacrambola)
            armacarambolaaaaaaa = armacarambola6['armacrambola']
        elif "Runa do ciclope" in inv:
            armacaambola = [
            {
            "type" : "list",
            "name" : "armacaambola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Soca-lás","Usar a Runa do ciclope"]
            }
            ]
            armacarambola7 = prompt(armacaambola)
            jorge2 = armacarambola7['armacaambola']
        elif inv == []:
            armacarabola = [
            {
            "type" : "list",
            "name" : "armacarabola",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Soca-lás"]
            }
            ]
            armacarambola8 = prompt(armacarabola)
            jorge = armacarambola8['armacarabola']
        if 1 == 1:
            if jorge2 == "Soca-lás" or jorge == "Soca-lás" or jorge10 == "Soca-lás":
                if soco1 >= 20:
                    if carambola1 > 0:
                        carambola1 -= 20
                        input("Você acertou um soco que mata a primeira carambola\n")
                    elif carambola1 <= 0 and carambola2 > 0:
                        carambola2 -= 20
                        input("Você acertou um soco que mata a segunda carambola\n")
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        carambola3 -= 20
                        input("Você acertou um soco que mata terceira carambola\n")
                elif soco1 == 1:
                    player -= 5
                    input("Seu soco foi tão patético que você cai de cara no chão perdendo 5 de vida\n")
                elif soco1 >= 2:
                    if carambola1 > 0:
                        carambola1 -= soco1
                        input(f"Você acertou um soco e deu {soco1} de dano na primeira carambola\n")
                    elif carambola1 <= 0 and carambola2 > 0:
                        carambola2 -= soco1
                        input(f"Você acertou um soco e deu {soco1} de dano na segunda carambola\n")
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        carambola3 -= soco1
                        input(f"Você acertou um soco e deu {soco1} de dano na terceira carambola\n")
            elif armacarambolaa == "Usar a Runa do ciclope" or armacarambolaaaaa == "Usar a Runa do ciclope" or armacarambolaaaa == "Usar a Runa do ciclope" or jorge2 == "Usar a Runa do ciclope" or jorge3 == "Usar a Runa do ciclope" or jorge5 == "Usar a Runa do ciclope" or jorge6 == "Usar a Runa do ciclope" or jorge9 == "Usar a Runa do ciclope":
                while "Runa do ciclope" in inv:
                    input('''
Você usa a Runa fazendo o ciclope aparecer de um portal. Ele esmaga as carambolas e depois vai embora, enquanto a runa se desistegra em suas mãos.
''')
                    carambola1 = 0
                    carambola2 = 0
                    carambola3 = 0
                    inv.remove("Runa do ciclope")
                    break        
            elif armacarambolaa == "Usar a espada" or armacarambolaaa == "Usar a espada" or armacarambolaaaa == "Usar a espada" or armacarambolaaaaaa == "Usar a espada" or jorge3 == "Usar a espada" or jorge4 == "Usar a espada" or jorge5 == "Usar a espada" or jorge7 == "Usar a espada":
                if espadada1 >= 20:
                    if carambola1 > 0:
                        input("Você acerta uma espadada que mata a primeira carambola\n")
                        carambola1 -= espadada1
                    elif carambola1 <= 0 and carambola2 > 0:
                        input("Você acerta uma espadada que mata a segunda carambola\n")
                        carambola2 -= espadada1
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        input("Você acerta uma espadada que mata a terceira carambola\n")
                        carambola3 -= espadada1
                else:
                    if carambola1 > 0:
                        input(f"Você acerta uma espadada que deu {espadada1} de dano na primeira carambola\n")
                        carambola1 -= espadada1
                    elif carambola1 <= 0 and carambola2 > 0:
                        input(f"Você acerta uma espadada que deu {espadada1} de dano na segunda carambola\n")
                        carambola2 -= espadada1
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        input(f"Você acerta uma espadada que deu {espadada1} de dano na terceira carambola\n")
                        carambola3 -= espadada1
            elif armacarambolaa == "Conjurar uma bola de fogo" or armacarambolaaa == "Conjurar uma bola de fogo" or armacarambolaaaaa == "Conjurar uma bola de fogo" or armacarambolaaaaaaa == "Conjurar uma bola de fogo" or jorge3 == "Conjurar uma bola de fogo" or jorge4 == "Conjurar uma bola de fogo" or jorge6 == "Conjurar uma bola de fogo" or jorge8 == "Conjurar uma bola de fogo":
                if bola1 >= 20:
                    if carambola1 > 0:
                        input("Você acerta uma bola de fogo que mata a primeira carambola\n")
                        carambola1 -= bola1
                    elif carambola1 <= 0 and carambola2 > 0:
                        input("Você acerta uma bola de fogo que mata a segunda carambola\n")
                        carambola2 -= bola1
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        input("Você acerta uma bola de fogo que mata a terceira carambola\n")
                        carambola3 -= bola1
                else:
                    if carambola1 > 0:
                        input(f"Você acerta uma bola de fogo que deu {bola1} de dano na primeira carambola\n")
                        carambola1 -= bola1
                    elif carambola1 <= 0 and carambola2 > 0:
                        input(f"Você acerta uma bola de fogo que deu {bola1} de dano na segunda carambola\n")
                        carambola2 -= bola1
                    elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                        input(f"Você acerta uma bola de fogo que deu {bola1} de dano na terceira carambola\n")
                        carambola3 -= bola1
            elif jorge3 == "Usar a Runa da Força" or jorge4 == "Usar a Runa da Força" or jorge5 == "Usar a Runa da Força" or jorge6 == "Usar a Runa da Força" or jorge7 == "Usar a Runa da Força" or jorge8 == "Usar a Runa da Força" or jorge9 == "Usar a Runa da Força" or jorge10 == "Usar a Runa da Força":
                porque.append("Runa da Força")
                input("Você se sente ficando mais forte\n")
            if carambola1 > 0:
                input(f"As carambolas te atacam dando {ataquecarambola1}, {ataquecarambola2} e {ataquecarambola3} de dano respectivamente\n")
                player -= ataquecarambola1
                player -= ataquecarambola2
                player -= ataquecarambola3
            elif carambola1 <= 0 and carambola2 > 0:
                input(f"As carambolas te atacam dando {ataquecarambola2} e {ataquecarambola3} de dano respectivamente\n")
                player -= ataquecarambola2
                player -= ataquecarambola3
            elif carambola1 <= 0 and carambola2 <= 0 and carambola3 > 0:
                input(f"A ultima carambola te ataca dando {ataquecarambola3} de dano\n")
                player -= ataquecarambola3
            if carambola3 <= 0:
                break
            if player <= 0:
                input(Fore.RED+morte)
                time.sleep(0.000001)
                i = ""
                print(Fore.WHITE+i)
                inv.clear
                jogo()
    input(Fore.GREEN+vitória)
    time.sleep(0.000001)
    i = ""
    print(Fore.WHITE+i)
    if "Força_Aumentada" in porque:
        input("Após vencer as carambolas sua vida e seu ataque são aumentados denovo!? e eu nem sei porque mas você também pega uma carambola para usar como arma\n")
        player = 1500
        inv.append("carambola")
    else:
        input("Após vencer as carambolas sua vida e seu ataque são magicamente aumentados e você pega uma para usar de arma\n")
        player = 200
        inv.append("carambola")
    input(f"Seu inventário está cada vez mais cheio. Você tem {inv}\n")
    if "Força_Aumentada" in porque:
        input("Cara se você matar o dragão com facilidade...\n") 
        input("Eu ia falar alguma coisa mas eu só posso fazer algo com você quando você entrar no castelo\n")
    else:
        input("Quando chega nos portões do castelo você ouve um barulho muito alto alto de asas batendo.\n")
        input("Quando percebe, um dragão de fogo pousa na sua frente\n")
    while True:
        ataquedragão = randint(1, 50)
        if "Força_Aumentada" in porque and "Runa da Força" in porque:
            espadada2 = randint(400, 600)
            bola2 = randint(100, 800)
            carambolada2 = randint(100, 600)
            porque.remove("Runa da Força")
        elif "Força_Aumentada" in porque:
            espadada2 = randint(200, 300)
            bola2 = randint(50, 400)
            carambolada2 = randint(50, 300)
        elif "Runa da Força" in porque:
            espadada2 = randint(40, 60)
            bola2 = randint(10, 80)
            carambolada2 = randint(10, 60)
            porque.remove("Runa da Força")
        else:
            espadada2 = randint(20, 30)
            bola2 = randint(5, 40)
            carambolada2 = randint(5, 30)
        print(f'''
Você {player} 

Dragão {dragão}
              
''')
        if "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv and "Runa da Força" in inv:
            dragones9 = [
            {
            "type" : "list",
            "name" : "dragones9",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola", "Usar a Runa da Força"]
            }
            ]
            dragon9 = prompt(dragones9)
            adragão9 = dragon9['dragones9']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            dragones1 = [
            {
            "type" : "list",
            "name" : "dragones1",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon1 = prompt(dragones1)
            adragão1 = dragon1['dragones1']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa da Força" in inv:
            dragones10 = [
            {
            "type" : "list",
            "name" : "dragones10",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            dragon10 = prompt(dragones10)
            adragão10 = dragon10['dragones10']
        elif "Espada" in inv and "Runa da Força" in inv and "Runa do ciclope" in inv:
            dragones11 = [
            {
            "type" : "list",
            "name" : "dragones11",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa da Força", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon11 = prompt(dragones11)
            adragão11 = dragon11['dragones11']
        elif "Runa da Força" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            dragones12 = [
            {
            "type" : "list",
            "name" : "dragones12",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon12 = prompt(dragones12)
            adragão12 = dragon12['dragones12']
        elif "Espada" in inv and "Livro de Feitiços" in inv:
            dragones2 = [
            {
            "type" : "list",
            "name" : "dragones2",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a carambola"]
            }
            ]
            dragon2 = prompt(dragones2)
            adragão2 = dragon2['dragones2']
        elif "Espada" in inv and "Runa do ciclope" in inv:
            dragones3 = [
            {
            "type" : "list",
            "name" : "dragones3",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon3 = prompt(dragones3)
            adragão3 = dragon3['dragones3']
        elif "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            dragones4 = [
            {
            "type" : "list",
            "name" : "dragones4",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon4 = prompt(dragones4)
            adragão4 = dragon4['dragones4']
        elif "Espada" in inv and "Runa da Força" in inv:
            dragones13 = [
            {
            "type" : "list",
            "name" : "dragones13",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            dragon13 = prompt(dragones13)
            adragão13 = dragon13['dragones13']
        elif "Livro de Feitiços" in inv and "Runa da Força" in inv:
            dragones14 = [
            {
            "type" : "list",
            "name" : "dragones14",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            dragon14 = prompt(dragones14)
            adragão14 = dragon14['dragones14']
        elif "Runa da Força" in inv and "Runa do ciclope" in inv:
            dragones15 = [
            {
            "type" : "list",
            "name" : "dragones15",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            dragon15 = prompt(dragones15)
            adragão15 = dragon15['dragones15']
        elif "Espada" in inv:
            dragones5 = [
            {
            "type" : "list",
            "name" : "dragones5",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a carambola"]
            }
            ]
            dragon5 = prompt(dragones5)
            adragão5 = dragon5['dragones5']
        elif "Livro de Feitiços" in inv:
            dragones6 = [
            {
            "type" : "list",
            "name" : "dragones6",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a carambola"]
            }
            ]
            dragon6 = prompt(dragones6)
            adragão6 = dragon6['dragones6']
        elif "Runa do ciclope" in inv:
            dragones7 = [
            {
            "type" : "list",
            "name" : "dragones7",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a carambola","Usar a Runa do ciclope"]
            }
            ]
            dragon7 = prompt(dragones7)
            adragão7 = dragon7['dragones7']
        elif "Runa da Força" in inv:
            dragones16 = [
            {
            "type" : "list",
            "name" : "dragones16",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            dragon16 = prompt(dragones16)
            adragão16 = dragon16['dragones16']
        elif "carambola" in inv:
            dragones8 = [
            {
            "type" : "list",
            "name" : "dragones8",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a carambola"]
            }
            ]
            dragon8 = prompt(dragones8)
            adragão8 = dragon8['dragones8']
        if adragão1 == "Usar a espada" or adragão2 == "Usar a espada" or adragão3 == "Usar a espada" or adragão5 == "Usar a espada" or adragão9 == "Usar a espada" or adragão10 == "Usar a espada" or adragão11 == "Usar a espada" or adragão13 == "Usar a espada":
            dragão -= espadada2
            input(f"Você deu uma espadada no dragão que deu {espadada2} de dano\n")
        elif adragão1 == "Conjurar uma bola de fogo" or adragão2 == "Conjurar uma bola de fogo" or adragão4 == "Conjurar uma bola de fogo" or adragão6 == "Conjurar uma bola de fogo" or adragão9 == "Conjurar uma bola de fogo" or adragão10 == "Conjurar uma bola de fogo" or adragão12 == "Conjurar uma bola de fogo" or adragão14 == "Conjurar uma bola de fogo":
            dragão -= bola2
            input(f"Você acertou uma bola de fogo que deu {bola2} de dano no dragão\n")
        elif adragão1 == "Usar a Runa do ciclope" or adragão3 == "Usar a Runa do ciclope" or adragão4 == "Usar a Runa do ciclope" or adragão7 == "Usar a Runa do ciclope":
            input('''
        O ciclope aparece de um portal e fala 'cara isso é um dragão de fogo, eu que não vou me matar tentando matar esse bicho'
                              ele vai embora enquanto a Runa se desintegra nas suas mãos
''')            
            inv.remove("Runa do ciclope")
        elif adragão1 == "Usar a carambola" or adragão2 == "Usar a carambola" or adragão3 == "Usar a carambola" or adragão4 == "Usar a carambola" or adragão5 == "Usar a carambola" or adragão6 == "Usar a carambola" or adragão7 == "Usar a carambola" or adragão8 == "Usar a carambola" or adragão9 == "Usar a carambola" or adragão11 == "Usar a carambola" or adragão12 == "Usar a carambola" or adragão15 == "Usar a carambola":
            dragão -= carambolada2
            input(f"Você dá um tiro com a carambola dando {carambolada2} de dano no dragão\n")
        elif adragão9 == "Usar a Runa da Força" or adragão10 == "Usar a Runa da Força" or adragão11 == "Usar a Runa da Força" or adragão12 == "Usar a Runa da Força" or adragão13 == "Usar a Runa da Força" or adragão14 == "Usar a Runa da Força" or adragão15 == "Usar a Runa da Força" or adragão16 == "Usar a Runa da Força":
            porque.append("Runa da Força")
            input("Você se sente ficando mais forte\n")
        if dragão <= 0:
            break
        else:
            player -= ataquedragão
            input(f"O dragão te ataca dando {ataquedragão} de dano\n")
        if player <= 0:
            input(Fore.RED+morte)
            time.sleep(0.000001)
            i = ""
            print(Fore.WHITE+i)
            inv.clear
            jogo()
    if "Força_Aumentada" in porque:
        input(Fore.GREEN+vitória23)
        time.sleep(0.000001)
        i = ""
        print(Fore.WHITE+i)
    else:
        input(Fore.GREEN+vitória2)
        time.sleep(0.000001)
        i = ""
        print(Fore.WHITE+i)
    if "Força_Aumentada" in porque:
        input("Bem você finalmente chegou aqui denovo...\n")
        input("Esse é o seu Grand Finale.\n")
    else:
        input("Entrando no castelo você vê uma figura de baixo de um manto, que é o verdeiro 'vilão'...\n")
        input("Eu mesmo! :)\n")
    input("Venha com toda a sua força.\n")
    while True:
        print(f'''
    Você {player}

    Narrador ???
                
    ''')
        if "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv and "Runa da Força" in inv:
            all9 = [
            {
            "type" : "list",
            "name" : "all9",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola", "Usar a Runa da Força"]
            }
            ]
            tristeza9 = prompt(all9)
            a9 = tristeza9['all9']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            all1 = [
            {
            "type" : "list",
            "name" : "all1",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza1 = prompt(all1)
            a1 = tristeza1['all1']
        elif "Espada" in inv and "Livro de Feitiços" in inv and "Runa da Força" in inv:
            all10 = [
            {
            "type" : "list",
            "name" : "all10",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            tristeza10 = prompt(all10)
            a10 = tristeza10['all10']
        elif "Espada" in inv and "Runa da Força" in inv and "Runa do ciclope" in inv:
            all11 = [
            {
            "type" : "list",
            "name" : "all11",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa da Força", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza11 = prompt(all11)
            a11 = tristeza11['all11']
        elif "Runa da Força" in inv and "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            all12 = [
            {
            "type" : "list",
            "name" : "all12",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza12 = prompt(all12)
            a12 = tristeza12['all12']
        elif "Espada" in inv and "Livro de Feitiços" in inv:
            all2 = [
            {
            "type" : "list",
            "name" : "all2",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Conjurar uma bola de fogo", "Usar a carambola"]
            }
            ]
            tristeza2 = prompt(all2)
            a2 = tristeza2['all2']
        elif "Espada" in inv and "Runa do ciclope" in inv:
            all3 = [
            {
            "type" : "list",
            "name" : "all3",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza3 = prompt(all3)
            a3 = tristeza3['all3']
        elif "Livro de Feitiços" in inv and "Runa do ciclope" in inv:
            all4 = [
            {
            "type" : "list",
            "name" : "all4",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza4 = prompt(all4)
            a4 = tristeza4['all4']
        elif "Espada" in inv and "Runa da Força" in inv:
            all13 = [
            {
            "type" : "list",
            "name" : "all13",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            tristeza13 = prompt(all13)
            a13 = tristeza13['all13']
        elif "Livro de Feitiços" in inv and "Runa da Força" in inv:
            all14 = [
            {
            "type" : "list",
            "name" : "all14",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            tristeza14 = prompt(all14)
            a14 = tristeza14['all14']
        elif "Runa da Força" in inv and "Runa do ciclope" in inv:
            all15 = [
            {
            "type" : "list",
            "name" : "all15",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Usar a Runa do ciclope", "Usar a carambola"]
            }
            ]
            tristeza15 = prompt(all15)
            a15 = tristeza15['all15']
        elif "Espada" in inv:
            all5 = [
            {
        "type" : "list",
            "name" : "all5",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a espada", "Usar a carambola"]
            }
            ]
            tristeza5 = prompt(all5)
            a5 = tristeza5['all5']
        elif "Livro de Feitiços" in inv:
            all6 = [
            {
            "type" : "list",
            "name" : "all6",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Conjurar uma bola de fogo", "Usar a carambola"]
            }
            ]
            tristeza6 = prompt(all6)
            a6 = tristeza6['all6']
        elif "Runa do ciclope" in inv:
            all7 = [
            {
            "type" : "list",
            "name" : "all7",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a carambola","Usar a Runa do ciclope"]
            }
            ]
            tristeza7 = prompt(all7)
            a7 = tristeza7['all7']
        elif "Runa da Força" in inv:
            all16 = [
            {
        "type" : "list",
            "name" : "all16",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a Runa da Força", "Usar a carambola"]
            }
            ]
            tristeza16 = prompt(all16)
            a16 = tristeza16['all16']
        elif "carambola" in inv:
            all8 = [
            {
            "type" : "list",
            "name" : "all8",
            "message" : "O que gostaria de usar para lutar?",
            "choices" : ["Usar a carambola"]
            }
            ]
            tristeza8 = prompt(all8)
            a8 = tristeza8['all8']
        if "Força_Aumentada" in porque:
            if a1 == "Usar a Runa do ciclope" or a3 == "Usar a Runa do ciclope" or a4 == "Usar a Runa do ciclope" or a7 == "Usar a Runa do ciclope" or a9 == "Usar a Runa do ciclope" or a11 == "Usar a Runa do ciclope" or a12 == "Usar a Runa do ciclope" or a15 == "Usar a Runa do ciclope":
                input("Bem eu ainda sou obrigado a narrar a história então...\n")
                input("O ciclope aparece de um portal e é morto com um soco\n")
            elif a9 == "Usar a Runa da Força" or a10 == "Usar a Runa da Força" or a11 == "Usar a Runa da Força" or a12 == "Usar a Runa da Força" or a13 == "Usar a Runa da Força" or a14 == "Usar a Runa da Força" or a15 == "Usar a Runa da Força" or a16 == "Usar a Runa da Força":
                input("Você realmente acha que não está forte o bastente?\n")
                input("Olha me ataca pra valer dessa vez\n")
            else:
                input("Haha, você realmente acha que algo tão insignificante vai fazer alguma coisa contra mim?\n")
                input("AAAAAAAAAHHHHH\n")
                input("Como você ficou tão forte?...\n")
                input("Não tem o que eu fazer...\n")
                input("Você venceu...\n")
                input("Parabéns...\n")
                input("...\n")
                input("Ah espera eu esqueci que eu sou imortal. :)\n")
                input("Sabe como é ninguém realmente chegou perto de me matar.\n")
                input("Nossa eu realmente pensei que você tinha ganhado\n")
                input("E agora você pode voltar para o seu loop infinito\n")
                input("EU CONJURO\n")
                input("BOLA DE FOGO!\n")
                input(Fore.RED+morte)
                time.sleep(0.000001)
                i = ""
                print(Fore.WHITE+i)
                qw = 1
                o = 1
                print('''
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢱⣸⠀⠀⠀⠀⠀⠀⠀⠀⡄⡄⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⢶⢠⠀⢀⡸⡄⠒⢺⠀⣸⣀⡀⣦⠽⠑⠁⠀⠀⠀⠀⠀⠀⠀⣆⣀⠗⠂⠀⠀⡆⢠⠃⡠⠜⠒⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⡄⠀⢤⠞⢳⠊⠓⠣⢸⡸⣲⠇⣘⣦⠚⢗⣻⠉⠻⡴⠂⢀⣀⠀⠀⣠⠂⠀⡇⠀⠀⠀⠀⡚⡲⢃⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠐⠺⠤⢼⡀⡞⢶⠦⣤⡖⠯⠭⡽⠟⡲⠀⠀⣆⠴⠊⢀⠀⠈⠅⡜⠒⠁⠀⠀⠉⢱⠀⠀⠀⠈⣑⡼⠁⢀⢠⢠⠄⢠⠆⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠢⢄⢳⣁⣀⠆⠃⣇⡇⠜⠍⢳⡄⢰⢃⡈⡩⣲⠾⡃⢀⠀⠘⠤⢁⣠⠃⢠⢼⣇⣰⢃⣼⠀⠀⠀⣩⡾⠦⣆⠷⣅⠜⠉⠁⠀⠀⠀⠀
    ⠀⠀⠀⢦⠀⠈⠒⡥⣽⢁⠌⢹⢶⡤⡧⣾⠀⠀⠙⣾⣤⠖⠿⡿⣄⡗⢴⢣⡌⢲⣩⠚⠸⣌⣍⠹⣸⣚⡙⢷⣤⠞⠡⢄⣀⡳⣎⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⢄⣣⡈⠦⡜⣸⡹⣰⠃⡀⢱⣛⣰⣑⢽⣧⠀⢰⣿⡇⠰⠋⠑⡜⡗⡞⠋⠂⠘⢦⠳⣠⠿⠦⣼⢩⣤⢊⡾⠋⠀⠀⠀⠋⠀⢨⠏⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⢁⠇⠀⡏⠀⠈⢾⡄⠙⣤⠃⣟⠀⠋⣿⣅⡾⢻⢀⡀⡆⣰⣥⣟⢱⣞⣀⠀⣨⠧⣯⡀⠀⢸⣈⣷⡟⠀⢀⢦⠀⠀⠀⢠⠏⠀⠀⡀⣷⠀⠀⠀⠀
    ⠤⢲⠚⢒⢻⠙⢶⣴⢺⠉⠒⡧⠔⠛⠲⢤⣸⣿⠁⣼⡶⠿⠿⣽⣓⣸⢿⣓⡶⣚⢧⡷⣿⢫⣦⣸⣿⠏⢹⡴⠋⠸⡄⠀⠀⡞⠀⢰⣰⢣⠊⠀⣰⡠⠀
    ⠀⠈⡄⠀⢭⡇⡀⠉⠻⣇⠀⡇⠀⠀⠀⣀⡝⢿⡆⣿⢁⢀⡴⠋⣏⣏⡼⠋⡷⣇⡝⣇⣿⡜⠋⣿⣿⡆⣼⡝⡄⣠⢹⠀⣸⠁⠀⠀⠀⠛⣄⣸⡖⠊⠀
    ⠐⠴⣅⡆⠘⡎⢢⠀⠀⢹⣎⣷⠀⠀⣀⡕⠻⢚⣿⣿⡉⠉⠳⣄⣰⠟⠑⢶⠁⠹⢴⠁⡇⣠⣴⠿⣏⣾⡇⢹⡃⡗⢸⣷⢃⣠⠔⠋⠀⢠⠃⠀⠑⠹⠀
    ⠀⢤⢎⣈⡲⠵⣈⠉⠓⣾⠙⣾⣇⠀⠀⠛⣆⡇⢻⣿⡇⠀⣠⡾⠛⢶⡆⠈⣇⣰⠏⢰⣿⢏⡏⢠⣏⣼⠞⠉⠉⠱⣿⢿⡭⣄⠀⠀⢠⠏⠀⠀⠀⠀⠀
    ⠐⠚⠒⠂⠼⣄⠀⠉⠢⣼⡀⠈⢻⣆⠠⡄⠳⡇⢸⣿⣧⣾⡟⠀⠀⢸⡇⠀⣸⠋⠀⣼⡏⢾⠛⣿⢹⡏⠀⠀⢀⡼⠃⢘⠂⢨⠀⢀⡞⠀⢀⠄⢀⠆⡀
    ⠀⠀⠀⠀⠀⠈⠳⣄⠀⠈⠳⣄⠀⣿⣆⠸⡠⠜⣆⣿⣿⠏⠀⠀⠀⢸⡇⢰⠇⠀⢀⣿⠁⣿⢰⡇⣼⠁⠀⢠⡞⠁⠀⠸⣚⣮⠵⠟⠓⠦⣸⠀⡤⠼⠓
    ⠀⠀⠀⠀⠀⠀⠀⠙⢦⣀⣀⣈⠳⣜⢿⣯⠀⠀⢈⣿⡿⠦⣤⣀⠀⢸⣷⡏⠀⠀⣸⣿⡾⠋⣿⢁⡟⠀⣰⣯⣤⠶⠞⣋⠽⢓⣒⡡⠤⠒⠛⠳⢧⡀⡄
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠙⠳⣿⣷⡀⢸⣿⡇⠀⠀⠉⠛⢾⣿⠀⠀⠀⣿⡟⠁⣸⣿⣾⣿⣿⠟⢉⣠⣴⠞⠋⠉⠉⠉⠂⠀⠀⠀⠀⠈⠃⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣾⣿⡇⠀⠀⠀⠀⢸⣿⠀⠀⢸⡟⢀⣼⡿⠋⣼⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣿⣿⡇⠀⠀⠀⠀⠀⣿⡀⠀⣿⣷⡿⠋⠀⢠⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣄⠀⠀⠀⠀⢿⡇⣸⣿⠟⠀⠀⢀⣾⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣆⠀⠀⠀⣸⣷⣿⡇⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡏⢿⣿⣦⣀⣾⣿⢯⣿⠀⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣮⣿⣿⣿⡿⠁⣸⡟⠀⠀⣼⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣿⡟⠀⢠⣿⠃⠀⣼⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣷⣠⣾⣿⣤⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⠟⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡿⠿⠛⠻⣿⣿⠿⠿⠿⢿⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠈⠡⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
            
      ____  _____            _   _  _____ ______ 
     / __ \|  __ \     /\   | \ | |/ ____|  ____|
    | |  | | |__) |   /  \  |  \| | |  __| |__   
    | |  | |  _  /   / /\ \ | . ` | | |_ |  __|  
    | |__| | | \ \  / ____ \| |\  | |__| | |____ 
     \____/|_|  \_\/_/    \_\_| \_|\_____|______|
                                                
            
                OBRIGADO POR JOGAR!      
    ''')
        elif a1 == "Usar a Runa do ciclope" or a3 == "Usar a Runa do ciclope" or a4 == "Usar a Runa do ciclope" or a7 == "Usar a Runa do ciclope" or a9 == "Usar a Runa do ciclope" or a11 == "Usar a Runa do ciclope" or a12 == "Usar a Runa do ciclope" or a15 == "Usar a Runa do ciclope":
            input("Bem eu ainda sou obrigado a narrar a história então...\n")
            input("O ciclope aparece de um portal e é morto com um soco\n")
        elif a9 == "Usar a Runa da Força" or a10 == "Usar a Runa da Força" or a11 == "Usar a Runa da Força" or a12 == "Usar a Runa da Força" or a13 == "Usar a Runa da Força" or a14 == "Usar a Runa da Força" or a15 == "Usar a Runa da Força" or a16 == "Usar a Runa da Força":
            input("Cara eu sou o boss final você realmente acha que ia conseguir aguentar um soco meu?\n")
        else:
            input("Bem eu ainda sou obrigado a narrar a história então...\n")
            input("Seu ataque não parece surtir efeito\n")
        if abc == 1:
            input("Olha eu sei que quando te matar você apenas ira voltar aqui de novo, mas ainda não sei de que jeito miraculoso você vai conseguir me derrotar...\n")
            input("Bem, vamos testar.\n")
            input(Fore.RED+morte)
            time.sleep(0.000001)
            i = ""
            print(Fore.WHITE+i)
            inv.clear
            porque.clear
            porque.append("Força_Aumentada")
            input("Ah, eu esqueci que você não consegue enxergar mas o que aconteceu é que eu abri um buraco no seu peito com um soco\n")
            jogo()
        elif o == 1:
            input()
            menu()
menu()
#eae