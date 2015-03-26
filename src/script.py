import numpy as np
import scisoftpy as dnp

# np?

np.sum(np.random.rand(100,100))

# %timeit previous

# %pylab

import pandas as pd
df = pd.DataFrame()
df['a'] = np.random.rand(100)
df['b'] = np.random.rand(100)
df.plot()

# dnp plotting
dnp.plot.line(np.random.rand(100))
dnp.plot.image(dnp.random.rand(100,100))
dnp.plot.surface(dnp.random.rand(100,100))

dnp.plot.image(dnp.random.rand(100,100), name="Wibble")
dnp.plot.image(dnp.random.rand(100,100), name="Plot 2")

# async
for i in range(1000):
    dnp.plot.image(dnp.random.rand(100,100))
    print(i)

#  Show variables
a = np.random.rand(100)
b = np.random.rand(100)


# show debgging
from demo import foo

foo.mul(a,b)



