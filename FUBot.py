import os
from random import randint
import time
from time import sleep

victim = ""
victim_word = ""
words_polish = {
    "1":":(",
    "2":"Przykro mi to słyszeć.",
    "3":"PRZESTAŃ!",
    "4":"Chyba ty.",
    "5":"To nie prawda."
}

words_english = {
    "1":":(",
    "2":"I am sorry to hear it.",
    "3":"STOP!",
    "4":"I think you.",
    "5":"It's not true."
}

words_german = {
    "1":":(",
    "2":"Es tut mir leid, das zu hören.",
    "3":"PAUSE!",
    "4":"Ich denke du.",
    "5":"Es ist nicht wahr."
}

words_russian = {
    "1":":(",
    "2":"Мне жаль это слышать.",
    "3":"ОСТАНОВКА!",
    "4":"Я думаю ты.",
    "5":"Это неправда."
}

words_ukrainian = {
    "1":":(",
    "2":"Мені шкода це чути.",
    "3":"СТОП!",
    "4":"Я думаю, що ви.",
    "5":"Це неправда."
}

def config_polish():
  print("Witam w programie FUBot!")
  input("Naciśnij ENTER, aby kontynuować lub Ctrl+C aby wyjść.")
  print("Podaj imię swojej ofiary.")
  victim = input("> ")
  print(f"Imię twojej ofiary to {victim}.")
  input("Naciśnij ENTER, aby zacząć.")
  return victim

def config_english():
  print("Welcome to the FUBot program!")
  input("Press ENTER to continue or Ctrl + C to exit.")
  print("Name your victim.")
  victim = input("> ")
  print(f"Your victim's name is {victim}.")
  input("Press ENTER to start.")
  return victim

def config_german():
  print("Willkommen beim FUBot-Programm!")
  print("Drücken Sie die EINGABETASTE, um fortzufahren, ")
  input("oder Strg + C, um den Vorgang zu beenden.")
  print("Nennen Sie Ihr Opfer.")
  victim = input("> ")
  print(f"Der Name Ihres Opfers ist {victim}.")
  input("Drücken Sie zum Starten die EINGABETASTE.")
  return victim

def config_russian():
  print("Добро пожаловать в программу FUBot!")
  input("Нажмите ENTER, чтобы продолжить, или Ctrl + C, чтобы выйти.")
  print("Назовите свою жертву.")
  victim = input("> ")
  print(f"Имя вашей жертвы {victim}.")
  input("Нажмите ENTER, чтобы начать.")
  return victim

def config_ukrainian():
  print("Ласкаво просимо до програми FUBot!")
  input("Натисніть ENTER, щоб продовжити, або Ctrl + C, щоб вийти.")
  print("Назвіть свою жертву.")
  victim = input("> ")
  print(f"Ім'я вашої жертви {victim}.")
  input("Натисніть ENTER, щоб почати.")
  return victim

