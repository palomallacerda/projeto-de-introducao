
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

x = fort2["Ano"] ## vetor vertical ##
y = fort2["Fort"]

graf = plt.plot(x,y)
plt.show(graf)

#gerando box#

import pandas as pd
import matplotlib.pyplot as plt 

fortaleza = pd.read_csv("fortaleza.csv") 


plt.boxplot(fortaleza.Fort)
plt.show()

# com malha#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt 

fortaleza = pd.read_csv("fortaleza.csv") 
fort1 = fortaleza[0:29]

plt.plot(fort1.Ano, fort1.Fort)
plt.xlabel('ANO(s)')
plt.ylabel('Preciptacao')

plt.title('Precipitação atmosférica em Fortaleza, CE')

plt.grid(True)
plt.xticks(fort1.Ano, fort1.Ano, rotation = 'vertical')
plt.show()
