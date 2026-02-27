# Alibaba Cloud Serverless Performance Analysis

**A comprehensive data analysis suite for Alibaba Cloud Function Compute (FC) and CloudFlow serverless workloads**

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com/tahaglbz/Alibaba-Serverless-Analysis)

---

## 🎯 Project Overview

This project analyzes **21 serverless functions** from Alibaba Cloud's production environment, examining performance characteristics under varying resource configurations. The analysis reveals critical insights into memory-performance relationships, identifies performance bottlenecks, and provides actionable optimization recommendations.

**Analyzed 1,206+ configurations per function across 21 serverless functions with emphasis on performance profiling and resource optimization.**

---

## 🔬 Key Results

### Critical Findings

#### 1. **Negative Memory-Performance Correlation** ⚠️
- **19 out of 21 functions** show negative correlation between memory and execution time
- **Counterintuitive Discovery**: Increasing memory actually slows down performance
- **Potential Impact**: 45-60% performance improvement possible through memory optimization

#### 2. **Top Performers**
- **f5**: 87.7/100 (A - Excellent)
- **f17**: 85.5/100 (B - Good) 
- **f7**: 83.5/100 (B - Good)

#### 3. **Critical Problem Areas**
- **f16**: 6.0/100 - Extreme variance (σ=3,133ms) - UNPREDICTABLE
- **f1**: 13.9/100 - Slowest function (3,102ms avg) - 10.6x slower than f17
- **f11, f15**: 21.7/100, 25.6/100 - High latency

---

## 📁 Repository Structure

```
├── README.md                    # Documentation (this file)
├── .gitignore                   # Git configuration
│
├── src/                        # Python analysis code
│   ├── run_analysis.py        # Main entry point
│   ├── main.py                # Core analysis engine
│   ├── advanced_analysis.py   # Advanced analytics
│   ├── explore_data.py        # Data exploration
│   ├── verify_setup.py        # Setup verification
│   └── requirements.txt       # Dependencies
│
├── docs/                       # Documentation
│   ├── QUICKSTART.md          # 5-minute quick start
│   ├── SETUP_GUIDE.md         # Detailed setup
│   ├── PROJECT_DOCUMENTATION.md
│   ├── COMPLETION_CHECKLIST.md
│   ├── FILE_INVENTORY.md
│   ├── PROJECT_SUMMARY.md
│   └── START_HERE.md
│
├── outputs/                    # Analysis results
│   ├── analysis_report.txt
│   ├── advanced_analysis_report.txt
│   ├── function_performance_analysis.csv
│   ├── workflow_execution_analysis.csv
│   ├── 01_function_duration_comparison.png
│   └── 02_resource_correlation.png
│
└── datasets/                   # Source data (local only)
    ├── aliyunfc_functions_perf_profile_cpu/
    ├── aliyunfc_functions_invoke_results_got_by_cloudwatchlog/
    └── aliyunfc_StateMachine_invoke_results/
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip/conda package manager

### Installation

```bash
git clone https://github.com/tahaglbz/Alibaba-Serverless-Analysis.git
cd Alibaba-Serverless-Analysis

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r src/requirements.txt
```

### Run Analysis

```bash
python src/run_analysis.py
```

**Results generated in `outputs/` folder within ~30-60 seconds.**

---

## 📊 Analysis Highlights

### Performance Metrics Generated
- ✅ Average, Min, Max, Std Dev execution times
- ✅ Memory/CPU correlation coefficients  
- ✅ Efficiency grades (A-F scale)
- ✅ Bottleneck identification
- ✅ Optimization recommendations
- ✅ Professional visualizations (PNG)
- ✅ Excel-ready data (CSV)

### Output Files
1. **analysis_report.txt** - Detailed metrics for all 21 functions
2. **advanced_analysis_report.txt** - Efficiency rankings & recommendations  
3. **function_performance_analysis.csv** - All metrics in spreadsheet format
4. **Visualization graphs** - Performance and correlation charts

---

## 🔍 Key Insights

### Memory Allocation Paradox
Most functions show **negative correlation** with memory:
- More memory ≠ Faster execution
- Current allocation strategy appears suboptimal
- Recommendation: Reduce memory for f1-f19, f21

### Performance Variance
- f16 shows extreme unpredictability (σ=3,133ms)
- Suggests underlying sys tem issues or configuration problems
- Requires immediate investigation

### Function-Specific Tuning
- No one-size-fits-all solution
- f5, f17, f7 are already well-optimized
- f1, f11, f15, f16 need focused optimization

---

## 📈 Technology Stack

| Component | Tools |
|-----------|-------|
| **Programming** | Python 3.7+ |
| **Data Processing** | pandas, numpy |
| **Visualization** | matplotlib |
| **Statistics** | scipy |
| **Excel Support** | openpyxl, xlrd |

---

## 📖 Documentation

| Guide | Purpose |
|-------|---------|
| [QUICKSTART.md](docs/QUICKSTART.md) | Get started in 5 minutes |
| [SETUP_GUIDE.md](docs/SETUP_GUIDE.md) | Detailed installation |
| [PROJECT_DOCUMENTATION.md](docs/PROJECT_DOCUMENTATION.md) | Technical details |
| [COMPLETION_CHECKLIST.md](docs/COMPLETION_CHECKLIST.md) | Project timeline |

---

## 💡 Next Steps

1. ✅ Clone repository
2. ✅ Follow [QUICKSTART.md](docs/QUICKSTART.md)
3. ✅ Run `python src/run_analysis.py`
4. ✅ Review results in `outputs/`

---

**Happy analyzing! 📊✨** 

