from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox, filedialog
import pandas as pd, json

root = Tk()
root.title("Mall Pelayanan Publik Jember")

class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

class antrianQueue:
    def destroy():
        for widget in root.winfo_children():
            widget.destroy()
    def __init__(self,n=50):
        self.size = n
        self.sizeIn = 0
        self.data = []
    def antrianFull(self):
        if self.sizeIn == self.size:
            return True
        else:
            return False
    def antrianKosong(self):
        if self.sizeIn == 0:
            return True
        else:
            return False
    def enqueue(self,name):
        import time, os
        if self.antrianFull():
            print("Mohon Maaf Sementara Ini Antrian Sudah Terlalu Penuh")
            print("Silahkan Menunggu Terlebih Dahulu ! Terima Kasih.")
        else:
            self.data.append(name)
            self.sizeIn = len(self.data)
            messagebox.showinfo("Info","Telah Berhasil ditambahkan ke antrian")
            menuCusT()
            os.system("cls")
            print(name,"Telah berhasil ditambahkan ke antrian.")
    def dequeue(self):
        if self.antrianKosong():
            print("Antrian masih dalam keadaan kosong")
            return None
        else:
            clearData = self.data.pop(0)
            self.sizeIn == len(self.data)
            print("Antrian dengan nama :", clearData)
            print("Dimohon untuk melakukan konfirmasi")
            print("Antrian setelah ini adalah :", self.data)
        print("Tekan enter untuk lanjut")
        input()
    def lihatAntrian(self):
        if self.antrianKosong():
            print("Saat ini antrian masih kosong")
        else:
            print("========== DAFTAR ANTRIAN MALL PELAYANAN PUBLIK ==========")
            number = 1
            for i in self.data:
                print(" "+str(number)+". ",i)
                number += 1
            print("Total antrian saat ini :", len(self.data))
        print("Tekan enter untuk lanjut")
        input()

data2 = antrianQueue()

def destroy():
    for widget in root.winfo_children():
        widget.destroy()

def menuAwal():
    global root
    destroy()
    root.geometry("500x300")

    frameMA1 = LabelFrame(master=root)
    frameMA1.pack(padx=40, pady=10, fill="both", expand=True)

    jdlMenu = Label(master=frameMA1, text="Mall Pelayanan Publik \nJember", font=("Roboto", 20, "bold"))
    jdlMenu.pack(padx=10, pady=10)

    frameMA2 = LabelFrame(master=frameMA1)
    frameMA2.pack(padx=40, pady=10, fill="both", expand=True)

    BtnCusT = Button(master=frameMA2, text="Customer", command=menuCusT, width=40)
    BtnCusT.pack(pady=10)
    BtnAdm = Button(master=frameMA2, text="Admin", command=LogAdmin, width=40)
    BtnAdm.pack(pady=10)
    BtnEx = Button(master=frameMA2, text="Keluar", command=root.quit, width=40)
    BtnEx.pack(pady=10)

def menuCusT():
    destroy()
    global root
    root.geometry("400x300")
    frameCusT = LabelFrame(master=root)
    frameCusT.pack(padx=40, pady=30, fill="both", expand=True)

    jdlCus = Label(master=frameCusT, text="MALL PELAYANAN PUBLIK \n JEMBER", font=("Roboto", 15, "bold"))
    jdlCus.pack(padx=10, pady=10)

    frame1 = LabelFrame(master=frameCusT)
    frame1.pack(padx=40, pady=10, fill="both", expand=True)

    jdlCus1 = Label(master=frame1, text="Menu Customer", font=("Roboto", 10))
    jdlCus1.pack(padx=10, pady=10)

    BtnCusT = Button(master=frame1, text="Ambil Nomor Antrian", width=40, command=AmbAnt)
    BtnCusT.pack(pady=10)
    BtnCusT = Button(master=frame1, text="Keluar", command=menuAwal, width=40)
    BtnCusT.pack(pady=10)
    
