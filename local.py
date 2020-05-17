#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 15:24:07 2020

@author: isitarcan
"""


#Local ve Global Degiskenler 


x = 10
y = 20


def carpma_yap(x=2,y=1):
    return x*y


carpma_yap(2,3)

#Local Erki Alanindan Global Etki Alanini Degistirmek


x = []
def eleman_ekle(y):
    x.append(y)
    print(str(y)+ "ifadesi eklendi")
    
eleman_ekle("ali")
    

