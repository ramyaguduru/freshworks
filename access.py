import code as x 
x.create("sastra",25)
x.create("src",70,3600) 
x.read("sastra")
x.read("src")
x.create("sastra",50)
x.modify("sastra",55)
x.delete("sastra")
t1=Thread(target=(create or read or delete),args=(key_name,value,timeout))
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) 
t2.start()
t2.sleep()
