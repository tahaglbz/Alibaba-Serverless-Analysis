# 📂 PROJE DOSYA HARITASI (PROJECT FILE INVENTORY)

## 📁 Dizin Yapısı (Directory Structure)

```
miniproject1/
├── 📊 ANALİZ DOSYALARI (Analysis Scripts)
│   ├── main.py                      [Main analysis module]
│   ├── advanced_analysis.py         [Advanced analytics module]
│   ├── run_analysis.py              [Integrated pipeline - START HERE]
│   └── explore_data.py              [Data exploration utility]
│
├── 📚 REHBER VE DOKÜMANTASYON (Guides & Documentation)
│   ├── README.md                    [Project overview - GEREKLİ]
│   ├── PROJECT_SUMMARY.md           [Complete summary - BAŞLAYIN BURADAN]
│   ├── QUICKSTART.md                [5-minute quick start - ÖNERİLİ]
│   ├── SETUP_GUIDE.md               [Detailed setup instructions]
│   ├── PROJECT_DOCUMENTATION.md     [Full documentation (TR/EN)]
│   ├── COMPLETION_CHECKLIST.md      [Weekly plan & checklist]
│   └── FILE_INVENTORY.md            [Bu dosya]
│
├── ⚙️  YAPIOLANDIRMA (Configuration)
│   ├── requirements.txt             [Python dependencies]
│   └── verify_setup.py              [Verification script]
│
├── 📦 VERİ (Data) - Orijinal dosyalar
│   └── datasets/
│       ├── aliyunfc_functions_perf_profile_cpu/
│       │   ├── f1_perf_profile.json
│       │   ├── f2_perf_profile.json
│       │   └── ... (f1 to f21)
│       │
│       ├── aliyunfc_functions_invoke_results_got_by_cloudwatchlog/
│       │   ├── NEW10/ NEW16/ NEW21/
│       │   └── (Excel log files)
│       │
│       └── aliyunfc_StateMachine_invoke_results/
│           ├── 1/ 2/ 3/
│           └── (Workflow logs)
│
└── 📊 ÇIKTI (Output) - Otomatik oluşturulur
    └── analysis_output/          [Created after running analysis]
        ├── analysis_report.txt
        ├── advanced_analysis_report.txt
        ├── function_performance_analysis.csv
        ├── workflow_execution_analysis.csv
        ├── 01_function_duration_comparison.png
        └── 02_resource_correlation.png
```

---

## 📝 DOSYA TARIFLERİ (FILE DESCRIPTIONS)

### A. BAŞLAMA FAYLARı (STARTUP FILES)

#### **PROJECT_SUMMARY.md** ⭐ ÖNERİLİ
- **Amaç:** Tüm projeye hızlı giriş
- **Boyut:** ~5 sayfa
- **Okuma Süresi:** 10 dakika
- **İçeriği:** 
  - Neler hazırlandığı
  - Neden başlanması gerektiği
  - İlk 3 adımı
- **Ne Yapmalı:** İlk olarak bunu okuyun!

#### **QUICKSTART.md**
- **Amaç:** 5 dakikada analiz çalıştırmak
- **Boyut:** ~3 sayfa
- **Okuma Süresi:** 5 dakika
- **İçeriği:**
  - Adım adım kurulum
  - Komutlar
  - Sorun çözümü (FAQ)
- **Ne Yapmalı:** Hızlı başlamak isterseniz bunu kullanın

#### **SETUP_GUIDE.md**
- **Amaç:** Kurulum ve konfigürasyon
- **Boyut:** ~2 sayfa
- **Okuma Süresi:** 5 dakika
- **İçeriği:**
  - Detaylı kurulum adımları
  - Windows/macOS/Linux için
  - Sorun giderme
- **Ne Yapmalı:** Kurulumda sorun varsa bunu okuyun

---

### B. DOKÜMANTASYON FAYLARı (DOCUMENTATION FILES)

#### **PROJECT_DOCUMENTATION.md** 📖 KAPSAMLI
- **Amaç:** Tüm proje detayları
- **Boyut:** ~15 sayfa
- **Dil:** Türkçe + İngilizce
- **Bölümler:**
  1. Proje Özeti (Türkçe)
  2. Teknik Kesinti (İngilizce)
  3. Veri Yapısı Açıklaması
  4. Analiz Yöntemleri
  5. Çıktılar Açıklaması
  6. Kod Örnekleri
  7. Sorun Giderme
- **Ne Yapmalı:** Derinlemesine anlamak isterseniz bunu okuyun

#### **COMPLETION_CHECKLIST.md** 📋 PROJE PLANI
- **Amaç:** Haftalık plan ve kontrol listesi
- **Boyut:** ~10 sayfa
- **İçeriği:**
  1. Haftalık görevler
  2. Adım adım kontrol listeler
  3. Rapor yazma şablonu
  4. Kalite kontrol
- **Ne Yapmalı:** Projeyi planlama ve takip etmek için kullanın

