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
from ml_analysis import AcademicMLComparison


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
        print("\n[Step 2/3] Running advanced analysis...")
        advanced = AdvancedAnalyzer(analyzer)
        advanced.run_all_advanced_analysis()
        
        print("\n✅ Advanced analysis complete!")
        
        # ==================== STEP 3: MACHINE LEARNING ANALYSIS ====================
        print("\n[Step 3/3] Running academic machine learning analysis...")
        ml_analyzer = AcademicMLComparison()
        ml_success = ml_analyzer.run_complete_pipeline()
        
        if ml_success:
            print("\n✅ Academic ML analysis complete!")
        else:
            print("\n⚠️  ML analysis encountered issues but continuing...")
        
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
        print("   ├── analysis_report.md")
        print("   ├── advanced_analysis_report.md")
        print("   ├── ml_academic_results.md")
        print("   ├── function_performance_analysis.csv")
        print("   ├── workflow_execution_analysis.csv")
        print("   ├── 01_function_duration_comparison.png")
        print("   ├── 02_resource_correlation.png")
        print("   └── plots/")
        print("       ├── 00_models_comparison.png")
        print("       ├── 01_model_logistic_regression.png")
        print("       ├── 02_model_random_forest.png")
        print("       ├── 03_model_svm.png")
        print("       ├── 04_model_gradient_boosting.png")
        print("       ├── 05_model_neural_network.png")
        print("       └── 06_roc_curves_overlay.png")
        
        print("\n💡 Next Steps:")
        print("   1. Review analysis_report.md for detailed metrics")
        print("   2. Check advanced_analysis_report.md for optimization recommendations")
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
