#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 18:48:02 2020

@author: isitarcan
"""


sozluk = {"REG" : "Regresyon Modeli",
          "LOJ" : "Lojistik Regresyon",
          "CART" : "Classification and Reg"}
sozluk[0]


sozluk["REG"]

sozluk = {"REG" : {"RMSE":10,
                   "MSE" :20,
                   "SSE" :30},
          
          "LOJ" : {"RMSE":10,
                   "MSE" :20,
                   "SSE" :30},
          
          
          "CART" : {"RMSE": 10,
                    "MSE" : 20,
                    "SSE" : 30}} 

sozluk["GBM"] = "Gradient Boosting Mac"
sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"
sozluk

sozluk[1]= "Yapay Sinir Aglari"

sozluk

#Veri Yapilari - Setler


#Set olusturmak

s = set()
s

l= [1,"a","ali",123]
s = set(l)
s

ali ="lutfen_ata_bak ma_uza ya_git"
type(ali)

s= set(ali)
s

l=["ali","lutfen", "ata","bakma","uzaya","git","git","ali","git"]
l

s=set(l)
s
dir(s)


#Setler - Klasik Kume Islemleri


# =============================================================================
# #difference() ile iki kumenin farkini ya da "-"ifadesi
# #intersection() iki kume kesisimi ya da "&" ifadesi
# #union() iki kumenin birlesimi
# #symmetric_difference() ikisinde de olmayanlari
# =============================================================================


#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)


#intersection & union

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.intersection(set2)
set2.intersection(set1)


kesisisim = set1&set2
kesisim