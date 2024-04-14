from colorama import Fore, Back, Style
import time
import os
import pygame
import pyttsx3
from playsound import playsound

mem = int(input(f"{Fore.GREEN}Включить или выключить мемный режим 1 или 0:{Style.RESET_ALL} "))
os.system("cls")

if mem == 1:
    pygame.mixer.init()


    song = pygame.mixer.Sound('loading.mp3')
    song.play()

    for _ in range(0,14):
        print("Loading")
        time.sleep(0.2)
        os.system("cls")
        print("Loading.")
        time.sleep(0.2)
        os.system("cls")
        print("Loading..")
        time.sleep(0.2)
        os.system("cls")
        print("Loading...")
        time.sleep(0.2)
        os.system("cls")



    try:
        ###################__task_1__####################
        print(f"{Fore.RED}Первое задание на 3{Style.RESET_ALL}")
        engine = pyttsx3.init()
        text = "Первое задание на троёчку.....Введите двоичное число"
        engine.say(text)
        engine.runAndWait()
        num_1 = str(input("Введите двоичное число: "))

        if len(num_1) == 2:
            num_2 = int(num_1) // 10
            print(f"Десятки {num_2}")
            num_2 = int(num_1) % 10
            print(f"Единицы {num_2}\n")
            song = pygame.mixer.Sound('omg.mp3')
            song.play()
            time.sleep(0.8)

        else:
            print("Я сказал ВВЕДИТЕ ДВОИЧНОЕ ЧИСЛО!\n")
            song = pygame.mixer.Sound('puk-v-ekho.mp3')
            song.play()


        ###################__task_2__####################
        print(f"{Fore.YELLOW}Второе задание на 4{Style.RESET_ALL}")
        engine = pyttsx3.init()
        text = "Второе задание на четвёрочку.....Введите троичное число"
        engine.say(text)
        engine.runAndWait()
        num_1 = str(input("Введите троичное число: "))

        if len(num_1) == 3:
            num_2 = int(num_1) // 100
            print(f"Сотни {num_2}")
            num_3 = int(num_1) // 10 % 10
            print(f"Десятки {num_3}")
            num_2 = int(num_1) % 10
            print(f"Единицы {num_2}\n")
            song = pygame.mixer.Sound('omg.mp3')
            song.play()
            time.sleep(0.8)

        else:
            print("Я сказал ВВЕДИТЕ ТРООИЧНОЕ ЧИСЛО!\n")
            song = pygame.mixer.Sound('puk-v-ekho.mp3')
            song.play()


        ###################__task_3__####################
        print(f"{Fore.GREEN}Третье задание на 5{Style.RESET_ALL}")
        engine = pyttsx3.init()
        text = "Третье задание на 5 на пятёрачку.....Введите числа и они сложатя"
        engine.say(text)
        engine.runAndWait()
        num_1 = int(input("Введите числа: "))

        i = 0
        for _ in str(num_1):
            i = i + int(_)

        print(f"Сумма {i}")
        engine = pyttsx3.init()
        text = "Ураааа поооообееееееда!!!"
        engine.say(text)
        engine.runAndWait()
        time.sleep(0.5)
        os.system("cls")
        os.system("python _.py")

    except:
        os.system("cls")

        i = 0
        while True:
            if i == 0:
                song = pygame.mixer.Sound('idi-nakhui-pudzh.mp3')
                song.play()
                i = + 1
            if i == 1000:
                break

            else:
                print(f"{Fore.WHITE + Back.RED}ИДИ НАХУЙ  {Style.RESET_ALL}"*21)
                i = + 1


elif mem == 0:
    ###################__task_1__####################
    print(f"{Fore.RED}Первое задание на 3{Style.RESET_ALL}")
    num_1 = str(input("Введите двоичное число: "))

    if len(num_1) == 2:
        num_2 = int(num_1) // 10
        print(f"Десятки {num_2}")
        num_2 = int(num_1) % 10
        print(f"Единицы {num_2}\n")

    else:
        print("Число не двоичное\n")


    ###################__task_2__####################
    print(f"{Fore.YELLOW}Второе задание на 4{Style.RESET_ALL}")
    num_1 = str(input("Введите троичное число: "))

    if len(num_1) == 3:
        num_2 = int(num_1) // 100
        print(f"Сотни {num_2}")
        num_3 = int(num_1) // 10 % 10
        print(f"Десятки {num_3}")
        num_2 = int(num_1) % 10
        print(f"Единицы {num_2}\n")

    else:
        print("Число не троичное\n")


    ###################__task_3__####################
    print(f"{Fore.GREEN}Третье задание на 5{Style.RESET_ALL}")
    num_1 = int(input("Введите числа: "))

    i = 0
    for _ in str(num_1):
        i = i + int(_)

    print(f"Сумма {i}")

else:
    print("Введены не правельные параметры")