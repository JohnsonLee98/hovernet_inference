# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:37:39 2020

@author: lenovo
"""
import numpy as np
import  pandas as pd
import  json
import os

clinical = '../clinical.cart.2020-09-17.json'
clinical_data = pd.read_json(clinical)
biosp = '../biospecimen.cart.2020-09-17.json'
bio_data = pd.read_json(biosp)
meta = '../metadata.cart.2020-09-17.json'
meta_data = pd.read_json(meta)

data_dir = '../data/'
file_list = os.listdir(data_dir)

for i in range(len(file_list))
    print(i)



