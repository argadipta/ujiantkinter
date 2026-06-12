soal nomor 1
from tkinter import ttk, messagebox

soal nomor 2
root.title("Students Form Application AW3")

soal nomor 3
tk.Label(root, text="Please input your identity").grid(row=1, column=0)

#Input Nama
tk.Label(root, text="First Name").grid(row=2, column=0)
soal nomor 4 
entry_firstname.grid(row=2, column=1)

tk.Label(root, text="Last Name").grid(row=3, column=0)
entry_lastname = tk.Entry(root)
entry_lastname.grid(row=3, column=1)

#Input Email
tk.Label(root, text="Email").grid(row=4, column=0)
soal nomor 5 
entry_email.grid(row=4, column=1)

#Input Password
tk.Label(root, text="Password").grid(row=5, column=0)
soal nomor 6
entry_password.grid(row=5, column=1)

#Input Tempat Tanggal Lahir
tk.Label(root, text="Place and Date of Birth").grid(row=6, column=0)
entry_place = tk.Entry(root)
soal nomor 7
frame_bod = tk.Frame(root)
frame_bod.grid(row=7, column=1)

#Tanggal
soal nomor 8
date.grid(row=0, column=0)
date.set("1")

#Bulan
month = ttk.Combobox(frame_bod, values=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"], width=5, state="readonly")
month.grid(row=0, column=1)
month.set("Jan")

#Year
soal nomor 9
year.grid(row=0, column=2)
year.set("1990")

#membuat Jenis Kelamin dengan radiobutton
tk.Label(root, text="Choose Your Gender!").grid(row=8, column=0)
gender = tk.IntVar()
soal nomor 10 
soal nomor 11

#Nomor telepon
tk.Label(root, text="Phone Number").grid(row=10, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=10, column=1)

#Alamat Rumah
tk.Label(root, text="Address").grid(row=11, column=0)
entry_address = tk.Entry(root)
entry_address.grid(row=11, column=1)

#Membuat kelas dengan combo box
tk.Label(root, text="Choose Your Class").grid(row=12, column=0)
combo_box = ttk.Combobox(root, values=["7AE1", "7AE2", "7AE3", "8AE1", "8AE2", "8AE3"], state="readonly")
combo_box.grid(row=12, column=1, sticky="w")
combo_box.set("7AE1")

#Membuat makanan kesukaan dengan check button
tk.Label(root, text="Choose Your Favorite Food").grid(row=13, column=0)
food1 = tk.IntVar()
tk.Checkbutton(root, text="Nasi Padang", variable=food1).grid(row=13, column=1, sticky="w")
food2 = tk.IntVar()
soal nomor 12
food3 = tk.IntVar()
tk.Checkbutton(root, text="Bakso", variable=food3).grid(row=15, column=1, sticky="w")
soal nomor 13
tk.Checkbutton(root, text="Sate", variable=food4).grid(row=16, column=1, sticky="w")

#Function Tombol Register
soal nomor 14
    first_name = entry_firstname.get()
    last_name = entry_lastname.get()
    email = entry_email.get()
    password = entry_password.get()
    phone = entry_phone.get()
    address = entry_address.get()
    
    #Validasi email dan password
    if email == "" or password == "":
        soal nomor 15
    elif "@" not in email:
        messagebox.showerror("Error!", "Email Invalid!")
    soal nomor 16
        messagebox.showinfo("Success!", "The data has been successfully saved")
        
    #Gender
    soal nomor 17
        gender_text = "Male"
    elif gender.get() == 2:
        gender_text = "Female"
    else:
        gender_text = "Not Selected"
        
    #nomor telepon
    phone = entry_phone.get()
    if not phone.isdigit():
        messagebox.showerror("Error", "Phone must be filled by numbers!")
        soal nomor 18
    
    #Class
    classes = combo_box.get()
    
    #Tanggal Lahir
    place = entry_place.get()
    d = date.get()
    soal nomor 19
    y = year.get()
    
    #Food check button
    foods = []
    if food1.get() == 1:
        foods.append("Nasi Padang")
    if food2.get() == 1:
        foods.append("Nasi Goreng")
    if food3.get() == 1:
        foods.append("Bakso")
    if food4.get() == 1:
        foods.append("Sate")
    if not foods:
        foods_text = "None"
    else:
        foods_text = ", ".join(foods)
        
    #SUMMARY DATA INPUT
    summary = f"""
    ===== STUDENT DATA =====
    {soal nomor 20}
    Email       : {email}
    Born Date   : {place}, {d} {m} {y}
    Phone       : {phone}
    Address     : {address}
    Gender      : {gender_text}
    Class       : {classes}
    Food        : {foods_text}
    """
    soal nomor 21
    
#Tombol
soal nomor 22
soal nomor 23

soal nomor 24
btn_exit.grid(row=30, column=1, padx=5, pady=10)

soal nomor 25