def session_polish(victim):
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("logs.txt","a")
    f.write(f"Session openned at {time.asctime(time.localtime(time.time()))} in Polish\n")
    user_input = ""
    while not user_input == "/exit":
        user_input = input("(Napisz /exit aby wyjść.)> ")
        if not user_input == "/exit":
            print(f"TY: {user_input}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] USER: {user_input}\n")
            sleep(3)
            print(f"{victim} pisze...", end="\r")
            sleep(2)
            print("                              ", end="\r")
            victim_word = words_polish[str(randint(1,5))]
            print(f"{victim}: {victim_word}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] {victim}: {victim_word}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    f.write(f"Session closed at {time.asctime(time.localtime(time.time()))}\n")
    f.close()
    print("Sesja zamknięta.")
    input("Naciśnij ENTER, aby wyjść.")

def session_english(victim):
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("logs.txt","a")
    f.write(f"Session openned at {time.asctime(time.localtime(time.time()))} in English\n")
    user_input = ""
    while not user_input == "/exit":
        user_input = input("(Write /exit to exit.)> ")
        if not user_input == "/exit":
            print(f"YOU: {user_input}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] USER: {user_input}\n")
            sleep(3)
            print(f"{victim} is writing...", end="\r")
            sleep(2)
            print("                              ", end="\r")
            victim_word = words_english[str(randint(1,5))]
            print(f"{victim}: {victim_word}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] {victim}: {victim_word}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    f.write(f"Session closed at {time.asctime(time.localtime(time.time()))}\n")
    f.close()
    print("Session closed.")
    input("Press ENTER to exit.")

def session_german(victim):
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("logs.txt","a")
    f.write(f"Session openned at {time.asctime(time.localtime(time.time()))} in German\n")
    user_input = ""
    while not user_input == "/exit":
        user_input = input("(Geben Sie /exit ein, um zu beenden.)> ")
        if not user_input == "/exit":
            print(f"DU: {user_input}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] USER: {user_input}\n")
            sleep(3)
            print(f"{victim} schreibt...", end="\r")
            sleep(2)
            print("                              ", end="\r")
            victim_word = words_german[str(randint(1,5))]
            print(f"{victim}: {victim_word}")
            f.write(f"[{time.asctime(time.localtime(time.time()))}] {victim}: {victim_word}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    f.write(f"Session closed at {time.asctime(time.localtime(time.time()))}\n")
    f.close()
    print("Sitzung geschlossen.")
    input("Drücken Sie zum Beenden ENTER.")

def session_russian(victim):
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("logs.txt","a")
    f.write(f"Chat registration is not available in Russian due to some errors.")
    user_input = ""
    while not user_input == "/exit":
        user_input = input("(Введите /exit, чтобы выйти.)> ")
        if not user_input == "/exit":
            print(f"ТЫ: {user_input}")
            #f.write(f"[{time.asctime(time.localtime(time.time()))}] USER: {user_input}\n")
            sleep(3)
            print(f"{victim} пишет...", end="\r")
            sleep(2)
            print("                              ", end="\r")
            victim_word = words_russian[str(randint(1,5))]
            print(f"{victim}: {victim_word}")
            #f.write(f"[{time.asctime(time.localtime(time.time()))}] {victim}: {victim_word}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    #f.write(f"Session closed at {time.asctime(time.localtime(time.time()))}\n")
    f.close()
    print("Сессия закрыта.")
    input("Нажмите ENTER для выхода.")

def session_ukrainian(victim):
    os.system('cls' if os.name == 'nt' else 'clear')
    f = open("logs.txt","a")
    f.write(f"Chat registration is not available in Ukrainian due to some errors.")
    user_input = ""
    while not user_input == "/exit":
        user_input = input("(Написати /exit вийти.)> ")
        if not user_input == "/exit":
            print(f"ТИ: {user_input}")
            #f.write(f"[{time.asctime(time.localtime(time.time()))}] USER: {user_input}\n")
            sleep(3)
            print(f"{victim} пише...", end="\r")
            sleep(2)
            print("                              ", end="\r")
            victim_word = words_ukrainian[str(randint(1,5))]
            print(f"{victim}: {victim_word}")
            #f.write(f"[{time.asctime(time.localtime(time.time()))}] {victim}: {victim_word}\n")
    os.system('cls' if os.name == 'nt' else 'clear')
    #f.write(f"Session closed at {time.asctime(time.localtime(time.time()))}\n")
    f.close()
    print("Засідання закрито.")
    input("Натисніть ENTER, щоб вийти.")

def about():
    print("FUBot version: 1.0")
    print("Createdf by: Piotr305")
    print("License: GNU GPL v3")
    input()
    start()

def start():
    print("")
    print("Wybierz język/Select language/Sprache wählen/выберите язык/вибрати мову")
    print("1) Polski")
    print("2) English")
    print("3) Deutsch")
    print("4) Русский")
    print("5) український")
    print("")
    print("Inne/Other/Sonstiges/Другой/Інший")
    print("6) O/About/Um/О/про")
    print("7) Wyjście/Exit/Ausgang/Выход/Вихід")
    language = input("> ")
    if language == "1":
        session_polish(config_polish())
    elif language == "2":
        session_english(config_english())
    elif language == "3":
        session_german(config_german())
    elif language == "4":
        session_russian(config_russian())
    elif language == "5":
        session_ukrainian(config_ukrainian())
    elif language == "6":
        about()
    elif language == "7":
        exit()

start()