def LogAdmin():
    global root, newphoto, img1
    destroy()
    root.geometry("800x400")

    frameLA1 = LabelFrame(master=root, border=0)
    frameLA1.place(width=400, height=400)
    photo = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\peng.png")
    resize = photo.resize((420, 320), Image.ANTIALIAS)
    newphoto = ImageTk.PhotoImage(resize)
    lbl = Label(master=frameLA1,image=newphoto, border=0, bg="white")
    lbl.place(x=0, y=0, width=400, height=400)

    frameLA2 = LabelFrame(master=root, border=0, bg="white")
    frameLA2.place(x=400,width=400, height=400)

    img1 = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\Vec1.png")
    size = img1.resize((400, 316), Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(size)
    Label(master=frameLA2,image=img1,border=0,bg='white').place(x=100,y=190)

    jdlAdm = Label(master=frameLA2, text="SIGN IN", font=("Roboto", 20, "bold"), fg="#FF7572", bg="white")
    jdlAdm.pack(padx=10, pady=50)

    def on_enter(e):
        eUser.delete(0,'end')
        eUser.config(fg="black")  
        Frame(frameLA2,width=245,height=2,bg='#FF7572').place(x=80,y=140)    
    def on_leave(e):
        if eUser.get()=='':   
            eUser.insert(0,'Username')
            eUser.config(fg="gray") 
            Frame(frameLA2,width=245,height=2,bg='#4471D8').place(x=80,y=140) 

    eUser = Entry(master=frameLA2, width=40, border=0, fg="gray")
    eUser.config(font=("Roboto", 10))
    eUser.bind("<FocusIn>", on_enter)
    eUser.bind("<FocusOut>", on_leave)
    eUser.insert(0,'Username')
    eUser.place(x=80, y=110, height=30)
    Frame(frameLA2,width=245,height=2,bg='#4471D8').place(x=80,y=140) 

    def on_enter(e):
        ePass.delete(0,'end')
        ePass.config(fg="black", show="*")  
        Frame(frameLA2,width=245,height=2,bg='#FF7572').place(x=80,y=200)   
    def on_leave(e):
        if ePass.get()=='':   
            ePass.insert(0,'Password')
            ePass.config(fg="gray", show="")
            Frame(frameLA2,width=245,height=2,bg='#4471D8').place(x=80,y=200) 

    ePass = Entry(master=frameLA2, width=40, border=0, fg="gray")
    ePass.config(font=("Roboto", 10),)
    ePass.bind("<FocusIn>", on_enter)
    ePass.bind("<FocusOut>", on_leave)
    ePass.insert(0,'Password')
    ePass.place(x=80, y=170, height=30)
    Frame(frameLA2,width=245,height=2,bg='#4471D8').place(x=80,y=200) 

    def masuk():
        user = eUser.get()
        Pass = ePass.get()
        if user == "Admin" and Pass == "Admin":
            menuAdmin()
        elif user and Pass != "Admin" or user == "Admin" and Pass != "Admin" or user != "Admin" and Pass == "Admin" or user == "" and Pass == "":
            messagebox.askretrycancel("Info","Username atau Password anda salah!")

    LogBtn = Button(master=frameLA2, text="Login", command=masuk)
    LogBtn.config(font=("Roboto", 10), fg="white", bg="#4471D8", border=0, activebackground="#FF7572", activeforeground="white")
    LogBtn.place(x=105, y=230, width=200, height=30)
    ExgBtn = Button(master=frameLA2, bg='#FF7572', border=0, fg="white", text="<Kembali", width=10, command=menuAwal)
    ExgBtn.place(x=0, y=370)

def menuAdmin():
    destroy()
    global root
    root.geometry("400x400")
    frameMAD1 = LabelFrame(master=root)
    frameMAD1.pack(padx=40, pady=10, fill="both", expand=True)

    jdlAdm = Label(master=frameMAD1, text="MALL PELAYANAN PUBLIK \n JEMBER", font=("Roboto", 15, "bold"))
    jdlAdm.pack(padx=10, pady=10)

    frameA1 = LabelFrame(master=frameMAD1)
    frameA1.pack(padx=40, pady=10, fill="both", expand=True)

    jdlAd = Label(master=frameA1, text="Menu Admin", font=("Roboto", 10))
    jdlAd.pack(padx=10, pady=10)

    LAntriBtn = Button(master=frameA1, text="Lihat Daftar Antrian", width=40, command=lihAnt)
    LAntriBtn.pack(padx=10, pady=10)
    PAntrianBtn = Button(master=frameA1, text="Panggil Antrian", width=40, command="")
    PAntrianBtn.pack(padx=10, pady=10)
    PerPBtn = Button(master=frameA1, text="Pengajuan Permohonan", width=40, command=menuPengajuan)
    PerPBtn.pack(padx=10, pady=10)
    ExgBtn = Button(master=frameA1, text="Keluar", width=40, command=menuAwal)
    ExgBtn.pack(padx=10, pady=10)

def menuPengajuan():
    destroy()
    global root
    root.geometry("800x500")
    frame1 = LabelFrame(master=root)
    frame1.place(width=250, height=500)
    frame2 = LabelFrame(master=root)
    frame2.place(x=250,width=550, height=500)

    jdl = Label(master=frame1, text="PENGAJUAN PERMOHONAN", font=("Roboto", 10, "bold"))
    jdl.pack(padx=10, pady=20)

    def destroyy():
        for widget in frame2.winfo_children():
            widget.destroy()

    def formKtpR():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
        exBtn.place(y=460, x=10)
    def formKtpU():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        UbhLbl = Label(master=frame1, text="Ubah Data :")
        UbhLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        UbhEnt = Entry(master=frame1)
        UbhEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKtpC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
        exBtn.place(y=460, x=10)
    def formKtpD():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        DeltLbl = Label(master=frame1, text="Hapus Data :")
        DeltLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        DeltEnt = Entry(master=frame1)
        DeltEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        DeltBtn = Button(master=frame1, text="Hapus", font=("Roboto", 8), command="")
        DeltBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
        exBtn.place(y=460, x=10)

    def formKKR():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Kk)
        exBtn.place(y=460, x=10)
    def formKKpU():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        UbhLbl = Label(master=frame1, text="Ubah Data :")
        UbhLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        UbhEnt = Entry(master=frame1)
        UbhEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKkC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Kk)
        exBtn.place(y=460, x=10)
    def formKKpD():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        DeltLbl = Label(master=frame1, text="Hapus Data :")
        DeltLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        DeltEnt = Entry(master=frame1)
        DeltEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        DeltBtn = Button(master=frame1, text="Hapus", font=("Roboto", 8), command="")
        DeltBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Kk)
        exBtn.place(y=460, x=10)

    def formAktKR():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktK)
        exBtn.place(y=460, x=10)
    def formAktaKU():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        UbhLbl = Label(master=frame1, text="Ubah Data :")
        UbhLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        UbhEnt = Entry(master=frame1)
        UbhEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKtpC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktK)
        exBtn.place(y=460, x=10)
    def formAktaKD():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        DeltLbl = Label(master=frame1, text="Hapus Data :")
        DeltLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        DeltEnt = Entry(master=frame1)
        DeltEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        DeltBtn = Button(master=frame1, text="Hapus", font=("Roboto", 8), command="")
        DeltBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktK)
        exBtn.place(y=460, x=10)

    def formAktPR():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktP)
        exBtn.place(y=460, x=10)
    def formAktaPU():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        UbhLbl = Label(master=frame1, text="Ubah Data :")
        UbhLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        UbhEnt = Entry(master=frame1)
        UbhEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKtpC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktP)
        exBtn.place(y=460, x=10)
    def formAktaPD():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        DeltLbl = Label(master=frame1, text="Hapus Data :")
        DeltLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        DeltEnt = Entry(master=frame1)
        DeltEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        DeltBtn = Button(master=frame1, text="Hapus", font=("Roboto", 8), command="")
        DeltBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=AktP)
        exBtn.place(y=460, x=10)

    def formKiAR():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=KiA)
        exBtn.place(y=460, x=10)
    def formKiAU():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        UbhLbl = Label(master=frame1, text="Ubah Data :")
        UbhLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        UbhEnt = Entry(master=frame1)
        UbhEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKiAC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=KiA)
        exBtn.place(y=460, x=10)
    def formKiAD():
        destroyy()
        jdl = Label(master=frame2, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
        jdl.pack(pady=5)
        frame1 = LabelFrame(master=frame2)
        frame1.place(width=550, height=400, y=50)
        # frame1.pack(pady=5, fill=BOTH, expand=True)

        DeltLbl = Label(master=frame1, text="Hapus Data :")
        DeltLbl.place(y=10, x=21)
        scrLbl = Label(master=frame1, text="Search :")
        scrLbl.place(y=10, x=350)

        DeltEnt = Entry(master=frame1)
        DeltEnt.place(y=10, x=92, width=40)
        scrEnt = Entry(master=frame1)
        scrEnt.place(y=10, x=400)

        DeltBtn = Button(master=frame1, text="Hapus", font=("Roboto", 8), command="")
        DeltBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=KiA)
        exBtn.place(y=460, x=10)

    def Ktp():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\delete.png")
        resizeC = photoC.resize((100, 100), Image.ANTIALIAS)
        resizeR = photoR.resize((100, 100), Image.ANTIALIAS)
        resizeU = photoU.resize((100, 100), Image.ANTIALIAS)
        resizeD = photoD.resize((100, 100), Image.ANTIALIAS)
        newphotoC = ImageTk.PhotoImage(resizeC)
        newphotoR = ImageTk.PhotoImage(resizeR)
        newphotoU = ImageTk.PhotoImage(resizeU)
        newphotoD = ImageTk.PhotoImage(resizeD)
        jdl = Label(master=frame2, text="PENGAJUAN PERMOHONAN KTP", font=("Roboto", 10, "bold"))
        jdl.pack(padx=10, pady=20)
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185, command=formKtpC)
        btn1.place(x=40, y=60)
        btn2 = Button(master=frame2, image=newphotoR, width=213, height=185, command=formKtpR)
        btn2.place(x=290, y=60)
        btn3 = Button(master=frame2, image=newphotoU, width=213, height=185, command=formKtpU)
        btn3.place(x=40, y=280)
        btn4 = Button(master=frame2, image=newphotoD, width=213, height=185, command=formKtpD)
        btn4.place(x=290, y=280)
    def Kk():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\delete.png")
        resizeC = photoC.resize((100, 100), Image.ANTIALIAS)
        resizeR = photoR.resize((100, 100), Image.ANTIALIAS)
        resizeU = photoU.resize((100, 100), Image.ANTIALIAS)
        resizeD = photoD.resize((100, 100), Image.ANTIALIAS)
        newphotoC = ImageTk.PhotoImage(resizeC)
        newphotoR = ImageTk.PhotoImage(resizeR)
        newphotoU = ImageTk.PhotoImage(resizeU)
        newphotoD = ImageTk.PhotoImage(resizeD)
        jdl = Label(master=frame2, text="PENGAJUAN PERMOHONAN KK", font=("Roboto", 10, "bold"))
        jdl.pack(padx=10, pady=20)
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185, command=formKkC)
        btn1.place(x=40, y=60)
        btn2 = Button(master=frame2, image=newphotoR, width=213, height=185, command=formKKR)
        btn2.place(x=290, y=60)
        btn3 = Button(master=frame2, image=newphotoU, width=213, height=185, command=formKKpU)
        btn3.place(x=40, y=280)
        btn4 = Button(master=frame2, image=newphotoD, width=213, height=185, command=formKKpD)
        btn4.place(x=290, y=280)
    def AktK():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\delete.png")
        resizeC = photoC.resize((100, 100), Image.ANTIALIAS)
        resizeR = photoR.resize((100, 100), Image.ANTIALIAS)
        resizeU = photoU.resize((100, 100), Image.ANTIALIAS)
        resizeD = photoD.resize((100, 100), Image.ANTIALIAS)
        newphotoC = ImageTk.PhotoImage(resizeC)
        newphotoR = ImageTk.PhotoImage(resizeR)
        newphotoU = ImageTk.PhotoImage(resizeU)
        newphotoD = ImageTk.PhotoImage(resizeD)
        jdl = Label(master=frame2, text="PENGAJUAN PERMOHONAN AKTA KELAHIRAN", font=("Roboto", 10, "bold"))
        jdl.pack(padx=10, pady=20)
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185, command=formAktKC)
        btn1.place(x=40, y=60)
        btn2 = Button(master=frame2, image=newphotoR, width=213, height=185, command=formAktKR)
        btn2.place(x=290, y=60)
        btn3 = Button(master=frame2, image=newphotoU, width=213, height=185, command=formAktaKU)
        btn3.place(x=40, y=280)
        btn4 = Button(master=frame2, image=newphotoD, width=213, height=185, command=formAktaKD)
        btn4.place(x=290, y=280)
    def AktP():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\delete.png")
        resizeC = photoC.resize((100, 100), Image.ANTIALIAS)
        resizeR = photoR.resize((100, 100), Image.ANTIALIAS)
        resizeU = photoU.resize((100, 100), Image.ANTIALIAS)
        resizeD = photoD.resize((100, 100), Image.ANTIALIAS)
        newphotoC = ImageTk.PhotoImage(resizeC)
        newphotoR = ImageTk.PhotoImage(resizeR)
        newphotoU = ImageTk.PhotoImage(resizeU)
        newphotoD = ImageTk.PhotoImage(resizeD)
        jdl = Label(master=frame2, text="PENGAJUAN PERMOHONAN AKTA PERKAWINAN", font=("Roboto", 10, "bold"))
        jdl.pack(padx=10, pady=20)
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185, command=formAktPC)
        btn1.place(x=40, y=60)
        btn2 = Button(master=frame2, image=newphotoR, width=213, height=185, command=formAktPR)
        btn2.place(x=290, y=60)
        btn3 = Button(master=frame2, image=newphotoU, width=213, height=185, command=formAktaPU)
        btn3.place(x=40, y=280)
        btn4 = Button(master=frame2, image=newphotoD, width=213, height=185, command=formAktaPD)
        btn4.place(x=290, y=280)
    def KiA():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\Mall-Pelayanan-Publik-Tkinter\\img\\delete.png")
        resizeC = photoC.resize((100, 100), Image.ANTIALIAS)
        resizeR = photoR.resize((100, 100), Image.ANTIALIAS)
        resizeU = photoU.resize((100, 100), Image.ANTIALIAS)
        resizeD = photoD.resize((100, 100), Image.ANTIALIAS)
        newphotoC = ImageTk.PhotoImage(resizeC)
        newphotoR = ImageTk.PhotoImage(resizeR)
        newphotoU = ImageTk.PhotoImage(resizeU)
        newphotoD = ImageTk.PhotoImage(resizeD)
        jdl = Label(master=frame2, text="PENGAJUAN PERMOHONAN KIA", font=("Roboto", 10, "bold"))
        jdl.pack(padx=10, pady=20)
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185, command=formKiAC)
        btn1.place(x=40, y=60)
        btn2 = Button(master=frame2, image=newphotoR, width=213, height=185, command=formKiAR)
        btn2.place(x=290, y=60)
        btn3 = Button(master=frame2, image=newphotoU, width=213, height=185, command=formKiAU)
        btn3.place(x=40, y=280)
        btn4 = Button(master=frame2, image=newphotoD, width=213, height=185, command=formKiAD)
        btn4.place(x=290, y=280)
    
    frame3 = LabelFrame(master=frame1)
    frame3.pack(padx=10, pady=10)

    Ktpbtn = Button(master=frame3, text="Pengajuan Ktp", command=Ktp, width=40, height=2)
    Ktpbtn.pack(padx=10, pady=10)
    Kkbtn = Button(master=frame3, text="Pengajuan Kartu Keluarga", command=Kk, width=40, height=2)
    Kkbtn.pack(padx=10, pady=10)
    Aktbtn = Button(master=frame3, text="Pengajuan Akta Kelahiran", command=AktK, width=40, height=2)
    Aktbtn.pack(padx=10, pady=10)
    AktPtn = Button(master=frame3, text="Pengajuan Akta Perkawinan", command=AktP, width=40, height=2)
    AktPtn.pack(padx=10, pady=10)
    KiAPtn = Button(master=frame3, text="Pengajuan KIA", command=KiA, width=40, height=2)
    KiAPtn.pack(padx=10, pady=10)
    Exbtn = Button(master=frame3, text="Keluar", command=menuAdmin, width=40, height=2)
    Exbtn.pack(padx=10, pady=10)

