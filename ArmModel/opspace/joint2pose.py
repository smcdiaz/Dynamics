# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 18:03:59 2013

@author: Santiago
"""
from dkyn_q import coord_q3,coord_q4,coord_q5,coord_q6
from plant import *

def j2p(y):
    #Substitution of angles in direct kynematics
    XYZ_m3=[]
    XYZ_m4=[]
    XYZ_m5=[]
    XYZ_m6=[]

    for i in range(len(y[:,1])-1):
        xyz_m3=coord_q3
        xyz_m4=coord_q4
        xyz_m5=coord_q5
        xyz_m6=coord_q6
        
        xyz_m3=xyz_m3.subs({q3:y[i,0],q4:y[i,1],q5:y[i,2]})
        XYZ_m3.append(xyz_m3)
        
        xyz_m4=xyz_m4.subs({q3:y[i,0],q4:y[i,1],q5:y[i,2]})
        XYZ_m4.append(xyz_m4)
        
        xyz_m5=xyz_m5.subs({q3:y[i,0],q4:y[i,1],q5:y[i,2]})
        XYZ_m5.append(xyz_m5)
        
        xyz_m6=xyz_m6.subs({q3:y[i,0],q4:y[i,1],q5:y[i,2]})
        XYZ_m6.append(xyz_m6)
    return  XYZ_m3, XYZ_m4, XYZ_m5, XYZ_m6
 
def traj(XYZ_m3, XYZ_m4, XYZ_m5, XYZ_m6):    
    #Joints trajectory   
    tray=[]
    for i in range(0,len(XYZ_m3)-1):
        #Scaling factor 0.5
        q_tray=[(XYZ_m3[i][0],XYZ_m3[i][1]),(XYZ_m4[i][0],XYZ_m4[i][1]),
                (XYZ_m5[i][0],XYZ_m5[i][1]),(XYZ_m6[i][0],XYZ_m6[i][1])]
        tray.append(q_tray)
    return tray
