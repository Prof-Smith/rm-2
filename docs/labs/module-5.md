# Module 5 Lab: Credit and Counterparty Risk

!!! info "Synthetic teaching model"
    The values in this lab are synthetic and demonstrate the risk mechanism. They are not audited historical observations.

## Objective
Use the compact Python model below to generate evidence for the module decision artifact. You may run it in Jupyter, Google Colab, or another Python environment.

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pdv=np.array([.01,.02,.04,.08]); lgd=np.array([.35,.4,.45,.55]); ead=np.array([100,80,60,40]); print(pd.DataFrame({'PD':pdv,'LGD':lgd,'EAD':ead,'EL':pdv*lgd*ead}))
```

## Decision checkpoint

1. What does the measure reveal?
2. Which assumption is most fragile?
3. What action follows from the result?
4. What observable result would reverse the recommendation?

## Submission evidence
Retain one calculation table or chart, explain its decision relevance in complete sentences, and disclose the model's most material limitation.