def formKtpC():
    global root
    new = Toplevel(root)
    new.title("Form KTP")
    new.geometry("600x330")
    jdlForm = Label(master=new, text="FORMULIR PERMOHONAN KTP", font=("Roboto", 15, "bold"))
    jdlForm.pack(pady=5)
    frame2 = LabelFrame(master=new)
    frame2.pack(padx=10,fill=BOTH, expand=True)

    prov = Label(master=frame2, text="Pemerintah Provinsi                                   :", font=("Roboto", 10 ,"bold"))
    prov.place(x=10, y=10)
    kab = Label(master=frame2, text="Pemerintah Kabupaten/Kota                      :", font=("Roboto", 10 ,"bold"))
    kab.place(x=10, y=30)
    kect = Label(master=frame2, text="Kecamatan                                                 :", font=("Roboto", 10 ,"bold"))
    kect.place(x=10, y=50)
    dess = Label(master=frame2, text="Kelurahan/Desa                                          :", font=("Roboto", 10 ,"bold"))
    dess.place(x=10, y=70)
    eProv = Entry(master=frame2, width=43)
    eProv.place(x=300, y=10)
    eKab = Entry(master=frame2, width=43)
    eKab.place(x=300, y=30)
    eKect = Entry(master=frame2, width=43)
    eKect.place(x=300, y=50)
    eDess = Entry(master=frame2, width=43)
    eDess.place(x=300, y=70)

    perM = Label(master=frame2, text="Permohonan KTP", font=("Roboto", 10 ,"bold", "italic", "underline"))
    perM.place(x=10, y=100)

    r = StringVar()

    rBar = Checkbutton(master=frame2, text="A. Baru", variable=r,onvalue="baru").place(x=220, y=100)
    rPerP = Checkbutton(master=frame2, text="B. Perpanjang", variable=r,onvalue="perpanjang").place(x=320, y=100)
    rPengG = Checkbutton(master=frame2, text="C. Pengganti", variable=r,onvalue="pengganti").place(x=455, y=100)
    
    Nama = Label(master=frame2, text="Nama Lengkap        :", font=("Roboto", 10 ,"bold"))
    Nama.place(x=10, y=135)
    noKK = Label(master=frame2, text="Nomor KK                :", font=("Roboto", 10 ,"bold"))
    noKK.place(x=10, y=155)
    Nik = Label(master=frame2, text="NIK                           :", font=("Roboto", 10 ,"bold"))
    Nik.place(x=10, y=175)
    Almt = Label(master=frame2, text="Alamat                     :", font=("Roboto", 10 ,"bold"))
    Almt.place(x=10, y=195)

    eNam = Entry(master=frame2, width=66)
    eNam.place(x=160, y=135)
    eKK = Entry(master=frame2, width=66)
    eKK.place(x=160, y=155)
    eNik = Entry(master=frame2, width=66)
    eNik.place(x=160, y=175)
    eAlmt = Entry(master=frame2, width=66)
    eAlmt.place(x=160, y=195)

    nRt = Label(master=frame2, text="RT", font=("Roboto", 10))
    nRt.place(x=160, y=215)
    eRt = Entry(master=frame2, width=5)
    eRt.place(x=190, y=215)
    nRw = Label(master=frame2, text="RW", font=("Roboto", 10))
    nRw.place(x=240, y=215)
    eRw = Entry(master=frame2, width=5)
    eRw.place(x=280, y=215)
    nPos = Label(master=frame2, text="Kode Pos :", font=("Roboto", 10))
    nPos.place(x=350, y=215)
    ePos = Entry(master=frame2, width=15)
    ePos.place(x=430, y=215)

    submBtn = Button(master=new, text="Submit", width=40, command="")
    submBtn.pack(pady=5)

