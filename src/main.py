# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:03:00 2019

@author: pom_p
"""
import compress as comp
import numpy as np

X = comp.load_data('Train')
comp.compress_images(X,1000)
