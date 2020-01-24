
import pandas as pd
import matplotlib.pyplot as plt 

mancha = pd.read_csv("MANCHAS.csv") 

x = mancha["Ano"]
y = mancha["manchas"]

graf = plt.plot(x,y)
plt.show(graf)

##os 10 primeiros##

man1 = mancha[0:10]
	
x = man1["Ano"]
y = man1["manchas"]

graf = plt.plot(x,y)
plt.show(graf)

##os 10 ultimos##

man2 = mancha[167:]

x = man2["Ano"] ## vetor vertical ##
y = man2["manchas"]

graf = plt.plot(x,y)
plt.show(graf)

#gerando box#

import pandas as pd
import matplotlib.pyplot as plt 

mancha = pd.read_csv("MANCHAS.csv") 


plt.boxplot(mancha.manchas)
plt.show()

# com malha#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt 

mancha = pd.read_csv("MANCHAS.csv") 
m1 = mancha[0:29]

plt.plot(m1.Ano, m1.manchas)
plt.xlabel('ANO(s)')
plt.ylabel('Quantidade')

plt.title('Numero de manchas solares')

plt.grid(True)
plt.xticks(m1.Ano, m1.manchas, rotation = 'vertical')
plt.show()