#### **README.md** (Orijinal)
- **Amaç:** Dataset açıklaması
- **Boyut:** ~3 sayfa
- **İçeriği:** Veri yapısının resmi dokümantasyonu
- **Ne Yapmalı:** Veri formatlarını anlarken referans olarak kullanın

---

### C. PYTHON ANALİZ FAYLARi (PYTHON ANALYSIS SCRIPTS)

#### **run_analysis.py** ⭐ BAŞLAYACAGINIZ
```bash
python run_analysis.py
```
- **Amaç:** Tüm analizi tek komutla çalıştırmak
- **Ne Yapar:** 
  - Basic + Advanced analizi birlikte çalıştırır
  - Tüm çıktıları oluşturur
  - Raporları kaydeder
- **Çalışma Süresi:** ~30-60 saniye
- **Çıktı:** `analysis_output/` klasöründe 6 dosya

#### **main.py**
- **Sınıf:** `AlibabaDataAnalyzer`
- **Metodları:**
  - `load_performance_profiles()` - JSON yükle
  - `load_function_logs()` - Excel yükle
  - `load_workflow_logs()` - Workflow yükle
  - `analyze_performance_profiles()` - Analiz
  - `analyze_workflow_patterns()` - İş akışı
  - `plot_performance_comparison()` - Grafikler
  - `generate_report()` - Rapor
  - `export_to_csv()` - CSV'ye aktar
- **Kullanım:** `run_analysis.py` tarafından otomatik olarak

#### **advanced_analysis.py**
- **Sınıf:** `AdvancedAnalyzer`
- **Metodları:**
  - `identify_performance_bottlenecks()` - Darboğaz
  - `compute_efficiency_scores()` - Puanlama
  - `generate_recommendations()` - Öneriler
  - `save_advanced_report()` - Rapor
- **Kullanım:** `run_analysis.py` tarafından otomatik olarak

#### **explore_data.py**
```bash
python explore_data.py
```
- **Amaç:** Veri yapısını anlamak
- **Ne Yapar:**
  - JSON dosyalarını örnek olarak gösterir
  - Excel dosyalarını okur
  - Temel istatistikleri hesaplar
- **Çalışma Süresi:** ~5-10 saniye
- **Kullanım:** Analiz öncesi veri keşfi

#### **verify_setup.py**
```bash
python verify_setup.py
```
- **Amaç:** Kurulumun doğru olup olmadığını kontrol
- **Ne Yapar:**
  - Python versiyonunu kontrol
  - Paketleri kontrol
  - Veri dosyalarını kontrol
  - Rapor yaz
- **Çalışma Süresi:** ~5 saniye
- **Kullanım:** Kurulum sonrası doğrulama

---

### D. YAPIOLANDIRMA FAYLARi (CONFIG FILES)

#### **requirements.txt**
```
pandas==2.0.3
numpy==1.24.3
matplotlib==3.7.2
openpyxl==3.1.2
scipy==1.11.2
```
- **Amaç:** Python paketleri belirtmek
- **Kurulum:** `pip install -r requirements.txt`
- **Paketler:** 5 adet (veri işleme + görselleştirme)

---

### E. ÇIKTI FAYLARi (OUTPUT FILES)

Generated after running `python run_analysis.py`:

#### **analysis_report.txt**
- **İçeriği:** 21 fonksiyonun detaylı metrikleri
- **Format:** Metin (txt)
- **Boyut:** ~10 KB
- **Örnek:**
  ```
  f1:
    Configurations tested: 12
    Average Duration: 2150.45 ms
    Memory Correlation: 0.823
    ...
  ```

#### **advanced_analysis_report.txt**
- **İçeriği:** Puanlar, öneriler, bottleneck analizi
- **Format:** Metin (txt)
- **Boyut:** ~8 KB
- **Örnek:**
  ```
  1. f5 - Overall: 92.5/100 [A (Excellent)]
  2. f3 - Overall: 89.3/100 [B (Good)]
  ...
  ```

