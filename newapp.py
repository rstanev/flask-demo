#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests
import quandl

quandl.ApiConfig.api_key = 'HWZYrHmanku_oE1Ydh5g'

data = quandl.get("WIKI/MSFT")

data['Close'].plot()
plt.show()


