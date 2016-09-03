"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):

    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/np.sum(np.exp(x),axis=0)
    #pass  # TODO: Compute and return softmax(x)


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
#print 'x is ', x
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print 'scores is ', scores
#plt.plot(x, softmax(scores).T, linewidth=2)
plt.plot(x,softmax(scores).T, linewidth=2)

plt.show()
