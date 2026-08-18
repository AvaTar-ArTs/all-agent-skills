---
name: pytorch-debugging
description: Debug PyTorch correctness, NaN, GPU memory, and training stability issues.
---

# PyTorch Debugging Skill

**Purpose**: Systematically debug PyTorch code and identify performance or correctness issues

**When to Use**: NaN/Inf in training; unexpected performance; GPU out of memory; training instability

**Entry Point**: When PyTorch code isn't working as expected

**Output**: Fixed code with identified root cause and prevention strategy

## Workflow

### Phase 1: Reproduce Issue Minimally
- Create minimal reproducible example
- Isolate problematic component
- Check if deterministic with fixed seed
- Document exact error and conditions

### Phase 2: Gradient Flow Check
- Use torch.autograd.gradcheck for custom functions
- Verify gradients are finite (not NaN/Inf)
- Check gradient magnitudes reasonable
- Debug backward pass if needed

### Phase 3: Shape & Broadcasting Issues
- Print tensor shapes at each step
- Verify broadcasting rules applied
- Check dimension mismatches
- Trace operations causing errors

### Phase 4: GPU Memory Issues
- Profile memory usage (nvidia-smi)
- Identify memory leaks (gradients not freed)
- Reduce batch size if OOM
- Use gradient checkpointing if needed

### Phase 5: Numerical Stability
- Check for underflow/overflow
- Use stable loss functions (log_softmax)
- Verify normalization correct
- Check learning rate not too large

### Phase 6: Performance Analysis
- Profile with torch.profiler
- Identify bottlenecks (compute vs memory)
- Check data loading not blocking
- Optimize hot paths

## Common Patterns

**Gradient Checking**
```python
from torch.autograd import gradcheck
# For custom function
assert gradcheck(func, inputs, eps=1e-6, atol=1e-4)
```

**Shape Debugging**
```python
x = input_tensor
print(f"Input shape: {x.shape}")
x = model.layer1(x)
print(f"After layer1: {x.shape}")
assert x.shape == expected_shape
```

**Memory Profiling**
```python
from torch.profiler import profile, record_function
with profile(activities=[...]) as prof:
    model(input)
print(prof.key_averages().table(sort_by="self_cpu_memory_usage"))
```

**NaN Debugging**
```python
# Add checks for NaN
assert not torch.isnan(loss), "Loss is NaN!"
assert not torch.isinf(loss), "Loss is Inf!"
# In backward
if torch.isnan(loss):
    print("Gradients:", model.layer1.weight.grad)
```

## Success Criteria

- ✅ Issue reproduced minimally
- ✅ Root cause identified (gradient, shape, stability, memory)
- ✅ Gradients verified finite and reasonable magnitude
- ✅ Tensor shapes traced and verified
- ✅ Training stabilizes and converges
- ✅ Performance profiled and bottlenecks eliminated
- ✅ Prevention strategy documented

## Integration

- Spawn **pytorch-expert** agent for expert debugging
- Use **model-trainer** to validate fixes in full training
- Use **systematic-debugging** skill for general debugging approach
- Use **pytorch-debugging** skill iteratively

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
