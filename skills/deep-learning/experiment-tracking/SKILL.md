---
name: experiment-tracking
description: Log, compare, and reproduce ML experiments with metrics, artifacts, and code versions.
---

# Experiment Tracking Skill

**Purpose**: Systematically log and analyze experiments for reproducibility and scientific rigor

**When to Use**: Starting any significant training run; comparing approaches; publishing results

**Entry Point**: When you want to log experiments and compare results scientifically

**Output**: Complete experiment records with metrics, hyperparameters, code version, and analysis

## Workflow

### Phase 1: Setup Tracking Infrastructure
- Choose tracking tool (Weights & Biases, MLflow, TensorBoard)
- Initialize experiment tracking in code
- Configure metric logging frequency
- Set up artifact storage (checkpoints, final models)

### Phase 2: Log Experiment Metadata
- Record all hyperparameters
- Save code hash/version for reproducibility
- Document dataset version/split info
- Save environment details (library versions)

### Phase 3: Metrics Tracking During Training
- Log loss curves at regular intervals
- Track validation metrics
- Monitor learning rates if scheduling
- Track any custom metrics

### Phase 4: Post-Training Logging
- Save final model checkpoint
- Log test set performance
- Save training configuration file
- Create summary/analysis

### Phase 5: Analysis & Reporting
- Generate comparison tables across experiments
- Create visualizations (loss curves, scatter plots)
- Compute statistical significance if applicable
- Generate shareable reports

## Common Patterns

**Weights & Biases Integration**
```python
import wandb
wandb.init(project="my-project", config=config)
# In training loop:
wandb.log({"loss": loss, "accuracy": acc, "epoch": epoch})
# After training:
wandb.log_model(path_to_model, name="final-model")
```

**MLflow Tracking**
```python
import mlflow
mlflow.start_run()
mlflow.log_params(config)
mlflow.log_metrics({"accuracy": 0.95})
mlflow.log_model(model, "model")
mlflow.end_run()
```

**TensorBoard Logging**
```python
from torch.utils.tensorboard import SummaryWriter
writer = SummaryWriter()
writer.add_scalar('Loss/train', loss, epoch)
writer.add_scalar('Accuracy/val', acc, epoch)
writer.close()
```

## Success Criteria

- ✅ All experiments logged with hyperparameters
- ✅ Code version recorded for reproducibility
- ✅ Metrics logged at appropriate frequency
- ✅ Comparison across experiments possible
- ✅ Results reproducible within variance bounds
- ✅ Final models saved with metadata
- ✅ Results communicated clearly via dashboard/report

## Integration

- Spawn **experiment-tracker** agent for setup and optimization
- Use **model-trainer** to integrate logging into training
- Use **model-evaluator** for test set analysis
- Use **hyperparameter-optimizer** for sweep logging

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
