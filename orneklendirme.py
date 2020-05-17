#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 13:06:25 2020

@author: isitarcan
"""


#NESNE YONELIMLI PROGRAMLAMA


#Sinif Ozellikleri(Class attributes)

class VeriBilimci():
    bolum =''
    sql ='Evet'
    deneyim_yili = 0
    bildigi_diller =[]
    
#Siniflarin ozelliklerini erismek
VeriBilimci.bolum
VeriBilimci.sql

#siniflarin ozelliklerini degistirmek
VeriBilimci.sql="Hayır"
VeriBilimci.sql

#Sinif Orneklendirmesi (instantiation)

ali = VeriBilimci()

ali.sql
ali.deneyim_yili
ali.bolum
ali.bildigi_diller.append("Python")
ali.bildigi_diller

veli = VeriBilimci()
veli.sql

veli.bildigi_diller

#Ornek ozellikleri


class VeriVilimci():
    bildigi_diller = ["R","PYTHON"]
    def __init__(self):
        self.bildigi_diller = []
        
ali = VeriBilimci()
ali.bildigi_diller

veli = VeriBilimci()
veli.bildigi_diller

ali.bildigi_diller.append("Python")
ali.bildigi_diller

