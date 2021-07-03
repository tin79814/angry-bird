# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 19:04:19 2020

@author: User
"""

import turtle,math,os
os.getcwd()

w_ratio=0.9
h_ratio=0.9
turtle.setup(width=w_ratio,height=h_ratio)
turtle.setworldcoordinates(-10,-10,10,10)
w0,h0=turtle.screensize()
if w0 >960:
    w_ratio=w_ratio*960/w0
if h0 > 600:
    h_ratio=h_ratio*600/h0
turtle.setup(width=w_ratio,height=h_ratio)
turtle.setworldcoordinates(-10,-10,10,10)
w0,h0=turtle.screensize()
turtle.setworldcoordinates(-0.5*w0,-0.5*h0,0.5*w0,0.5*h0)
turtle.bgpic("bgpict_angry_bird_960x600.gif")
turtle.ht()

icon=["angry_bird_black.gif","angry_bird_green.gif","angry_bird_red.gif"
      ,"angry_bird_white.gif","angry_bird_yellow.gif"]
for i in range(len(icon)):#把圖案弄進烏龜圖片檔
    turtle.register_shape(icon[i])
for i in range(len(icon)):
   
   
    fturtle=turtle.Turtle()
    fturtle.penup()
    fturtle.goto(-300,-76)
    fturtle.pendown()
    fturtle.shape(icon[i])
    print()
    print('玩家',i+1,'號')
    v0=float(input('請輸入初速'))
    angle=float(input('請輸入仰角(度)'))
    vx=v0*math.sin(angle*math.pi/180)
    vy=v0*math.cos(angle*math.pi/180)
    x=-300
    y=-76
    g=-9.8
    d=0
    y_gnd=-150
    t=0
    t1=0
   
    while y>=y_gnd:
        dt=0.1
        t=t+dt        
        piglst=[(180,-70),(288,-70),(230,-124)]
        pig=turtle.Turtle()
        pig_radius=15                                
        def position(vx,vy,dt):
            vx=vx+dt*d
            vy=vy+g*dt
            return(vx,vy)
        def velocity(x,y,vx,vy,dt):
            x=x+vx*dt
            y=y+vy*dt
            return(x,y)
        def checktarget(fturtle,piglst,pig_radius):
            hit=False
            x,y=fturtle.pos()
            for i in range(len(piglst)):
                pigx,pigy=piglst[i]
                distance=math.sqrt((x-pigx)**2+(y-pigy)**2)
                if distance<=pig_radius:
                    hit==True
                    fturtle.dot(pig_radius*2,'red')
                      
        checktarget(fturtle,piglst,pig_radius)        
        vx,vy=position(vx,vy,dt)
        x,y= velocity(x,y,vx,vy,dt)
        fturtle.goto(x,y)
        while t<=3:
            turtle1=turtle.Turtle()
            def pos1(vx,vy,dt):
                vx=vx+dt*d
                vy=vy+g*dt
                return(vx,vy)
            def velocity(x,y,vx,vy,dt):
                x=x+vx*dt
                y=y+vy*dt
                return(x,y)
            def checktarget(fturtle,piglst,pig_radius):
                hit=False
                x,y=fturtle.pos()
                for i in range(len(piglst)):
                    pigx,pigy=piglst[i]
                    distance=math.sqrt((x-pigx)**2+(y-pigy)**2)
                    if distance<=pig_radius:
                        hit==True
                        fturtle.dot(pig_radius*2,'red')
                          
            checktarget(fturtle,piglst,pig_radius)        
            vx,vy=position(vx,vy,dt)
            x,y= velocity(x,y,vx,vy,dt)
            fturtle.goto(x,y)
            


    