def formKkC():
    global root
    new = Toplevel(root)
    new.title("Form Kartu Keluarga")
    new.geometry("600x530")
    jdlForm = Label(master=new, text="FORMULIR PERMOHONAN KARTU KELUARGA", font=("Roboto", 13, "bold"))
    jdlForm.pack(pady=5)

    frame1 = LabelFrame(master=new)
    frame1.pack(padx=10,fill=BOTH, expand=True)

    prov = Label(master=frame1, text="Pemerintah Provinsi                                   :", font=("Roboto", 10 ,"bold"))
    prov.place(x=10, y=10)
    kab = Label(master=frame1, text="Pemerintah Kabupaten/Kota                      :", font=("Roboto", 10 ,"bold"))
    kab.place(x=10, y=30)
    kect = Label(master=frame1, text="Kecamatan                                                 :", font=("Roboto", 10 ,"bold"))
    kect.place(x=10, y=50)
    dess = Label(master=frame1, text="Kelurahan/Desa                                          :", font=("Roboto", 10 ,"bold"))
    dess.place(x=10, y=70)
    eProv = Entry(master=frame1, width=43)
    eProv.place(x=300, y=10)
    eKab = Entry(master=frame1, width=43)
    eKab.place(x=300, y=30)
    eKect = Entry(master=frame1, width=43)
    eKect.place(x=300, y=50)
    eDess = Entry(master=frame1, width=43)
    eDess.place(x=300, y=70)

    frame2 = LabelFrame(master=frame1)
    frame2.place(y=95, x=0, width=576, height=155)

    NmPem = Label(master=frame2, text="Nama Lengkap Pemohon  :", font=("Roboto", 8))
    NmPem.place(x=8, y=5)
    NiKPem = Label(master=frame2, text="NIK Pemohon                    :", font=("Roboto", 8))
    NiKPem.place(x=8, y=25)
    NkKPem = Label(master=frame2, text="No. KK Semula                 :", font=("Roboto", 8))
    NkKPem.place(x=8, y=45)
    AlmtPem = Label(master=frame2, text="Alamat Pemohon              :", font=("Roboto", 8))
    AlmtPem.place(x=8, y=65)
    AlsPem = Label(master=frame2, text="Alasan Pemohon              :", font=("Roboto", 8))
    AlsPem.place(x=8, y=85)
    Als1Pem = Label(master=frame2, text="1. Karena Penambahan Anggota Keluarga (Kelahiran, Kedatangan)", font=("Roboto", 8))
    Als1Pem.place(x=190, y=85)
    Als2Pem = Label(master=frame2, text="2. Karena Pengurangan Anggota Keluarga (Kematian, Kepindahan)", font=("Roboto", 8))
    Als2Pem.place(x=190, y=105)
    eNumPem = Entry(master=frame2, width=68)
    eNumPem.place(x=150, y=5)
    eNikPem = Entry(master=frame2, width=68)
    eNikPem.place(x=150, y=25)
    eNkKPem = Entry(master=frame2, width=68)
    eNkKPem.place(x=150, y=45)
    eAlmtPem = Entry(master=frame2, width=68)
    eAlmtPem.place(x=150, y=65)
    eAlsPem = Entry(master=frame2, width=5)
    eAlsPem.place(x=150, y=85)

    JmlAngg = Label(master=frame2, text="Jumlah Anggota Keluarga  :", font=("Roboto", 8))
    JmlAngg.place(x=8, y=125)
    eJmlAngg = Entry(master=frame2, width=5)
    eJmlAngg.place(x=150, y=125)

    frame3 = LabelFrame(master=frame1)
    frame3.place(y=255, x=0, width=576, height=180)

    DafAngg = Label(master=frame3, text="DAFTAR ANGGOTA KELUARGA PEMOHON (hanya diisi Anggota Keluarga saja)", font=("Roboto", 8, "bold"))
    DafAngg.place(x=8, y=5)

    Ak1 = Label(master=frame3, text="Anggota Keluarga 1           :", font=("Roboto", 8))
    Ak1.place(x=8, y=25)
    Ak2 = Label(master=frame3, text="Anggota Keluarga 2           :", font=("Roboto", 8))
    Ak2.place(x=8, y=45)
    Ak3 = Label(master=frame3, text="Anggota Keluarga 3           :", font=("Roboto", 8))
    Ak3.place(x=8, y=65)
    Ak4 = Label(master=frame3, text="Anggota Keluarga 4           :", font=("Roboto", 8))
    Ak4.place(x=8, y=85)
    Ak5 = Label(master=frame3, text="Anggota Keluarga 5           :", font=("Roboto", 8))
    Ak5.place(x=8, y=105)
    Ak6 = Label(master=frame3, text="Anggota Keluarga 6           :", font=("Roboto", 8))
    Ak6.place(x=8, y=125)
    Ak7 = Label(master=frame3, text="Anggota Keluarga 7           :", font=("Roboto", 8))
    Ak7.place(x=8, y=145)

    eAk1 = Entry(master=frame3, width=68)
    eAk1.place(x=150, y=25)
    eAk2 = Entry(master=frame3, width=68)
    eAk2.place(x=150, y=45)
    eAk3 = Entry(master=frame3, width=68)
    eAk3.place(x=150, y=65)
    eAk4 = Entry(master=frame3, width=68)
    eAk4.place(x=150, y=85)
    eAk5 = Entry(master=frame3, width=68)
    eAk5.place(x=150, y=105)
    eAk6 = Entry(master=frame3, width=68)
    eAk6.place(x=150, y=125)
    eAk7 = Entry(master=frame3, width=68)
    eAk7.place(x=150, y=145)

    SubBtn = Button(master=new, text="Submit", width=25)
    SubBtn.pack(pady=10)

