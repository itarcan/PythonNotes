#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 16:23:43 2020

@author: isitarcan
"""


#mini uygulama
sinir = 50000

magaza_adi= input("Magaza Adi Nedir?")
gelir = input("Gelirinizi Giriniz:")

if gelir>sinir:
    print("Tebrikler:" + magaza_adi + " promosyon kazandiniz!")
elif gelir< sinir:
    print("Uyari! Cok dusuk gelir:" + str(gelir))
else:
    print("Takibe devam")