# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 15:01:43 2020

@author: lenovo
"""

import numpy as np
import  pandas as pd
import  json
import os
import shutil

data_dir = '../ouput_dir/0'
file_list = os.listdir(data_dir)
etx = '.npz'
for file in file_list:
    file_name = file+'/'+file+etx
    src_path = os.path.join(data_dir,file_name)
    shutil.move(src_path,data_dir)
    
