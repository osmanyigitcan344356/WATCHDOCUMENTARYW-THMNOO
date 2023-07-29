import time
import time
import tkinter
# from PIL import ImageTk,Image
# import vlc
# import platform
from tkinter import *
from tkinter import PhotoImage


import cv2
import messagebox
from PIL import Image



page1=Tk()
genis=200
uzunluk=200
page1.title("MAİN PAGE")
page1.minsize(genis,uzunluk)
page1.config(bg="light blue")
FONT=("Arial",40,"bold")
info_lab=Label(page1,text="WELCOME :-)",font=FONT)
info_lab.pack()

foto=PhotoImage(file="profil.png")
photo1=Label(image=foto)
photo1.place(x=-10,y=10)
def time_1():
    my_time=time.strftime("%H:%M:%S")
    clo_label.config(text=my_time)
    page1.after(1000,time_1)


clo_label = Label()
clo_label.config(width=14,height=4,font="Calibri")
clo_label.pack()
time_1()





def but_giris_page():
    pagegiris=tkinter.Toplevel()
    pagegiris.minsize(width=750,height=750)
    pagegiris.title("USER LOGİN")
    def time2():
        myt=time.strftime("%H:%M:%S")
        time_lab.config(text=myt)
        pagegiris.after(1000,time2)

    time_lab=Label(pagegiris)
    time_lab.config(height=3,width=15)
    time_lab.pack(side="top")
    time_lab.config(bg="light blue",fg="black")
    time_lab.config(padx=12,pady=12)
    time2()

    lab_use=Label(pagegiris,text="USERNAME :")
    lab_use.pack()
    lab_use1=Entry(pagegiris,width=30)
    lab_use1.pack()
    lab_paw=Label(pagegiris,text="PASSWORD :")
    lab_paw1=Entry(pagegiris,width=30)
    lab_paw.pack()
    lab_paw1.pack()

    def kullanıcı_giris(instance=None):
        username=str(lab_use1.get())
        password=str(lab_paw1.get())
        if len(lab_use1.get())==0 or len(lab_paw1.get())==0:
            messagebox.showinfo("WARNİNG","PLEASE ENTER YOUR İNFORMATİON")
        elif username=="osman" and password=="123":
            messagebox.showinfo("GOOD","YOU'RE RİGHT!")
            page4=Tk()
            page4.minsize(width=400,height=400)
            mymovie=Listbox(page4)
            movie_list=["MOVİE","MY COMMENT","MY POİNT"]
            mymovie.config(height=4,width=30)
            for x in range(len(movie_list)):
                mymovie.insert(x,movie_list[x])

            def watch(event):
                global degerlendir
                items = mymovie.get(mymovie.curselection())
                selec=mymovie.curselection()
                first=mymovie.get(selec[0])
                if items=="MOVİE":
                    Page = Tk()
                    Page.title(first)
                    link=cv2.VideoCapture("Belgesel.mp4")



                    while(True):
                        ret,frame=link.read()
                        cv2.imshow("video play",frame)
                        cv2.volume=1.0
                        if (cv2.waitKey(1) & 0xFF==ord('g')):
                            break
                        else:
                            continue
                    Page.mainloop()

                elif items=="MY COMMENT":
                    text45=Text(page4)
                    text45.insert(END,items)
                    text45.pack()

                elif items=="MY POİNT":
                    page44=Tk()
                    myspin=Spinbox(page44)
                    myspin.config(from_=0,to=10)
                    myspin.pack()
                    değerlendirme=int(myspin.get())
                    if değerlendirme:
                        lab3=Label(page44)
                        lab3.config(text="what's your point about app ?")
                        lab3.pack()
                        def degerlendir():
                            if değerlendirme==3 or değerlendirme==2 or değerlendirme==1 or değerlendirme==0:
                                bad=Label(page44)
                                bad.config(text="I think that's app its so bad")
                                bad.pack(side="top")
                            elif değerlendirme==7 or değerlendirme==6 or değerlendirme==5 or değerlendirme==4:
                                norm=Label(page44)
                                norm.config(text="I think that's app is normal , not bad or not good")
                                norm.pack(side="top")
                            else:
                                good=Label(page44)
                                good.config(text="that's so crazy dude! ı like it ")
                                good.pack(side="top")


                    chose=Button(page44)
                    chose.config(text="about app")
                    chose.config(command=degerlendir)
                    chose.pack()
                    page44.mainloop()





            mymovie.bind("<<ListboxSelect>>",watch)
            mymovie.pack(side="bottom")


            page4.mainloop()

        else:
            messagebox.showinfo("WARNİNG !!","GUESS YOUR PASSWORD OR USERNAME İS FAULSE")

    giris=Button(pagegiris)
    giris.config(text="LOGİN")
    giris.config(command=kullanıcı_giris)
    giris.pack()
    photo2=PhotoImage(file="komik.gif")
    photo22=Label(pagegiris,image=photo2)
    photo22.pack()
    pagegiris.mainloop()




#but_login.place(x=255,y=140)




but_giris=Button()
but_giris.config(text="user login =>")
but_giris.config(command=but_giris_page)
#but_giris.place(x=200,y=100)

def renklendirme():
    pass
    color_list=["orange","red","yellow",
                "green","white"]
    for x in color_list:
        metin.config(bg=x)

metin=Label()
metin.config(text="HI I AM OSMAN , I AM STUDENT OF UNIVERSTY THEN MY DEPARTMENT İS SOFTWARE AND I AM FROM TURKEY""\n""WELCOME TO MY APP , İN HERE YOU CAN CONTROL THE TİME , PLAY THE VİDEO""\n""AND SOMETHİNG LİKE THAT , GOOD PLAY :-)")

metin.config(padx=100,pady=100)
metin.config(bg="orange",fg="white")


but_giris.pack(side="top")
metin.pack(side="top")

isar=PhotoImage(file="İŞARET.png")

isaret=Label(image=isar)
isaret.pack(side="bottom")
isaret.width=50
isaret.height=50
page1.mainloop()