def formAktKC():
    global root
    new = Toplevel(root)
    new.title("Form Akta Kelahiran")
    new.geometry("550x540")
    jdlForm = Label(master=new, text="FORMULIR PERMOHONAN AKTA KELAHIRAN",font=("Roboto", 13, "bold"))
    jdlForm.pack(pady=5)

    NkK = Label(master=new, text="Nama Kepala Keluarga :",font=("Roboto", 8))
    NkK.place(x=5, y=40)
    NoKk = Label(master=new, text="Nomor Kartu Keluarga  :",font=("Roboto", 8))
    NoKk.place(x=5, y=60)
    eNkk = Entry(master=new, width=68)
    eNkk.place(x=130, y=40)
    eNokk = Entry(master=new, width=68)
    eNokk.place(x=130, y=60)

    frame1 = LabelFrame(master=new)
    frame1.place(x=5, y=90, width=542, height=415)

    frame2 = LabelFrame(master=frame1, text="BAYI", font=("Roboto", 8))
    frame2.place(x=5, y=5, width=528, height=110)

    NaNk = Label(master=frame2, text="Nama Anak                      :",font=("Roboto", 8))
    NaNk.place(x=5, y=5)
    TtL = Label(master=frame2, text="Tempat, Tanggal Lahir     :",font=("Roboto", 8))
    TtL.place(x=5, y=25)
    Jk = Label(master=frame2, text="Jenis Kelamin                   :",font=("Roboto", 8))
    Jk.place(x=5, y=45)
    AnkKe = Label(master=frame2, text="Anak Ke                           :",font=("Roboto", 8))
    AnkKe.place(x=5, y=65)
    eNaNk = Entry(master=frame2, width=62)
    eNaNk.place(x=140, y=5)
    eTtL = Entry(master=frame2, width=62)
    eTtL.place(x=140, y=25)
    eJk = Entry(master=frame2, width=62)
    eJk.place(x=140, y=45)
    eAnkKe = Entry(master=frame2, width=62)
    eAnkKe.place(x=140, y=65)

    frame3 = LabelFrame(master=frame1, text="IBU", font=("Roboto", 8))
    frame3.place(x=5, y=115, width=528, height=70)

    NaIb = Label(master=frame3, text="Nama Ibu                          :",font=("Roboto", 8))
    NaIb.place(x=5, y=5)
    NiKIb = Label(master=frame3, text="NIK Ibu                              :",font=("Roboto", 8))
    NiKIb.place(x=5, y=25)
    eNaIb = Entry(master=frame3, width=62)
    eNaIb.place(x=140, y=5)
    eNiKIb = Entry(master=frame3, width=62)
    eNiKIb.place(x=140, y=25)

    frame4 = LabelFrame(master=frame1, text="AYAH", font=("Roboto", 8))
    frame4.place(x=5, y=185, width=528, height=70)

    NaAyh = Label(master=frame4, text="Nama Ayah                      :",font=("Roboto", 8))
    NaAyh.place(x=5, y=5)
    NiAyh = Label(master=frame4, text="NIK Ayah                          :",font=("Roboto", 8))
    NiAyh.place(x=5, y=25)
    eNaAyh = Entry(master=frame4, width=62)
    eNaAyh.place(x=140, y=5)
    eNiKAyh = Entry(master=frame4, width=62)
    eNiKAyh.place(x=140, y=25)

    frame5 = LabelFrame(master=frame1, text="SAKSI", font=("Roboto", 8))
    frame5.place(x=5, y=255, width=528, height=70)

    NaSks1 = Label(master=frame5, text="Nama Saksi                      :",font=("Roboto", 8))
    NaSks1.place(x=5, y=5)
    NiSks1 = Label(master=frame5, text="NIK Saksi                          :",font=("Roboto", 8))
    NiSks1.place(x=5, y=25)
    eNaSks1 = Entry(master=frame5, width=62)
    eNaSks1.place(x=140, y=5)
    eNiKSks1 = Entry(master=frame5, width=62)
    eNiKSks1.place(x=140, y=25)

    frame6 = LabelFrame(master=frame1, font=("Roboto", 8))
    frame6.place(x=5, y=325, width=528, height=55)

    NaSks2 = Label(master=frame6, text="Nama Saksi                      :",font=("Roboto", 8))
    NaSks2.place(x=5, y=5)
    NiSks2 = Label(master=frame6, text="NIK Saksi                          :",font=("Roboto", 8))
    NiSks2.place(x=5, y=25)
    eNaSks2 = Entry(master=frame6, width=62)
    eNaSks2.place(x=140, y=5)
    eNiKSks2 = Entry(master=frame6, width=62)
    eNiKSks2.place(x=140, y=25)

    NaAktK = Label(master=frame1, text="Nomor Akta Kelahiran   :",font=("Roboto", 8))
    NaAktK.place(x=5, y=385)
    eNaAktK = Entry(master=frame1, width=66)
    eNaAktK.place(x=130, y=385)

    SubBtn = Button(master=new, text="Submit", width=25)
    SubBtn.place(x=180, y=510)

