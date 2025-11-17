import tkinter as tk
from tkinter import ttk

data_rental = []
harga_mobil = {
    "Porsche 911 GT3 RS": 2500000,
    "Le Mans SF 90XX": 3000000, 
    "Senna": 3500000}

def open_page1(): 
    page1.tkraise()

def open_page2(): 
    page2.tkraise()

def open_page3(): 
    clear_form()
    page3.tkraise()

def open_page4(): 
    tampilkan_data()
    page4.tkraise()

def open_page5(): 
    page5.tkraise()

def open_page6(): 
    hitung_pendapatan()
    page6.tkraise()

def login():
    if User.get() == 'Victor' and Password.get() == '123':
        page2.tkraise()
        salah.config(text='')
    else:
        salah.config(text='user/pass salah', fg='red')

def clear_form():
    entry_nama.delete(0, tk.END)
    entry_nohp.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    combo_mobil.set('')
    entry_lama.delete(0, tk.END)
    label_harga.config(text='Rp 0')

def hitung_harga(event=None):
    mobil = combo_mobil.get()
    lama = entry_lama.get()

    if mobil in harga_mobil and lama.isdigit():
        label_harga.config(text=f'Rp {harga_mobil[mobil] * int(lama):,}')

def tambah_data():
    if not all([entry_nama.get(), entry_nohp.get(), entry_email.get(), combo_mobil.get(), entry_lama.get()]):
        label_status.config(text='Semua field harus diisi!', foreground='red')
        return
    
    harga_total = harga_mobil[combo_mobil.get()] * int(entry_lama.get())
    data_rental.append({
        'nama': entry_nama.get(),
        'nohp': entry_nohp.get(),
        'email': entry_email.get(),
        'mobil': combo_mobil.get(),
        'lama': int(entry_lama.get()),
        'harga': harga_total
    })
    label_status.config(text='Data berhasil disimpan!', foreground='green')
    clear_form()

def tampilkan_data():
    for item in tree_data.get_children(): tree_data.delete(item)
    if data_rental:
        for i, data in enumerate(data_rental, 1):
            tree_data.insert('', tk.END, values=(
                i, data['nama'], data['nohp'], data['email'], 
                data['mobil'], data['lama'], f"Rp {data['harga']:,}"
            ))
    else:
        tree_data.insert('', tk.END, values=('Tidak ada data', '', '', '', '', ''))

def cari_data():
    keyword = entry_cari.get().lower()
    for item in tree_cari.get_children(): tree_cari.delete(item)
    if keyword:
        hasil = [data for data in data_rental if keyword in data['nama'].lower()]
        if hasil:
            for i, data in enumerate(hasil, 1):
                tree_cari.insert('', tk.END, values=(
                    i, data['nama'], data['nohp'], data['email'],
                    data['mobil'], data['lama'], f"Rp {data['harga']:,}"
                ))
        else:
            tree_cari.insert('', tk.END, values=('Data tidak ditemukan', '', '', '', '', ''))

# MAIN WINDOW
window = tk.Tk()
window.title('Rental Mobil Mewah')
window.geometry('800x500')
window.configure(cursor='hand2')

style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TLabel', background='#f0f0f0', font=('Arial', 9))
style.configure('TButton', font=('Arial', 9, 'bold'))

# Create pages
page1 = ttk.Frame(window, cursor='hand2')
page2 = ttk.Frame(window, cursor='hand2')
page3 = ttk.Frame(window, cursor='hand2')
page4 = ttk.Frame(window, cursor='hand2')
page5 = ttk.Frame(window, cursor='hand2')
page6 = ttk.Frame(window, cursor='hand2')

for frame in (page1, page2, page3, page4, page5, page6):
    frame.place(x=0, y=0, relwidth=1, relheight=1)

# PAGE 1 - LOGIN
ttk.Label(page1, text='Silahkan login terlebih dahulu!', font=('Arial', 14, 'bold')).pack(pady=30)

ttk.Label(page1, text='Username:').pack()
User = tk.Entry(page1, width=25, cursor='xterm')
User.pack(pady=5)

ttk.Label(page1, text='Password:').pack()
Password = tk.Entry(page1, width=25, show='*', cursor='xterm')
Password.pack(pady=5)

ttk.Button(page1, text='Login', command=login, cursor='hand2').pack(pady=10)

salah = ttk.Label(page1, text='')
salah.pack()

# PAGE 2 - MENU
ttk.Label(page2, text='Silahkan diklik', font=('Arial', 16, 'bold')).pack(pady=30)

frame_menu = ttk.Frame(page2)
frame_menu.pack(pady=20)

ttk.Button(frame_menu, text='🚗 Input Data Rental', command=open_page3, cursor='hand2').grid(row=0, column=0, padx=15, pady=10)
ttk.Button(frame_menu, text='📊 Tampil Data', command=open_page4, cursor='hand2').grid(row=0, column=1, padx=15, pady=10)
ttk.Button(frame_menu, text='🔍 Cari Data', command=open_page5, cursor='hand2').grid(row=1, column=0, padx=15, pady=10)
ttk.Button(frame_menu, text='💰 Pendapatan', command=open_page6, cursor='hand2').grid(row=1, column=1, padx=15, pady=10)

# PAGE 3 - INPUT DATA
ttk.Label(page3, text= 'Data mobil rental', font=('Arial', 14, 'bold')).pack(pady=15)
frame_input = ttk.Frame(page3)
frame_input.pack(pady=15)

