## Gambler's ruin simulation using Python 

# Importing libraries
import matplotlib.pyplot as plt
import numpy as np

# Initializing variables
np.random.seed(123)
tot_amount=[]

# Simulating random walks 1000 times
for i in range(500):
    amount = [0]
    for x in range(100):
        step=amount[-1]
        dice=np.random.randint(1,7)
        if dice <= 3:
            step=step-1
        elif dice <=5:
            step=step+1
        else:
            step=step+np.random.randint(1,7)
        amount.append(step)
    tot_amount.append(amount)
    
# Visualizing the gambler's financial status 
np_ta_t = np.transpose(np.array(tot_amount))
plt.plot(np_ta_t)
plt.show()

# Plotting histogram
ends=np_ta_t[-1]
plt.hist(ends)
plt.show()