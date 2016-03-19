1
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:32:21 2016

@author: fxdhi
"""

z1="#########"
z2="       # "
z3="      #  "
z4="     #   "
z4="    #    "
z5="   #     "
z6="  #      "
z7=" #       "
z8="#########"
h1="#        "
h2="#        "
h3="#        "
h4="#########"
h5="#       #"
h6="#       #"
h7="#       #"
h8="#       #"
o1="#########"
o2="#       #"
o3="#       #"
o4="#       #"
o5="#       #"
o6="#       #"
o7="#       #"
o8="#########"
u1="#       #"
u2="#       #"
u3="#       #"
u4="#       #"
u5="#       #"
u6="#       #"
u7="#       #"
u8="#########"





def change_mode():
    try:
        mode = raw_input("Enter the run_mode(0-1): ")
    except:
        pass
    if mode == '0':
        myname()
    elif mode == '1':
        randomorder()
        
    

def myname():
   print z1,h1,o1,u1
   print z2,h2,o2,u2
   print z3,h3,o3,u3
   print z4,h4,o4,u4
   print z5,h5,o5,u5
   print z6,h6,o6,u6
   print z7,h7,o7,u7
   print z8,h8,o8,u8



def randomorder():
    print u1,o1,h1,z1
    print u2,o2,h2,z2
    print u3,o3,h3,z3
    print u4,o4,h4,z4
    print u5,o5,h5,z5
    print u6,o6,h6,z6
    print u7,o7,h7,z7
    print u8,o8,h8,z8

change_mode()




         
