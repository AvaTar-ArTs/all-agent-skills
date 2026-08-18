---
name: transfer-learning-design
description: Adapt pretrained models to new domains with limited data using transfer learning.
---

# Transfer Learning Design Skill

**Purpose**: Design and implement effective transfer learning strategies for new domains with limited data

**When to Use**: Limited target domain data; related pretrained model available; need to quickly adapt model

**Entry Point**: When you have pretrained model and want to adapt to new domain

**Output**: Effective transfer learning strategy with performance validation

## Workflow

### Phase 1: Pretrained Model Selection
- Identify models pretrained on related domain
- Compare model sizes and architectures
- Evaluate available pretrained checkpoints
- Understand pretraining data and task

### Phase 2: Architecture Design
- Keep most pretrained layers, replace/add task-specific head
- Decide input preprocessing (match pretraining)
- Add custom layers if needed for task
- Document architectural choices

### Phase 3: Fine-tuning Strategy
- Freeze pretrained layers initially
- Train only task-specific head first
- Monitor convergence and overfitting
- Gradually unfreeze layers if needed

### Phase 4: Learning Rate Tuning
- Use lower learning rate than training from scratch
- Apply learning rate scheduling (warmup + decay)
- Monitor per-layer learning rates if available
- Adjust if overfitting or underfitting detected

### Phase 5: Regularization
- Monitor for catastrophic forgetting
- Use weight decay to prevent divergence
- Consider early stopping on validation
- Add dropout if overfitting

### Phase 6: Evaluation & Analysis
- Compare against baseline (training from scratch)
- Measure transfer benefit quantitatively
- Analyze which layers learned task-specific features
- Document domain gap if present

## Common Patterns

**Feature Extraction (Frozen Backbone)**
```python
pretrained_model = torchvision.models.resnet50(pretrained=True)
for param in pretrained_model.parameters():
    param.requires_grad = False
# Replace head
pretrained_model.fc = nn.Linear(2048, num_classes)
```

**Fine-tuning with Layer Unfreezing**
```python
# Freeze all except last layer
for param in model.parameters():
    param.requires_grad = False
model.fc.requires_grad = True

# Train...

# Unfreeze more layers
for param in model.layer4.parameters():
    param.requires_grad = True
# Continue training with lower LR
```

**Learning Rate Scheduling for Fine-tuning**
```python
optimizer = optim.SGD(model.parameters(), lr=0.001)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
for epoch in range(num_epochs):
    train_one_epoch()
    scheduler.step()
```

## Success Criteria

- ✅ Pretrained model well-justified for domain
- ✅ Fine-tuning converges with expected improvement
- ✅ Learning rate appropriate (not too aggressive)
- ✅ Layer strategy validated via ablation
- ✅ Transfer benefit > training from scratch
- ✅ Domain gap understood and addressed
- ✅ Catastrophic forgetting monitored and controlled

## Integration

- Spawn **transfer-learning-architect** agent for strategy design
- Use **model-trainer** for training loop
- Use **pytorch-expert** or **tensorflow-expert** for layer manipulation
- Use **model-evaluator** for transfer analysis

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
