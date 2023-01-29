from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox, filedialog
import pandas as pd

root = Tk()
root.title("Mall Pelayanan Publik Jember")

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

    BtnCusT = Button(master=frame1, text="Ambil Nomor Antrian", width=40)
    BtnCusT.pack(pady=10)
    BtnCusT = Button(master=frame1, text="Keluar", command=menuAwal, width=40)
    BtnCusT.pack(pady=10)
    
def LogAdmin():
    global root, newphoto
    destroy()
    root.geometry("800x400")

    frameLA1 = LabelFrame(master=root)
    frameLA1.place(width=400, height=400)
    photo = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\peng.png")
    resize = photo.resize((400, 300), Image.ANTIALIAS)
    newphoto = ImageTk.PhotoImage(resize)
    lbl = Label(master=frameLA1,image=newphoto)
    lbl.place(x=0, y=0, width=400, height=400)

    frameLA2 = LabelFrame(master=root)
    frameLA2.place(x=400,width=400, height=400)

    jdlAdm = Label(master=frameLA2, text="LOGIN SYSTEM!! \n ADMIN", font=("Roboto", 20, "bold"))
    jdlAdm.pack(padx=10, pady=10)

    UserLbl = Label(master=frameLA2, text="Username")
    UserLbl.place(x=72, y=90)

    PassLbl = Label(master=frameLA2, text="Password")
    PassLbl.place(x=72, y=140)

    eUser = Entry(master=frameLA2, width=40)
    eUser.pack(padx=10, pady=20)
    ePass = Entry(master=frameLA2, width=40, show="*")
    ePass.pack(padx=10, pady=10)

    def masuk():
        user = eUser.get()
        Pass = ePass.get()
        if user == "Admin" and Pass == "Admin":
            menuAdmin()
        elif user and Pass != "Admin" or user == "Admin" and Pass != "Admin" or user != "Admin" and Pass == "Admin":
            messagebox.askretrycancel("Info","Username atau Password anda salah!")

    LogBtn = Button(master=frameLA2, text="Login", width=15, command=masuk)
    LogBtn.pack(padx=10, pady=10)
    ExgBtn = Button(master=frameLA2, text="<Kembali", width=10, command=menuAwal)
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

    LAntriBtn = Button(master=frameA1, text="Lihat Daftar Antrian", width=40, command=menuAwal)
    LAntriBtn.pack(padx=10, pady=10)
    PAntrianBtn = Button(master=frameA1, text="Panggil Antrian", width=40, command=menuAwal)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKtpC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8), command=formKtpC)
        ubhBtn.place(y=8, x=140, width=40)

        frameDt = LabelFrame(master=frame1, text="Daftar Data Permohonan")
        frameDt.place(width=500, height=328, y=40, x=25)
        # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
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

        exBtn = Button(master=frame2, text="<Kembali", width=10, command=Ktp)
        exBtn.place(y=460, x=10)

    def Ktp():
        global newphotoC, newphotoR, newphotoU, newphotoD
        destroyy()
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\delete.png")
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
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\delete.png")
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
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185)
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
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\delete.png")
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
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185)
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
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\delete.png")
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
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185)
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
        photoC = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\create.png")
        photoR = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\read.png")
        photoU = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\update.png")
        photoD = Image.open("C:\\Users\\Shrmanto\\Desktop\\CobaPython\\MallPelayananPublik\\img\\delete.png")
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
        btn1 = Button(master=frame2, image=newphotoC, width=213, height=185)
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

def formKtpR():
    # destroyy()
    global root
    root.geometry("550x500")
    jdl = Label(master=root, text="DAFTAR DATA PERMOHONAN", font=("Roboto", 15, "bold"))
    jdl.pack(pady=5)
    frame1 = LabelFrame(master=root)
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

    ubhBtn = Button(master=frame1, text="Ubah", font=("Roboto", 8))
    ubhBtn.place(y=8, x=140, width=40)

    frame2 = LabelFrame(master=frame1, text="Daftar Data Permohonan")
    frame2.place(width=500, height=328, y=40, x=25)
    # frame2.pack(padx=10, pady=10, fill=BOTH, expand=True)

    exBtn = Button(master=root, text="<Kembali", width=10)
    exBtn.place(y=460, x=10)

menuAwal()

root.mainloop()