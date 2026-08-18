---
name: tensorflow-debugging
description: Debug TensorFlow graph, eager execution, NaN, device placement, and distributed issues.
---

# TensorFlow Debugging Skill

**Purpose**: Systematically debug TensorFlow code and identify graph, eager, or distributed execution issues

**When to Use**: tf.function compilation issues; NaN/Inf in training; unexpected behavior; device placement problems

**Entry Point**: When TensorFlow code isn't working as expected

**Output**: Fixed code with identified root cause and prevention strategy

## Workflow

### Phase 1: Eager vs Graph Execution
- Disable tf.function to debug eagerly
- Add assertions and print statements in graph mode
- Use tf.debugging.set_log_device_placement to track ops
- Check if bug reproduces in both modes

### Phase 2: Gradient Issues
- Use tape.gradient to compute gradients explicitly
- Add tf.debugging.assert_finite to gradients
- Use GradientTape with persistent=True for debugging
- Check for disconnected gradients

### Phase 3: Shape & Type Issues
- Add tf.debugging.assert_rank for shape checking
- Use tf.print for debugging in graph mode
- Check dtype consistency (float32 vs float64)
- Verify broadcasting rules applied

### Phase 4: Device & Distribution Issues
- Check device placement with set_log_device_placement
- Verify strategy scope applied correctly
- Test on single device before distributed
- Check for variable access issues in distributed training

### Phase 5: Numerical Stability
- Use stable loss functions (from_logits=True)
- Check for underflow/overflow
- Verify normalization applied
- Monitor loss magnitudes during training

### Phase 6: Performance Analysis
- Profile with tf.profiler
- Identify compute vs I/O bottlenecks
- Check data loading performance
- Optimize hot paths

## Common Patterns

**Gradient Debugging in tf.GradientTape**
```python
with tf.GradientTape() as tape:
    output = model(inputs)
    loss = criterion(output, labels)
grads = tape.gradient(loss, model.trainable_variables)
for grad in grads:
    assert not tf.reduce_any(tf.math.is_nan(grad))
```

**Shape Debugging with tf.debugging**
```python
x = tf.debugging.assert_rank(x, 4)
x = tf.debugging.assert_all_finite(x)
```

**Graph Debugging**
```python
@tf.function
def train_step(x, y):
    # Use tf.print for debugging
    tf.print("Input shape:", tf.shape(x))
    with tf.GradientTape() as tape:
        predictions = model(x)
    return predictions
```

**Device Placement Tracking**
```python
tf.debugging.set_log_device_placement(True)
with tf.device('/GPU:0'):
    a = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    b = tf.constant([[1.0, 2.0], [3.0, 4.0]])
    c = tf.matmul(a, b)
```

## Success Criteria

- ✅ Issue reproduced in eager mode
- ✅ Root cause identified (graph, gradient, shape, device)
- ✅ Gradients verified finite and reasonable
- ✅ Tensor shapes and types correct throughout
- ✅ Device placement verified and correct
- ✅ Training stabilizes and converges
- ✅ Performance bottlenecks eliminated

## Integration

- Spawn **tensorflow-expert** agent for expert debugging
- Use **model-trainer** to validate fixes in full training
- Use **systematic-debugging** skill for general approach
- Use **tensorflow-debugging** skill iteratively

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
