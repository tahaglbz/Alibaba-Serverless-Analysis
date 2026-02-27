#!/usr/bin/env python3
"""
Integrated Alibaba Cloud Serverless Analysis Pipeline
Combines basic analysis with advanced insights and recommendations
"""

import sys
from pathlib import Path

# Add project root to path
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT))

from main import AlibabaDataAnalyzer
from advanced_analysis import AdvancedAnalyzer


def run_complete_analysis():
    """Execute complete analysis pipeline with all features"""
    
    print("\n" + "="*70)
    print("🚀 ALIBABA CLOUD SERVERLESS PERFORMANCE ANALYSIS")
    print("Complete Analysis Pipeline")
    print("="*70)
    
    try:
        # ==================== STEP 1: BASIC ANALYSIS ====================
        print("\n[Step 1/2] Running basic analysis...")
        analyzer = AlibabaDataAnalyzer()
        
        # Load all datasets
        analyzer.load_performance_profiles()
        analyzer.load_function_logs()
        analyzer.load_workflow_logs()
        
        # Perform basic analysis
        analyzer.analyze_performance_profiles()
        analyzer.analyze_workflow_patterns()
        
        # Generate basic outputs
        analyzer.plot_performance_comparison()
        analyzer.generate_report()
        analyzer.export_to_csv()
        
        print("\n✅ Basic analysis complete!")
        
        # ==================== STEP 2: ADVANCED ANALYSIS ====================
        print("\n[Step 2/2] Running advanced analysis...")
        advanced = AdvancedAnalyzer(analyzer)
        advanced.run_all_advanced_analysis()
        
        print("\n✅ Advanced analysis complete!")
        
        # ==================== SUMMARY ====================
        print("\n" + "="*70)
        print("📊 ANALYSIS COMPLETE - SUMMARY")
        print("="*70)
        
        perf_results = analyzer.analysis_results.get('perf_profiles', {})
        workflow_results = analyzer.analysis_results.get('workflow_patterns', {})
        
        print(f"\n📈 Functions Analyzed: {len(perf_results)}")
        print(f"📊 Workflow Runs: {len(workflow_results)}")
        
        if perf_results:
            avg_durations = [v['avg_duration'] for v in perf_results.values()]
            print(f"⏱️  Average Function Duration: {sum(avg_durations)/len(avg_durations):.2f}ms")
        
        print("\n📁 Output Files Generated:")
        print("   analysis_output/")
        print("   ├── analysis_report.txt")
        print("   ├── advanced_analysis_report.txt")
        print("   ├── function_performance_analysis.csv")
        print("   ├── workflow_execution_analysis.csv")
        print("   ├── 01_function_duration_comparison.png")
        print("   └── 02_resource_correlation.png")
        
        print("\n💡 Next Steps:")
        print("   1. Review analysis_report.txt for detailed metrics")
        print("   2. Check advanced_analysis_report.txt for optimization recommendations")
        print("   3. Examine PNG files for visual insights")
        print("   4. Use CSV files for further analysis or reports")
        
        print("\n" + "="*70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_complete_analysis()
    sys.exit(0 if success else 1)
