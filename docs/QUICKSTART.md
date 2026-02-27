# 🚀 QUICK START GUIDE (Hızlı Başlama Rehberi)

## ⏱️ 5 Dakikada Başlayın (Get Started in 5 Minutes!)

### 1. Terminal Açın ve Klasöre Gidin

```bash
cd /Users/tahagulbaz/Desktop/4.\ sınıf\ eng/cloud/miniproject1/
```

### 2. Sanal Ortam Oluşturun (macOS)

```bash
python3 -m venv venv
source venv/bin/activate
```

**Not:** Aktivasyon başarılı ise prompt'ud `(venv)` görüneceksiniz.

### 3. Gerekli Paketleri Yükleyin

```bash
pip install -r requirements.txt
```

**Bekleme süresi:** ~1-2 dakika (internet hızına bağlı)

### 4. Analizi Çalıştırın

```bash
python run_analysis.py
```

**Bekleme süresi:** ~30-60 saniye

### 5. Sonuçları Açın

```bash
# Metin raporu oku
cat analysis_output/analysis_report.txt

# Grafikeri gör (macOS)
open analysis_output/

# CSV'yi Excel'de aç
open analysis_output/function_performance_analysis.csv
```

---

## 📊 Sonuçları Anlama (Understanding Results)

### Analiz Sonrası Elde Edecekleriniz

```
✅ analysis_report.txt
   → 21 fonksiyonun detaylı metrikleri
   → Her fonksiyon için: ortalama, min, max, std sapma
   → Bellek ve CPU korelasyonları

✅ advanced_analysis_report.txt  
   → Fonksiyonlara A-F arası puan
   → Hangi fonksiyonlar yavaş?
   → Hangi optimizasyonlar yapılmalı?

✅ function_performance_analysis.csv
   → Excel/Sheets'te açılabilir
   → Kendi grafiklerinizi çizebilirsiniz

✅ workflow_execution_analysis.csv
   → İş akışlarının performans verileri
   → Her run'ın detayları

✅ PNG Grafikler (2 adet)
   → Görsel karşılaştırmalar
   → Raporunuza ekleyebilirsiniz
```

---

## 🎯 Proje İçin Yazacağınız Rapor

### 1. Giriş (Introduction)
```
"Bu proje, Alibaba Cloud'da çalışan 21 serverless fonksiyonunun 
performans verilerini analiz etmektedir. Bellek, CPU ve iş akışı 
sürelerinin ilişkisini inceleyerek bulut kaynaklarının optimal 
kullanımını sağlayacak öneriler sunmaktadır."
```

### 2. Veri Kaynağı (Data Source)
```
- 21 fonksiyonun performans profilleri (JSON)
- Fonksiyon çalışma logları (Excel)
- 3 farklı iş akışının logları (Excel)
- Toplam: ~XXX bin veri noktası
```

### 3. Metodoloji (Methodology)
```
1. Veri Yükleme: JSON ve Excel dosyalarını Python'a aktarma
2. Analiz: İstatistiksel hesaplamalar ve korelasyon analizi
3. Puanlama: Verimlilik skorları hesaplama
4. Raporlama: Görsel ve metinsel sonuçlar üretme
```

### 4. Sonuçlar (Results)

**Kullanı analiz_output'dan sayılar:**

```markdown
## Bulguların Özeti (Key Findings)

### En Verimli Fonksiyonlar (Top 3)
[Analiz raporundan al]

### En Yavaş Fonksiyonlar (Bottom 3)
[Analiz raporundan al]

### Bellek-Performans İlişkisi
- Güçlü korelasyon olan fonksiyonlar: [Liste]
- Zayıf korelasyon olan fonksiyonlar: [Liste]

### CPU-Performans İlişkisi
- Güçlü CPU bağımlılığı: [Liste]
- CPU'dan etkilenmeyen: [Liste]

### İş Akışı Performansı
- Ortalama süresi en kısa: [Veri]
- Ortalama süresi en uzun: [Veri]
- En tutarlı iş akışı: [Veri]
```

### 5. Öneriler (Recommendations)

```markdown
## Optimizasyon Önerileri

### 1. Bellek Optimizasyonu
[Rapordan gelecek öneriler]

### 2. CPU Optimizasyonu  
[Rapordan gelecek öneriler]

### 3. İş Akışı Optimizasyonu
[Rapordan gelecek öneriler]
```

### 6. Sonuç (Conclusion)

