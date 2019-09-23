#!/usr/bin/python3
# -*-coding:utf-8 -*-
# Reference:**********************************************
# @Time     : 2019/9/22 20:02
# @Author   : Dorad
# @File     : cicle.py
# @User     : cug_x
# @Email     : cug.xia@gmail.com
# @Software: PyCharm

import numpy as np
from scipy.sparse.linalg import expm
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def get_sita(p):
    sita=np.arccos(np.dot(np.array((1,0,0)),p)/np.linalg.norm(p))
    if(p[1]<0):
        sita=np.pi*2-sita
    return sita

def get_arc_points(center, p1, p2,step=0.01):
    center = np.array(center)
    p1 = np.array(p1)
    p2 = np.array(p2)
    # R
    R = np.sqrt(np.sum(np.power(p1 - center, 2)))
    # get the plane, a*x+b*y+c*z=d
    cp = np.cross(center - p1, p2 - p1)
    a, b, c = cp
    d = np.dot(cp, center)
    # get the arc, need the min length
    cs = np.arccos(np.dot(p1 - center, p2 - center)/np.linalg.norm(p1 - center)/np.linalg.norm(p2 - center))
    roteAxis=np.cross(cp,[0,0,1])
    sita=np.arccos(np.dot(cp,[0,0,1])/np.linalg.norm(cp))
    if(get_sita(cp-np.array((0,0,1))))>0:
        sita=-sita
    roteMatrix=expm(np.cross(np.eye(3),roteAxis/np.linalg.norm(roteAxis)*sita))
    roteBackMatrix=expm(np.cross(np.eye(3),roteAxis/np.linalg.norm(roteAxis)*(-sita)))
    P=np.vstack((center,p1,p2))
    RP=np.dot(P,roteMatrix)
    sp1=get_sita(RP[1,:]-RP[0,:])
    sp2=get_sita(RP[2,:]-RP[0,:])
    if np.abs(sp1-sp2)>np.pi:
        st=np.hstack((np.arange(sp1,2*np.pi,step),np.arange(0,sp2,step))) if sp1>sp2 else np.hstack((np.arange(sp2,2*np.pi,step),np.arange(0,sp1,step)))
    else:
        st=np.arange(sp1,sp2,step) if sp2>sp1 else np.arange(sp2,sp1,step)
    arc=np.array((R*np.cos(st)+RP[0,0],R*np.sin(st)+RP[0,1],st*0+RP[0,2]))
    for i in np.arange(0,arc.shape[1]):
        arc[:,i]=np.dot(arc[:,i],roteBackMatrix)
    return arc


if __name__=='__main__':
    # key points of arc.
    P1 = [0, 1, 1]
    P2 = [1, 0, 1]
    C = [0, 0, 0]
    # get points of arc
    arc = get_arc_points(C, P1, P2, 0.01)
    # show the result
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot3D(arc[0, :], arc[1, :], arc[2, :])
    ax.set_zlabel('Z')
    ax.set_ylabel('Y')
    ax.set_xlabel('X')
    ax.scatter3D(P1[0], P1[1], P1[2])
    ax.scatter3D(P2[0], P2[1], P2[2])
    ax.scatter3D(C[0], C[1], C[2])
    plt.show()