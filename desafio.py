
## grafico um com a malha ##
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np


fort = pd.read_csv("fortaleza.csv") 


plt.plot(fort.Ano, fort.Fort)
plt.xlabel('ANO (s)')
plt.ylabel('Preciptacao')
plt.title('Precipitação atmosférica em Fortaleza, CE')
plt.grid(True)
plt.tight_layout()
plt.xticks(fort.Ano, fort.Ano)

plt.show()

## 10 primeiros com malha##
plt.clean()
fort1 = fort[0:10]

x = fort1["Ano"]
y = fort1["Fort"]

graf = plt.plot(x,y)

plt.xlabel('ANO (s)')
plt.ylabel('Preciptacao')
plt.title('10 primeiros dados da preciptacao atmosférica')
plt.grid(True)
plt.tight_layout()
plt.xticks(fort.Ano, fort.Ano)
plt.show()


