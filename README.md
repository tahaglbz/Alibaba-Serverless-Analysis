# Alibaba Cloud Serverless Performance Analysis

**Professional performance analysis suite for Alibaba Cloud Function Compute (FC) and CloudFlow serverless workloads**

[![Python 3.7+](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Project Description

This project provides a comprehensive performance analysis framework for Alibaba Cloud serverless workloads. The analysis examines **21 serverless functions** across **1,206+ configurations** per function, revealing critical insights into resource allocation strategies, performance bottlenecks, and optimization opportunities.

### Key Scope
- **Functions Analyzed**: 21 (f1 through f21)
- **Configurations Tested**: 1,206+ per function (memory/CPU combinations)
- **Workflows Examined**: 3 different CloudFlow workflows (10, 16, and 21 functions)
- **Total Data Points**: 25,000+
- **Analysis Period**: Complete production traces

---

## 🔬 Analysis Results Summary

### Efficiency Rankings (A-F Scale)

#### Top Performers
| Function | Score | Status | Avg Duration |
|----------|-------|--------|--------------|
| f5 | 87.7/100 | ✅ A - Excellent | 298ms |
| f17 | 85.5/100 | ✅ B - Good | 292ms |
| f7 | 83.5/100 | ✅ B - Good | 365ms |

#### Bottom Performers (Critical Issues)
| Function | Score | Status | Issue |
|----------|-------|--------|-------|
| f16 | 6.0/100 | 🔴 F - Critical | Extreme variance (σ=3,133ms) |
| f1 | 13.9/100 | 🔴 F - Critical | Slowest (3,102ms avg) |
| f11 | 21.7/100 | 🔴 F - Critical | High latency (2,871ms avg) |
| f15 | 25.6/100 | 🔴 F - Critical | High latency (2,747ms avg) |

### Memory-Performance Paradox (📊 Key Finding)

**Critical Discovery: 19 out of 21 functions show NEGATIVE correlation between memory allocation and execution time**

```
Memory Correlation Analysis:
├── Negative correlation (-0.38 to -0.69): 19 functions
│   → More memory = SLOWER execution
│   → Potential 45-60% improvement by REDUCING memory
├── Neutral correlation (-0.01 to +0.03): 1 function (f20)
└── Positive correlation: 1 function (f5)
    → More memory = faster execution

CPU Correlation:
├── Similar negative pattern: 19 functions (-0.30 to -0.64)
└── Indicates resource optimization misconfiguration
```

### Performance Metrics

- **Average Function Duration**: 1,057.45ms
- **Fastest Function**: f17 (292ms)
- **Slowest Function**: f1 (3,102ms) - **10.6x slower than f17**
- **Highest Variance**: f16 (σ=3,133ms) - Extremely unpredictable
- **Performance Range**: 6.0 to 87.7 efficiency score (14.6x difference)

---

## 📂 Repository Structure

```
Alibaba-Serverless-Analysis/
│
├── README.md                    # Project documentation (this file)
├── .gitignore                   # Git ignore rules
│
├── src/                         # Python analysis source code
│   ├── run_analysis.py         # Main entry point - run this to start analysis
│   ├── main.py                 # Core AlibabaDataAnalyzer class
│   ├── advanced_analysis.py    # Advanced analytics (bottleneck, grades, recommendations)
│   ├── explore_data.py         # Data exploration utility
│   ├── verify_setup.py         # Setup verification script
│   └── requirements.txt        # Python dependencies (pandas, numpy, matplotlib, etc.)
│
├── data/                        # Original datasets (not in repo, local only)
│   └── aliyunfc_*/              # Alibaba Cloud FC data files
│       ├── functions_perf_profile_cpu/      # JSON performance profiles
│       ├── functions_invoke_results/        # Excel function logs
│       └── StateMachine_invoke_results/     # Excel workflow logs
│
└── analysis_output/             # Analysis results (auto-generated)
    ├── analysis_report.txt           # Detailed metrics for all 21 functions
    ├── advanced_analysis_report.txt  # Efficiency rankings & optimization recommendations
    ├── function_performance_analysis.csv      # All metrics in CSV format
    ├── workflow_execution_analysis.csv        # Workflow execution statistics
    ├── 01_function_duration_comparison.png    # Performance visualization chart
    └── 02_resource_correlation.png            # Memory/CPU correlation analysis chart
```

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

