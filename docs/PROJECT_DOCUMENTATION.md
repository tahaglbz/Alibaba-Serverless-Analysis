# 📚 PROJE DÖKÜMENTASYONU (PROJECT DOCUMENTATION)

## 📋 İçindekiler (Table of Contents)

1. **Proje Özeti (Project Overview)**
2. **Veri Yapısı Açıklaması (Data Structure)**
3. **Teknik Mimarı (Technical Architecture)**
4. **Analiz Yöntemleri (Analysis Methods)**
5. **Çıktılar ve Raporlar (Outputs & Reports)**
6. **Kullanım Kılavuzu (Usage Guide)**

---

## 1️⃣ PROJe ÖZETI (PROJECT OVERVIEW)

### Proje Nedir?

Bu miniproje, **Alibaba Cloud** tarafından sağlanan sunucusuz bilişim (serverless) ortamında çalışan fonksiyonların performans verilerini analiz etmekle ilgilidir.

### Hedefler (Objectives)

- ✅ 21 ayrı bulut fonksiyonunun performans metriklerini inceleme
- ✅ Bellek (Memory) ve CPU kaynaklarının performansa etkisini anlama
- ✅ İş akışlarının (workflows) zaman karakteristiklerini analiz etme
- ✅ Kaynak optimizasyonu için veri tabanlı öneriler sunma
- ✅ Bulut ortamında en iyi uygulamaları belirlemek

### Hedef Kitle (Stakeholders)

- Cloud engineers (Bulut mühendisleri)
- System administrators (Sistem yöneticileri)
- DevOps professionals
- Araştırmacılar (Performance modeling)

---

## 2️⃣ VERI YAPISI AÇIKLAMASI (DATA STRUCTURE)

### A. Fonksiyon Performans Profilleri (Function Performance Profiles)

**Konum:** `datasets/aliyunfc_functions_perf_profile_cpu/`

**Dosyalar:** `f1_perf_profile.json` × 21 (f1 to f21)

**Veri Formatı:**
```json
{
  "512,0.25": 2920,      // 512MB bellek, 0.25 vCPU → 2920ms
  "512,0.5": 1850,       // 512MB bellek, 0.5 vCPU → 1850ms
  "1024,0.25": 2450,     // 1024MB bellek, 0.25 vCPU → 2450ms
  "1024,0.5": 1200
}
```

**Ne Anlama Gelir?**
Bu dosyalar, her fonksiyonun farklı bellek/CPU kombinasyonlarında ne kadar hızlı çalıştığını gösterir.

### B. Fonksiyon Çalışma Logları (Function Invocation Logs)

**Konum:** `datasets/aliyunfc_functions_invoke_results_got_by_cloudwatchlog/`

**Dosyalar:** En az 3 klasör (NEW10, NEW16, NEW21) ve her birinde:
- 1/ → log4_metrics.txt (metnsel kaydedilen sonuçlar)
- 2/ → log5_metrics.txt
- 3/ → log6_metrics.txt

**Sütunlar (Columns):**

| Sütun | Anlamı | Örnek |
|-------|--------|--------|
| `FunctionName` | Fonksiyonun adı | f1, f2, f3... |
| `MemorySize` | Tahsis edilen bellek (MB) | 512, 1024 |
| `CpuSize` | Tahsis edilen CPU (vCPU) | 0.25, 0.5, 1.0 |
| `BilledDuration` | İşlem süresi (ms) | 1244, 2156 |
| `FunctionState` | Başarı durumu | Success, Failed |
| `RequestID` | İsteğin benzersiz kimliği | 1-6839dc92-... |
| `UTCTimeStamp` | İşlem zamanı | 1.75E+12 |

### C. İş Akışı Logları (Workflow Execution Logs)

**Konum:** `datasets/aliyunfc_StateMachine_invoke_results/`

**Yapı:**
```
1/ → Run 1 (New10, New16, New21 workflows)
2/ → Run 2 (New10, New16, New21 workflows)
3/ → Run 3 (New10, New16, New21 workflows)
```

**Sütunlar:**

| Sütun | Anlamı | Örnek |
|-------|--------|--------|
| `Start` | İş akışı başlangıç zamanı | 2025-06-17T08:19:09.562Z |
| `End` | İş akışı bitiş zamanı | 2025-06-17T08:19:27.481Z |
| `Duration` | Toplam süre (ms) | 17919 |

---

## 3️⃣ TEKNIK MİMARİ (TECHNICAL ARCHITECTURE)

### Dosya Yapısı

