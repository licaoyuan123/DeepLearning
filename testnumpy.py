import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
print x

print '========'
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])
print 'scores is ', scores

plt.plot(x, scores.T, linewidth=2)
plt.show()