"""
Advanced Analysis Module
Provides deeper insights and recommendations for serverless optimization
"""

import pandas as pd
import numpy as np
from pathlib import Path
import json


class AdvancedAnalyzer:
    """Advanced analytics for Alibaba Cloud performance data"""
    
    def __init__(self, base_analyzer):
        self.analyzer = base_analyzer
        self.insights = {}
    
    def identify_performance_bottlenecks(self):
        """Identify functions with performance issues"""
        print("\n🔴 Identifying Performance Bottlenecks...")
        
        insights = {
            'slow_functions': [],
            'high_variance': [],
            'resource_sensitive': []
        }
        
        if not self.analyzer.analysis_results.get('perf_profiles'):
            return insights
        
        results = self.analyzer.analysis_results['perf_profiles']
        avg_durations = [v['avg_duration'] for v in results.values()]
        overall_avg = np.mean(avg_durations)
        overall_std = np.std(avg_durations)
        
        # Identify slow functions (> avg + 1 std)
        threshold_slow = overall_avg + overall_std
        for func_name, metrics in results.items():
            if metrics['avg_duration'] > threshold_slow:
                insights['slow_functions'].append({
                    'function': func_name,
                    'duration': metrics['avg_duration'],
                    'severity': 'HIGH' if metrics['avg_duration'] > overall_avg + 2*overall_std else 'MEDIUM'
                })
        
        # Identify high variance functions
        std_devs = [v['std_duration'] for v in results.values()]
        std_threshold = np.mean(std_devs) + np.std(std_devs)
        for func_name, metrics in results.items():
            if metrics['std_duration'] > std_threshold:
                insights['high_variance'].append({
                    'function': func_name,
                    'std_deviation': metrics['std_duration'],
                    'issue': 'Inconsistent performance'
                })
        
        # Identify resource-sensitive functions
        for func_name, metrics in results.items():
            memory_corr = abs(metrics['memory_correlation'])
            cpu_corr = abs(metrics['cpu_correlation'])
            if memory_corr > 0.7 or cpu_corr > 0.7:
                insights['resource_sensitive'].append({
                    'function': func_name,
                    'memory_sensitivity': memory_corr,
                    'cpu_sensitivity': cpu_corr,
                    'recommendation': 'Optimize memory/CPU allocation for this function'
                })
        
        self.insights['bottlenecks'] = insights
        self._print_bottlenecks(insights)
        return insights
    
    def _print_bottlenecks(self, insights):
        """Pretty print bottleneck analysis"""
        if insights['slow_functions']:
            print("\n  ⚠️  SLOW FUNCTIONS:")
            for item in sorted(insights['slow_functions'], key=lambda x: x['duration'], reverse=True):
                print(f"     {item['function']}: {item['duration']:.2f}ms [{item['severity']}]")
        
        if insights['high_variance']:
            print("\n  📊 HIGH VARIANCE FUNCTIONS:")
            for item in sorted(insights['high_variance'], key=lambda x: x['std_deviation'], reverse=True)[:5]:
                print(f"     {item['function']}: σ={item['std_deviation']:.2f}ms")
        
        if insights['resource_sensitive']:
            print("\n  💾 RESOURCE-SENSITIVE FUNCTIONS:")
            for item in sorted(insights['resource_sensitive'], 
                             key=lambda x: max(x['memory_sensitivity'], x['cpu_sensitivity']), 
                             reverse=True)[:5]:
                print(f"     {item['function']}: Mem={item['memory_sensitivity']:.3f}, CPU={item['cpu_sensitivity']:.3f}")
    
    def compute_efficiency_scores(self):
        """Calculate efficiency scores for each function"""
        print("\n📊 Computing Efficiency Scores...")
        
        if not self.analyzer.analysis_results.get('perf_profiles'):
            return {}
        
        results = self.analyzer.analysis_results['perf_profiles']
        efficiency_scores = {}
        
        durations = [v['avg_duration'] for v in results.values()]
        min_duration = min(durations)
        max_duration = max(durations)
        
        for func_name, metrics in results.items():
            # Normalize score 0-100 (lower duration = higher score)
            speed_score = 100 - ((metrics['avg_duration'] - min_duration) / 
                                (max_duration - min_duration) * 100)
            
            # Consistency score (lower std = higher consistency)
            consistency_score = 100 - (min(metrics['std_duration'] / metrics['avg_duration'], 1) * 100)
            
            # Overall efficiency score (80% speed, 20% consistency)
            overall_score = (speed_score * 0.8) + (consistency_score * 0.2)
            
            efficiency_scores[func_name] = {
                'overall_score': overall_score,
                'speed_score': speed_score,
                'consistency_score': consistency_score,
                'grade': self._get_grade(overall_score)
            }
        
        self.insights['efficiency'] = efficiency_scores
        self._print_efficiency_scores(efficiency_scores)
        return efficiency_scores
    
    def _get_grade(self, score):
        """Convert score to letter grade"""
        if score >= 90:
            return 'A (Excellent)'
        elif score >= 80:
            return 'B (Good)'
        elif score >= 70:
            return 'C (Average)'
        elif score >= 60:
            return 'D (Below Average)'
        else:
            return 'F (Poor)'
    
    def _print_efficiency_scores(self, scores):
        """Pretty print efficiency scores"""
        sorted_scores = sorted(scores.items(), key=lambda x: x[1]['overall_score'], reverse=True)
        print("\n  📈 TOP 5 MOST EFFICIENT FUNCTIONS:")
        for func_name, score in sorted_scores[:5]:
            print(f"     {func_name}: {score['overall_score']:.1f}/100 [{score['grade']}]")
        
        print("\n  📈 TOP 5 LEAST EFFICIENT FUNCTIONS:")
        for func_name, score in sorted_scores[-5:]:
            print(f"     {func_name}: {score['overall_score']:.1f}/100 [{score['grade']}]")
    
    def generate_recommendations(self):
        """Generate optimization recommendations"""
        print("\n💡 Generating Optimization Recommendations...")
        
        recommendations = {
            'memory_optimization': [],
            'cpu_optimization': [],
            'general_optimization': []
        }
        
        if not self.analyzer.analysis_results.get('perf_profiles'):
            return recommendations
        
        results = self.analyzer.analysis_results['perf_profiles']
        
        for func_name, metrics in results.items():
            # Memory optimization
            if metrics['memory_correlation'] < -0.3:  # Negative correlation: less memory = faster
                recommendations['memory_optimization'].append({
                    'function': func_name,
                    'action': 'REDUCE memory allocation',
                    'reason': 'Negative correlation detected',
                    'potential_savings': 'Medium'
                })
            elif metrics['memory_correlation'] > 0.7:  # Strong positive: more memory = faster
                recommendations['memory_optimization'].append({
                    'function': func_name,
                    'action': 'INCREASE memory allocation',
                    'reason': 'Strong positive correlation with performance',
                    'potential_gain': 'High'
                })
            
            # CPU optimization
            if metrics['cpu_correlation'] > 0.7:
                recommendations['cpu_optimization'].append({
                    'function': func_name,
                    'action': 'INCREASE CPU allocation',
                    'reason': 'Strong CPU dependency detected',
                    'potential_gain': 'High'
                })
            
            # General optimization
            if metrics['std_duration'] / metrics['avg_duration'] > 0.3:  # High variance
                recommendations['general_optimization'].append({
                    'function': func_name,
                    'action': 'INVESTIGATE inconsistency',
                    'reason': f'High variance ({metrics["std_duration"]/metrics["avg_duration"]:.1%})',
                    'priority': 'Medium'
                })
        
        self.insights['recommendations'] = recommendations
        self._print_recommendations(recommendations)
        return recommendations
    
    def _print_recommendations(self, recommendations):
        """Pretty print recommendations"""
        if recommendations['memory_optimization']:
            print("\n  💾 MEMORY OPTIMIZATION:")
            for rec in recommendations['memory_optimization'][:5]:
                print(f"     {rec['function']}: {rec['action']} - {rec['reason']}")
        
        if recommendations['cpu_optimization']:
            print("\n  ⚙️  CPU OPTIMIZATION:")
            for rec in recommendations['cpu_optimization'][:5]:
                print(f"     {rec['function']}: {rec['action']} - {rec['reason']}")
        
        if recommendations['general_optimization']:
            print("\n  🔧 GENERAL OPTIMIZATION:")
            for rec in recommendations['general_optimization'][:5]:
                print(f"     {rec['function']}: {rec['action']}")
    
    def save_advanced_report(self, output_dir="analysis_output"):
        """Save detailed advanced analysis report"""
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        report_path = f"{output_dir}/advanced_analysis_report.txt"
        
        with open(report_path, 'w') as f:
            f.write("="*70 + "\n")
            f.write("ADVANCED SERVERLESS PERFORMANCE ANALYSIS\n")
            f.write("="*70 + "\n\n")
            
            # Efficiency Scores
            f.write("1. EFFICIENCY RANKINGS\n")
            f.write("-"*70 + "\n")
            if self.insights.get('efficiency'):
                sorted_scores = sorted(self.insights['efficiency'].items(), 
                                     key=lambda x: x[1]['overall_score'], reverse=True)
                for rank, (func_name, score) in enumerate(sorted_scores, 1):
                    f.write(f"{rank:2d}. {func_name:10s} - "
                           f"Overall: {score['overall_score']:6.1f}/100 [{score['grade']}]\n")
                    f.write(f"        Speed: {score['speed_score']:6.1f}  |  "
                           f"Consistency: {score['consistency_score']:6.1f}\n")
            
            # Bottlenecks
            f.write("\n2. PERFORMANCE BOTTLENECKS\n")
            f.write("-"*70 + "\n")
            if self.insights.get('bottlenecks'):
                bn = self.insights['bottlenecks']
                if bn['slow_functions']:
                    f.write("\nSlow Functions:\n")
                    for item in bn['slow_functions']:
                        f.write(f"  • {item['function']}: {item['duration']:.2f}ms [{item['severity']}]\n")
                
                if bn['high_variance']:
                    f.write("\nHigh Variance Functions:\n")
                    for item in bn['high_variance']:
                        f.write(f"  • {item['function']}: σ={item['std_deviation']:.2f}ms\n")
            
            # Recommendations
            f.write("\n3. OPTIMIZATION RECOMMENDATIONS\n")
            f.write("-"*70 + "\n")
            if self.insights.get('recommendations'):
                recs = self.insights['recommendations']
                if recs['memory_optimization']:
                    f.write("\nMemory Optimization:\n")
                    for rec in recs['memory_optimization']:
                        f.write(f"  • {rec['function']}: {rec['action']}\n")
                        f.write(f"    Reason: {rec['reason']}\n")
                
                if recs['cpu_optimization']:
                    f.write("\nCPU Optimization:\n")
                    for rec in recs['cpu_optimization']:
                        f.write(f"  • {rec['function']}: {rec['action']}\n")
                        f.write(f"    Reason: {rec['reason']}\n")
        
        print(f"\n✅ Advanced report saved: {report_path}")
        return report_path
    
    def run_all_advanced_analysis(self):
        """Execute all advanced analysis methods"""
        print("\n" + "="*70)
        print("🔬 RUNNING ADVANCED ANALYSIS")
        print("="*70)
        
        self.identify_performance_bottlenecks()
        self.compute_efficiency_scores()
        self.generate_recommendations()
        self.save_advanced_report()