labels = ['Nama:', 'No HP:', 'Email:', 'Mobil:', 'Lama (hari):']
entries = []
for i, text in enumerate(labels):
    ttk.Label(frame_input, text=text).grid(row=i, column=0, sticky='w', pady=8)
    if text == 'Mobil:':
        entry = ttk.Combobox(frame_input, values=list(harga_mobil.keys()), width=25)
        entry.bind('<<ComboboxSelected>>', hitung_harga)
    else:
        entry = tk.Entry(frame_input, width=28)
        if text == 'Lama (hari):':
            entry.bind('<KeyRelease>', hitung_harga)
    entry.grid(row=i, column=1, pady=8, padx=10)
    entry.configure(cursor='xterm')
    entries.append(entry)

entry_nama, entry_nohp, entry_email, combo_mobil, entry_lama = entries

ttk.Label(frame_input, text='Total Harga:').grid(row=5, column=0, sticky='w', pady=8)
label_harga = ttk.Label(frame_input, text='Rp 0', foreground='green', font=('Arial', 11, 'bold'))
label_harga.grid(row=5, column=1, sticky='w', pady=8)

ttk.Button(page3, text='💾 Simpan Data', command=tambah_data, cursor='hand2').pack(pady=10)

label_status = ttk.Label(page3, text='')
label_status.pack()

ttk.Button(page3, text='⬅ Kembali', command=open_page2, cursor='hand2').pack(pady=5)

# PAGE 4 - TAMPIL DATA
ttk.Label(page4, text='Data rental', font=('Arial', 14, 'bold')).pack(pady=15)

# Frame untuk tabel dengan scrollbar
frame_table = ttk.Frame(page4)
frame_table.pack(pady=10, padx=20, fill='both', expand=True)

columns = ('No', 'Nama', 'No HP', 'Email', 'Mobil', 'Lama', 'Harga')
tree_data = ttk.Treeview(frame_table, columns=columns, show='headings', height=12, cursor='hand2')

# Atur lebar kolom agar rata di tengah
tree_data.column('No', width=50, anchor='center')
tree_data.column('Nama', width=120, anchor='center')
tree_data.column('No HP', width=100, anchor='center')
tree_data.column('Email', width=150, anchor='center')
tree_data.column('Mobil', width=150, anchor='center')
tree_data.column('Lama', width=80, anchor='center')
tree_data.column('Harga', width=120, anchor='center')

for col in columns:
    tree_data.heading(col, text=col, anchor='center')

# Scrollbar
scrollbar = ttk.Scrollbar(frame_table, orient='vertical', command=tree_data.yview)
tree_data.configure(yscrollcommand=scrollbar.set)

tree_data.pack(side='left', fill='both', expand=True)
scrollbar.pack(side='right', fill='y')

ttk.Button(page4, text='⬅ Kembali', command=open_page2, cursor='hand2').pack(pady=10)

# PAGE 5 - CARI DATA
ttk.Label(page5, text='CARI DATA RENTAL', font=('Arial', 14, 'bold')).pack(pady=15)

frame_cari = ttk.Frame(page5)
frame_cari.pack(pady=10)

ttk.Label(frame_cari, text='Cari Nama:').pack(side='left')

entry_cari = tk.Entry(frame_cari, width=25, cursor='xterm')
entry_cari.pack(side='left', padx=5)

ttk.Button(frame_cari, text='🔍 Cari', command=cari_data, cursor='hand2').pack(side='left')

# Frame untuk tabel pencarian
frame_table_cari = ttk.Frame(page5)
frame_table_cari.pack(pady=10, padx=20, fill='both', expand=True)

tree_cari = ttk.Treeview(frame_table_cari, columns=columns, show='headings', height=10, cursor='hand2')

# Atur lebar kolom agar rata di tengah
tree_cari.column('No', width=50, anchor='center')
tree_cari.column('Nama', width=120, anchor='center')
tree_cari.column('No HP', width=100, anchor='center')
tree_cari.column('Email', width=150, anchor='center')
tree_cari.column('Mobil', width=150, anchor='center')
tree_cari.column('Lama', width=80, anchor='center')
tree_cari.column('Harga', width=120, anchor='center')

for col in columns:
    tree_cari.heading(col, text=col, anchor='center')

scrollbar_cari = ttk.Scrollbar(frame_table_cari, orient='vertical', command=tree_cari.yview)
tree_cari.configure(yscrollcommand=scrollbar_cari.set)

tree_cari.pack(side='left', fill='both', expand=True)
scrollbar_cari.pack(side='right', fill='y')

ttk.Button(page5, text='⬅ Kembali', command=open_page2, cursor='hand2').pack(pady=10)

# PAGE 6 - PENDAPATAN
ttk.Label(page6, text='LAPORAN PENDAPATAN', font=('Arial', 16, 'bold')).pack(pady=30)
ttk.Label(page6, text='Total Pendapatan:').pack()
label_total = ttk.Label(page6, text='Rp 0', font=('Arial', 18, 'bold'), foreground='green')
label_total.pack(pady=10)
ttk.Label(page6, text='Jumlah Transaksi:').pack()
label_jumlah = ttk.Label(page6, text='0 transaksi', font=('Arial', 14, 'bold'))
label_jumlah.pack(pady=10)
ttk.Button(page6, text='⬅ Kembali', command=open_page2, cursor='hand2').pack(pady=20)

def hitung_pendapatan():
    total = sum(data['harga'] for data in data_rental)
    label_total.config(text=f'Rp {total:,}')
    label_jumlah.config(text=f'{len(data_rental)} transaksi')

page1.tkraise()
window.mainloop()