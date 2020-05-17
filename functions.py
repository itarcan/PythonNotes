#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 14:43:21 2020

@author: isitarcan
"""


#FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI

print()
?print
print()


#Fonksiyon Nasil Yazilir?

4*4
3**3


def kare_al(x):
    print(x**2)
    
kare_al(3)

kare_al(5)


#Bilgi Notuyla Cikti Uretmek

def kare_al(x):
    print("Girilen Sayinin Karesi:"+str(x**2))
    
kare_al(3)


def kare_al(x):
    print("Girilen Sayi: " +str(x)+" Karesi:"+str(x**2))
    
kare_al(3)

def kare_al(x):
    print("Girilen Sayi: " +str(x)+" Karesi:"+str(x**2))
    
kare_al(3)




#Iki Argumanli Fonksiyon Tanimlamak

def kare_al(x):
    print(x**2)
    
def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(2,3)


#On tanimli Argumanlar

?print

def carpma_yap(x,y=1):
    print(x*y)
    
carpma_yap(3)

#Argumanlarin Siralamasi 


#Ne Zaman Fonksiyon Yazilir ? 

#isi,nem,sarj

(40+25)/90 


def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)
    
direk_hesap(25,40,70)


#Fonksiyon Ciktilarini Girdi Olarak Kullanmak



def direk_hesap(isi,nem,sarj):
    return((isi+nem)/sarj)
    
 cikti=direk_hesap(25,40,70)*9
cikti
