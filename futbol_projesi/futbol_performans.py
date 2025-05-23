import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import tkinter as tk
from tkinter import messagebox

# --- Bulanık Mantık Tanımlamaları ---

# Girdi değişkenleri
pas_isabet = ctrl.Antecedent(np.arange(0, 101, 1), 'Pas İsabet Oranı')
top_kapma = ctrl.Antecedent(np.arange(0, 21, 1), 'Top Kapma Sayısı')
sut_isabet = ctrl.Antecedent(np.arange(0, 101, 1), 'Şut İsabet Oranı')
kosu_mesafe = ctrl.Antecedent(np.arange(0, 15, 0.1), 'Koşu Mesafesi (km)')
faul_sayisi = ctrl.Antecedent(np.arange(0, 11, 1), 'Faul Sayısı')

# Çıktı değişkenleri
genel_performans = ctrl.Consequent(np.arange(0, 101, 1), 'Genel Performans')
kondisyon = ctrl.Consequent(np.arange(0, 101, 1), 'Kondisyon')

# Üyelik fonksiyonları
pas_isabet['Düşük'] = fuzz.trimf(pas_isabet.universe, [0, 0, 50])
pas_isabet['Orta'] = fuzz.trimf(pas_isabet.universe, [30, 50, 70])
pas_isabet['Yüksek'] = fuzz.trimf(pas_isabet.universe, [50, 100, 100])

top_kapma['Az'] = fuzz.trimf(top_kapma.universe, [0, 0, 7])
top_kapma['Orta'] = fuzz.trimf(top_kapma.universe, [5, 10, 15])
top_kapma['Fazla'] = fuzz.trimf(top_kapma.universe, [12, 20, 20])

sut_isabet['Düşük'] = fuzz.trimf(sut_isabet.universe, [0, 0, 50])
sut_isabet['Orta'] = fuzz.trimf(sut_isabet.universe, [30, 50, 70])
sut_isabet['Yüksek'] = fuzz.trimf(sut_isabet.universe, [50, 100, 100])

kosu_mesafe['Kısa'] = fuzz.trimf(kosu_mesafe.universe, [0, 0, 5])
kosu_mesafe['Orta'] = fuzz.trimf(kosu_mesafe.universe, [3, 7, 11])
kosu_mesafe['Uzun'] = fuzz.trimf(kosu_mesafe.universe, [9, 15, 15])

faul_sayisi['Az'] = fuzz.trimf(faul_sayisi.universe, [0, 0, 3])
faul_sayisi['Orta'] = fuzz.trimf(faul_sayisi.universe, [2, 5, 8])
faul_sayisi['Fazla'] = fuzz.trimf(faul_sayisi.universe, [6, 10, 10])

genel_performans['Düşük'] = fuzz.trimf(genel_performans.universe, [0, 0, 50])
genel_performans['Orta'] = fuzz.trimf(genel_performans.universe, [30, 50, 70])
genel_performans['Yüksek'] = fuzz.trimf(genel_performans.universe, [50, 100, 100])

kondisyon['Dinlenmeli'] = fuzz.trimf(kondisyon.universe, [0, 0, 50])
kondisyon['Normal'] = fuzz.trimf(kondisyon.universe, [30, 50, 70])
kondisyon['Ekstra'] = fuzz.trimf(kondisyon.universe, [50, 100, 100])

# Kurallar
rule1 = ctrl.Rule(pas_isabet['Yüksek'] & top_kapma['Fazla'] & sut_isabet['Yüksek'], genel_performans['Yüksek'])
rule2 = ctrl.Rule(pas_isabet['Orta'] | sut_isabet['Orta'], genel_performans['Orta'])
rule3 = ctrl.Rule(faul_sayisi['Fazla'], genel_performans['Düşük'])
rule4 = ctrl.Rule(kosu_mesafe['Uzun'] & faul_sayisi['Az'], kondisyon['Ekstra'])
rule5 = ctrl.Rule(kosu_mesafe['Orta'], kondisyon['Normal'])
rule6 = ctrl.Rule(kosu_mesafe['Kısa'] | faul_sayisi['Fazla'], kondisyon['Dinlenmeli'])

performans_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6])
performans = ctrl.ControlSystemSimulation(performans_ctrl)

# --- Tkinter Arayüzü ---

class FutbolcuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Futbolcu Performans Değerlendirme")
        self.geometry("400x350")
        self.resizable(False, False)

        # Başlık
        tk.Label(self, text="Futbolcu Performans Değerlendirme", font=("Helvetica", 16, "bold")).pack(pady=10)

        # Girdi alanları
        self.entries = {}
        self.create_input("Pas İsabet Oranı (%)", 0, 0)
        self.create_input("Top Kapma Sayısı", 1, 0)
        self.create_input("Şut İsabet Oranı (%)", 2, 0)
        self.create_input("Koşu Mesafesi (km)", 3, 0)
        self.create_input("Faul Sayısı", 4, 0)

        # Hesapla butonu
        calc_btn = tk.Button(self, text="Hesapla", command=self.hesapla, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
        calc_btn.pack(pady=20)

        # Sonuç kutusu
        self.sonuc_label = tk.Label(self, text="", font=("Helvetica", 12))
        self.sonuc_label.pack(pady=10)

    def create_input(self, label_text, row, col):
        frame = tk.Frame(self)
        frame.pack(pady=3, padx=10, fill="x")
        label = tk.Label(frame, text=label_text, width=20, anchor="w")
        label.pack(side="left")
        entry = tk.Entry(frame, width=10)
        entry.pack(side="right")
        self.entries[label_text] = entry

    def hesapla(self):
        try:
            # Girdi değerleri al
            pas = float(self.entries["Pas İsabet Oranı (%)"].get())
            top = float(self.entries["Top Kapma Sayısı"].get())
            sut = float(self.entries["Şut İsabet Oranı (%)"].get())
            kosu = float(self.entries["Koşu Mesafesi (km)"].get())
            faul = float(self.entries["Faul Sayısı"].get())

            # Bulanık mantık hesaplama
            performans.input['Pas İsabet Oranı'] = pas
            performans.input['Top Kapma Sayısı'] = top
            performans.input['Şut İsabet Oranı'] = sut
            performans.input['Koşu Mesafesi (km)'] = kosu
            performans.input['Faul Sayısı'] = faul

            performans.compute()

            gen_perf = performans.output['Genel Performans']
            kond = performans.output['Kondisyon']

            # Çıktıyı anlamlı metne çevir
            gen_perf_str = self.deger_cevir(gen_perf)
            kond_str = self.kondisyon_cevir(kond)

            self.sonuc_label.config(text=f"Genel Performans: {gen_perf_str} ({gen_perf:.1f})\nKondisyon Önerisi: {kond_str} ({kond:.1f})")

            # Grafik çıktıları otomatik göster
            genel_performans.view(sim=performans)
            kondisyon.view(sim=performans)

        except ValueError:
            messagebox.showerror("Hata", "Lütfen tüm alanlara geçerli sayılar giriniz.")

    def deger_cevir(self, val):
        if val < 40:
            return "Düşük"
        elif val < 70:
            return "Orta"
        else:
            return "Yüksek"

    def kondisyon_cevir(self, val):
        if val < 40:
            return "Dinlenmeli"
        elif val < 70:
            return "Normal"
        else:
            return "Ekstra Antrenman"

if __name__ == "__main__":
    app = FutbolcuApp()
    app.mainloop()
