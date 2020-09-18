# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 19:37:39 2020

@author: lenovo
"""
import numpy as np
import  pandas as pd
import  json
import os
import shutil
clinical = '../clinical.cart.2020-09-17.json'
clinical_data = pd.read_json(clinical)
biosp = '../biospecimen.cart.2020-09-17.json'
bio_data = pd.read_json(biosp)
meta = '../metadata.cart.2020-09-17.json'
meta_data = pd.read_json(meta)

data_dir = '../data/'
file_list = os.listdir(data_dir)

for i in range(100):
    m = meta_data[i:i+1]
    
    fname = m.at[i,'file_name']
    case_id = m.at[i,'associated_entities'][0]['case_id']
    c_data = clinical_data[clinical_data.case_id ==case_id]
    diag  = c_data.at[c_data.index[0],'diagnoses'][0]
    tumor_stage = diag['tumor_stage']
    fid = m.at[i,'file_id']
    # print(tumor_stage)
    src_name = fid+'/'+fname
    src_file = os.path.join(data_dir,src_name)
    
    if(tumor_stage == 'not reported'):
        fpath = os.path.join(data_dir,0)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage i'):
        fpath = os.path.join(data_dir,1)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iia'):
        fpath = os.path.join(data_dir,2)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)

    elif (tumor_stage == 'stage iib'):
        fpath = os.path.join(data_dir,2)
        if not os.path.exists(fpath):
            os.makedirs(fpath) 
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage ii'):
        fpath = os.path.join(data_dir,2)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iii'):
        fpath = os.path.join(data_dir,3)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iiia'):
        fpath = os.path.join(data_dir,3)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iiib'):
        fpath = os.path.join(data_dir,3)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iv'):
        fpath = os.path.join(data_dir,4)
        if not os.path.exists(fpath):
            os.makedirs(fpath)  
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage iva'):
        fpath = os.path.join(data_dir,4)
        if not os.path.exists(fpath):
            os.makedirs(fpath)
        shutil.move(src_file,fpath)
    elif (tumor_stage == 'stage ivb'):
        fpath = os.path.join(data_dir,4)
        if not os.path.exists(fpath):
            os.makedirs(fpath) 
        shutil.move(src_file,fpath)
    
    