def formAktPC():
    global root
    new = Toplevel(root)
    new.title("Form Akta Perkawinan")
    new.geometry("550x410")
    jdlForm = Label(master=new, text="FORMULIR PERMOHONAN AKTA PERKAWINAN",font=("Roboto", 13, "bold"))
    jdlForm.pack(pady=5)

    SrBp = Label(master=new, text="Surat Bukti Perkawinan   :",font=("Roboto", 8))
    SrBp.place(x=5, y=40)
    SrKl = Label(master=new, text="Surat Keterangan Lurah  :",font=("Roboto", 8))
    SrKl.place(x=5, y=60)
    eSrBp = Entry(master=new, width=66)
    eSrBp.place(x=140, y=40)
    eSrKl = Entry(master=new, width=66)
    eSrKl.place(x=140, y=60)

    frame1 = LabelFrame(master=new)
    frame1.place(x=5, y=90, width=542, height=285)

    frame2 = LabelFrame(master=frame1, text="PRIA", font=("Roboto", 8))
    frame2.place(x=5, y=5, width=528, height=70)

    NaPria = Label(master=frame2, text="Nama Pria                        :",font=("Roboto", 8))
    NaPria.place(x=5, y=5)
    NiPria = Label(master=frame2, text="NIK Pria                            :",font=("Roboto", 8))
    NiPria.place(x=5, y=25)
    eNaPria = Entry(master=frame2, width=62)
    eNaPria.place(x=140, y=5)
    eNiPria = Entry(master=frame2, width=62)
    eNiPria.place(x=140, y=25)

    frame3 = LabelFrame(master=frame1, text="WANITA", font=("Roboto", 8))
    frame3.place(x=5, y=75, width=528, height=70)

    NaWna = Label(master=frame3, text="Nama Wanita                   :",font=("Roboto", 8))
    NaWna.place(x=5, y=5)
    NiWna = Label(master=frame3, text="NIK Wanita                       :",font=("Roboto", 8))
    NiWna.place(x=5, y=25)
    eNaWna = Entry(master=frame3, width=62)
    eNaWna.place(x=140, y=5)
    eNiWna = Entry(master=frame3, width=62)
    eNiWna.place(x=140, y=25)

    frame4 = LabelFrame(master=frame1, text="SAKSI", font=("Roboto", 8))
    frame4.place(x=5, y=145, width=528, height=70)

    NSks1 = Label(master=frame4, text="Nama Saksi                      :",font=("Roboto", 8))
    NSks1.place(x=5, y=5)
    NkSks1 = Label(master=frame4, text="NIK Saksi                          :",font=("Roboto", 8))
    NkSks1.place(x=5, y=25)
    eNSks1 = Entry(master=frame4, width=62)
    eNSks1.place(x=140, y=5)
    eNKSks1 = Entry(master=frame4, width=62)
    eNKSks1.place(x=140, y=25)

    frame5 = LabelFrame(master=frame1, font=("Roboto", 8))
    frame5.place(x=5, y=215, width=528, height=55)

    NSks2 = Label(master=frame5, text="Nama Saksi                      :",font=("Roboto", 8))
    NSks2.place(x=5, y=5)
    NkSks2 = Label(master=frame5, text="NIK Saksi                          :",font=("Roboto", 8))
    NkSks2.place(x=5, y=25)
    eNSks2 = Entry(master=frame5, width=62)
    eNSks2.place(x=140, y=5)
    eNKSks2 = Entry(master=frame5, width=62)
    eNKSks2.place(x=140, y=25)

    SubBtn = Button(master=new, text="Submit", width=25)
    SubBtn.place(x=180, y=380)

