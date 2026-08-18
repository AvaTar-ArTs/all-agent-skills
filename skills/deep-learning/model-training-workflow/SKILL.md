---
name: model-training-workflow
description: Design, implement, debug, and monitor deep learning training loops.
---

# Model Training Workflow Skill

**Purpose**: Systematic approach to designing, implementing, and debugging training loops for deep learning models

**When to Use**: Starting any model training from scratch; debugging convergence issues; optimizing training efficiency

**Entry Point**: When you have a model architecture and want to train it effectively

**Output**: Production-ready training code with robust convergence, monitoring, and checkpointing

## Workflow

### Phase 1: Training Loop Design
- Define optimizer (Adam/SGD), learning rate schedule
- Choose loss function and evaluation metrics
- Design validation strategy and early stopping
- Set up logging and monitoring infrastructure

### Phase 2: Implementation
- Implement training loop with gradient computation
- Add gradient clipping/normalization if needed
- Implement checkpointing and model saving
- Add tensorboard/wandb logging

### Phase 3: Validation & Debugging
- Run on small dataset to verify correctness
- Check gradient flow (no NaNs/Infs)
- Verify learning curves show expected behavior
- Debug convergence issues if present

### Phase 4: Optimization
- Profile to identify bottlenecks
- Implement gradient accumulation for larger batches
- Optimize data loading pipeline
- Tune learning rate schedule

### Phase 5: Production Readiness
- Ensure training reproducible with seeds
- Test checkpoint save/restore
- Validate performance matches expected baselines
- Document training procedures

## Common Patterns

**Basic Training Loop (PyTorch)**
```python
for epoch in range(num_epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        output = model(batch)
        loss = criterion(output, labels)
        loss.backward()
        optimizer.step()
    validate_and_checkpoint()
```

**With Learning Rate Scheduling**
```python
scheduler = torch.optim.lr_scheduler.CosineAnnealingWarmRestarts(optimizer)
for epoch in range(num_epochs):
    train_one_epoch()
    scheduler.step()
```

**With Gradient Accumulation**
```python
for i, batch in enumerate(train_loader):
    output = model(batch)
    loss = criterion(output, labels) / accumulation_steps
    loss.backward()
    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

## Success Criteria

- ✅ Training converges consistently
- ✅ Loss curves smooth (no extreme spikes)
- ✅ Validation performance matches training (no overfitting until later epochs)
- ✅ No NaNs or Infs in gradients
- ✅ Checkpoints save/restore correctly
- ✅ Learning rate schedule applied as expected
- ✅ Training completes within expected time

## Integration

- Spawn **model-trainer** agent for complex training issues
- Use **pytorch-expert** or **tensorflow-expert** for framework-specific problems
- Use **experiment-tracker** for logging and monitoring
- Use **hyperparameter-optimizer** for learning rate tuning

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