```
"Bu analiz, Alibaba Cloud servislerinde kaynak tahsisinin 
performansı doğrudan etkilediğini göstermektedir. Önerilen 
optimizasyonlar uygulanması halinde %X - %Y verimlilik 
artışı sağlanabilecektir."
```

---

## 🔧 Sık Sorun Çözümleri (FAQ)

### S: "Python bulunamadı" hatası alıyorum

**C:**
```bash
# Python sürümünü kontrol edin
python3 --version

# Eğer yüklü değilse macOS'ta:
brew install python3
```

### S: Excel dosyasının içindeki dosya formatından emin değilim

**C:**
Fiziksel dosyalar `.xls` veya `.xlsx` olabilir. Kod her ikisini de destekler.
```python
# Kodda bu satır her ikisini de yükler:
if file.suffix in ['.xlsx', '.xls']:
```

### S: Grafiklerin çözünürlüğü kötü görünüyor

**C:**
Kodu açın ve değiştirin:
```python
# Şu satırı bulun:
plt.savefig(..., dpi=300)

# dpi değerini artırın:
plt.savefig(..., dpi=600)  # Daha yüksek kalite
```

### S: Belirli bir fonksiyonu detaylı incelemek istiyorum

**C:**
```python
from main import AlibabaDataAnalyzer

analyzer = AlibabaDataAnalyzer()
analyzer.load_performance_profiles()

# f1'i göstermek için:
f1_data = analyzer.perf_profiles['f1']
for config, duration in f1_data.items():
    print(f"{config}: {duration}ms")
```

---

## 📈 Grafikleri Raporunuza Nasıl Ekleyin?

### Word/Google Docs için:
1. `analysis_output/` klasörünü açın
2. PNG dosyalarını sağ tıkla → Kopyala
3. Word'e yapıştır

### PowerPoint için:
1. Insert → Pictures → Bu bilgisayardan
2. `analysis_output/` klasöründen seç
3. Slayt sunumuna ekle

### LaTeX/PDF için:
```latex
\begin{figure}[h]
  \includegraphics[width=0.8\textwidth]{analysis_output/01_function_duration_comparison}
  \caption{Fonksiyonlar Arasında Sürü Karşılaştırması}
\end{figure}
```

---

## 💻 CSV Verileriyle Excel'de İleri Analiz

### Ornek: Fonksiyonları Kategorilendirme

Excel'de açtığınız `function_performance_analysis.csv` dosyasında:

1. **Conditional Formatting** kullanarak renk kodlaması:
   - Yeşil: avg_duration < 2000ms (Hızlı)
   - Sarı: 2000-5000ms (Orta)
   - Kırmızı: > 5000ms (Yavaş)

2. **Pivot Table** oluşturma:
   - Fonksiyonları CPU korelasyonuna göre gruplandır
   - Ortalama sürelerri hesapla

3. **Kendi grafiklerini** çiz

---

## 📚 Kaynaklar (Resources)

- **Pandas Dokümantasyon:** https://pandas.pydata.org/
- **NumPy Kullanımı:** https://numpy.org/
- **Matplotlib Grafikler:** https://matplotlib.org/
- **Alibaba Cloud FC:** https://www.alibabacloud.com/product/function-compute

---

## ✅ Kontrol Listesi (Checklist)

Tamamlayınız:

- [ ] Python 3.7+ kurulu mu?
- [ ] pip install yapıldı mı?
- [ ] run_analysis.py başarıyla çalıştı mı?
- [ ] analysis_output/ klasörü oluştu mu?
- [ ] Tüm çıktı dosyaları mevcut mu?
- [ ] Raporları okudum ve anladım mı?
- [ ] Grafikleri inceledim mi?
- [ ] Proje raporunu yazmaya başladım mı?

---

## 🎓 Öğrenme Çıktıları (Learning Outcomes)

Bu projeden sonra şunları yapabileceksiniz:

✅ Serverless bulut ortamlarının performans özelliklerini analiz etme  
✅ JSON ve Excel dosyalarını Python'da işleme  
✅ İstatistiksel analiz yaparak verilerden insights çıkarma  
✅ Korelasyon ve regresyon analizi uygulamak  
✅ Veri görselleştirme ile bulguları sunma  
✅ Teknik rapor yazma ve öneriler sunma  

---

**Sorular? Başlamaya hazırsınız! 🚀**

*Happy analyzing! 📊*
