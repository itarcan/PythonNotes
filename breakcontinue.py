#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 17:36:36 2020

@author: isitarcan
"""


#mini uygulama 

maaslar = [100,2000,3000,4000,5000]

def maas_ust(x):
    print(x*10/100+x)
    
def maas_alt(x):
    print(x*20/200+x)
    
for i in maaslar:
    if i >=3000:
        maas_ust(i)
    else:
        maas_alt(i)


#break & continue 

maaslar = [8000,5000,2000,1000,3000,7000,1000]
dir(maaslar)

maaslar.sort()
maaslar

for i in maaslar:
    if i == 3000:
        print("kesildi")
        break
    print(i)
