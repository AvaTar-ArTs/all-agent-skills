---
name: dataset-preparation
description: Prepare, augment, validate, and split datasets for deep learning training.
---

# Dataset Preparation Skill

**Purpose**: Prepare, augment, and validate datasets for optimal deep learning training

**When to Use**: Starting a new dataset; improving data quality; addressing imbalance or augmentation needs

**Entry Point**: When you have raw data and need to prepare it for training

**Output**: Well-prepared, validated training/validation/test splits with appropriate augmentation

## Workflow

### Phase 1: Data Exploration
- Load and inspect dataset (size, distribution, missing values)
- Analyze class distribution (balanced or imbalanced?)
- Visualize samples and identify outliers
- Check for data quality issues

### Phase 2: Preprocessing
- Handle missing values (imputation or removal)
- Normalize/standardize features appropriately
- Remove obvious outliers or corrupted samples
- Convert formats if needed (PIL, numpy, tensors)

### Phase 3: Train/Val/Test Splitting
- Stratified split for classification (preserve class distribution)
- Time-aware split for temporal data
- Ensure no data leakage between splits
- Document splitting strategy

### Phase 4: Augmentation Strategy
- Select augmentations preserving task-relevant information
- Implement separate augmentation for train vs val
- Test augmentation doesn't corrupt labels
- Consider class-specific augmentation if needed

### Phase 5: Validation & Loading
- Verify augmentation with visualization
- Check loading performance (not bottleneck)
- Validate normalization correct
- Test edge cases and error handling

## Common Patterns

**Image Augmentation with albumentations**
```python
import albumentations as A
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.2),
    A.Normalize(),
], bbox_params=A.BboxParams(format='pascal_voc'))
```

**Handling Class Imbalance**
```python
# Option 1: Weighted loss
class_weights = compute_class_weight('balanced', classes, labels)
loss = nn.CrossEntropyLoss(weight=weights)

# Option 2: Oversampling
from torch.utils.data import WeightedRandomSampler
sampler = WeightedRandomSampler(weights, len(dataset))
loader = DataLoader(dataset, sampler=sampler)
```

**Stratified Split**
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42
)
```

## Success Criteria

- ✅ Dataset loads without errors
- ✅ Class distribution preserved in splits
- ✅ Augmentation visualized and verified
- ✅ No data leakage between splits
- ✅ Data loading not training bottleneck
- ✅ Imbalance handled appropriately
- ✅ Normalization matches model expectations

## Integration

- Spawn **dataset-optimizer** agent for complex data issues
- Use **model-trainer** to validate dataset with training
- Use **data-labeler** if manual annotation needed
- Use **pytorch-expert** or **tensorflow-expert** for loading optimization

**Tier**: Tier 0-DL (Deep Learning Specialization)  
**Published**: Yes
