from tkinter import *
from vehicle import vehicles
from inspection import inspections
from insurance import insurances

def sorgula():
    plaka = plaka_entry.get().strip().replace(" ", "").upper()

    for widget in window.winfo_children():
        widget.destroy()

    result_frame = Frame(window, bg="#c7c1f1")
    result_frame.pack(fill="both", expand=True)

    Label(result_frame, text=f"Sorgulanan Plaka: {plaka}", font="Arial 20 bold", bg="#8477d4").pack(pady=20)

    found_vehicle = next((v for v in vehicles if v.license_plate == plaka), None)

    if found_vehicle:
        found_inspection = next((i for i in inspections if i.vehicle == found_vehicle), None)
        found_insurance = next((ins for ins in insurances if ins.vehicle == found_vehicle), None)

        Label(result_frame, text="Araç Bilgisi", font="Arial 18 bold", bg="#8477d4").pack(anchor="w", padx=40)
        Label(result_frame, text=str(found_vehicle), font="Helvetica 14", bg="#c7c1f1", justify="left").pack(anchor="w", padx=60, pady=10)

        if found_inspection:
            Label(result_frame, text="Muayene Bilgisi", font="Arial 18 bold", bg="#8477d4").pack(anchor="w", padx=40)
            Label(result_frame, text=str(found_inspection), font="Helvetica 14", bg="#c7c1f1", justify="left").pack(anchor="w", padx=60, pady=10)

        if found_insurance:
            Label(result_frame, text="Sigorta Bilgisi", font="Arial 18 bold", bg="#8477d4").pack(anchor="w", padx=40)
            Label(result_frame, text=str(found_insurance), font="Helvetica 14", bg="#c7c1f1", justify="left").pack(anchor="w", padx=60, pady=10)
    else:
        Label(result_frame, text="Plakaya ait bilgi bulunamadı.", font="Arial 16", bg="#c7c1f1", fg="red").pack(pady=30)


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
       command=sorgula).pack(pady=400)

window.mainloop()