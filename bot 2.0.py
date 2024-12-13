from pyautogui import *
import pyautogui
import os
import keyboard
import time
import datetime




dataiczas = datetime.datetime.now()

bonnies = os.listdir('C:/Users/Nikiciaq/Desktop/Nikiciaq-mspbot-50660c9/ZWIERZAKI/')
z = len(bonnies)
for z in bonnies:
    print(z)

def wylancz():
    try:
        iks = pyautogui.locateOnScreen("iksik.png", confidence=0.8, region=(425,150,1355,700))
        pyautogui.click(iks)
    except:
        pass

def isbonnie(u):
    try:
        location = pyautogui.locateCenterOnScreen('C:/Users/Nikiciaq/Desktop/Nikiciaq-mspbot-50660c9/ZWIERZAKI/' + u, confidence=0.6, region=(425,150,1355,700))
        x, y = location
        print(u)
        pyautogui.click(x, y)
        del(x,y)
    except:
        pass
def czytrafil():
    trafione = False 
    while trafione is False:
        try:
            pokoje = pyautogui.locateOnScreen("pokoje.png", confidence=0.8)
            trafione = True
        except:
            pyautogui.click(1400, 90)
            time.sleep(2)
            pyautogui.click(737, 233)
    with open('counter.txt') as f:
        for line in f:
            pass
            last_line = line
            print(last_line)
        last = int(last_line[0]) 
        f = 0
    while f < last:
        pyautogui.click(1705, 333)
        time.sleep(5)
        f = f + 1
    
def czykrzak():
    pyautogui.click(852, 78)
    time.sleep(5)
    try:
      pyautogui.locateOnScreen("aktywnosc.png", confidence=0.8)
      return False
    except:
         return True   
def inkrzak():
    if czykrzak() is True:
        print("zaczynam odkrzaczanie")
        pyautogui.click(1900, 0)
        pyautogui.press("win")
        time.sleep(2)
        pyautogui.write("moviestarplanet") 
        time.sleep(1) 
        pyautogui.click(163, 518)
        time.sleep(2)
        t = 0
        while t == 0:
            try:
                login = pyautogui.locateOnScreen("login.png", confidence=0.8) 
                pyautogui.click(login)
                t = 1
            except:
                pass
        b = 0
        while b == 0:
            try:
                swinia = pyautogui.locateOnScreen("swinkacheck.png", confidence=0.8) 
                b = 1
            except:
                pass
        time.sleep(5)
        pyautogui.click(1400, 90)
        time.sleep(2)
        pyautogui.click(737, 233)
        czytrafil()
    else:
        print("dalej dziala")
        pass
czyusuwac = input("Usunąć zapis kroków i zacząć przeglądać pokoje od nowa? Y/N")
if czyusuwac == "Y":
    open('counter.txt', 'w').close()
    global counter
    counter = 1
elif czyusuwac == "N":
    with open('counter.txt') as f:
        for line in f:
            pass
            last_line = line
            print(last_line)
        last = int(last_line[0]) 
        counter = last
        czytrafil()
        
while keyboard.is_pressed('q') == False:

        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 387)
        time.sleep(7)
        
        wylancz()     
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        
        click(1189, 426)
        time.sleep(7)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 497)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 556)
        time.sleep(7)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 628)
        time.sleep(3)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 689)
        time.sleep(7)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        
        click(1400, 90)
        time.sleep(3)
        wylancz()
        
        click(1189, 765)
        time.sleep(7)
        
        wylancz()
        for z in bonnies:
             isbonnie(z)
        inkrzak()
        
        # highscores
        click(1400, 90)
        time.sleep(3)
        wylancz()
        # arrow
        click(1705, 333)
        counter = counter + 1
        licznik = str(counter)
        data = str(dataiczas)
        with open('counter.txt', "a") as plik:
            plik.write("\n")
            plik.write(licznik)
            plik.write(" ")
            plik.write(data)
        time.sleep(3)

        