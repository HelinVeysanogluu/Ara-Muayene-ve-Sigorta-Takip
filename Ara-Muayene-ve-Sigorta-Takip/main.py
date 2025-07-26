from tkinter import *
from vehicle import get_vehicle_by_plate
from inspection import get_all_inspections_by_plate
from insurance import get_insurance_by_plate

def render_grid_block(parent, title, text, start_row=0):
    if title:
        Label(parent, text=title, font="Arial 18 bold", bg="#8477d4").grid(row=start_row, column=0, columnspan=2, sticky="w", pady=(20, 10))
        start_row += 1
    for line in text.strip().split('\n'):
        if ':' in line:
            key, val = line.split(':', 1)
            Label(parent, text=key.strip(), font="Helvetica 14", bg="#c7c1f1", anchor="w").grid(row=start_row, column=0, sticky="w")
            Label(parent, text=": " + val.strip(), font="Helvetica 14", bg="#c7c1f1", anchor="w").grid(row=start_row, column=1, sticky="w")
            start_row += 1
        else:
            Label(parent, text=line.strip(), font="Helvetica 14", bg="#c7c1f1", anchor="w").grid(row=start_row, column=0, columnspan=2, sticky="w")
            start_row += 1
    return start_row

def sorgula():
    plaka = plaka_entry.get().strip().replace(" ", "").upper()

    for widget in window.winfo_children():
        widget.destroy()

    result_frame = Frame(window, bg="#c7c1f1")
    result_frame.pack(fill="both", expand=True)

    Label(result_frame, text=f"Sorgulanan Plaka: {plaka}", font="Arial 20 bold", bg="#8477d4").pack(pady=20)

    found_vehicle = get_vehicle_by_plate(plaka)

    if found_vehicle:
        inspections = get_all_inspections_by_plate(plaka)
        found_insurance = get_insurance_by_plate(plaka)

        left_frame = Frame(result_frame, bg="#c7c1f1")
        left_frame.pack(side=LEFT, fill=BOTH, expand=True, padx=40)

        right_frame = Frame(result_frame, bg="#c7c1f1")
        right_frame.pack(side=RIGHT, fill=BOTH, expand=True, padx=40)

        row_index = render_grid_block(left_frame, "Araç Bilgisi", str(found_vehicle))

        if found_insurance:
            row_index = render_grid_block(left_frame, "Sigorta Bilgisi", str(found_insurance), start_row=row_index)

        if inspections:
            row_index = render_grid_block(right_frame, "Muayene Bilgileri", "")
            for inspection in inspections:
                row_index = render_grid_block(right_frame, "", str(inspection), start_row=row_index)
                # araya çizgi boşluk ekle
                Label(right_frame, text="".ljust(80, "-"), font="Helvetica 12", bg="#c7c1f1", fg="gray").grid(row=row_index, column=0, columnspan=2, sticky="w", pady=(5, 10))
                row_index += 1

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