def formKiAC():
    global root
    new = Toplevel(root)
    new.title("Form KIA")
    new.geometry("550x260")

    jdlLbl = Label(master=new, text="FORMULIR PERMOHONAN KIA", font=("Roboto", 13, "bold"))
    jdlLbl.pack(pady=5)
    NoKaK = Label(master=new, text="Nomor Kartu Keluarga      :",font=("Roboto", 8))
    NoKaK.place(x=5, y=40)
    eNoKaK = Entry(master=new, width=66)
    eNoKaK.place(x=140, y=40)

    frame1 = LabelFrame(master=new)
    frame1.place(x=5, y=70, width=540, height=150)

    Naayhh = Label(master=frame1, text="Nama Ayah                    :",font=("Roboto", 8))
    Naayhh.place(x=5, y=5)
    Niayhh = Label(master=frame1, text="NIK Ayah                        :",font=("Roboto", 8))
    Niayhh.place(x=5, y=25)
    eNaayhh = Entry(master=frame1, width=64)
    eNaayhh.place(x=140, y=5)
    eNiayhh = Entry(master=frame1, width=64)
    eNiayhh.place(x=140, y=25)

    NaIbu = Label(master=frame1, text="Nama Ibu                        :",font=("Roboto", 8))
    NaIbu.place(x=5, y=50)
    NiIbu = Label(master=frame1, text="NIK Ibu                            :",font=("Roboto", 8))
    NiIbu.place(x=5, y=70)
    eNaIbu = Entry(master=frame1, width=64)
    eNaIbu.place(x=140, y=50)
    eNiIbu = Entry(master=frame1, width=64)
    eNiIbu.place(x=140, y=70)

    Nanak = Label(master=frame1, text="Nama Anak                     :",font=("Roboto", 8))
    Nanak.place(x=5, y=95)
    Nianak = Label(master=frame1, text="Nomor Akta Kelahiran     :",font=("Roboto", 8))
    Nianak.place(x=5, y=115)
    eNanak = Entry(master=frame1, width=64)
    eNanak.place(x=140, y=95)
    eNianak = Entry(master=frame1, width=64)
    eNianak.place(x=140, y=115)

    SubmBtn = Button(master=new, text="Submit", width=20)
    SubmBtn.place(x=200, y=225)

