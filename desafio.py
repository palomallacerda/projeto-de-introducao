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
plt.xticks(fort.Ano, fort.Ano)

plt.show()

## 10 primeiros com malha##
# com malha#
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt 

forta = pd.read_csv("fortaleza.csv") 
fort1 = forta[0:10]

plt.plot(fort1.Ano, fort1.Fort)
plt.xlabel('ANO (s)')
plt.ylabel('Preciptacao')
plt.title('Precipitação atmosférica os 10 primeiros')
plt.grid(True)
plt.xticks(fort1.Ano, fort1.Ano, rotation = 'vertical')
plt.show()

## 10 ultimos com malha##
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

forta = pd.read_csv("fortaleza.csv") 
fort1 = forta[139:]

plt.plot(fort1.Ano, fort1.Fort)
plt.xlabel('ANO (s)')
plt.ylabel('Preciptacao')
plt.title('Precipitação atmosférica os 10 ultimos')
plt.grid(True)
plt.xticks(fort1.Ano, fort1.Ano, rotation = 'vertical')
plt.show()


#gerando box com malha#

import pandas as pd
import matplotlib.pyplot as plt 

fort1= pd.read_csv("fortaleza.csv") 

plt.boxplot(fort1.Fort)
plt.xlabel('ANO(s)')
plt.ylabel('Preciptacao')
plt.title('Precipitação atmosférica')
plt.grid(True)

plt.show()
