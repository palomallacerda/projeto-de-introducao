
cd Download
python

import pandas as pd
import matplotlib.pyplot as plt 

fortaleza = pd.read_csv("fortaleza.csv") 

x = fortaleza["Ano"]
y = fortaleza["Fort"]

fort = plt.plot(x,y)
plt.show(fort)

##os 10 primeiros##

fort1 = fortaleza[0:10]

x = fort1["Ano"]
y = fort1["Fort"]

graf = plt.plot(x,y)
plt.show(graf)

##os 10 ultimos##

fort2 = fortaleza[139:]

x = fort2["Ano"]
y = fort2["Fort"]

graf = plt.plot(x,y)
plt.show(graf)
