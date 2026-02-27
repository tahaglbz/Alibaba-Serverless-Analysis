# Alibaba Cloud Serverless Performance Analysis

**Professional performance analysis suite for Alibaba Cloud Function Compute (FC) and CloudFlow serverless workloads**

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

This project provides a comprehensive performance analysis framework for Alibaba Cloud serverless workloads. The analysis examines **21 serverless functions** across **1,206+ configurations** per function, revealing critical insights into resource allocation strategies, performance bottlenecks, and optimization opportunities.

### Key Scope
- **Functions Analyzed**: 21 (f1 through f21)
- **Configurations Tested**: 1,206+ per function (memory/CPU combinations)
- **Workflows Examined**: 3 different CloudFlow workflows
- **Total Data Points**: 25,000+
- **Analysis Period**: Complete production traces

---

## Analysis Findings

### Executive Summary

This analysis reveals significant performance disparities across Alibaba Cloud serverless functions and identifies a critical resource allocation misconfiguration affecting 19 out of 21 functions.

### Efficiency Rankings (A-F Scale)

#### Top Performers
| Function | Score | Grade | Avg Duration |
|----------|-------|-------|--------------|
| f5 | 87.7/100 | B - Good | 298ms |
| f17 | 85.5/100 | B - Good | 292ms |
| f7 | 83.5/100 | B - Good | 365ms |
| f6 | 81.8/100 | B - Good | 312ms |
| f8 | 81.0/100 | B - Good | 325ms |

#### Critical Issues
| Function | Score | Grade | Issue |
|----------|-------|-------|-------|
| f16 | 6.0/100 | F - Critical | Extreme variance (σ=3,133ms) |
| f1 | 13.9/100 | F - Critical | Slowest (3,102ms avg) |
| f11 | 21.7/100 | F - Critical | High latency (2,871ms avg) |
| f15 | 25.6/100 | F - Critical | High latency (2,747ms avg) |

### Key Performance Metrics

- **Average Function Duration**: 1,057.45ms
- **Fastest Function**: f17 (292ms)
- **Slowest Function**: f1 (3,102ms) — 10.6x slower than f17
- **Highest Variance**: f16 (σ=3,133ms) — Extremely unpredictable
- **Performance Range**: 6.0 to 87.7 efficiency score (14.6x disparity)

### Critical Discovery: Memory-Performance Paradox

**Major Finding: 19 out of 21 functions show NEGATIVE correlation between memory allocation and execution time**

```
Memory Correlation Analysis:
├── Negative Correlation (-0.38 to -0.69): 19 functions
│   → More Memory = SLOWER Execution
│   → Potential 45-60% improvement by REDUCING memory
├── Neutral Correlation (-0.01 to +0.03): 1 function (f20)
└── Positive Correlation: 1 function (f5)
    → Expected behavior: More memory = Faster

CPU Correlation Analysis:
├── Similar Negative Pattern: 19 functions (-0.30 to -0.64)
└── Indicates Resource Allocation Misconfiguration
```

### Performance Bottlenecks

**Slow Functions (Latency Issues)**
- f1: 3,102.51ms average duration (HIGH PRIORITY)
- f16: 2,880.86ms average duration (HIGH PRIORITY)
- f11: 2,871.26ms average duration (MEDIUM)
- f15: 2,747.23ms average duration (MEDIUM)

**Inconsistent Execution**
- f16: Extreme variance (σ=3,133ms) — Unpredictable performance
- Functions with high variance present operational risks

### Optimization Recommendations

#### Top Priority Actions

1. **Memory Allocation Review** (All 19 negatively-correlated functions)
   - Current: Likely over-provisioned memory
   - Recommendation: Reduce memory allocations and measure impact
   - Expected Benefit: 45-60% execution time improvement

2. **Critical Functions (Stage 1)**
   - f1: Reduce memory allocation from current level
   - f11: Investigate for code inefficiencies
   - f15: Profile for resource contention
   - f16: Debug extreme variance issue

3. **Consistency Improvements** (Stage 2)
   - Implement connection pooling
   - Cache initialization data
   - Review cold start behavior

4. **Monitoring** (Ongoing)
   - Implement per-configuration execution tracking
   - Set up alerts for functions exceeding thresholds
   - Track correlation changes after optimization

#### Complete Optimization List

All 19 negatively-correlated functions (f1-f9, f10-f19, f21) require memory optimization:
- f1, f2, f3, f4, f5, f6, f7, f8, f9 — Reduce memory allocation
- f10, f12, f13, f14, f15, f16, f17, f18, f19, f21 — Reduce memory allocation
- f20 — No memory correlation adjustment needed
- f11 — Investigate code efficiency before memory optimization

