#!/usr/bin/env python3
"""
Data Exploration Utility
Quick overview of data structure and quality
"""

import json
import pandas as pd
from pathlib import Path


def explore_performance_profiles():
    """Quick overview of JSON performance profiles"""
    print("\n" + "="*70)
    print("📊 PERFORMANCE PROFILES EXPLORATION")
    print("="*70)
    
    perf_path = Path("datasets/aliyunfc_functions_perf_profile_cpu")
    files = sorted(perf_path.glob("f*_perf_profile.json"))
    
    print(f"\n📁 Found {len(files)} function profile files")
    
    for file in files[:3]:  # Show first 3 as examples
        print(f"\n📄 {file.name}")
        with open(file, 'r') as f:
            data = json.load(f)
        
        print(f"   Configurations: {len(data)}")
        print(f"   Sample configs:")
        for i, (config, duration) in enumerate(list(data.items())[:3]):
            print(f"      {config} → {duration}ms")
        if len(data) > 3:
            print(f"      ... and {len(data)-3} more")


def explore_function_logs():
    """Quick overview of function invocation logs"""
    print("\n" + "="*70)
    print("📊 FUNCTION INVOCATION LOGS EXPLORATION")
    print("="*70)
    
    logs_path = Path("datasets/aliyunfc_functions_invoke_results_got_by_cloudwatchlog")
    
    for folder in sorted(logs_path.glob("*")):
        if folder.is_dir():
            files = list(folder.glob("*"))
            print(f"\n📁 {folder.name}: {len(files)} files")
            
            for file in files[:1]:  # Show first file details
                try:
                    if file.suffix in ['.xlsx', '.xls']:
                        df = pd.read_excel(file)
                        print(f"\n   File: {file.name}")
                        print(f"   Rows: {len(df)}")
                        print(f"   Columns: {list(df.columns)}")
                        print(f"\n   Sample data:")
                        print(f"   {df.head(2).to_string()}")
                except Exception as e:
                    print(f"   Error reading {file.name}: {e}")


def explore_workflow_logs():
    """Quick overview of workflow execution logs"""
    print("\n" + "="*70)
    print("⚙️  WORKFLOW EXECUTION LOGS EXPLORATION")
    print("="*70)
    
    workflow_path = Path("datasets/aliyunfc_StateMachine_invoke_results")
    
    for run_folder in sorted(workflow_path.glob("*")):
        if run_folder.is_dir():
            files = list(run_folder.glob("*"))
            print(f"\n📁 Run {run_folder.name}: {len(files)} workflow files")
            
            for file in files[:1]:  # Show first file details
                try:
                    if file.suffix in ['.xlsx', '.xls']:
                        df = pd.read_excel(file)
                        print(f"\n   File: {file.name}")
                        print(f"   Rows: {len(df)}")
                        print(f"   Columns: {list(df.columns)}")
                        if 'Duration' in df.columns:
                            durations = pd.to_numeric(df['Duration'], errors='coerce').dropna()
                            print(f"   Duration Stats (ms):")
                            print(f"      Min: {durations.min():.2f}")
                            print(f"      Max: {durations.max():.2f}")
                            print(f"      Avg: {durations.mean():.2f}")
                except Exception as e:
                    print(f"   Error reading {file.name}: {e}")


def print_data_summary():
    """Print overall data summary"""
    print("\n" + "="*70)
    print("📈 DATA SUMMARY")
    print("="*70)
    
    perf_path = Path("datasets/aliyunfc_functions_perf_profile_cpu")
    num_functions = len(list(perf_path.glob("f*_perf_profile.json")))
    
    print(f"\n✅ Functions to analyze: {num_functions}")
    print(f"✅ Performance profiles: JSON files")
    print(f"✅ Function logs: Excel files (.xls/.xlsx)")
    print(f"✅ Workflow logs: 3 runs × multiple workflows")
    
    print(f"\n💡 What you can do with this data:")
    print(f"   1. Compare performance across 21 functions")
    print(f"   2. Analyze memory/CPU impact on performance")
    print(f"   3. Study workflow execution patterns")
    print(f"   4. Find performance bottlenecks")
    print(f"   5. Recommend resource optimization")


def run_exploration():
    """Run complete data exploration"""
    print("\n🔍 Starting Data Exploration...\n")
    
    try:
        explore_performance_profiles()
        explore_function_logs()
        explore_workflow_logs()
        print_data_summary()
        
        print("\n" + "="*70)
        print("✅ EXPLORATION COMPLETE")
        print("="*70)
        print("\n📝 Next steps:")
        print("   1. Run 'python run_analysis.py' for full analysis")
        print("   2. Check 'analysis_output/' for results")
        print("   3. Read PROJECT_DOCUMENTATION.md for detailed info")
        
    except Exception as e:
        print(f"\n❌ Error during exploration: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    run_exploration()
