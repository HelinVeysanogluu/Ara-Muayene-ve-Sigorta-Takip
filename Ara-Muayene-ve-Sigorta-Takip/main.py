from tkinter import *

def yeni_sayfa_ac():
    plaka = plaka_entry.get()
    yeni_pencere = Toplevel(window)
    yeni_pencere.title("Sorgu Sonucu")
    yeni_pencere.configure(bg="#c7c1f1")

    Label(yeni_pencere, text=f"Plaka: {plaka}", font="Arial 18", bg="#c7c1f1").pack(pady=40)

window = Tk()
window.title("Araç Muayene ve Sigorta Takip")
window.configure(bg="#c7c1f1")
window.attributes("-fullscreen", True)
window.bind("<Escape>", lambda event: window.attributes("-fullscreen", False))

frame1 = Frame(window, height=300, width=450, bg="#c7c1f1",
               highlightbackground="#c7c1f1", highlightthickness=1)
frame1.place(x=550, y=300)

frame2 = Frame(window, height=300, width=450, bg="#c7c1f1",
               highlightbackground="#c7c1f1", highlightthickness=1)
frame2.place(x=650, y=302)

Label(frame1, text="Plaka :", font="Arial 20 bold", bg="#c7c1f1").pack()
plaka_entry = Entry(frame2, font="Arial 20", bg="#e8e5f8", justify="center")
plaka_entry.pack()

Button(window, text="Sorgula", font="Arial 15 bold", bg="#5c4ea7", fg="#c7c1f1",
       activebackground="#5c4ea7", activeforeground="#c7c1f1",
       command=yeni_sayfa_ac).pack(pady=400)

window.mainloop()