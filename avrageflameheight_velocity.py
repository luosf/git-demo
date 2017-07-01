# -*- coding: utf-8 -*-
"""
Created on Tue May 16 22:38:02 2017

@author: luoshengfeng
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio


# matlb  文件名
matfn=r"d:\我的文件\MATLAB\My thesis exmple testing\flame height and flame front (clip)\alldata(4.4cm)\2015-05-25（01）.mat";
data=sio.loadmat(matfn)
#获取火焰高度与火蔓延速率
clip_time_flameheight=data['clip_Time_Flameheight'];
clip_time_location=data['clip_Time_Locations'];
clip_time_location=clip_time_location[:,1:];
avLoc=np.average(clip_time_location,1)
iloc=np.arange(1,len(avLoc),25)
avLoc=avLoc[iloc]