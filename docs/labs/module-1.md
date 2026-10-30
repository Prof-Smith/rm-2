# Module 1 Lab: Risk, Uncertainty, and Judgment

!!! info "Synthetic teaching model"
    The values in this lab are synthetic and demonstrate the risk mechanism. They are not audited historical observations.

## Objective
Use the compact Python model below to generate evidence for the module decision artifact. You may run it in Jupyter, Google Colab, or another Python environment.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

losses=np.array([0.4,0.6,0.5,0.7,0.8,12.0]); print(pd.Series(losses).describe()); print('Tail share:',losses.max()/losses.sum())
```

## Decision checkpoint

1. What does the measure reveal?
2. Which assumption is most fragile?
3. What action follows from the result?
4. What observable result would reverse the recommendation?

## Submission evidence
Retain one calculation table or chart, explain its decision relevance in complete sentences, and disclose the model's most material limitation.
