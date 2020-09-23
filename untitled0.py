# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 16:55:33 2020

@author: lenovo
"""

import  keras
 
bagnet9= 'https://bitbucket.org/wielandbrendel/bag-of-feature-pretrained-models/raw/d413271344758455ac086992beb579e256447839/bagnet32.h5'
model_path = keras.utils.get_file(
	                'bagnet32.h5',
	                bagnet9,
	                cache_subdir='models',
	                file_hash='96d8842eec8b8ce5b3bc6a5f4ff3c8c0278df3722c12bc84408e1487811f8f0f')

bg = '../bagnet8.h5'
model = keras.models.load_model(model_path)
# model.summary()
