import threading 
from threading import*
import time

dt={} 

def create(key,value,timeout=0):
    if key in dt:
        print("error: this key already exists") 
    else:
        if(key.isalpha()):
            if len(dt)<(1024*1024*1024) and value<=(16*1024*1024):  
                if timeout==0:
                    ls=[value,timeout]
                else:
                    ls=[value,time.time()+timeout]
                if len(key)<=32:
                    dt[key]=ls
            else:
                print("error: Memory limit exceeded!! ")
        else:
            print("error: Invalind key_name!! key_name must contain only alphabets and no special characters or numbers")
def read(key):
    if key not in dt:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        bd=dt[key]
        if bd[1]!=0:
            if time.time()<bd[1]: 
                stri=str(key)+":"+str(bd[0]) 
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            stri=str(key)+":"+str(bd[0])
            return stri
def delete(key):
    if key not in dt:
        print("error: given key does not exist in database. Please enter a valid key") 
    else:
        bd=dt[key]
        if bd[1]!=0:
            if time.time()<bd[1]: 
                del dt[key]
                print("key is successfully deleted")
            else:
                print("error: time-to-live of",key,"has expired") 
        else:
            del dt[key]
            print("key is successfully deleted")


def modify(key,value):
    bd=dt[key]
    if bd[1]!=0:
        if time.time()<bd[1]:
            if key not in dt:
                print("error: given key does not exist in database. Please enter a valid key") 
            else:
                ls=[]
                ls.append(value)
                ls.append(b[1])
                dt[key]=l
        else:
            print("error: time-to-live of",key,"has expired") 
    else:
        if key not in dt:
            print("error: given key does not exist in database. Please enter a valid key") 
        else:
            ls=[]
            ls.append(value)
            ls.append(b[1])
            dt[key]=ls
