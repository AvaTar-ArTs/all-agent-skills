---
name: model-evaluation
description: Evaluate model performance, failure modes, and readiness beyond simple accuracy metrics.
---

# Model Evaluation Skill

**Purpose**: Comprehensively evaluate model performance beyond simple accuracy metrics

**When to Use**: After training to validate model; before deployment; understanding failure modes

**Entry Point**: When you want to evaluate model quality thoroughly

**Output**: Complete evaluation report with metrics, analysis, and failure mode insights

## Workflow

### Phase 1: Metric Selection
- Choose task-appropriate metrics (accuracy, F1, BLEU, ROUGE, etc.)
- Select domain-specific metrics if needed
- Identify business metrics vs ML metrics
- Plan evaluation on train/val/test splits

### Phase 2: Cross-Validation (if needed)
- Decide k-fold vs hold-out validation
- Implement stratified cross-validation
- Compute confidence intervals on metrics
- Check for variance across folds

### Phase 3: Error Analysis
- Identify misclassified examples
- Group errors by type/category
- Visualize confusion matrices
- Find systematic failure patterns

### Phase 4: Robustness Testing
- Test on adversarial examples
- Evaluate on out-of-distribution data
- Check performance on edge cases
- Analyze sensitivity to input perturbations

### Phase 5: Fairness & Bias Analysis
- Evaluate performance across demographic groups
- Identify disparities if present
- Document fairness properties
- Compare against fairness metrics

### Phase 6: Reporting
- Create comparison table vs baselines
- Generate visualizations (confusion matrix, ROC curve)
- Write analysis of strengths/weaknesses
- Document limitations and failure modes

## Common Patterns

**Classification Metrics**
```python
from sklearn.metrics import confusion_matrix, classification_report, roc_auc_score
cm = confusion_matrix(y_true, y_pred)
print(classification_report(y_true, y_pred))
roc_auc = roc_auc_score(y_true, y_pred_proba)
```

**Cross-Validation**
```python
from sklearn.model_selection import cross_validate
scores = cross_validate(model, X, y, cv=5, scoring=['accuracy', 'f1'])
print(f"Accuracy: {scores['test_accuracy'].mean():.3f} ± {scores['test_accuracy'].std():.3f}")
```

**Error Analysis**
```python
errors = y_true != y_pred
error_indices = np.where(errors)[0]
for idx in error_indices[:10]:
    print(f"True: {y_true[idx]}, Pred: {y_pred[idx]}")
    visualize(X[idx])
```

## Success Criteria

- ✅ Appropriate metrics for task chosen
- ✅ Confidence intervals or error bars included
- ✅ Error analysis identifies improvement opportunities
- ✅ Robustness tested on adversarial/OOD examples
- ✅ Fairness analysis shows model properties
- ✅ Comparison with baselines clear
- ✅ Limitations and failure modes documented

## Integration

- Spawn **model-evaluator** agent for complex analysis
- Use **model-trainer** to collect predictions for analysis
- Use **experiment-tracker** for logging results
- Use **data-labeler** if error analysis reveals labeling issues

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
