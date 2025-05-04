import tkinter as tk
from tkinter import messagebox

class Urun:
    def __init__(self, ad, stok):
        self.ad = ad
        self.stok = stok

    def stok_guncelle(self, miktar):
        self.stok += miktar

    def siparis_olustur(self, miktar):
        if miktar <= self.stok:
            self.stok -= miktar
            return True
        else:
            return False

    def __str__(self):
        return f"{self.ad} - Stok: {self.stok}"

class Stok:
    def __init__(self):
        self.urunler = {}

    def urun_ekle(self, urun):
        self.urunler[urun.ad] = urun

    def stok_durumu(self):
        return [str(urun) for urun in self.urunler.values()]

    def urun_getir(self, ad):
        return self.urunler.get(ad, None)

class Siparis:
    def __init__(self, siparis_no, urun, miktar):
        self.siparis_no = siparis_no
        self.urun = urun
        self.miktar = miktar

    def __str__(self):
        return f"Sipariş #{self.siparis_no}: {self.urun.ad} x {self.miktar}"

stok = Stok()
siparisler = []
siparis_no = 1

root = tk.Tk()
root.title("Stok ve Sipariş Sistemi")

tk.Label(root, text="Ürün Adı").grid(row=0, column=0)
tk.Label(root, text="Stok Miktarı").grid(row=1, column=0)

entry_ad = tk.Entry(root)
entry_stok = tk.Entry(root)
entry_ad.grid(row=0, column=1)
entry_stok.grid(row=1, column=1)

def urun_ekle():
    ad = entry_ad.get()
    try:
        miktar = int(entry_stok.get())
        urun = Urun(ad, miktar)
        stok.urun_ekle(urun)
        messagebox.showinfo("Başarılı", f"{ad} eklendi!")
        entry_ad.delete(0, tk.END)
        entry_stok.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Hata", "Geçerli bir sayı girin.")

tk.Button(root, text="Ürün Ekle", command=urun_ekle).grid(row=2, column=0, columnspan=2, pady=5)

def stok_goster():
    stok_listesi.delete(0, tk.END)
    for urun in stok.stok_durumu():
        stok_listesi.insert(tk.END, urun)

tk.Button(root, text="Stokları Göster", command=stok_goster).grid(row=3, column=0, columnspan=2, pady=5)

stok_listesi = tk.Listbox(root, width=40)
stok_listesi.grid(row=4, column=0, columnspan=2)

tk.Label(root, text="Sipariş Ürün Adı").grid(row=5, column=0)
tk.Label(root, text="Miktar").grid(row=6, column=0)

entry_siparis_ad = tk.Entry(root)
entry_siparis_miktar = tk.Entry(root)
entry_siparis_ad.grid(row=5, column=1)
entry_siparis_miktar.grid(row=6, column=1)

def siparis_olustur():
    global siparis_no
    ad = entry_siparis_ad.get()
    try:
        miktar = int(entry_siparis_miktar.get())
        urun = stok.urun_getir(ad)
        if urun and urun.siparis_olustur(miktar):
            yeni = Siparis(siparis_no, urun, miktar)
            siparisler.append(yeni)
            messagebox.showinfo("Sipariş", f"Sipariş #{siparis_no} oluşturuldu.")
            siparis_no += 1
            entry_siparis_ad.delete(0, tk.END)
            entry_siparis_miktar.delete(0, tk.END)
            siparisleri_goster()
            stok_goster()
        else:
            messagebox.showwarning("Yetersiz", "Yetersiz stok veya ürün yok.")
    except ValueError:
        messagebox.showerror("Hata", "Geçerli miktar girin.")

tk.Button(root, text="Sipariş Oluştur", command=siparis_olustur).grid(row=7, column=0, columnspan=2, pady=5)

siparis_listesi = tk.Listbox(root, width=40)
siparis_listesi.grid(row=8, column=0, columnspan=2)

def siparisleri_goster():
    siparis_listesi.delete(0, tk.END)
    for s in siparisler:
        siparis_listesi.insert(tk.END, str(s))

tk.Button(root, text="Siparişleri Göster", command=siparisleri_goster).grid(row=9, column=0, columnspan=2, pady=5)

root.mainloop()

