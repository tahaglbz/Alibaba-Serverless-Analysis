"""
Machine Learning Analysis Module - Five Model Comparison
Comprehensive analysis with Logistic Regression, Random Forest, SVM, XGBoost, and Neural Network
"""

import json
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from datetime import datetime
import warnings

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.svm import SVC
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, roc_curve, auc, roc_auc_score, classification_report
)

warnings.filterwarnings('ignore')

# Configuration
BASE_PATH = Path(__file__).parent
DATASETS_PATH = BASE_PATH.parent / "data" / "datasets"
OUTPUT_PATH = BASE_PATH.parent / "analysis_output"
PLOTS_PATH = OUTPUT_PATH / "plots"


class AcademicMLComparison:
    """Five-model ML comparison for academic research"""
    
    def __init__(self):
        self.X = None
        self.y = None
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.scaler = None
        self.models = {}
        self.results = {}
        self.data_summary = {}
        
    def load_and_prepare_data(self):
        """Load and prepare data for all models"""
        print("\n🔧 ACADEMIC ML: Loading and preparing data...")
        
        perf_path = DATASETS_PATH / "aliyunfc_functions_perf_profile_cpu"
        
        all_features = []
        all_labels = []
        function_names = []
        
        # Load all performance profiles
        for file in sorted(perf_path.glob("f*_perf_profile.json")):
            func_name = file.stem.replace("_perf_profile", "")
            try:
                with open(file, 'r') as f:
                    profile = json.load(f)
                
                durations = []
                for config_key, duration_ms in profile.items():
                    try:
                        memory, cpu = config_key.split(',')
                        memory = int(memory)
                        cpu = float(cpu)
                        duration = float(duration_ms)
                        
                        all_features.append([memory, cpu])
                        all_labels.append(duration)
                        function_names.append(func_name)
                        durations.append(duration)
                        
                    except Exception:
                        continue
                
                if durations:
                    self.data_summary[func_name] = {
                        'count': len(durations),
                        'mean_duration': np.mean(durations),
                        'std_duration': np.std(durations),
                        'min_duration': np.min(durations),
                        'max_duration': np.max(durations)
                    }
                
            except Exception as e:
                print(f"  ⚠️  Error loading {func_name}: {e}")
        
        # Create DataFrame
        df = pd.DataFrame({
            'Memory': [f[0] for f in all_features],
            'CPU': [f[1] for f in all_features],
            'Duration': all_labels,
            'Function': function_names
        })
        
        # Create binary classification target
        median_duration = df['Duration'].median()
        df['Performance'] = (df['Duration'] <= median_duration).astype(int)
        
        print(f"  ✓ Loaded {len(df)} data points from {len(set(function_names))} functions")
        print(f"  ✓ Performance threshold: {median_duration:.2f}ms")
        print(f"  ✓ Class distribution - High: {(df['Performance'] == 1).sum()}, Low: {(df['Performance'] == 0).sum()}")
        
        self.X = df[['Memory', 'CPU']].values
        self.y = df['Performance'].values
        
        return df
    
    def split_and_scale_data(self, test_size=0.2, random_state=42):
        """Split and scale data"""
        print("\n📊 ACADEMIC ML: Splitting and scaling data...")
        
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            self.X, self.y, test_size=test_size, random_state=random_state, stratify=self.y
        )
        
        self.scaler = StandardScaler()
        self.X_train = self.scaler.fit_transform(self.X_train)
        self.X_test = self.scaler.transform(self.X_test)
        
        print(f"  ✓ Training set: {len(self.X_train)} samples")
        print(f"  ✓ Testing set: {len(self.X_test)} samples")
        print(f"  ✓ Features standardized")
        
    def train_logistic_regression(self):
        """Train Logistic Regression model"""
        print("\n🤖 Training Model 1: Logistic Regression...")
        
        model = LogisticRegression(max_iter=1000, random_state=42, n_jobs=-1)
        model.fit(self.X_train, self.y_train)
        
        self.models['Logistic Regression'] = model
        self._evaluate_model('Logistic Regression')
        
    def train_random_forest(self):
        """Train Random Forest model"""
        print("\n🤖 Training Model 2: Random Forest...")
        
        model = RandomForestClassifier(
            n_estimators=100, max_depth=10, min_samples_split=5,
            min_samples_leaf=2, random_state=42, n_jobs=-1, class_weight='balanced'
        )
        model.fit(self.X_train, self.y_train)
        
        self.models['Random Forest'] = model
        self._evaluate_model('Random Forest')
        
    def train_svm(self):
        """Train Support Vector Machine"""
        print("\n🤖 Training Model 3: Support Vector Machine (SVM)...")
        
        model = SVC(kernel='rbf', C=1.0, gamma='scale', probability=True,
                   random_state=42, class_weight='balanced')
        model.fit(self.X_train, self.y_train)
        
        self.models['SVM'] = model
        self._evaluate_model('SVM')
        
    def train_gradient_boosting(self):
        """Train Gradient Boosting (XGBoost equivalent using sklearn)"""
        print("\n🤖 Training Model 4: Gradient Boosting (XGBoost)...")
        
        model = GradientBoostingClassifier(
            n_estimators=100, learning_rate=0.1, max_depth=5,
            random_state=42, subsample=0.8
        )
        model.fit(self.X_train, self.y_train)
        
        self.models['Gradient Boosting'] = model
        self._evaluate_model('Gradient Boosting')
        
    def train_neural_network(self):
        """Train Neural Network (MLP)"""
        print("\n🤖 Training Model 5: Neural Network (MLP)...")
        
        model = MLPClassifier(
            hidden_layer_sizes=(128, 64, 32), activation='relu',
            learning_rate_init=0.001, max_iter=500, random_state=42,
            early_stopping=True, validation_fraction=0.1
        )
        model.fit(self.X_train, self.y_train)
        
        self.models['Neural Network'] = model
        self._evaluate_model('Neural Network')
        
    def _evaluate_model(self, model_name):
        """Evaluate a trained model"""
        model = self.models[model_name]
        
        # Predictions
        y_pred = model.predict(self.X_test)
        y_pred_proba = model.predict_proba(self.X_test)[:, 1]
        
        # Metrics
        metrics = {
            'accuracy': accuracy_score(self.y_test, y_pred),
            'precision': precision_score(self.y_test, y_pred, zero_division=0),
            'recall': recall_score(self.y_test, y_pred, zero_division=0),
            'f1_score': f1_score(self.y_test, y_pred, zero_division=0),
            'roc_auc': roc_auc_score(self.y_test, y_pred_proba),
            'confusion_matrix': confusion_matrix(self.y_test, y_pred),
            'classification_report': classification_report(self.y_test, y_pred),
            'y_pred': y_pred,
            'y_pred_proba': y_pred_proba
        }
        
        self.results[model_name] = metrics
        
        print(f"  ✓ {model_name}:")
        print(f"     Accuracy: {metrics['accuracy']:.4f}")
        print(f"     Precision: {metrics['precision']:.4f}")
        print(f"     Recall: {metrics['recall']:.4f}")
        print(f"     F1-Score: {metrics['f1_score']:.4f}")
        print(f"     ROC-AUC: {metrics['roc_auc']:.4f}")
    
    def plot_model_comparison(self):
        """Generate comparison plots across all models"""
        print("\n📊 ACADEMIC ML: Generating comparison plots...")
        
        os.makedirs(PLOTS_PATH, exist_ok=True)
        
        # Extract metrics
        model_names = list(self.results.keys())
        accuracies = [self.results[m]['accuracy'] for m in model_names]
        precisions = [self.results[m]['precision'] for m in model_names]
        recalls = [self.results[m]['recall'] for m in model_names]
        f1_scores = [self.results[m]['f1_score'] for m in model_names]
        roc_aucs = [self.results[m]['roc_auc'] for m in model_names]
        
        # Plot 1: Overall Metrics Comparison
        fig, axes = plt.subplots(2, 3, figsize=(16, 10))
        fig.suptitle('Five-Model Performance Comparison', fontsize=16, fontweight='bold')
        
        # Accuracy
        ax = axes[0, 0]
        bars = ax.bar(model_names, accuracies, color='steelblue', alpha=0.8)
        ax.set_ylabel('Score', fontweight='bold')
        ax.set_title('Accuracy', fontweight='bold')
        ax.set_ylim([0, 1])
        ax.axhline(y=np.mean(accuracies), color='red', linestyle='--', alpha=0.5, label='Mean')
        ax.grid(axis='y', alpha=0.3)
        for bar, val in zip(bars, accuracies):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # Precision
        ax = axes[0, 1]
        bars = ax.bar(model_names, precisions, color='coral', alpha=0.8)
        ax.set_ylabel('Score', fontweight='bold')
        ax.set_title('Precision', fontweight='bold')
        ax.set_ylim([0, 1])
        ax.axhline(y=np.mean(precisions), color='red', linestyle='--', alpha=0.5, label='Mean')
        ax.grid(axis='y', alpha=0.3)
        for bar, val in zip(bars, precisions):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # Recall
        ax = axes[0, 2]
        bars = ax.bar(model_names, recalls, color='lightgreen', alpha=0.8)
        ax.set_ylabel('Score', fontweight='bold')
        ax.set_title('Recall', fontweight='bold')
        ax.set_ylim([0, 1])
        ax.axhline(y=np.mean(recalls), color='red', linestyle='--', alpha=0.5, label='Mean')
        ax.grid(axis='y', alpha=0.3)
        for bar, val in zip(bars, recalls):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # F1-Score
        ax = axes[1, 0]
        bars = ax.bar(model_names, f1_scores, color='gold', alpha=0.8)
        ax.set_ylabel('Score', fontweight='bold')
        ax.set_title('F1-Score', fontweight='bold')
        ax.set_ylim([0, 1])
        ax.axhline(y=np.mean(f1_scores), color='red', linestyle='--', alpha=0.5, label='Mean')
        ax.grid(axis='y', alpha=0.3)
        for bar, val in zip(bars, f1_scores):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # ROC-AUC
        ax = axes[1, 1]
        bars = ax.bar(model_names, roc_aucs, color='mediumpurple', alpha=0.8)
        ax.set_ylabel('AUC Score', fontweight='bold')
        ax.set_title('ROC-AUC', fontweight='bold')
        ax.set_ylim([0, 1])
        ax.axhline(y=np.mean(roc_aucs), color='red', linestyle='--', alpha=0.5, label='Mean')
        ax.grid(axis='y', alpha=0.3)
        for bar, val in zip(bars, roc_aucs):
            ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                   ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        # Summary Text
        ax = axes[1, 2]
        ax.axis('off')
        summary_text = "MODEL SUMMARY\n\n"
        summary_text += f"Best Accuracy: {max(zip(model_names, accuracies), key=lambda x: x[1])[0]}\n"
        summary_text += f"Best F1-Score: {max(zip(model_names, f1_scores), key=lambda x: x[1])[0]}\n"
        summary_text += f"Best ROC-AUC: {max(zip(model_names, roc_aucs), key=lambda x: x[1])[0]}\n"
        summary_text += f"Best Recall: {max(zip(model_names, recalls), key=lambda x: x[1])[0]}\n\n"
        summary_text += f"Samples Trained: {len(self.X_train)}\n"
        summary_text += f"Samples Tested: {len(self.X_test)}\n"
        
        ax.text(0.1, 0.9, summary_text, transform=ax.transAxes, fontsize=11,
               verticalalignment='top', fontfamily='monospace',
               bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        
        plt.xticks(rotation=45, ha='right')
        plt.tight_layout()
        plt.savefig(PLOTS_PATH / '00_models_comparison.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: 00_models_comparison.png")
        plt.close()
        
    def plot_individual_models(self):
        """Generate individual plots for each model"""
        print("\n📊 ACADEMIC ML: Generating individual model plots...")
        
        os.makedirs(PLOTS_PATH, exist_ok=True)
        
        for idx, (model_name, metrics) in enumerate(self.results.items(), 1):
            # Create 2x2 subplot for each model
            fig, axes = plt.subplots(2, 2, figsize=(12, 10))
            fig.suptitle(f'Model {idx}: {model_name} - Detailed Analysis', 
                        fontsize=14, fontweight='bold')
            
            # Confusion Matrix
            cm = metrics['confusion_matrix']
            ax = axes[0, 0]
            sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
                       xticklabels=['Low Perf', 'High Perf'],
                       yticklabels=['Low Perf', 'High Perf'],
                       ax=ax, cbar_kws={'label': 'Count'})
            ax.set_ylabel('True Label', fontweight='bold')
            ax.set_xlabel('Predicted Label', fontweight='bold')
            ax.set_title('Confusion Matrix', fontweight='bold')
            
            # ROC Curve
            ax = axes[0, 1]
            fpr, tpr, _ = roc_curve(self.y_test, metrics['y_pred_proba'])
            roc_auc = metrics['roc_auc']
            ax.plot(fpr, tpr, color='darkorange', lw=2.5, 
                   label=f'ROC (AUC = {roc_auc:.4f})')
            ax.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label='Random')
            ax.set_xlim([0.0, 1.0])
            ax.set_ylim([0.0, 1.05])
            ax.set_xlabel('False Positive Rate', fontweight='bold')
            ax.set_ylabel('True Positive Rate', fontweight='bold')
            ax.set_title('ROC Curve', fontweight='bold')
            ax.legend(loc="lower right")
            ax.grid(True, alpha=0.3)
            
            # Metrics Bar Chart
            ax = axes[1, 0]
            metrics_names = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
            metrics_values = [metrics['accuracy'], metrics['precision'], 
                            metrics['recall'], metrics['f1_score']]
            colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
            bars = ax.bar(metrics_names, metrics_values, color=colors, alpha=0.8)
            ax.set_ylabel('Score', fontweight='bold')
            ax.set_title('Performance Metrics', fontweight='bold')
            ax.set_ylim([0, 1])
            ax.grid(axis='y', alpha=0.3)
            for bar, val in zip(bars, metrics_values):
                ax.text(bar.get_x() + bar.get_width()/2, val + 0.02, f'{val:.3f}', 
                       ha='center', va='bottom', fontweight='bold')
            
            # Classification Report Text
            ax = axes[1, 1]
            ax.axis('off')
            report_text = "CLASSIFICATION REPORT\n\n" + metrics['classification_report']
            ax.text(0.05, 0.95, report_text, transform=ax.transAxes, fontsize=9,
                   verticalalignment='top', fontfamily='monospace',
                   bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.7))
            
            plt.tight_layout()
            filename = f'0{idx}_model_{model_name.lower().replace(" ", "_")}.png'
            plt.savefig(PLOTS_PATH / filename, dpi=300, bbox_inches='tight')
            print(f"  ✓ Saved: {filename}")
            plt.close()
    
    def plot_roc_curves_overlay(self):
        """Plot all ROC curves on one figure"""
        print("\n📊 ACADEMIC ML: Generating overlaid ROC curves...")
        
        fig, ax = plt.subplots(figsize=(10, 8))
        
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        
        for (model_name, metrics), color in zip(self.results.items(), colors):
            fpr, tpr, _ = roc_curve(self.y_test, metrics['y_pred_proba'])
            roc_auc = metrics['roc_auc']
            ax.plot(fpr, tpr, color=color, lw=2.5, 
                   label=f'{model_name} (AUC = {roc_auc:.4f})')
        
        ax.plot([0, 1], [0, 1], color='black', lw=2, linestyle='--', label='Random Classifier')
        ax.set_xlim([0.0, 1.0])
        ax.set_ylim([0.0, 1.05])
        ax.set_xlabel('False Positive Rate', fontsize=12, fontweight='bold')
        ax.set_ylabel('True Positive Rate', fontsize=12, fontweight='bold')
        ax.set_title('ROC Curves - All Models Comparison', fontsize=14, fontweight='bold')
        ax.legend(loc="lower right", fontsize=11)
        ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig(PLOTS_PATH / '06_roc_curves_overlay.png', dpi=300, bbox_inches='tight')
        print(f"  ✓ Saved: 06_roc_curves_overlay.png")
        plt.close()
    
    def generate_academic_report(self):
        """Generate comprehensive academic results summary"""
        print("\n📄 ACADEMIC ML: Generating results summary...")
        
        os.makedirs(OUTPUT_PATH, exist_ok=True)
        
        report_path = OUTPUT_PATH / "ml_academic_results.md"
        
        with open(report_path, 'w') as f:
            f.write("# Machine Learning Five-Model Comparison Results\n\n")
            f.write(f"**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("---\n\n")
            
            # Summary Table
            f.write("## Overall Performance Summary\n\n")
            f.write("| Model | Accuracy | Precision | Recall | F1-Score | ROC-AUC |\n")
            f.write("|-------|----------|-----------|--------|----------|----------|\n")
            
            for model_name, metrics in self.results.items():
                f.write(f"| {model_name} | {metrics['accuracy']:.4f} | {metrics['precision']:.4f} | ")
                f.write(f"{metrics['recall']:.4f} | {metrics['f1_score']:.4f} | {metrics['roc_auc']:.4f} |\n")
            
            f.write("\n")
            
            # Best performers
            f.write("## Best Performing Models\n\n")
            best_accuracy = max(self.results.items(), key=lambda x: x[1]['accuracy'])
            best_f1 = max(self.results.items(), key=lambda x: x[1]['f1_score'])
            best_roc = max(self.results.items(), key=lambda x: x[1]['roc_auc'])
            
            f.write(f"- **Best Accuracy:** {best_accuracy[0]} ({best_accuracy[1]['accuracy']:.4f})\n")
            f.write(f"- **Best F1-Score:** {best_f1[0]} ({best_f1[1]['f1_score']:.4f})\n")
            f.write(f"- **Best ROC-AUC:** {best_roc[0]} ({best_roc[1]['roc_auc']:.4f})\n\n")
            
            # Detailed Results
            f.write("## Detailed Model Results\n\n")
            
            for idx, (model_name, metrics) in enumerate(self.results.items(), 1):
                f.write(f"### Model {idx}: {model_name}\n\n")
                f.write(f"**Metrics:**\n")
                f.write(f"- Accuracy: {metrics['accuracy']:.4f}\n")
                f.write(f"- Precision: {metrics['precision']:.4f}\n")
                f.write(f"- Recall: {metrics['recall']:.4f}\n")
                f.write(f"- F1-Score: {metrics['f1_score']:.4f}\n")
                f.write(f"- ROC-AUC: {metrics['roc_auc']:.4f}\n\n")
                
                cm = metrics['confusion_matrix']
                f.write(f"**Confusion Matrix:**\n")
                f.write(f"```\n")
                f.write(f"TN: {cm[0,0]}  |  FP: {cm[0,1]}\n")
                f.write(f"FN: {cm[1,0]}  |  TP: {cm[1,1]}\n")
                f.write(f"```\n\n")
        
        print(f"  ✓ Saved: ml_academic_results.md")
        return report_path
    
    def run_complete_pipeline(self):
        """Execute the complete academic ML pipeline"""
        print("\n" + "="*75)
        print("🎓 ACADEMIC MACHINE LEARNING ANALYSIS")
        print("Five-Model Comprehensive Comparison")
        print("="*75)
        
        try:
            # Step 1: Load data
            self.load_and_prepare_data()
            
            # Step 2: Split and scale
            self.split_and_scale_data()
            
            # Step 3: Train all models
            print("\n" + "-"*75)
            print("TRAINING ALL MODELS")
            print("-"*75)
            
            self.train_logistic_regression()
            self.train_random_forest()
            self.train_svm()
            self.train_gradient_boosting()
            self.train_neural_network()
            
            # Step 4: Generate plots
            print("\n" + "-"*75)
            print("GENERATING VISUALIZATIONS")
            print("-"*75)
            
            self.plot_model_comparison()
            self.plot_individual_models()
            self.plot_roc_curves_overlay()
            
            # Step 5: Generate report
            self.generate_academic_report()
            
            # Summary
            print("\n" + "="*75)
            print("✅ ACADEMIC ML ANALYSIS COMPLETE")
            print("="*75)
            print("\n📁 Generated Files:")
            print("   analysis_output/")
            print("   ├── ml_academic_results.md")
            print("   └── plots/")
            print("       ├── 00_models_comparison.png")
            print("       ├── 01_model_logistic_regression.png")
            print("       ├── 02_model_random_forest.png")
            print("       ├── 03_model_svm.png")
            print("       ├── 04_model_gradient_boosting.png")
            print("       ├── 05_model_neural_network.png")
            print("       └── 06_roc_curves_overlay.png")
            print("\n")
            
            return True
            
        except Exception as e:
            print(f"\n❌ ERROR in Academic ML Pipeline: {e}")
            import traceback
            traceback.print_exc()
            return False


if __name__ == "__main__":
    academic_ml = AcademicMLComparison()
    success = academic_ml.run_complete_pipeline()
    import sys
    sys.exit(0 if success else 1)