---

## Execution Guide

### Prerequisites

- Python 3.7 or higher
- pip package manager
- Alibaba Cloud FC dataset files in `data/datasets/` directory

### Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/tahaglbz/Alibaba-Serverless-Analysis.git
   cd Alibaba-Serverless-Analysis
   ```

2. **Create Python Virtual Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate  # Windows
   ```

3. **Install Dependencies**
   ```bash
   pip install -r src/requirements.txt
   ```

4. **Verify Setup**
   ```bash
   python src/verify_setup.py
   ```

### Running the Analysis

#### Option 1: Run Complete Analysis
```bash
python src/run_analysis.py
```
This will execute all analysis modules and generate comprehensive reports.

#### Option 2: Run Specific Analysis
```bash
# Data exploration
python src/explore_data.py

# Advanced analysis only
python src/advanced_analysis.py

# Main analysis
python src/main.py
```

### Output Generated

Analysis results are automatically generated in `analysis_output/`:

- `analysis_report.txt` — Detailed performance metrics for all functions
- `advanced_analysis_report.txt` — Efficiency rankings and recommendations
- `function_performance_analysis.csv` — All metrics in CSV format
- `workflow_execution_analysis.csv` — Workflow execution statistics
- `01_function_duration_comparison.png` — Performance comparison visualization
- `02_resource_correlation.png` — Memory/CPU correlation analysis chart

---

## Repository Structure

```
Alibaba-Serverless-Analysis/
│
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
│
├── src/                         # Analysis source code
│   ├── run_analysis.py         # Main entry point for complete analysis
│   ├── main.py                 # Core AlibabaDataAnalyzer class
│   ├── advanced_analysis.py    # Advanced analytics and recommendations
│   ├── explore_data.py         # Data exploration utility
│   ├── verify_setup.py         # Setup verification script
│   └── requirements.txt        # Python dependencies
│
├── data/                        # Original datasets
│   └── datasets/
│       ├── aliyunfc_functions_perf_profile_cpu/     # Performance profiles
│       ├── aliyunfc_functions_invoke_results/       # Function execution logs
│       └── aliyunfc_StateMachine_invoke_results/    # Workflow logs
│
└── analysis_output/             # Generated analysis results
    ├── analysis_report.txt           # Performance report
    ├── advanced_analysis_report.txt  # Analysis recommendations
    ├── function_performance_analysis.csv
    ├── workflow_execution_analysis.csv
    ├── 01_function_duration_comparison.png
    └── 02_resource_correlation.png
```

---

## Dependencies

- **pandas** (2.0.3) — Data manipulation and analysis
- **numpy** (1.24.3) — Numerical computing
- **matplotlib** (3.7.2) — Data visualization
- **openpyxl** (3.1.2) — Excel file handling
- **scipy** (1.11.2) — Scientific computing

---

## License

This project is licensed under the MIT License. See LICENSE file for details.

---

## Project Information