```
miniproject1/
├── main.py                          # Ana analiz modülü
├── advanced_analysis.py             # İleri analytics
├── run_analysis.py                  # Tümleşik çalıştırıcı
├── requirements.txt                 # Python bağımlılıkları
├── SETUP_GUIDE.md                   # Kurulum rehberi
├── PROJECT_DOCUMENTATION.md         # Bu dosya
│
└── datasets/
    ├── aliyunfc_functions_perf_profile_cpu/
    ├── aliyunfc_functions_invoke_results_got_by_cloudwatchlog/
    └── aliyunfc_StateMachine_invoke_results/
│
└── analysis_output/                 # Çıktı klasörü (otomatik oluşturulur)
    ├── analysis_report.txt
    ├── advanced_analysis_report.txt
    ├── function_performance_analysis.csv
    ├── workflow_execution_analysis.csv
    ├── 01_function_duration_comparison.png
    └── 02_resource_correlation.png
```

### Python Modülleri

**main.py - `AlibabaDataAnalyzer` sınıfı:**
- `load_performance_profiles()` - JSON dosyalarını yükler
- `load_function_logs()` - Excel fonksiyon loglarını yükler
- `load_workflow_logs()` - Excel iş akışı loglarını yükler
- `analyze_performance_profiles()` - Performans metriklerini hesaplar
- `analyze_workflow_patterns()` - İş akışı desenlerini analiz eder
- `plot_performance_comparison()` - Grafikler oluşturur
- `export_to_csv()` - CSV dosyalarına dışa aktarır

**advanced_analysis.py - `AdvancedAnalyzer` sınıfı:**
- `identify_performance_bottlenecks()` - Darboğazları bulur
- `compute_efficiency_scores()` - Verimlilik puanları hesaplar
- `generate_recommendations()` - Optimizasyon önerileri üretir
- `save_advanced_report()` - Detaylı rapor kaydeder

---

## 4️⃣ ANALİZ YÖNTEMLERİ (ANALYSIS METHODS)

### A. Temel İstatistikler (Basic Statistics)

Her fonksiyon için hesaplanan metrikler:

```
✓ Ortalama Süre (Average Duration)
✓ Minimum Süre (Min Duration)  
✓ Maksimum Süre (Max Duration)
✓ Standart Sapma (Std Deviation)
✓ Test Sayısı (Number of configurations)
```

### B. Korelasyon Analizi (Correlation Analysis)

**Bellek-Performans Korelasyonu:**
- -1.0 ~ 0.0: Bellek az olsa daha hızlı (nadir)
- 0.0 ~ 0.3: Zayıf ilişki
- 0.3 ~ 0.7: Orta ilişki  
- 0.7 ~ 1.0: Güçlü ilişki (bellek artarsa hızlı çalışır)

**CPU-Performans Korelasyonu:**
- Pozitif değerler: CPU artarsa fonksiyon hızlanır
- Negatif değerler: CPU gerekli değil

### C. Verimlilik Puanlandırması (Efficiency Scoring)

```
Genel Puan = (Hız Puanı × 0.8) + (Tutarlılık Puanı × 0.2)

Hızlıktan 0-100: Düşük süre = yüksek puan
Tutarlılıktan 0-100: Düşük değişkenlik = yüksek puan
```

**Puan Derecelendirmesi:**
- 90-100: A (Mükemmel)
- 80-89: B (İyi)
- 70-79: C (Orta)
- 60-69: D (Zayıf)
- <60: F (Çok Zayıf)

### D. Darboğaz Tespiti (Bottleneck Detection)

1. **Yavaş Fonksiyonlar:** Ortalamadan 1+ std sapma kadar yavaş
2. **Yüksek Değişkenlik:** Tutarlı olmayan performans gösteren
3. **Kaynak Duyarlı:** Bellek/CPU'ya çok bağımlı olan

---

## 5️⃣ ÇIKTILAR VE RAPORLAR (OUTPUTS & REPORTS)

### A. Metin Raporları

#### `analysis_report.txt`
Tüm fonksiyonların ayrıntılı metrikleri içerir.

**Örnek Çıktı:**
```
FUNCTION PERFORMANCE ANALYSIS
==============================

f1:
  Configurations tested: 12
  Average Duration: 2150.45 ms
  Min Duration: 1200.00 ms
  Max Duration: 3450.00 ms
  Std Deviation: 650.32 ms
  Memory Correlation: 0.823
  CPU Correlation: 0.456
```

#### `advanced_analysis_report.txt`
Puanlar, öneriler ve optimizasyon ipuçları içerir.

### B. CSV Dosyaları

#### `function_performance_analysis.csv`
All functions with their metrics in spreadsheet format.

```csv
,avg_duration,min_duration,max_duration,std_duration,memory_correlation,cpu_correlation,config_count
f1,2150.45,1200.0,3450.0,650.32,0.823,0.456,12
f2,1890.32,950.0,2800.0,580.15,0.712,-0.123,12
```

#### `workflow_execution_analysis.csv`
Her iş akışı çalışması için metrikleri içerir.

