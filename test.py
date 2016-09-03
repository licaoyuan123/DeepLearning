scores = [3.0, 1.0, 0.2]

import numpy as np

def softmax(x):

    """Compute softmax values for each sets of scores in x."""
    return np.exp(x)/np.sum(np.exp(x),axis=0)
    #pass  # TODO: Compute and return softmax(x)


print(softmax(scores))
print ''
score1 = scores*10
print score1

#print (softmax(scores*10))
#print (softmax(scores/10))