def AmbAnt():
    global root
    new = Toplevel(root)
    new.title("Ambil Antrian")
    new.geometry("300x150")
    frame = LabelFrame(master=new)
    frame.pack(padx=5, pady=5, fill=BOTH, expand=True)
    Jdl = Label(master=frame, text="Ambil Antrian", font=("Roboto", 10, "bold"))
    Jdl.pack()

    frame2 = LabelFrame(master=frame)
    frame2.pack(padx=5, pady=5, fill=BOTH, expand=True)
    Nma = Label(master=frame2, text="Masukan Nama :", font=("Roboto", 8))
    Nma.place(x=5, y=5)
    eNma = Entry(master=frame2, width=20)
    eNma.place(x=5, y=25)

    def SubData():
        dataName = eNma.get()
        data2.enqueue(dataName)

    subBtn = Button(master=frame2, text="Submit", command=SubData)
    subBtn.place(x=140, y=5, width=125, height=90)

def lihAnt():
    global root
    root.geometry("400x300")
    frame = LabelFrame(master=root)
    frame.place(x=5, y=40, width=392, height=200)
    jdlLbl = Label(master=root, text="Daftar Antrian", font=("Roboto", 15, "bold"))
    jdlLbl.place(x=258, y=5)
    Kembtn = Button(master=root, text="<<Kembali", width=10, command=menuAdmin)
    Kembtn.place(x=5, y=5)

menuAwal()
# LogAdmin()
# lihAnt()

root.mainloop()