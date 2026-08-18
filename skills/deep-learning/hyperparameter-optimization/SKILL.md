---
name: hyperparameter-optimization
description: Tune learning rates, batch sizes, architectures, and training settings with systematic search.
---

# Hyperparameter Optimization Skill

**Purpose**: Systematic search for optimal hyperparameters balancing exploration, exploitation, and computational budget

**When to Use**: Need to tune learning rate, batch size, architecture parameters, or other hyperparameters

**Entry Point**: When you have a working baseline and want to optimize performance

**Output**: Optimized hyperparameters with evidence of improvement and importance analysis

## Workflow

### Phase 1: Search Space Definition
- Identify critical hyperparameters (learning rate, batch size, regularization)
- Set reasonable bounds based on domain knowledge
- Determine search budget (number of trials, compute hours)

### Phase 2: Baseline & Learning Rate
- Run learning rate finder to set initial bounds
- Establish baseline performance with default hyperparameters
- Compare against state-of-the-art if available

### Phase 3: Search Strategy Selection
- Learning rate finder: Quick manual search
- Grid search: Small discrete parameter space
- Random search: Higher dimensional space
- Bayesian optimization: Efficient exploration
- Population-based training: Long training runs

### Phase 4: Execution
- Run search with early stopping to save compute
- Log all trials and results
- Monitor search progress and convergence

### Phase 5: Analysis & Validation
- Analyze hyperparameter importance (which parameters mattered most?)
- Generate comparison tables and visualization
- Test best hyperparameters on held-out test set
- Compare final performance to baselines

## Common Patterns

**Learning Rate Finder (PyTorch)**
```python
from torch_lr_finder import LRFinder
lr_finder = LRFinder(model, optimizer, criterion)
lr_finder.range_test(train_loader, end_lr=100)
lr_finder.plot()
```

**Bayesian Optimization with Optuna**
```python
def objective(trial):
    lr = trial.suggest_float('lr', 1e-5, 1e-1, log=True)
    batch_size = trial.suggest_int('batch_size', 16, 256)
    # train model and return validation score
    return validation_accuracy

study = optuna.create_study(direction='maximize')
study.optimize(objective, n_trials=50)
```

**Grid Search**
```python
from sklearn.model_selection import GridSearchCV
param_grid = {'C': [0.1, 1, 10], 'kernel': ['linear', 'rbf']}
grid = GridSearchCV(estimator, param_grid, cv=5)
grid.fit(X_train, y_train)
```

## Success Criteria

- ✅ Search converges to reasonable hyperparameters
- ✅ Best trial significantly outperforms baseline
- ✅ Final model validates on held-out test set
- ✅ Hyperparameter importance analyzed
- ✅ Search completed within compute budget
- ✅ Results reproducible with seed control
- ✅ Improvement documented with comparison table

## Integration

- Spawn **hyperparameter-optimizer** agent for complex searches
- Use **model-trainer** for evaluation during search
- Use **experiment-tracker** for logging all trials
- Use **pytorch-expert** or **tensorflow-expert** for implementation

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
