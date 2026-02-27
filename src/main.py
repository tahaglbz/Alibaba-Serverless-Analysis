"""
Alibaba Cloud Serverless Performance Analysis
Main analysis script for function compute and workflow logs
"""

import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from datetime import datetime
import warnings

warnings.filterwarnings('ignore')

# Configuration
BASE_PATH = Path(__file__).parent
DATASETS_PATH = BASE_PATH.parent / "data" / "datasets"

class AlibabaDataAnalyzer:
    """Main analyzer for Alibaba Cloud serverless logs"""
    
    def __init__(self):
        self.perf_profiles = {}
        self.function_logs = {}
        self.workflow_logs = {}
        self.analysis_results = {}
        
    def load_performance_profiles(self):
        """Load JSON performance profiles for all functions"""
        print("📂 Loading performance profiles...")
        perf_path = DATASETS_PATH / "aliyunfc_functions_perf_profile_cpu"
        
        for file in sorted(perf_path.glob("f*_perf_profile.json")):
            func_name = file.stem.replace("_perf_profile", "")
            try:
                with open(file, 'r') as f:
                    self.perf_profiles[func_name] = json.load(f)
                print(f"  ✓ Loaded {func_name}")
            except Exception as e:
                print(f"  ✗ Error loading {func_name}: {e}")
    
    def load_function_logs(self):
        """Load Excel files with function invocation logs"""
        print("\n📊 Loading function invocation logs...")
        logs_path = DATASETS_PATH / "aliyunfc_functions_invoke_results_got_by_cloudwatchlog"
        
        # Look for logs in subdirectories
        for folder in logs_path.glob("*"):
            if folder.is_dir():
                for file in folder.glob("*"):
                    if file.suffix in ['.xlsx', '.xls']:
                        try:
                            df = pd.read_excel(file)
                            folder_name = folder.name
                            if folder_name not in self.function_logs:
                                self.function_logs[folder_name] = df
                            print(f"  ✓ Loaded {folder_name} ({len(df)} records)")
                        except Exception as e:
                            print(f"  ✗ Error loading {file.name}: {e}")
    
    def load_workflow_logs(self):
        """Load Excel files with workflow execution logs"""
        print("\n⚙️ Loading workflow execution logs...")
        workflow_path = DATASETS_PATH / "aliyunfc_StateMachine_invoke_results"
        
        for run_folder in sorted(workflow_path.glob("*")):
            if run_folder.is_dir():
                run_num = run_folder.name
                self.workflow_logs[run_num] = {}
                
                for file in run_folder.glob("*"):
                    if file.suffix in ['.xlsx', '.xls']:
                        try:
                            df = pd.read_excel(file)
                            workflow_name = file.stem.replace("aliyunfc_StateMachine_", "").replace("_Logs", "")
                            self.workflow_logs[run_num][workflow_name] = df
                            print(f"  ✓ Loaded Run {run_num}: {workflow_name} ({len(df)} records)")
                        except Exception as e:
                            print(f"  ✗ Error loading {file.name}: {e}")
    
    def analyze_performance_profiles(self):
        """Analyze memory/CPU vs execution time correlations"""
        print("\n🔍 Analyzing performance profiles...")
        results = {}
        
        for func_name, profile in self.perf_profiles.items():
            memory_values = []
            cpu_values = []
            duration_values = []
            
            for config_key, duration_ms in profile.items():
                try:
                    memory, cpu = config_key.split(',')
                    memory_values.append(int(memory))
                    cpu_values.append(float(cpu))
                    duration_values.append(float(duration_ms))
                except:
                    continue
            
            if memory_values:
                results[func_name] = {
                    'avg_duration': np.mean(duration_values),
                    'min_duration': np.min(duration_values),
                    'max_duration': np.max(duration_values),
                    'std_duration': np.std(duration_values),
                    'memory_correlation': np.corrcoef(memory_values, duration_values)[0, 1] if len(set(memory_values)) > 1 else 0,
                    'cpu_correlation': np.corrcoef(cpu_values, duration_values)[0, 1] if len(set(cpu_values)) > 1 else 0,
                    'config_count': len(duration_values)
                }
        
        self.analysis_results['perf_profiles'] = results
        print(f"  ✓ Analyzed {len(results)} functions")
        return results
    
    def analyze_workflow_patterns(self):
        """Analyze workflow execution patterns"""
        print("\n⚙️ Analyzing workflow patterns...")
        results = {}
        
        for run_num, workflows in self.workflow_logs.items():
            results[run_num] = {}
            
            for workflow_name, df in workflows.items():
                if 'Duration' in df.columns:
                    durations = pd.to_numeric(df['Duration'], errors='coerce').dropna()
                    
                    results[run_num][workflow_name] = {
                        'total_executions': len(durations),
                        'avg_duration': durations.mean(),
                        'median_duration': durations.median(),
                        'std_duration': durations.std(),
                        'min_duration': durations.min(),
                        'max_duration': durations.max()
                    }
        
        self.analysis_results['workflow_patterns'] = results
        print(f"  ✓ Analyzed workflow patterns")
        return results
    
    def plot_performance_comparison(self, output_dir="analysis_output"):
        """Create visualization plots"""
        print("\n📈 Creating visualizations...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Plot 1: Average duration by function
        if self.analysis_results.get('perf_profiles'):
            results = self.analysis_results['perf_profiles']
            func_names = list(results.keys())
            avg_durations = [results[f]['avg_duration'] for f in func_names]
            
            plt.figure(figsize=(14, 6))
            plt.bar(func_names, avg_durations, color='steelblue')
            plt.xlabel('Function Name')
            plt.ylabel('Average Duration (ms)')
            plt.title('Average Execution Duration by Function')
            plt.xticks(rotation=45)
            plt.grid(axis='y', alpha=0.3)
            plt.tight_layout()
            plt.savefig(f"{output_dir}/01_function_duration_comparison.png", dpi=300)
            print(f"  ✓ Saved: 01_function_duration_comparison.png")
            plt.close()
        
        # Plot 2: Correlation heatmap
        if self.analysis_results.get('perf_profiles'):
            results = self.analysis_results['perf_profiles']
            memory_corr = [results[f]['memory_correlation'] for f in results.keys()]
            cpu_corr = [results[f]['cpu_correlation'] for f in results.keys()]
            func_names = list(results.keys())
            
            fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
            
            ax1.bar(func_names, memory_corr, color='coral')
            ax1.set_title('Memory vs Execution Time Correlation')
            ax1.set_ylabel('Correlation Coefficient')
            ax1.set_xlabel('Function')
            ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            ax1.set_xticklabels(func_names, rotation=45)
            ax1.grid(axis='y', alpha=0.3)
            
            ax2.bar(func_names, cpu_corr, color='lightgreen')
            ax2.set_title('CPU vs Execution Time Correlation')
            ax2.set_ylabel('Correlation Coefficient')
            ax2.set_xlabel('Function')
            ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
            ax2.set_xticklabels(func_names, rotation=45)
            ax2.grid(axis='y', alpha=0.3)
            
            plt.tight_layout()
            plt.savefig(f"{output_dir}/02_resource_correlation.png", dpi=300)
            print(f"  ✓ Saved: 02_resource_correlation.png")
            plt.close()
    
    def generate_report(self, output_dir="analysis_output"):
        """Generate comprehensive analysis report in Markdown format"""
        print("\n📄 Generating analysis report...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        report_path = f"{output_dir}/analysis_report.md"
        
        with open(report_path, 'w') as f:
            # Header
            f.write("# Alibaba Cloud Serverless Performance Analysis Report\n\n")
            f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            
            # Section 1: Performance Profiles
            f.write("## 1. Function Performance Analysis\n\n")
            if self.analysis_results.get('perf_profiles'):
                f.write("### Performance Metrics by Function\n\n")
                f.write("| Function | Configs | Avg Duration (ms) | Min (ms) | Max (ms) | Std Dev | Memory Corr | CPU Corr |\n")
                f.write("|----------|---------|-------------------|----------|----------|---------|-------------|----------|\n")
                
                for func_name, metrics in sorted(self.analysis_results['perf_profiles'].items()):
                    f.write(f"| **{func_name}** | {metrics['config_count']} | "
                           f"{metrics['avg_duration']:.2f} | {metrics['min_duration']:.2f} | "
                           f"{metrics['max_duration']:.2f} | {metrics['std_duration']:.2f} | "
                           f"{metrics['memory_correlation']:.3f} | {metrics['cpu_correlation']:.3f} |\n")
                
                f.write("\n#### Key Metrics Explanation\n\n")
                f.write("- **Avg Duration**: Mean execution time across all configurations\n")
                f.write("- **Std Dev**: Standard deviation of execution times\n")
                f.write("- **Memory Corr**: Correlation between memory allocation and execution time (-1 to 1)\n")
                f.write("- **CPU Corr**: Correlation between CPU allocation and execution time (-1 to 1)\n")
                f.write("  - **Negative** (<-0.3): More resources = Slower execution (optimization opportunity)\n")
                f.write("  - **Positive** (>0.3): More resources = Faster execution (standard behavior)\n\n")
            
            # Section 2: Workflow Analysis
            f.write("## 2. Workflow Execution Analysis\n\n")
            if self.analysis_results.get('workflow_patterns'):
                for run_num, workflows in sorted(self.analysis_results['workflow_patterns'].items()):
                    f.write(f"### Run {run_num}\n\n")
                    f.write("| Workflow | Executions | Avg Duration (ms) | Median (ms) | Std Dev | Range (ms) |\n")
                    f.write("|----------|------------|-------------------|-------------|---------|------------|\n")
                    
                    for workflow_name, metrics in workflows.items():
                        f.write(f"| **{workflow_name}** | {metrics['total_executions']} | "
                               f"{metrics['avg_duration']:.2f} | {metrics['median_duration']:.2f} | "
                               f"{metrics['std_duration']:.2f} | "
                               f"{metrics['min_duration']:.2f} - {metrics['max_duration']:.2f} |\n")
                    f.write("\n")
            
            # Section 3: Key Findings
            f.write("## 3. Key Findings\n\n")
            f.write(f"- **Total Functions Analyzed**: {len(self.perf_profiles)}\n")
            f.write(f"- **Total Workflow Runs**: {len(self.workflow_logs)}\n")
            f.write("- **Analysis Scope**: Performance profiling, resource correlation analysis\n")
            f.write("- **Key Insight**: Negative correlations in memory/CPU suggest over-provisioning in many functions\n\n")
            
            # Section 4: Summary Statistics
            if self.analysis_results.get('perf_profiles'):
                results = self.analysis_results['perf_profiles']
                durations = [v['avg_duration'] for v in results.values()]
                memory_corrs = [v['memory_correlation'] for v in results.values()]
                cpu_corrs = [v['cpu_correlation'] for v in results.values()]
                
                f.write("## 4. Summary Statistics\n\n")
                f.write(f"- **Average Function Duration**: {np.mean(durations):.2f} ms\n")
                f.write(f"- **Fastest Function**: {min(results, key=lambda x: results[x]['avg_duration'])} "
                       f"({min(durations):.2f} ms)\n")
                f.write(f"- **Slowest Function**: {max(results, key=lambda x: results[x]['avg_duration'])} "
                       f"({max(durations):.2f} ms)\n")
                f.write(f"- **Average Memory Correlation**: {np.mean(memory_corrs):.3f}\n")
                f.write(f"- **Average CPU Correlation**: {np.mean(cpu_corrs):.3f}\n")
                f.write(f"- **Negative Memory Correlations**: {sum(1 for c in memory_corrs if c < -0.3)} functions\n")
                f.write(f"- **Negative CPU Correlations**: {sum(1 for c in cpu_corrs if c < -0.3)} functions\n\n")
        
        print(f"  ✓ Report saved: {report_path}")
        return report_path
    
    def export_to_csv(self, output_dir="analysis_output"):
        """Export analysis results to CSV files"""
        print("\n💾 Exporting results to CSV...")
        
        os.makedirs(output_dir, exist_ok=True)
        
        # Export performance profiles
        if self.analysis_results.get('perf_profiles'):
            df = pd.DataFrame(self.analysis_results['perf_profiles']).T
            csv_path = f"{output_dir}/function_performance_analysis.csv"
            df.to_csv(csv_path)
            print(f"  ✓ Exported: function_performance_analysis.csv")
        
        # Export workflow patterns
        if self.analysis_results.get('workflow_patterns'):
            workflow_data = []
            for run_num, workflows in self.analysis_results['workflow_patterns'].items():
                for workflow_name, metrics in workflows.items():
                    row = {'Run': run_num, 'Workflow': workflow_name, **metrics}
                    workflow_data.append(row)
            
            df = pd.DataFrame(workflow_data)
            csv_path = f"{output_dir}/workflow_execution_analysis.csv"
            df.to_csv(csv_path, index=False)
            print(f"  ✓ Exported: workflow_execution_analysis.csv")
    
    def run_full_analysis(self):
        """Execute complete analysis pipeline"""
        print("\n" + "="*70)
        print("🚀 STARTING ALIBABA CLOUD SERVERLESS ANALYSIS")
        print("="*70)
        
        try:
            # Load all data
            self.load_performance_profiles()
            self.load_function_logs()
            self.load_workflow_logs()
            
            # Perform analysis
            self.analyze_performance_profiles()
            self.analyze_workflow_patterns()
            
            # Generate outputs
            self.plot_performance_comparison()
            self.generate_report()
            self.export_to_csv()
            
            print("\n" + "="*70)
            print("✅ ANALYSIS COMPLETE!")
            print("="*70)
            print("\nOutput files saved in: analysis_output/")
            
        except Exception as e:
            print(f"\n❌ Error during analysis: {e}")
            raise


if __name__ == "__main__":
    analyzer = AlibabaDataAnalyzer()
    analyzer.run_full_analysis()
