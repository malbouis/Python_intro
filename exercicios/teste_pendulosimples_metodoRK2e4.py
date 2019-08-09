import numpy as np
import math
import scipy.integrate 
import matplotlib.pyplot as plt

import scipy.constants as cts

def ddtheta(theta,l):
    return -cts.g*math.sin(theta)/l

def solveEulerCromer(l,t,dt,theta0,dtheta0):
    """ solucao do pendulo com metodo euler-cromer, que funcionamelhor em osciladores"""
    t_list = [i*dt for i in range(0,int(t/dt)+1)]
    theta_list =[]
    theta_list.append(theta0)
    dtheta_list=[]
    dtheta_list.append(dtheta0)
    #print(dt,len(t_list))
    for i, ti in enumerate(t_list[1:]):
        dtheta = dtheta_list[i] + ddtheta(theta_list[i],l) * dt
        theta = theta_list[i] + dtheta * dt ## usa o dtheta atualizado !
        theta_list.append(theta)
        dtheta_list.append(dtheta)
    
    return t_list, theta_list,dtheta_list

def solveEuler(l,t,dt,theta0,dtheta0):
    t_list = [i*dt for i in range(0,int(t/dt)+1)]
    theta_list =[]
    theta_list.append(theta0)
    dtheta_list=[]
    dtheta_list.append(dtheta0)
    
    for i, ti in enumerate(t_list[1:]):
        dtheta = dtheta_list[i] + ddtheta(theta_list[i],l) * dt
        theta = theta_list[i] + dtheta_list[i] * dt #usa dtheta da iteracao anterior
        theta_list.append(theta)
        dtheta_list.append(dtheta)
    
    return t_list, theta_list,dtheta_list
   


def solveRK2_mine(l,t,dt,theta0,dtheta0):
    t_list = [i*dt for i in range(0,int(t/dt)+1)]
    theta_list=[]
    theta_list.append(theta0)
    dtheta_list=[]
    dtheta_list.append(dtheta0)
    for i, ti in enumerate(t_list[1:]):
        dtheta_i = dtheta_list[i] + dt/2* (ddtheta(theta_list[i],l) + ddtheta(theta_list[i]+dt*dtheta_list[i],l)) #avaliar no ponto medio
        dtheta_list.append(dtheta_i)
        theta_i = theta_list[i] + dt/2 * (dtheta_i+dtheta_list[i])
        theta_list.append(theta_i)
    return t_list,theta_list,dtheta_list
        
        
    
def solveRK4_mine(l,t,dt,theta0,dtheta0):
    t_list = [i*dt for i in range(0,int(t/dt)+1)]
    theta_list=[]
    theta_list.append(theta0)
    dtheta_list=[]
    dtheta_list.append(dtheta0)
    k1 = dt * ddtheta(theta0,l)
    k2 = dt* ddtheta(theta0+(dtheta0+k1)*dt/2,l)
    k3 = dt* ddtheta(theta0+(dtheta0+k2)*dt/2,l)
    k4 = dt* ddtheta(theta0+(dtheta0+k3)*dt,l)
    for i, ti in enumerate(t_list[1:]):
        dtheta_i = dtheta_list[i] + 1/6*(k1+2*k2+2*k3+k4)
        dtheta_list.append(dtheta_i)
        kt1 = dt* dtheta_list[i]
        kt2 = dt* (dtheta_list[i]+ dt/2 * ddtheta(theta_list[i]+kt1,l))
        kt3 = dt* (dtheta_list[i] + dt/2 * ddtheta(theta_list[i]+kt2,l))
        kt4 = dt* (dtheta_list[i] + dt * ddtheta(theta_list[i] +kt3,l))
        theta_i = theta_list[i] + 1/6 * (kt1+ 2*kt2 + 2*kt3 + kt4)
        theta_list.append(theta_i)
        k1 = dt * ddtheta(theta_i,l)
        k2 = dt* ddtheta(theta_i+(dtheta_i+k1)*dt/2,l)
        k3 = dt* ddtheta(theta_i+(dtheta_i+k2)*dt/2,l)
        k4 = dt* ddtheta(theta_i+(dtheta_i+k3)*dt,l)
    return t_list,theta_list,dtheta_list
        
def f(t,y,l): ## y[0] --> theta e y[1]--> dtheta ; o retorno e  dy0/dt, dy1/dt ou seja  --> dtheta , ddtheta
    return y[1],ddtheta(y[0],l)
    
def solveSciPyInt(l,t,dt,theta0,dtheta0):
    sol_spring=scipy.integrate.solve_ivp(lambda t , y : f(t,y,l),(0,t),(theta0,dtheta0),max_step=dt,method="RK23")
    return sol_spring.t,sol_spring.y[0],sol_spring.y[1]

    
if __name__=="__main__":
    l=1
    ttot=30
    dt=0.01
    ang0=math.radians(5)
    vang0=0.1
    trk,thetark,dthetark    = solveRK2_mine(l,ttot,dt,ang0,vang0)
    trk4,thetark4,dthetark4 = solveRK4_mine(l,ttot,dt,ang0,vang0)
    t,theta,dtheta          = solveEuler(l,ttot,dt,ang0,vang0)
    tec,thetaec,dthetaec    = solveEulerCromer(l,ttot,dt,ang0,vang0)
    tsp,thetasp,dthetasp    = solveSciPyInt(l,ttot,dt,ang0,vang0)
   
    
    plt.plot(t,theta,label="Euler")
    plt.plot(trk,thetark,label="Runge-Kutta 2 grau")
    plt.plot(trk4,thetark4,label="Runge-Kutta 4 grau")
    plt.plot(tec,thetaec,label="Euler-Cromer")
    plt.plot(tsp,thetasp,label="SciPy Integrate RK23")

    B  = math.sqrt(cts.g/l)
    tgC= (ang0/vang0)*B
    C  = math.atan(tgC)
    A  = ang0/math.sin(C)
    print(A,B,C)
    thetateo= [A*math.sin(ti*B+ C) for ti in t]
    plt.plot(t,thetateo,label="Teorico")
    plt.xlabel("t [s]")
    plt.ylabel("θ [rad]")
    plt.legend(loc="upper left")
    plt.show()
