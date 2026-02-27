#!/usr/bin/env python3
"""
Project Verification Script
Checks if everything is set up correctly before running full analysis
"""

import sys
from pathlib import Path


def check_python_version():
    """Check if Python version is 3.7+"""
    print("\n✅ Checking Python version...")
    version = sys.version_info
    print(f"   Python {version.major}.{version.minor}.{version.micro}")
    
    if version.major >= 3 and version.minor >= 7:
        print("   ✓ Python version is adequate")
        return True
    else:
        print("   ✗ Please upgrade to Python 3.7 or higher")
        return False


def check_required_packages():
    """Check if all required packages are installed"""
    print("\n✅ Checking required packages...")
    
    required = {
        'pandas': 'Data manipulation',
        'numpy': 'Numerical computing',
        'matplotlib': 'Plotting and visualization',
        'openpyxl': 'Excel file reading'
    }
    
    missing = []
    for package, description in required.items():
        try:
            __import__(package)
            print(f"   ✓ {package:15s} - {description}")
        except ImportError:
            print(f"   ✗ {package:15s} - MISSING!")
            missing.append(package)
    
    if missing:
        print(f"\n   Run: pip install {' '.join(missing)}")
        return False
    
    return True


def check_data_files():
    """Check if all data files are present"""
    print("\n✅ Checking data files...")
    
    datasets_path = Path("datasets")
    
    if not datasets_path.exists():
        print(f"   ✗ datasets/ folder not found")
        return False
    
    # Check subdirectories
    subdirs = {
        'aliyunfc_functions_perf_profile_cpu': 'Performance profiles',
        'aliyunfc_functions_invoke_results_got_by_cloudwatchlog': 'Function logs',
        'aliyunfc_StateMachine_invoke_results': 'Workflow logs'
    }
    
    for subdir, description in subdirs.items():
        path = datasets_path / subdir
        if path.exists():
            file_count = len(list(path.glob("*"))) + len(list(path.glob("*/*")))
            print(f"   ✓ {subdir}")
            print(f"      {description} - {file_count} files found")
        else:
            print(f"   ✗ {subdir} - NOT FOUND")
            return False
    
    return True


def check_project_files():
    """Check if all project files are created"""
    print("\n✅ Checking project Python files...")
    
    required_files = {
        'main.py': 'Main analysis module',
        'advanced_analysis.py': 'Advanced analytics',
        'run_analysis.py': 'Integrated pipeline',
        'explore_data.py': 'Data exploration utility',
        'requirements.txt': 'Dependencies file'
    }
    
    for filename, description in required_files.items():
        path = Path(filename)
        if path.exists():
            size = path.stat().st_size
            print(f"   ✓ {filename:25s} - {description} ({size} bytes)")
        else:
            print(f"   ✗ {filename:25s} - NOT FOUND")
            return False
    
    return True


def check_documentation():
    """Check if documentation files are present"""
    print("\n✅ Checking documentation files...")
    
    docs = {
        'README.md': 'Project readme',
        'SETUP_GUIDE.md': 'Setup guide',
        'QUICKSTART.md': 'Quick start',
        'PROJECT_DOCUMENTATION.md': 'Full documentation',
        'COMPLETION_CHECKLIST.md': 'Completion checklist',
        'PROJECT_SUMMARY.md': 'Project summary'
    }
    
    found = 0
    for filename, description in docs.items():
        path = Path(filename)
        if path.exists():
            print(f"   ✓ {filename:30s} - {description}")
            found += 1
        else:
            print(f"   ✗ {filename:30s} - NOT FOUND")
    
    return found >= 3  # At least 3 documentation files


def check_write_permissions():
    """Check if we can write to the output directory"""
    print("\n✅ Checking write permissions...")
    
    output_dir = Path("analysis_output")
    output_dir.mkdir(exist_ok=True)
    
    test_file = output_dir / ".test_write"
    try:
        test_file.write_text("test")
        test_file.unlink()
        print("   ✓ Can write to analysis_output/ directory")
        return True
    except:
        print("   ✗ Cannot write to analysis_output/ directory")
        return False


def run_quick_data_test():
    """Try to load a small sample of data"""
    print("\n✅ Attempting to load sample data...")
    
    try:
        import json
        import pandas as pd
        
        # Test JSON loading
        perf_path = Path("datasets/aliyunfc_functions_perf_profile_cpu/f1_perf_profile.json")
        if perf_path.exists():
            with open(perf_path, 'r') as f:
                data = json.load(f)
            print(f"   ✓ Successfully loaded f1_perf_profile.json ({len(data)} configurations)")
        
        # Test Excel loading
        logs_path = Path("datasets/aliyunfc_functions_invoke_results_got_by_cloudwatchlog")
        excel_files = list(logs_path.glob("*/gsh.py"))
        if not excel_files:
            # Try looking for actual Excel files
            excel_files = list(logs_path.rglob("*.xlsx")) + list(logs_path.rglob("*.xls"))
        
        if excel_files:
            print(f"   ✓ Found Excel files: {len(excel_files)} files ready to read")
        
        return True
    except Exception as e:
        print(f"   ✗ Error loading data: {e}")
        return False


def print_summary(results):
    """Print verification summary"""
    print("\n" + "="*70)
    print("📋 VERIFICATION SUMMARY")
    print("="*70)
    
    total_checks = len(results)
    passed_checks = sum(1 for v in results.values() if v)
    
    print(f"\nPassed: {passed_checks}/{total_checks} checks")
    
    if passed_checks == total_checks:
        print("\n✅ ALL CHECKS PASSED! You're ready to go!")
        print("\nNext steps:")
        print("   1. Run: python run_analysis.py")
        print("   2. Wait for analysis to complete (~1 minute)")
        print("   3. Check: analysis_output/ directory for results")
        print("   4. Read: analysis_output/analysis_report.txt")
        return True
    else:
        print("\n⚠️  Some checks failed. See details above.")
        print("\nFix the issues and run this script again:")
        print("   python verify_setup.py")
        return False


def main():
    """Run all verification checks"""
    print("\n" + "="*70)
    print("🔍 PROJECT VERIFICATION SCRIPT")
    print("="*70)
    
    results = {
        'Python Version': check_python_version(),
        'Required Packages': check_required_packages(),
        'Data Files': check_data_files(),
        'Project Files': check_project_files(),
        'Documentation': check_documentation(),
        'Write Permissions': check_write_permissions(),
        'Data Sample': run_quick_data_test(),
    }
    
    success = print_summary(results)
    
    print("\n" + "="*70)
    
    return success


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