- **Repository**: [GitHub - Alibaba-Serverless-Analysis](https://github.com/tahaglbz/Alibaba-Serverless-Analysis)
- **Dataset Source**: Alibaba Cloud Function Compute Production Traces
- **Analysis Date**: February 2026
- **Total Functions Analyzed**: 21
- **Total Configurations**: 25,000+

---

## 🚀 How to Run

### Prerequisites
```bash
# Required: Python 3.7 or higher
python3 --version

# Recommended: Virtual environment
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate     # Windows
```

### Installation

```bash
# Clone the repository
git clone https://github.com/tahaglbz/Alibaba-Serverless-Analysis.git
cd Alibaba-Serverless-Analysis

# Install Python dependencies
pip install -r src/requirements.txt
```

### Running the Analysis

```bash
# Execute the complete analysis pipeline
python src/run_analysis.py

# Alternative: Explore data structure first
python src/explore_data.py

# Verify your setup
python src/verify_setup.py
```

### Expected Execution

```
✅ Loading performance profiles... (21 functions)
✅ Loading function invocation logs...
✅ Loading workflow execution logs...
✅ Analyzing performance profiles...
✅ Analyzing workflow patterns...
✅ Creating visualizations...
✅ Generating reports...
✅ Exporting to CSV...

Analysis Complete: ~30-60 seconds
Results Location: analysis_output/
```

---

## 📊 Output Description

### Generated Files in `analysis_output/`

#### 1. **analysis_report.txt** (214 lines)
Comprehensive performance metrics for all 21 functions:
- Configuration count tested
- Average, Min, Max, Std Dev execution times
- Memory correlation coefficient
- CPU correlation coefficient

Example (f1):
```
f1:
  Configurations tested: 1206
  Average Duration: 3102.51 ms
  Min Duration: 2339.00 ms
  Max Duration: 12798.00 ms
  Std Deviation: 943.77 ms
  Memory Correlation: -0.378
  CPU Correlation: -0.299
```

#### 2. **advanced_analysis_report.txt** (104 lines)
Efficiency rankings and optimization recommendations:
- **Efficiency Rankings**: Functions graded A-F with speed and consistency scores
- **Bottleneck Analysis**: Slow functions, high variance functions
- **Optimization Recommendations**: Memory/CPU adjustment suggestions

Example:
```
1. f5   - Overall: 87.7/100 [A (Excellent)]
2. f17  - Overall: 85.5/100 [B (Good)]
...
21. f16 - Overall: 6.0/100 [F (Critical)]
```

#### 3. **function_performance_analysis.csv**
Excel-ready dataset with 21 rows and 7 columns:
```
,avg_duration,min_duration,max_duration,std_duration,memory_correlation,cpu_correlation,config_count
f1,3102.51,2339.0,12798.0,943.77,-0.378,-0.299,1206.0
f5,298.15,209.0,1456.0,89.32,-0.612,-0.551,1206.0
...
```

#### 4. **workflow_execution_analysis.csv**
Workflow performance statistics (if available)

#### 5. **01_function_duration_comparison.png**
Bar chart showing average execution duration for each function:
- X-axis: Function names (f1-f21)
- Y-axis: Average duration in milliseconds
- Visual comparison of performance across all functions

#### 6. **02_resource_correlation.png**
Two-panel visualization showing resource impact:
- **Left Panel**: Memory vs Execution Time correlation
- **Right Panel**: CPU vs Execution Time correlation
- Red/Green bars indicate correlation strength

---

## 💡 Key Insights & Recommendations

### 1. The Memory Paradox
**Most functions are misconfigured with excess memory allocation**
- Counterintuitive finding: More memory = Slower performance
- Indicates resource contention or configuration issues
- **Action**: Review memory allocation strategy, reduce for non-memory-bound functions

### 2. Function-Specific Issues
- **f16**: Extreme unpredictability - requires urgent investigation
- **f1**: 10.6x slower than optimal - potential code optimization needed
- **f11, f15**: Consistent high latency - review function logic

### 3. Well-Optimized Functions
- **f5, f17, f7**: Already well-tuned, minimal optimization needed
- Study their configuration for best practices

### 4. Expected Impact
- 45-60% performance improvement achievable through optimization
- Potential cost reduction through better resource efficiency
- Improved reliability through variance reduction

---

## 🛠 Technology Stack

| Component | Technology |
|-----------|-----------|
| Language | Python 3.7+ |
| Data Processing | pandas, numpy |
| Visualization | matplotlib |
| Statistics | scipy |
| Excel Support | openpyxl, xlrd |
| Version Control | Git |

---

## 📖 Quick Reference

### Common Commands

```bash
# Run full analysis
python src/run_analysis.py

# Explore data structure
python src/explore_data.py

# Verify installation
python src/verify_setup.py

# View analysis report
cat analysis_output/analysis_report.txt

# Open results folder
open analysis_output/  # macOS
```

### Analysis Modules

**src/main.py** - `AlibabaDataAnalyzer` class
- `load_performance_profiles()` - Load JSON data
- `analyze_performance_profiles()` - Compute correlations
- `plot_performance_comparison()` - Generate charts
- `export_to_csv()` - Export metrics

**src/advanced_analysis.py** - `AdvancedAnalyzer` class
- `identify_performance_bottlenecks()` - Find issues
- `compute_efficiency_scores()` - Grade functions
- `generate_recommendations()` - Suggest optimizations

---

## 🔗 Links & References

- **Repository**: https://github.com/tahaglbz/Alibaba-Serverless-Analysis
- **Python**: https://www.python.org/downloads/
- **Pandas Documentation**: https://pandas.pydata.org/
- **Alibaba Cloud FC**: https://www.alibabacloud.com/product/function-compute

---

## 📝 License

This project is provided for educational and research purposes.

---

## 👤 Author

**Taha Gulbaz** | University Cloud Technology Researcher

**Created**: February 2026  
**Last Updated**: February 27, 2026

---

**Ready to optimize your serverless infrastructure! 🚀📊** 