#### **function_performance_analysis.csv**
- **İçeriği:** 21 fonksiyonun tüm metrikleri
- **Format:** CSV (Excel'de açılabilir)
- **Sütunlar:** avg_duration, min_duration, max_duration, std_duration, 
              memory_correlation, cpu_correlation, config_count
- **Satırları:** 21 (her fonksiyon)

#### **workflow_execution_analysis.csv**
- **İçeriği:** İş akışı performans verileri
- **Format:** CSV (Excel'de açılabilir)
- **Sütunlar:** Run, Workflow, total_executions, avg_duration, 
              median_duration, std_duration, min_duration, max_duration
- **Satırları:** 9 (3 run × 3 workflow)

#### **01_function_duration_comparison.png**
- **Türü:** Bar Grafik
- **İçeriği:** Her fonksiyonun ortalama süresi
- **Boyut:** ~500 KB
- **Kullanım:** Raporda eklemek, sunum yapmak

#### **02_resource_correlation.png**
- **Türü:** İki grafik (Memory + CPU korelasyonu)
- **İçeriği:** Kaynak tahsisinin performansa etkisi
- **Boyut:** ~500 KB
- **Kullanım:** Raporda eklemek, sunum yapmak

---

## 🚀 DOSYA KULLANIM SIRALASI (FILE USAGE ORDER)

### 📍 Adım 1: BAŞLA
```
1. PROJECT_SUMMARY.md okumasu (10 dk)
```

### 📍 Adım 2: KUITUP VE TEST
```
1. Terminal açın
2. QUICKSTART.md'nin ilk 3 adımını takip edin
3. python verify_setup.py çalıştırın
```

### 📍 Adım 3: ANALİZ ÇALIŞTIR
```
1. python run_analysis.py yazın
2. Analitik tamamlanmasını bekleyin (1 dk)
```

### 📍 Adım 4: SONUÇLARI OKU
```
1. analysis_output/ klasörünü açın
2. analysis_report.txt okurum
3. advanced_analysis_report.txt okurum
4. PNG görsellerini incele
5. CSV dosyalarını Excel'de aç
```

### 📍 Adım 5: DETAY ÖĞREN
```
1. PROJECT_DOCUMENTATION.md okumasu
2. Kodu (main.py) incelemesi
3. explore_data.py çalıştırması
```

### 📍 Adım 6: PROJE YAPIN
```
1. COMPLETION_CHECKLIST.md kullanarak plan yapin
2. Haftalık görevleri takip edin
3. Raporunuzu yazın
```

---

## 📊 DOSYA BÜYÜKLÜĞÜ ÖZETI (FILE SIZE SUMMARY)

| Kategori | Dosya | Boyut |
|----------|-------|-------|
| Python | main.py | ~15 KB |
| Python | advanced_analysis.py | ~12 KB |
| Python | run_analysis.py | ~5 KB |
| Python | explore_data.py | ~4 KB |
| Python | verify_setup.py | ~6 KB |
| Docs | PROJECT_DOCUMENTATION.md | ~40 KB |
| Docs | COMPLETION_CHECKLIST.md | ~30 KB |
| Docs | QUICKSTART.md | ~15 KB |
| Config | requirements.txt | <1 KB |
| Output | analysis_report.txt | ~10 KB |
| Output | function_performance_analysis.csv | ~5 KB |
| Output | *.png | ~1 MB |

**Total:** ~2 MB (çıktıları dahil)

---

## ✅ DOSYA KONTROL (FILE CHECKLIST)

Kurulum tamamlandıktan sonra şunları kontrol edin:

```
☐ Python dosyaları (4 adet):
  ☐ main.py
  ☐ advanced_analysis.py
  ☐ run_analysis.py
  ☐ explore_data.py
  ☐ verify_setup.py

☐ Rehber dosyaları (en az 3 adet):
  ☐ PROJECT_SUMMARY.md
  ☐ QUICKSTART.md
  ☐ PROJECT_DOCUMENTATION.md
  ☐ COMPLETION_CHECKLIST.md (opsiyonel)

☐ Yapılandırma:
  ☐ requirements.txt

☐ Veri klasörleri:
  ☐ datasets/aliyunfc_functions_perf_profile_cpu/ (21 file)
  ☐ datasets/aliyunfc_functions_invoke_results_got_by_cloudwatchlog/
  ☐ datasets/aliyunfc_StateMachine_invoke_results/
```

---

## 💡 DOSYA SEÇİM KIZARLA (FILE SELECTION GUIDE)

**Zamanın az ise:**
→ QUICKSTART.md + run_analysis.py

**Temel anlamak istiyorsanız:**
→ PROJECT_SUMMARY.md + PROJECT_DOCUMENTATION.md

**Kapsamlı yapmak istiyorsanız:**
→ Tüm dosyaları kullanın

**Sorun giderme:**
→ SETUP_GUIDE.md + verify_setup.py

**Proje planlaması:**
→ COMPLETION_CHECKLIST.md

---

## 🎓 ÖĞRENME YOLU (LEARNING PATH)

```
1. Başla: PROJECT_SUMMARY.md (20 dk)
   ↓
2. Kurulum: QUICKSTART.md (15 dk)
   ↓
3. Analiz: python run_analysis.py (2 dk)
   ↓
4. Rapor: analysis_report.txt okumasu (15 dk)
   ↓
5. Detay: PROJECT_DOCUMENTATION.md (30 dk)
   ↓
6. Kodlama: main.py + advanced_analysis.py incelemesi (30 dk)
   ↓
7. Proje: COMPLETION_CHECKLIST.md + final raporını yazma (3 gün)
```

**Toplam Süre:** ~3 gün (5-15 saatlik çalışma)

---

**Başarılar! 🎓✨**

Her dosya belli bir amaca hizmet etmektedir. Ihtiyacınıza göre seçin!