```csv
Run,Workflow,total_executions,avg_duration,median_duration,std_duration,min_duration,max_duration
1,NEW10,250,18500.32,18450.0,1200.45,16200.0,22100.0
1,NEW16,250,28900.15,28850.0,1850.32,25600.0,33200.0
```

### C. Görsel Çıktılar (Visualizations)

#### `01_function_duration_comparison.png`
Her fonksiyonun ortalama çalışma süresini gösteren bar grafik.

**Kullanım:** Hangi fonksiyonların daha yavaş olduğunu hızlıca görmek.

#### `02_resource_correlation.png`
Bellek ve CPU'nun performansla ilişkisini gösteren iki grafik.

**Kullanım:** Kaynak optimizasyonu için kararlar almak.

---

## 6️⃣ KULLANIM KILAVUZU (USAGE GUIDE)

### Kurulum (Installation)

```bash
# Klasöre gidin
cd /Users/tahagulbaz/Desktop/4.\ sınıf\ eng/cloud/miniproject1/

# Sanal ortam oluşturun (opsiyonel ama önerilen)
python3 -m venv venv
source venv/bin/activate

# Gerekli kütüphaneleri yükleyin
pip install -r requirements.txt
```

### Analizi Çalıştırma (Running Analysis)

**Seçenek 1: Tümleşik analiz (Önerilen)**
```bash
python run_analysis.py
```
Bu komut temel ve ileri analizleri birlikte çalıştırır.

**Seçenek 2: Yalnızca temel analiz**
```bash
python main.py
```

**Seçenek 3: Özel kodu yazarak**
```python
from main import AlibabaDataAnalyzer

analyzer = AlibabaDataAnalyzer()
analyzer.load_performance_profiles()
analyzer.analyze_performance_profiles()
results = analyzer.analysis_results
```

### Çıktıları İnceleme (Reviewing Outputs)

```bash
# Raporları görüntüleyin
cat analysis_output/analysis_report.txt
cat analysis_output/advanced_analysis_report.txt

# CSV dosyalarını Excel'de aç
open analysis_output/function_performance_analysis.csv

# Görsel grafikleri aç
open analysis_output/01_function_duration_comparison.png
```

### Sorun Giderme (Troubleshooting)

**Problem:** "No module named 'pandas'"

**Çözüm:**
```bash
# Sanal ortamı devre dışı bırak ve aktivasyonu tekrarla
deactivate
source venv/bin/activate
pip install -r requirements.txt
```

**Problem:** "FileNotFoundError: datasets klasörü bulunamadı"

**Çözüm:**
```bash
# Doğru dizinde olduğunuzu kontrol edin
pwd
# Çıktı: /Users/tahagulbaz/Desktop/4. sınıf eng/cloud/miniproject1
```

---

## 📊 ANALİZ SONUÇLARI YORUMLAMA (INTERPRETING RESULTS)

### Verimlilik Puanları (Efficiency Scores)

- **Yüksek puan (>85):** Fonksiyon iyidir, kaynaklar iyi kullanıyor
- **Orta puan (70-85):** Normal performans, iyileştirilebilir
- **Düşük puan (<70):** İncelenmesi gereken sorunlar var

### Korelasyon Değerleri (Correlation Values)

- **0.8+:** Çok güçlü ilişki (bellek/CPU kritik)
- **0.5-0.8:** Orta-güçlü ilişki (etkisi vardır)
- **0.2-0.5:** Zayıf ilişki (etkisi az)
- **0 to 0.2:** Çok zayıf ilişki (neredeyse etki yok)

### Optimizasyon Önerileri (Optimization Recommendations)

Raporda verilen önerileri şu sırayla uygulayın:

1. **Darboğazları çöz:** Yavaş fonksiyonları optimize et
2. **Tutarlılığı artır:** Değişken performansı düzelt
3. **Kaynakları ayarla:** CPU/bellek tahsisini optimize et

---

## 💡 İLERİ KONULAR (ADVANCED TOPICS)

### Özel Analiz Eklemek

`main.py` dosyasını şu şekilde genişletin:

```python
def custom_analysis(self):
    """Kendi analiz fonksiyonunuzu ekleyin"""
    # Veri işle
    data = self.analysis_results['perf_profiles']
    
    # Hesap yap
    filtered = {k: v for k, v in data.items() 
               if v['avg_duration'] > 2000}
    
    # Sonuç döndür
    return filtered
```

### Grafikleri Özelleştirmek

`plot_performance_comparison()` metodunu değiştirerek kendi grafiklerinizi oluşturun.

---

## 📝 İLETİŞİM VE DESTEK (CONTACT & SUPPORT)

**Sorular, öneriler veya sorunlar için:**
- README.md dosyasını kontrol edin
- Kodda inline yorumları okuyun
- print() ifadeleriyle hata avunda çalışın

---

**Başarılar!** 🎓✨

*Bu proje sunucusuz bilişim ortamlarında performans analizi konusunda pratik deneyim kazandıracaktır.*
