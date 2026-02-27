# Alibaba Cloud Serverless Performance Analysis Report

**Generated:** 2026-02-27 14:23:00

---

## 1. Function Performance Analysis

### Performance Metrics by Function

| Function | Configs | Avg Duration (ms) | Min (ms) | Max (ms) | Std Dev | Memory Corr | CPU Corr |
|----------|---------|-------------------|----------|----------|---------|-------------|----------|
| **f1** | 1206 | 3102.51 | 2339.00 | 12798.00 | 943.77 | -0.378 | -0.299 |
| **f10** | 1206 | 997.54 | 623.00 | 5851.00 | 612.26 | -0.552 | -0.504 |
| **f11** | 1206 | 2871.26 | 1908.00 | 9517.00 | 657.48 | -0.176 | -0.161 |
| **f12** | 1206 | 487.71 | 253.00 | 3295.00 | 335.87 | -0.585 | -0.544 |
| **f13** | 1206 | 682.75 | 486.00 | 3678.00 | 390.40 | -0.551 | -0.500 |
| **f14** | 1206 | 575.73 | 291.00 | 3317.00 | 357.25 | -0.548 | -0.498 |
| **f15** | 1206 | 2747.23 | 1909.00 | 8334.00 | 553.77 | -0.423 | -0.352 |
| **f16** | 1206 | 2880.86 | 765.00 | 27224.00 | 3133.73 | -0.692 | -0.636 |
| **f17** | 1206 | 292.26 | 207.00 | 1611.00 | 161.83 | -0.527 | -0.472 |
| **f18** | 1206 | 476.70 | 251.00 | 3165.00 | 295.26 | -0.534 | -0.482 |
| **f19** | 1206 | 999.12 | 700.00 | 5548.00 | 592.84 | -0.553 | -0.503 |
| **f2** | 1206 | 524.43 | 401.00 | 2938.00 | 302.86 | -0.545 | -0.493 |
| **f20** | 1206 | 1861.01 | 1317.00 | 5067.00 | 336.87 | 0.029 | 0.012 |
| **f21** | 1206 | 516.14 | 393.00 | 2897.00 | 302.00 | -0.545 | -0.493 |
| **f3** | 1206 | 742.90 | 459.00 | 4420.00 | 457.34 | -0.548 | -0.497 |
| **f4** | 1206 | 499.01 | 276.00 | 3384.00 | 317.93 | -0.564 | -0.528 |
| **f5** | 1206 | 165.73 | 75.00 | 964.00 | 101.57 | -0.477 | -0.429 |
| **f6** | 1206 | 416.28 | 294.00 | 2362.00 | 237.12 | -0.543 | -0.492 |
| **f7** | 1206 | 358.72 | 257.00 | 1942.00 | 200.76 | -0.544 | -0.491 |
| **f8** | 1206 | 427.02 | 231.00 | 2458.00 | 254.03 | -0.546 | -0.495 |
| **f9** | 1206 | 581.48 | 447.00 | 3142.00 | 330.54 | -0.545 | -0.496 |

#### Key Metrics Explanation

- **Avg Duration**: Mean execution time across all configurations
- **Std Dev**: Standard deviation of execution times
- **Memory Corr**: Correlation between memory allocation and execution time (-1 to 1)
- **CPU Corr**: Correlation between CPU allocation and execution time (-1 to 1)
  - **Negative** (<-0.3): More resources = Slower execution (optimization opportunity)
  - **Positive** (>0.3): More resources = Faster execution (standard behavior)

## 2. Workflow Execution Analysis

### Run 1

| Workflow | Executions | Avg Duration (ms) | Median (ms) | Std Dev | Range (ms) |
|----------|------------|-------------------|-------------|---------|------------|

### Run 2

| Workflow | Executions | Avg Duration (ms) | Median (ms) | Std Dev | Range (ms) |
|----------|------------|-------------------|-------------|---------|------------|

### Run 3

| Workflow | Executions | Avg Duration (ms) | Median (ms) | Std Dev | Range (ms) |
|----------|------------|-------------------|-------------|---------|------------|

## 3. Key Findings

- **Total Functions Analyzed**: 21
- **Total Workflow Runs**: 3
- **Analysis Scope**: Performance profiling, resource correlation analysis
- **Key Insight**: Negative correlations in memory/CPU suggest over-provisioning in many functions

## 4. Summary Statistics

- **Average Function Duration**: 1057.45 ms
- **Fastest Function**: f5 (165.73 ms)
- **Slowest Function**: f1 (3102.51 ms)
- **Average Memory Correlation**: -0.493
- **Average CPU Correlation**: -0.445
- **Negative Memory Correlations**: 19 functions
- **Negative CPU Correlations**: 18 functions

