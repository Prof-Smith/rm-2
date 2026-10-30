# Module 4 Lab: Liquidity and Funding

!!! info "Synthetic teaching model"
    The values in this lab are synthetic and demonstrate the risk mechanism. They are not audited historical observations.

## Objective
Use the compact Python model below to generate evidence for the module decision artifact. You may run it in Jupyter, Google Colab, or another Python environment.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

days=np.arange(1,11); cash=100-np.cumsum(np.array([8,9,11,13,15,17,18,20,22,25])); print(pd.DataFrame({'day':days,'cash':cash})); print('First breach day:',days[cash<0][0])
```

## Decision checkpoint

1. What does the measure reveal?
2. Which assumption is most fragile?
3. What action follows from the result?
4. What observable result would reverse the recommendation?

## Submission evidence
Retain one calculation table or chart, explain its decision relevance in complete sentences, and disclose the model's most material limitation.
