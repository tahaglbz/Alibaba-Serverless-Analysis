# 🚀 Alibaba Cloud Serverless Analysis - Setup Guide

## Prerequisites

- Python 3.7 or higher installed
- pip or conda package manager
- macOS / Windows / Linux

## Installation Steps

### 1️⃣ Create Virtual Environment (Optional but Recommended)

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Analysis

```bash
python main.py
```

## Expected Output

The script will create an `analysis_output/` directory containing:

```
analysis_output/
├── analysis_report.txt                    # Comprehensive analysis report
├── function_performance_analysis.csv      # Performance metrics by function
├── workflow_execution_analysis.csv        # Workflow execution statistics
├── 01_function_duration_comparison.png    # Bar chart of function durations
└── 02_resource_correlation.png            # Memory/CPU correlation analysis
```

## What Each Output Contains

### 📊 Analysis Report
- Summary of all 21 functions analyzed
- Average, min, max execution times
- Memory and CPU correlation coefficients
- Workflow execution patterns
- Key performance indicators

### 📈 Performance CSV
| Column | Description |
|--------|-------------|
| avg_duration | Average execution time in milliseconds |
| min_duration | Minimum execution time observed |
| max_duration | Maximum execution time observed |
| std_duration | Standard deviation of execution times |
| memory_correlation | Correlation between memory and performance (-1 to 1) |
| cpu_correlation | Correlation between CPU and performance (-1 to 1) |
| config_count | Number of memory/CPU configurations tested |

### ⚙️ Workflow CSV
| Column | Description |
|--------|-------------|
| Run | Run number (1, 2, or 3) |
| Workflow | Workflow identifier (NEW10, NEW16, NEW21) |
| total_executions | Number of executions in this run |
| avg_duration | Average workflow execution time |
| median_duration | Median workflow execution time |
| std_duration | Standard deviation |
| min_duration | Minimum duration observed |
| max_duration | Maximum duration observed |

### 🎨 Visualizations
- **Function Duration Comparison**: Bar chart showing average execution time for each function
- **Resource Correlation**: Analyzes how memory and CPU allocations affect performance

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'pandas'"
**Solution:** Make sure to activate virtual environment and install requirements
```bash
source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
```

### Issue: "No such file or directory"
**Solution:** Ensure you're running the script from the project root directory
```bash
cd /Users/tahagulbaz/Desktop/4.\ sınıf\ eng/cloud/miniproject1/
python main.py
```

### Issue: "Unable to read Excel file"
**Solution:** Excel files might be corrupted. Try:
- Check file permissions
- Re-download datasets
- Ensure no files are open in Excel

## Next Steps

After running the analysis:

1. **Review the report** in `analysis_output/analysis_report.txt`
2. **Examine visualizations** (PNG files)
3. **Use CSV data** for further analysis in Excel or Python
4. **Modify code** for additional analysis (e.g., filtering by specific functions)

## Customization Examples

### Analyze only specific functions:
Edit `main.py` and modify the analysis methods to filter functions

### Change output directory:
```python
analyzer.run_full_analysis("custom_output_path")
```

### Generate additional plots:
Add custom visualization methods to the `AlibabaDataAnalyzer` class

## Questions or Issues?

Refer to the README.md for dataset structure and documentation.
