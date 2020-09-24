# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 21:07:34 2020

@author: lenovo
"""

import keras
import numpy as np
if __name__ = '__main__':
    path = ''
    path =args[0]
    # d = np.load('../0/TCGA-DX-AB35-01Z-00-DX3.B35C6035-4ED2-4E2F-A915-C59E1ACDE65D/TCGA-DX-AB35-01Z-00-DX3.B35C6035-4ED2-4E2F-A915-C59E1ACDE65D_2.npz'
    #             ,allow_pickle = True)
    d = np.load(path,allow_pickle=True)
    mask_2 = d['mask']
    t_2 = d['type']
    cen_2 = d['centroid']
    for i in range(6):
        print(i,':',list(t_2).count(i))