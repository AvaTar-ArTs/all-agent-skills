---
name: model-deployment
description: Package and deploy trained deep learning models for production inference.
---

# Model Deployment Skill

**Purpose**: Prepare, package, and deploy deep learning models for production inference

**When to Use**: Model trained and validated, ready for production; need API server; need containerization

**Entry Point**: When you have trained model and want to deploy it

**Output**: Production-ready deployment with API, monitoring, and documentation

## Workflow

### Phase 1: Model Optimization
- Quantize model if latency critical
- Profile inference performance
- Choose optimization technique (TorchScript, ONNX, etc.)
- Verify optimized model correctness

### Phase 2: API Design
- Choose framework (FastAPI, Flask, TensorFlow Serving)
- Design API endpoints and request/response format
- Implement input validation
- Add error handling and logging

### Phase 3: Containerization
- Write Dockerfile with dependencies
- Choose base image (pytorch, tensorflow, ubuntu)
- Verify docker build and run locally
- Test container with example requests

### Phase 4: Model Registry & Versioning
- Save model to registry (MLflow, wandb, custom)
- Version models explicitly
- Document model requirements and metadata
- Enable model rollback if needed

### Phase 5: Deployment
- Deploy to target platform (Docker, K8s, serverless)
- Set up health checks and monitoring
- Configure resource limits (GPU, memory)
- Test endpoint availability

### Phase 6: Monitoring & Maintenance
- Track inference metrics (latency, throughput)
- Monitor for data drift
- Set up alerts for performance degradation
- Plan retraining when drift detected

## Common Patterns

**FastAPI Deployment**
```python
from fastapi import FastAPI
import torch

app = FastAPI()
model = torch.load("model.pth")

@app.post("/predict")
async def predict(input_data: InputSchema):
    tensor = preprocess(input_data)
    with torch.no_grad():
        output = model(tensor)
    return postprocess(output)
```

**Docker Containerization**
```dockerfile
FROM pytorch/pytorch:2.0-cuda11.8-runtime-ubuntu22.04
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY model.pth .
COPY app.py .
CMD ["python", "app.py"]
```

**Model Quantization**
```python
# PyTorch quantization
quantized_model = torch.quantization.quantize_dynamic(
    model, {torch.nn.Linear}, dtype=torch.qint8
)
# Verify quantized model
with torch.no_grad():
    output_quantized = quantized_model(test_input)
```

## Success Criteria

- ✅ Model loads and serves successfully
- ✅ Inference latency meets requirements (<100ms?)
- ✅ API handles errors gracefully
- ✅ Container builds and runs locally
- ✅ Deployed endpoint responds correctly
- ✅ Monitoring captures key metrics
- ✅ Rollback procedure documented and tested

## Integration

- Spawn **ml-ops-engineer** agent for deployment architecture
- Use **deployment-pipeline-builder** for CI/CD setup
- Use **pytorch-expert** or **tensorflow-expert** for optimization
- Use **experiment-tracker** for model versioning

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
